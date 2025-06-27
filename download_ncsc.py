import requests
from pathlib import Path
from bs4 import BeautifulSoup
import re
from datetime import datetime

API_URL = "https://www.ncsc.gov.uk/api/1/services/v4/collection-content.json"
BASE_URL = "https://www.ncsc.gov.uk"

PRINCIPLES = [
    "principle-1-data-in-transit-protection",
    "principle-2-asset-protection-and-resilience",
    "principle-3-separation-between-customers",
    "principle-4-governance-framework",
    "principle-5-operational-security",
    "principle-6-personnel-security",
    "principle-7-secure-development",
    "principle-8-supply-chain-security",
    "principle-9-secure-user-management",
    "principle-10-identity-and-authentication",
    "principle-11-external-interface-protection",
    "principle-12-secure-service-administration",
    "principle-13-audit-information-and-alerting-for-customers",
    "principle-14-secure-use-of-the-service",
]

OUTPUT_DIR = Path("cloud_security_principles")
OUTPUT_DIR.mkdir(exist_ok=True)

def slug_to_filename(slug):
    match = re.match(r'principle-(\d+)-(.+)', slug)
    if match:
        num, name = match.groups()
        return f"{num.zfill(2)}_{name.replace('-', '_')}.md"
    return slug.replace('-', '_') + ".md"

def html_to_markdown(html_content):
    if not html_content:
        return ""
    soup = BeautifulSoup(html_content, "html.parser")
    # Convert links
    for a in soup.find_all("a"):
        href = a.get("href")
        if href:
            if href.startswith("/"):
                a["href"] = BASE_URL + href
            elif not href.startswith("http"):
                a.replace_with(a.get_text())
                continue
        else:
            a.replace_with(a.get_text())
    # Convert headings
    for i in range(1, 7):
        for h in soup.find_all(f"h{i}"):
            level = "#" * (i + 2)
            h.replace_with(f"\n{level} {h.get_text(strip=True)}\n\n")
    # Unordered lists
    for ul in soup.find_all("ul"):
        items = []
        for li in ul.find_all("li", recursive=False):
            items.append(f"- {li.get_text(strip=True)}")
        ul.replace_with("\n" + "\n".join(items) + "\n\n")
    # Ordered lists
    for ol in soup.find_all("ol"):
        items = []
        for i, li in enumerate(ol.find_all("li", recursive=False), 1):
            items.append(f"{i}. {li.get_text(strip=True)}")
        ol.replace_with("\n" + "\n".join(items) + "\n\n")
    # Paragraphs
    for p in soup.find_all("p"):
        text = p.get_text(strip=True)
        if text:
            p.replace_with(f"{text}\n\n")
        else:
            p.replace_with("")
    text = soup.get_text()
    text = re.sub(r'\n{3,}', '\n\n', text)
    text = text.strip()
    return text

def fetch_principle_api(slug):
    params = {
        "url": "/collection/cloud",
        "pageContentUrl": f"/collection/cloud/the-cloud-security-principles/{slug}"
    }
    headers = {
        "Accept": "application/json, text/plain, */*",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.5 Safari/605.1.15"
    }
    print(f"Fetching API for {slug}")
    resp = requests.get(API_URL, params=params, headers=headers)
    resp.raise_for_status()
    data = resp.json()
    page = data.get("page", {})
    body = page.get("bodyContent", {})
    title = body.get("title", slug.replace('-', ' ').title())
    summary = body.get("summary", "")
    content_items = body.get("content", {}).get("items", [])
    principle_match = re.match(r'principle-(\d+)-', slug)
    principle_num = principle_match.group(1) if principle_match else "Unknown"
    md = f"""---
title: \"{title}\"
principle: {principle_num}
summary: \"{summary}\"
source: \"https://www.ncsc.gov.uk/collection/cloud/the-cloud-security-principles/{slug}\"
ogl: \"Contains public sector information licensed under the Open Government Licence v3.0. https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/\"
---\n\n# {title}\n\n> {summary}\n\n"""
    for item in content_items:
        subheading = item.get("subheading", "")
        description = item.get("description", "")
        if subheading:
            if subheading.lower() == "further reading":
                soup_check = BeautifulSoup(description, "html.parser")
                links = soup_check.find_all("a")
                has_valid_links = any(link.get("href", "").startswith("http") for link in links)
                if not has_valid_links and links:
                    print(f"  Skipping 'Further reading' section with potentially broken links")
                    continue
            md += f"## {subheading}\n\n"
        md_content = html_to_markdown(description)
        if md_content:
            md += md_content + "\n\n"
    md = re.sub(r'\n{3,}', '\n\n', md)
    md = md.strip() + "\n"
    return title, md

def main():
    for slug in PRINCIPLES:
        try:
            title, md = fetch_principle_api(slug)
            filename = slug_to_filename(slug)
            out_path = OUTPUT_DIR / filename
            with open(out_path, "w", encoding="utf-8") as f:
                f.write(md)
            print(f"✅ Saved: {out_path}")
        except Exception as e:
            print(f"Error with {slug}: {e}")

if __name__ == "__main__":
    main()