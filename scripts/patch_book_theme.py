from __future__ import annotations

from pathlib import Path
import sys


REPO_ROOT = Path(__file__).resolve().parent.parent
THEME_ROOT = REPO_ROOT / "_build" / "templates" / "site" / "myst" / "book-theme"
SERVER_BUNDLE = THEME_ROOT / "build" / "index.js"
CLIENT_SHARED_DIR = THEME_ROOT / "public" / "build" / "_shared"

SERVER_OLD = (
    'function kls({github:t}){if(!t)return null;let e=t.replace(/^(https?:\\/\\/)?github\\.com\\//,"");'
    'return(0,Pf.jsx)("a",{href:`https://github.com/${e}`,title:`GitHub Repository: ${e}`,target:"_blank",'
    'rel:"noopener noreferrer",className:"myst-fm-github-link text-inherit hover:text-inherit",children:'
    '(0,Pf.jsx)(wMt,{width:"1.25rem",height:"1.25rem",className:"myst-fm-github-icon inline-block mr-1 '
    'opacity-60 hover:opacity-100"})})}function Rls({open_access:t})'
)

SERVER_NEW = (
    'function kls({github:t}){if(!t)return null;let e=t.replace(/^(https?:\\/\\/)?github\\.com\\//,"");'
    'return(0,Pf.jsx)("a",{href:`https://github.com/${e}`,title:`GitHub Repository: ${e}`,target:"_blank",'
    'rel:"noopener noreferrer",className:"myst-fm-github-link text-inherit hover:text-inherit",children:'
    '(0,Pf.jsx)(wMt,{width:"1.25rem",height:"1.25rem",className:"myst-fm-github-icon inline-block mr-1 '
    'opacity-60 hover:opacity-100"})})}function Dls({sourceUrl:t}){if(!t||!/\\.ipynb(?:$|[?#])/.test(t))'
    'return null;let e=t.replace(/^https:\\/\\/github\\.com\\//,"https://colab.research.google.com/github/");'
    'return e===t?null:(0,Pf.jsx)("a",{href:e,title:"Open in Colab",target:"_blank",rel:"noopener noreferrer",'
    '"aria-label":"Open notebook in Colab",className:"myst-fm-colab-link text-inherit hover:text-inherit",'
    'children:(0,Pf.jsx)("img",{src:"https://upload.wikimedia.org/wikipedia/commons/d/d0/'
    'Google_Colaboratory_SVG_Logo.svg",width:"20",height:"20",alt:"Open in Colab",className:'
    '"myst-fm-colab-icon inline-block mr-1 opacity-80 hover:opacity-100"})})}function Rls({open_access:t})'
)

SERVER_USE_OLD = (
    '(0,Pf.jsx)(kls,{github:g}),(0,Pf.jsx)(Ils,{editUrl:k??void 0})'
)

SERVER_USE_NEW = (
    '(0,Pf.jsx)(kls,{github:g}),(0,Pf.jsx)(Dls,{sourceUrl:Q}),(0,Pf.jsx)(Ils,{editUrl:k??void 0})'
)

SERVER_FRONTMATTER_OLD = (
    'published:m,github:g,doi:_,open_access:x,license:w,exports:S,downloads:E,edit_url:k}=t'
)

SERVER_FRONTMATTER_NEW = (
    'published:m,github:g,doi:_,open_access:x,license:w,exports:S,downloads:E,edit_url:k,source_url:Q}=t'
)

SERVER_FRONTMATTER_CURRENT = (
    'title:d,subtitle:h,subject:f,doi:m,open_access:v,license:p,github:g,venue:_,volume:x,issue:w,'
    'exports:S,downloads:E,date:A,authors:C,enumerator:R,edit_url:k}=t'
)

SERVER_FRONTMATTER_CURRENT_NEW = (
    'title:d,subtitle:h,subject:f,doi:m,open_access:v,license:p,github:g,venue:_,volume:x,issue:w,'
    'exports:S,downloads:E,date:A,authors:C,enumerator:R,edit_url:k,source_url:Q}=t'
)

CLIENT_OLD = (
    'function eI({github:f}){if(!f)return null;let c=f.replace(/^(https?:\\/\\/)?github\\.com\\//,"");'
    'return(0,sr.jsx)("a",{href:`https://github.com/${c}`,title:`GitHub Repository: ${c}`,target:"_blank",'
    'rel:"noopener noreferrer",className:"myst-fm-github-link text-inherit hover:text-inherit",children:'
    '(0,sr.jsx)(jv,{width:"1.25rem",height:"1.25rem",className:"myst-fm-github-icon inline-block mr-1 '
    'opacity-60 hover:opacity-100"})})}function rI({open_access:f})'
)

CLIENT_NEW = (
    'function eI({github:f}){if(!f)return null;let c=f.replace(/^(https?:\\/\\/)?github\\.com\\//,"");'
    'return(0,sr.jsx)("a",{href:`https://github.com/${c}`,title:`GitHub Repository: ${c}`,target:"_blank",'
    'rel:"noopener noreferrer",className:"myst-fm-github-link text-inherit hover:text-inherit",children:'
    '(0,sr.jsx)(jv,{width:"1.25rem",height:"1.25rem",className:"myst-fm-github-icon inline-block mr-1 '
    'opacity-60 hover:opacity-100"})})}function oI({sourceUrl:f}){if(!f||!/\\.ipynb(?:$|[?#])/.test(f))'
    'return null;let c=f.replace(/^https:\\/\\/github\\.com\\//,"https://colab.research.google.com/github/");'
    'return c===f?null:(0,sr.jsx)("a",{href:c,title:"Open in Colab",target:"_blank",rel:"noopener noreferrer",'
    '"aria-label":"Open notebook in Colab",className:"myst-fm-colab-link text-inherit hover:text-inherit",'
    'children:(0,sr.jsx)("img",{src:"https://upload.wikimedia.org/wikipedia/commons/d/d0/'
    'Google_Colaboratory_SVG_Logo.svg",width:"20",height:"20",alt:"Open in Colab",className:'
    '"myst-fm-colab-icon inline-block mr-1 opacity-80 hover:opacity-100"})})}function rI({open_access:f})'
)

CLIENT_USE_OLD = (
    '(0,sr.jsx)(eI,{github:B}),(0,sr.jsx)(iI,{editUrl:D!=null?D:void 0})'
)

CLIENT_USE_NEW = (
    '(0,sr.jsx)(eI,{github:B}),(0,sr.jsx)(oI,{sourceUrl:Z}),(0,sr.jsx)(iI,{editUrl:D!=null?D:void 0})'
)

CLIENT_FRONTMATTER_OLD = (
    'published:y,github:B,doi:U,open_access:G,license:j,exports:_,downloads:x,edit_url:D}=f'
)

CLIENT_FRONTMATTER_NEW = (
    'published:y,github:B,doi:U,open_access:G,license:j,exports:_,downloads:x,edit_url:D,source_url:Z}=f'
)

CLIENT_FRONTMATTER_CURRENT = (
    'title:b,subtitle:p,subject:C,doi:_,open_access:S,license:E,github:B,venue:R,volume:$,issue:I,'
    'exports:T,downloads:j,date:F,authors:X,enumerator:Z,edit_url:D}=f'
)

CLIENT_FRONTMATTER_CURRENT_NEW = (
    'title:b,subtitle:p,subject:C,doi:_,open_access:S,license:E,github:B,venue:R,volume:$,issue:I,'
    'exports:T,downloads:j,date:F,authors:X,enumerator:Z,edit_url:D,source_url:L}=f'
)

CLIENT_USE_CURRENT_OLD = (
    '(0,sr.jsx)(eI,{github:B})]}),(0,sr.jsx)(iI,{editUrl:D!=null?D:void 0})'
)

CLIENT_USE_CURRENT_NEW = (
    '(0,sr.jsx)(eI,{github:B})]}),(0,sr.jsx)(oI,{sourceUrl:L}),(0,sr.jsx)(iI,{editUrl:D!=null?D:void 0})'
)

SERVER_USE_CURRENT_OLD = (
    '(0,Pf.jsx)(kls,{github:g})]}),(0,Pf.jsx)(Ils,{editUrl:k??void 0})'
)

SERVER_USE_CURRENT_NEW = (
    '(0,Pf.jsx)(kls,{github:g})]}),(0,Pf.jsx)(Dls,{sourceUrl:Q}),(0,Pf.jsx)(Ils,{editUrl:k??void 0})'
)


def replace_first(text: str, candidates: list[str], replacement: str, path: Path) -> str:
    for candidate in candidates:
        if candidate in text:
            return text.replace(candidate, replacement, 1)
    raise RuntimeError(f"Expected snippet not found in {path}")


def patch_text(path: Path, replacements: list[tuple[list[str], str]]) -> bool:
    text = path.read_text()
    if "Open notebook in Colab" in text:
        return False
    original = text
    for candidates, new in replacements:
        text = replace_first(text, candidates, new, path)
    if text != original:
        path.write_text(text)
        return True
    return False


def find_client_chunk() -> Path:
    if not CLIENT_SHARED_DIR.exists():
        raise FileNotFoundError(f"Client shared directory not found: {CLIENT_SHARED_DIR}")
    for path in sorted(CLIENT_SHARED_DIR.glob("chunk-*.js")):
        text = path.read_text()
        if "GitHub Repository:" in text and "myst-fm-github-link" in text:
            return path
    raise FileNotFoundError("Could not find the shared client bundle for the MyST book theme")


def main() -> int:
    if not SERVER_BUNDLE.exists():
        print(
            "Theme cache not found. Run `jupyter book build --all` once to fetch the book theme, then rerun this script.",
            file=sys.stderr,
        )
        return 1

    client_chunk = find_client_chunk()
    changed = False
    changed |= patch_text(
        SERVER_BUNDLE,
        [
            ([SERVER_OLD], SERVER_NEW),
            ([SERVER_FRONTMATTER_OLD, SERVER_FRONTMATTER_CURRENT], SERVER_FRONTMATTER_CURRENT_NEW),
            ([SERVER_USE_OLD, SERVER_USE_CURRENT_OLD], SERVER_USE_CURRENT_NEW),
        ],
    )
    changed |= patch_text(
        client_chunk,
        [
            ([CLIENT_OLD], CLIENT_NEW),
            ([CLIENT_FRONTMATTER_OLD, CLIENT_FRONTMATTER_CURRENT], CLIENT_FRONTMATTER_CURRENT_NEW),
            ([CLIENT_USE_OLD, CLIENT_USE_CURRENT_OLD], CLIENT_USE_CURRENT_NEW),
        ],
    )

    if changed:
        print(f"Patched MyST book theme in {THEME_ROOT}")
    else:
        print(f"MyST book theme already patched in {THEME_ROOT}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
