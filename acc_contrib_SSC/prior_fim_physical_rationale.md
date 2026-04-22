# Physically Informed `theta` and `prior_FIM` Rationale (TCLab)

This note documents how the physically informed prior values used in
`acc_contrib_SSC/parmest_regularization.ipynb` were chosen.

## 1) Model structure used for intuition

The TCLab model equations in this repo are:

- Heater node dynamics:
  - `dTh/dt = (Ua*(Tamb-Th) + Ub*(Ts-Th) + alpha*P*u) * inv_CpH`
- Sensor node dynamics:
  - `dTs/dt = Ub*(Th-Ts) * inv_CpS`

See local source:

- `notebooks/tclab_pyomo.py` lines 426-452 (ODE definitions)
- `notebooks/tclab_pyomo.py` line 611 (unknown parameter order: `Ua, Ub, inv_CpH, inv_CpS`)

These equations are lumped-capacitance energy balances with Newton-style linear heat transfer terms.

## 2) Physical interpretation of the four parameters

- `Ua` (W/K): net heat loss from heater node to ambient.
- `Ub` (W/K): heater-to-sensor thermal coupling.
- `CpH` (J/K): effective thermal capacitance of heater node.
- `CpS` (J/K): effective thermal capacitance of sensor node.

In estimator space, the model uses `inv_CpH = 1/CpH` and `inv_CpS = 1/CpS`.

## 3) Prior mean (`theta0`) choices

Chosen nominal physical values:

- `Ua = 0.050` W/K
- `Ub = 0.015` W/K
- `CpH = 6.5` J/K
- `CpS = 0.35` J/K

Converted to estimator-space reference values:

- `theta0_phys = {Ua, Ub, inv_CpH=1/6.5, inv_CpS=1/0.35}`

These values are intentionally close to previously estimated magnitudes in this notebook workflow, while preserving physically plausible heat-transfer/capacitance scales.

## 4) Confidence assumptions (covariance model)

A prior covariance was built in physical parameter space using:

### 4.1 Standard deviations

- `sigma(Ua)=0.012`
- `sigma(Ub)=0.005`
- `sigma(CpH)=1.5`
- `sigma(CpS)=0.12`

### 4.2 Correlation assumptions

Correlation matrix in `[Ua, Ub, CpH, CpS]` order:

```text
[[ 1.00, -0.25,  0.55, 0.10],
 [-0.25,  1.00,  0.40, 0.75],
 [ 0.55,  0.40,  1.00, 0.20],
 [ 0.10,  0.75,  0.20, 1.00]]
```

Reasoning:

- `Ub` and `CpS` positively correlated: sensor-lag dynamics depend strongly on `Ub/CpS`.
- `Ua` and `CpH` positively correlated: heater time constant depends on `(Ua+Ub)/CpH`.
- `Ua` and `Ub` mildly negative: both can partially trade off in fitting heater cooling behavior.

## 5) Mapping covariance to estimator parameterization

Because parmest estimates `[Ua, Ub, inv_CpH, inv_CpS]`, covariance is transformed with a Jacobian:

- `x = g(p)` where `p=[Ua, Ub, CpH, CpS]` and `x=[Ua, Ub, 1/CpH, 1/CpS]`
- `Sigma_x = J * Sigma_p * J^T`

with diagonal Jacobian

```text
J = diag(1,
         1,
         -1/CpH^2,
         -1/CpS^2)
```

## 6) Prior Fisher Information Matrix

The prior information matrix is defined as:

- `prior_FIM_phys = inv(Sigma_x)`

An optional scale factor `prior_weight` is applied (currently `0.05`) to tune prior strength relative to data SSE in regularized estimation.

## 7) Where this is implemented in notebook

In `acc_contrib_SSC/parmest_regularization.ipynb`, see the appended physical-prior cell containing:

- `theta_phys`, `sigma_phys`, `corr_phys`
- Jacobian transform to estimator-space covariance
- `prior_FIM_phys`
- L1 call:
  - `parmest.Estimator(..., regularization='L1', prior_FIM=prior_FIM_phys, theta_ref=theta0_phys)`

## 8) Sources

### Local repo sources

- TCLab equations and unknown parameter ordering:
  - `notebooks/tclab_pyomo.py` lines 426-452 and 611
- Physical-prior implementation cell:
  - `acc_contrib_SSC/parmest_regularization.ipynb` (search for `theta_phys`, `corr_phys`, `prior_FIM_phys`, `pest_regL1_phys`)

### External references

- Newton cooling / lumped-capacitance intuition:
  - https://en.wikipedia.org/wiki/Newton%27s_law_of_cooling
- Fisher Information Matrix concept (information/covariance relationship):
  - https://en.wikipedia.org/wiki/Fisher_information
- Covariance propagation with Jacobian (`Sigma_y = J Sigma_x J^T`):
  - https://en.wikipedia.org/wiki/Propagation_of_uncertainty
- Pyomo parmest package docs:
  - https://pyomo.readthedocs.io/en/6.9.3/explanation/analysis/parmest/index.html
  - Source/API pages used for implementation context:
    - https://pyomo.readthedocs.io/en/stable/_modules/pyomo/contrib/parmest/parmest.html
    - https://pyomo.readthedocs.io/en/latest/api/pyomo.contrib.parmest.parmest.Estimator.html

## 9) Notes

- The prior is intentionally "weak-to-moderate" and not a hard constraint.
- If optimization is over-regularized, reduce `prior_weight`.
- If non-identifiability persists (flat profile likelihood), increase prior weight slightly or tighten selected prior variances.
