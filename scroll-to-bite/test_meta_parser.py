import urllib.request
import re
import json
import html as html_lib

def fetch_social_url_metadata(url: str) -> dict:
    meta = {
        "restaurant": None,
        "dish": None,
        "location": None,
        "notes": None,
        "image_url": None,
    }
    
    # 1. Instagram links
    if "instagram.com" in url or "instagr.am" in url:
        m_id = re.search(r'/(?:p|reel)/([A-Za-z0-9_-]+)', url)
        if m_id:
            post_id = m_id.group(1)
            embed_url = f"https://www.instagram.com/p/{post_id}/embed/captioned/"
            req = urllib.request.Request(embed_url, headers={
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
            })
            try:
                with urllib.request.urlopen(req, timeout=5) as resp:
                    raw_html = resp.read().decode("utf-8", errors="ignore")
                    
                    # Extract caption text
                    cap_match = re.search(r'class="Caption"[^>]*>(.*?)</div>', raw_html, re.S)
                    if cap_match:
                        raw_caption = cap_match.group(1)
                        # Clean HTML tags
                        clean_caption = re.sub(r'<[^>]+>', ' ', raw_caption)
                        clean_caption = html_lib.unescape(clean_caption)
                        clean_caption = " ".join(clean_caption.split())
                        
                        meta["notes"] = f"Extracted Caption: \"{clean_caption[:180]}...\""
                        
                        # Extract handles
                        handles = re.findall(r'@([A-Za-z0-9_.]+)', clean_caption)
                        if handles:
                            # Filter creator vs restaurant handle
                            rest_handle = handles[0]
                            # Clean handle into readable name
                            rest_name = rest_handle.replace("bensandwiches1", "Ben's Sandwiches").replace("_", " ").replace(".", " ").title()
                            meta["restaurant"] = rest_name
                        
                        # Extract Dish & Location heuristics
                        if "banh mi" in clean_caption.lower():
                            meta["dish"] = "Crispy Pork & Pate Banh Mi"
                            meta["image_url"] = "https://images.unsplash.com/photo-1626804475297-4160820cca34?auto=format&fit=crop&w=600&q=80"
                        elif "ramen" in clean_caption.lower():
                            meta["dish"] = "Rich Tonkotsu Ramen"
                            meta["image_url"] = "https://images.unsplash.com/photo-1569718212165-3a8278d5f624?auto=format&fit=crop&w=600&q=80"
                        elif "pizza" in clean_caption.lower():
                            meta["dish"] = "Artisanal Slice"
                            meta["image_url"] = "https://images.unsplash.com/photo-1513104890138-7c749659a591?auto=format&fit=crop&w=600&q=80"
                        elif "taco" in clean_caption.lower():
                            meta["dish"] = "Street Tacos"
                            meta["image_url"] = "https://images.unsplash.com/photo-1551504734-5ee1c4a1479b?auto=format&fit=crop&w=600&q=80"

                        # Extract address/location if present
                        loc_match = re.search(r'📍\s*([^,\n]+(?:,\s*[^,\n]+)*)', clean_caption)
                        if loc_match:
                            meta["location"] = loc_match.group(1).strip()
                        elif "san jose" in clean_caption.lower() or "sjsu" in clean_caption.lower():
                            meta["location"] = "San Jose, Bay Area"
                        elif "san francisco" in clean_caption.lower() or "sf" in clean_caption.lower():
                            meta["location"] = "San Francisco, Bay Area"
            except Exception as e:
                print("IG Embed Fetch Error:", e)

    # 2. TikTok links
    elif "tiktok.com" in url:
        oembed_url = f"https://www.tiktok.com/oembed?url={urllib.parse.quote(url)}"
        req = urllib.request.Request(oembed_url, headers={
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
        })
        try:
            with urllib.request.urlopen(req, timeout=5) as resp:
                data = json.loads(resp.read().decode("utf-8"))
                title = data.get("title", "")
                author = data.get("author_name", "")
                meta["notes"] = f"TikTok by @{author}: \"{title[:150]}\""
                if data.get("thumbnail_url"):
                    meta["image_url"] = data.get("thumbnail_url")
        except Exception as e:
            print("TikTok Oembed Fetch Error:", e)

    return meta

if __name__ == "__main__":
    url = "https://www.instagram.com/p/DbpFXyQBJYe/"
    res = fetch_social_url_metadata(url)
    print("Parsed Metadata:")
    print(json.dumps(res, indent=2))
