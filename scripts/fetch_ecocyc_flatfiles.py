#!/usr/bin/env python3
from __future__ import annotations

import argparse
import base64
import fnmatch
import os
import re
import sys
from html import unescape
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.parse import urljoin, urlparse
from urllib.request import Request, urlopen

PROJECT_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUTPUT = PROJECT_ROOT / "data/raw/ecocyc"


def main() -> int:
    parser = argparse.ArgumentParser(
        description=(
            "Download licensed EcoCyc/BioCyc flat files without storing "
            "confidential credentials in the repository."
        )
    )
    parser.add_argument("--url", default=os.getenv("BIOCYC_FLATFILES_URL", ""))
    parser.add_argument("--user", default=os.getenv("BIOCYC_FLATFILES_USER", ""))
    parser.add_argument("--password", default=os.getenv("BIOCYC_FLATFILES_PASSWORD", ""))
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--timeout", type=float, default=300.0, help="Per-request timeout in seconds.")
    parser.add_argument(
        "--include",
        action="append",
        default=[],
        help="Filename glob to download. Can repeat. Default downloads common flat-file archives and dat/col files.",
    )
    parser.add_argument("--dry-run", action="store_true", help="List matching remote files without downloading them.")
    args = parser.parse_args()

    if not args.url or not args.user or not args.password:
        print(
            "Missing EcoCyc credentials. Set BIOCYC_FLATFILES_URL, "
            "BIOCYC_FLATFILES_USER, and BIOCYC_FLATFILES_PASSWORD.",
            file=sys.stderr,
        )
        return 2

    include = args.include or ["*.tar.gz", "*.tgz", "*.zip", "*.dat", "*.col", "*.txt"]
    args.output_dir.mkdir(parents=True, exist_ok=True)

    try:
        html = fetch_text(args.url, args.user, args.password, timeout=args.timeout)
    except (HTTPError, URLError) as exc:
        print(f"Failed to fetch EcoCyc listing: {format_url_error(exc)}", file=sys.stderr)
        return 1

    links = extract_links(html, args.url)
    files = [link for link in links if should_download(link, include)]
    if not files:
        print("No matching files found in the EcoCyc listing.")
        return 0

    for file_url in files:
        name = Path(urlparse(file_url).path).name
        dest = args.output_dir / name
        if args.dry_run:
            print(f"would_download\t{name}\t{file_url}")
            continue
        print(f"downloading\t{name}")
        try:
            download(file_url, args.user, args.password, dest, timeout=args.timeout)
        except (HTTPError, URLError) as exc:
            print(f"failed\t{name}\t{format_url_error(exc)}", file=sys.stderr)
            return 1
    return 0


def auth_header(user: str, password: str) -> str:
    token = base64.b64encode(f"{user}:{password}".encode("utf-8")).decode("ascii")
    return f"Basic {token}"


def request(url: str, user: str, password: str) -> Request:
    return Request(url, headers={"Authorization": auth_header(user, password)})


def fetch_text(url: str, user: str, password: str, timeout: float) -> str:
    with urlopen(request(url, user, password), timeout=timeout) as response:
        return response.read().decode("utf-8", errors="replace")


def download(url: str, user: str, password: str, dest: Path, timeout: float) -> None:
    tmp = dest.with_suffix(dest.suffix + ".tmp")
    with urlopen(request(url, user, password), timeout=timeout) as response, tmp.open("wb") as handle:
        while True:
            chunk = response.read(1024 * 1024)
            if not chunk:
                break
            handle.write(chunk)
    tmp.replace(dest)


def extract_links(html: str, base_url: str) -> list[str]:
    hrefs = re.findall(r'href=["\']([^"\']+)["\']', html, flags=re.I)
    links = []
    for href in hrefs:
        href = unescape(href).strip()
        if not href or href.startswith("#") or href.startswith("?"):
            continue
        url = urljoin(base_url, href)
        if url.rstrip("/") == base_url.rstrip("/"):
            continue
        links.append(url)
    return sorted(set(links))


def should_download(url: str, patterns: list[str]) -> bool:
    name = Path(urlparse(url).path).name
    if not name or name in {".", ".."}:
        return False
    return any(fnmatch.fnmatch(name, pattern) for pattern in patterns)


def format_url_error(exc: HTTPError | URLError) -> str:
    if isinstance(exc, HTTPError):
        return f"HTTPError(code={exc.code}, reason={exc.reason})"
    return f"URLError(reason={exc.reason})"


if __name__ == "__main__":
    raise SystemExit(main())
