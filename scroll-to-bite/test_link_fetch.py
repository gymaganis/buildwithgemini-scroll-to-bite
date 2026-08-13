import urllib.request
import re
import html as html_lib

def fetch_social_url_metadata(url: str) -> dict:
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Accept-Language": "en-US,en;q=0.9",
    }
    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=5) as resp:
            raw_html = resp.read().decode("utf-8", errors="ignore")
            decoded_html = html_lib.unescape(raw_html)
            
            # Find og:description or title
            og_desc = None
            m = re.search(r'property=["\']og:description["\']\s+content=["\']([^"\']+)["\']', decoded_html, re.I)
            if not m:
                m = re.search(r'content=["\']([^"\']+)["\']\s+property=["\']og:description["\']', decoded_html, re.I)
            if not m:
                m = re.search(r'<meta\s+name=["\']description["\']\s+content=["\']([^"\']+)["\']', decoded_html, re.I)
            if m:
                og_desc = m.group(1)
            
            print("Extracted OG Desc:", og_desc)
            return {"og_desc": og_desc, "raw_html_len": len(raw_html)}
    except Exception as e:
        print("Fetch err:", e)
        return {}

if __name__ == "__main__":
    fetch_social_url_metadata("https://www.instagram.com/p/DbpFXyQBJYe/")
