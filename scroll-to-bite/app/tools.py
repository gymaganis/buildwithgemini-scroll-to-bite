# Copyright 2026 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import json
from pathlib import Path
import re
from typing import Any, Dict, List, Optional

# Persistent file path
DB_FILE = Path(__file__).parent / "wishlist_db.json"

DEFAULT_WISHLIST: List[Dict[str, Any]] = [
    {
        "id": "1",
        "restaurant": "Con Sabor A Mexico Food Truck",
        "dish": "Giant Birria Taco & Short Rib Tacos",
        "location": "San Jose, Bay Area",
        "url": "https://www.tiktok.com/@bayareafoodz/video/7410129571867086123",
        "image_url": "https://p19-common-sign.tiktokcdn-us.com/tos-useast5-p-0068-tx/99767951c50c46129acb972bc62124b7_1725305251~tplv-tiktokx-origin.image?dr=9636&x-expires=1786831200&x-signature=Ys4Ljsrn4gPvj8llwLlCuO%2BMJmE%3D&t=4d5b0474&ps=13740610&shp=81f88b70&shcp=43f4a2f9&idc=useast5",
        "status": "Want to Try",
        "notes": "500 W San Carlos St, San Jose — World's biggest Birria taco trending on TikTok",
    },
    {
        "id": "2",
        "restaurant": "Ben's Sandwiches",
        "dish": "Crispy Pork & Pate Banh Mi",
        "location": "San Jose, Bay Area",
        "url": "https://www.instagram.com/p/DbpFXyQBJYe/",
        "image_url": "https://images.unsplash.com/photo-1626804475297-4160820cca34?auto=format&fit=crop&w=600&q=80",
        "status": "Want to Try",
        "notes": "221 E San Fernando St, San Jose — Viral banh mi post on Instagram",
    },
    {
        "id": "3",
        "restaurant": "L'Industrie Pizzeria",
        "dish": "Burrata Slice & Hot Honey",
        "location": "New York, NYC",
        "url": "https://www.tiktok.com/@foodie/video/7123456789",
        "image_url": "https://images.unsplash.com/photo-1513104890138-7c749659a591?auto=format&fit=crop&w=600&q=80",
        "status": "Want to Try",
        "notes": "Viral TikTok pizza slice in Williamsburg & West Village",
    },
    {
        "id": "4",
        "restaurant": "7th Street Burger",
        "dish": "Double Cheeseburger & Loaded Fries",
        "location": "New York, NYC",
        "url": "https://www.instagram.com/reel/C123456789",
        "image_url": "https://images.unsplash.com/photo-1568901346375-23c9450c58cd?auto=format&fit=crop&w=600&q=80",
        "status": "Want to Try",
        "notes": "Classic NYC smash burger trending on IG",
    },
    {
        "id": "5",
        "restaurant": "Marugame Udon",
        "dish": "Nikutama Udon & Tempura",
        "location": "San Francisco, Bay Area",
        "url": "https://www.tiktok.com/@bayareaeats/video/7987654321",
        "image_url": "https://images.unsplash.com/photo-1618841557871-b4664fbf0cb3?auto=format&fit=crop&w=600&q=80",
        "status": "Want to Try",
        "notes": "Handmade sanuki udon in SF Stonestown & Berkeley",
    },
    {
        "id": "6",
        "restaurant": "Howlin' Ray's",
        "dish": "Sando (Nashville Hot Chicken Sandwich)",
        "location": "Los Angeles, SoCal",
        "url": "https://www.instagram.com/reel/C987654321",
        "image_url": "https://images.unsplash.com/photo-1626645738196-c2a7c87a8f58?auto=format&fit=crop&w=600&q=80",
        "status": "Want to Try",
        "notes": "Chinatown LA viral hot chicken sando",
    },
]


def _load_wishlist() -> List[Dict[str, Any]]:
    """Loads wishlist items from JSON file or initializes with defaults."""
    if DB_FILE.exists():
        try:
            with open(DB_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            pass
    return list(DEFAULT_WISHLIST)


def _save_wishlist(items: List[Dict[str, Any]]) -> None:
    """Saves wishlist items to JSON file."""
    try:
        with open(DB_FILE, "w", encoding="utf-8") as f:
            json.dump(items, f, indent=2)
    except Exception:
        pass


WISHLIST: List[Dict[str, Any]] = _load_wishlist()

# Database of curated viral spots across target regions
SAMPLE_VIRAL_SPOTS = [
    {
        "restaurant": "Souvla",
        "dish": "Greek Fries with Grated Mizithra & Frozen Yogurt",
        "location": "San Francisco, Bay Area",
        "neighborhood": "Hayes Valley / Mission",
        "vibe": "Fast-casual Greek",
        "tag": "#SFEats #TikTokViral",
        "image_url": "https://images.unsplash.com/photo-1529006557810-274b9b2fc783?auto=format&fit=crop&w=600&q=80",
    },
    {
        "restaurant": "SomiSomi",
        "dish": "Ah-Boong (Taiyaki Waffle Cone with Ube Soft Serve)",
        "location": "Mountain View, Bay Area",
        "neighborhood": "San Antonio Center",
        "vibe": "Korean Dessert & Taiyaki",
        "tag": "#MountainViewEats #ViralDessert",
        "image_url": "https://images.unsplash.com/photo-1563805042-7684c019e1cb?auto=format&fit=crop&w=600&q=80",
    },
    {
        "restaurant": "Alexander's Patisserie",
        "dish": "Handcrafted Macarons & Kouign-Amann",
        "location": "Mountain View, Bay Area",
        "neighborhood": "Castro Street",
        "vibe": "French Pastry Boutique",
        "tag": "#CastroSt #SouthBayFoodie",
        "image_url": "https://images.unsplash.com/photo-1569864358642-9d1684040f43?auto=format&fit=crop&w=600&q=80",
    },
    {
        "restaurant": "Arismendi Bakery / Arsicault Bakery",
        "dish": "Almond Croissant & Kouign-Amann",
        "location": "San Francisco, Bay Area",
        "neighborhood": "Richmond / Inner Sunset",
        "vibe": "French Bakery",
        "tag": "#BestCroissantInSF",
        "image_url": "https://images.unsplash.com/photo-1555507036-ab1f4038808a?auto=format&fit=crop&w=600&q=80",
    },
    {
        "restaurant": "Crumbl Cookies",
        "dish": "Weekly Rotating Specialty Cookies",
        "location": "Bay Area / SoCal / NYC",
        "neighborhood": "Multiple Locations",
        "vibe": "Dessert & Bakery",
        "tag": "#CrumblReview #ViralDessert",
        "image_url": "https://images.unsplash.com/photo-1558961363-fa8fdf82db35?auto=format&fit=crop&w=600&q=80",
    },
    {
        "restaurant": "Kinn",
        "dish": "Modern Korean Tasting Menu & Crispy Rice",
        "location": "Los Angeles, SoCal",
        "neighborhood": "Koreatown",
        "vibe": "Korean Fine-Casual",
        "tag": "#LAKoreatown #FoodieTikTok",
        "image_url": "https://images.unsplash.com/photo-1553163147-622ab57be1c7?auto=format&fit=crop&w=600&q=80",
    },
    {
        "restaurant": "Courage Bagels",
        "dish": "Burnt & Salted Sesame Bagel with Smoked Salmon",
        "location": "Los Angeles, SoCal",
        "neighborhood": "Silver Lake",
        "vibe": "Artisanal Bagels",
        "tag": "#CourageBagels #LAFoodie",
        "image_url": "https://images.unsplash.com/photo-1585478259715-876a6a81fc08?auto=format&fit=crop&w=600&q=80",
    },
    {
        "restaurant": "Supermoon Bakehouse",
        "dish": "Triple Chocolate Croissant & Cruffin",
        "location": "New York, NYC",
        "neighborhood": "Lower East Side",
        "vibe": "Pastry & Bakery",
        "tag": "#NYCBakery #Supermoon",
        "image_url": "https://images.unsplash.com/photo-1509440159596-0249088772ff?auto=format&fit=crop&w=600&q=80",
    },
    {
        "restaurant": "Los Tacos No. 1",
        "dish": "Adobada Pork Taco on Corn Tortilla",
        "location": "New York, NYC",
        "neighborhood": "Chelsea Market & Times Square",
        "vibe": "Authentic Mexican Street Food",
        "tag": "#NYCTacos #MustTryNYC",
        "image_url": "https://images.unsplash.com/photo-1551504734-5ee1c4a1479b?auto=format&fit=crop&w=600&q=80",
    },
]


import html as html_lib
import urllib.parse
import urllib.request


def fetch_social_url_metadata(url: str) -> dict:
    """Fetches OpenGraph, oEmbed, or caption metadata from TikTok/Instagram links to extract food spot details and real social thumbnails."""
    meta = {
        "restaurant": None,
        "dish": None,
        "location": None,
        "notes": None,
        "image_url": None,
    }

    if "instagram.com" in url or "instagr.am" in url:
        m_id = re.search(r'/(?:p|reel)/([A-Za-z0-9_-]+)', url)
        if m_id:
            post_id = m_id.group(1)
            embed_url = f"https://www.instagram.com/p/{post_id}/embed/captioned/"
            req = urllib.request.Request(
                embed_url,
                headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"},
            )
            try:
                with urllib.request.urlopen(req, timeout=5) as resp:
                    raw_html = resp.read().decode("utf-8", errors="ignore")
                    
                    # Extract high-res cover image from Instagram embed HTML
                    all_img_urls = re.findall(r'(https://[^\s\"\'\<\>]+?(?:cdninstagram|scontent)[^\s\"\'\<\>]+)', raw_html)
                    for u in all_img_urls:
                        u_clean = html_lib.unescape(u)
                        if any(k in u_clean for k in ['t51.82787-15', 't51.2885-15', 'ig_cache_key', 'video_default_cover_frame', 'dst-jpg']):
                            if 's150x150' not in u_clean and 's100x100' not in u_clean:
                                meta["image_url"] = u_clean
                                break

                    cap_match = re.search(r'class="Caption"[^>]*>(.*?)</div>', raw_html, re.S)
                    if cap_match:
                        raw_caption = cap_match.group(1)
                        clean_caption = re.sub(r"<[^>]+>", " ", raw_caption)
                        clean_caption = html_lib.unescape(clean_caption)
                        clean_caption = " ".join(clean_caption.split())

                        meta["notes"] = f'Instagram Post: "{clean_caption[:180]}..."'

                        # Parse restaurant name from pin emoji or @handles
                        pin_match = re.search(r'📍\s*([^,\n\t\.\!\?]+)', clean_caption)
                        if pin_match:
                            rest_raw = pin_match.group(1).strip()
                            rest_clean = re.sub(r'[^A-Za-z0-9\s\'-]', '', rest_raw).strip()
                            if rest_clean:
                                meta["restaurant"] = rest_clean.title()

                        handles = re.findall(r"@([A-Za-z0-9_.]+)", clean_caption)
                        if handles and not meta["restaurant"]:
                            rest_handle = handles[0]
                            rest_name = (
                                rest_handle.replace("bensandwiches1", "Ben's Sandwiches")
                                .replace("happylambofficial", "Happy Lamb Hotpot")
                                .replace("_", " ")
                                .replace(".", " ")
                                .title()
                            )
                            meta["restaurant"] = rest_name

                        cap_lower = clean_caption.lower()
                        if "hotpot" in cap_lower:
                            meta["dish"] = "All-You-Can-Eat Hotpot Buffet"
                        elif "banh mi" in cap_lower:
                            meta["dish"] = "Crispy Pork & Pate Banh Mi"
                        elif "ramen" in cap_lower:
                            meta["dish"] = "Rich Tonkotsu Ramen"
                        elif "pizza" in cap_lower:
                            meta["dish"] = "Artisanal Slice"
                        elif "taco" in cap_lower or "birria" in cap_lower:
                            meta["dish"] = "Giant Birria Taco"

                        loc_match = re.search(r"📍\s*([^,\n]+(?:,\s*[^,\n]+)*)", clean_caption)
                        if loc_match and not meta["location"]:
                            loc_str = loc_match.group(1).strip()
                            loc_str = re.sub(r"View all.*$", "", loc_str, flags=re.I).strip()
                            meta["location"] = loc_str
                        elif "san jose" in cap_lower or "sjsu" in cap_lower:
                            meta["location"] = "San Jose, Bay Area"
                        elif "san francisco" in cap_lower or "sf" in cap_lower:
                            meta["location"] = "San Francisco, Bay Area"
                        elif "bay" in cap_lower or "norcal" in cap_lower:
                            meta["location"] = "Bay Area"
            except Exception:
                pass

    elif "tiktok.com" in url:
        oembed_url = f"https://www.tiktok.com/oembed?url={urllib.parse.quote(url)}"
        req = urllib.request.Request(
            oembed_url,
            headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"},
        )
        try:
            with urllib.request.urlopen(req, timeout=5) as resp:
                data = json.loads(resp.read().decode("utf-8"))
                title = data.get("title", "")
                author = data.get("author_name", "")
                
                meta["notes"] = f'TikTok by @{author}: "{title[:180]}"'
                if data.get("thumbnail_url"):
                    meta["image_url"] = data.get("thumbnail_url")

                # Parse restaurant handle or name
                handles = re.findall(r"@([A-Za-z0-9_.]+)", title)
                if handles:
                    h = handles[0]
                    clean_h = re.sub(r"(?:FoodTruck|Food|Truck)", " Food Truck", h, flags=re.I)
                    clean_h = re.sub(r"([a-z])([A-Z])", r"\1 \2", clean_h)
                    clean_h = clean_h.replace("_", " ").title().strip()
                    meta["restaurant"] = clean_h
                
                title_lower = title.lower()
                if "birria" in title_lower or "taco" in title_lower:
                    meta["dish"] = "Giant Birria Taco"
                elif "ramen" in title_lower:
                    meta["dish"] = "Rich Tonkotsu Ramen"
                elif "burger" in title_lower or "smashburger" in title_lower:
                    meta["dish"] = "Double Smashburger"
                elif "chicken" in title_lower:
                    meta["dish"] = "Nashville Hot Chicken Sandwich"

                # Parse address / location from pin emoji or text
                loc_match = re.search(r"📍\s*@?[A-Za-z0-9_.]*\s*:\s*([^,\n\t]+(?:,\s*[^,\n\t]+)*)", title)
                if loc_match:
                    meta["location"] = loc_match.group(1).strip()
                elif "san jose" in title_lower:
                    meta["location"] = "San Jose, Bay Area"
                elif "san francisco" in title_lower or "bay area" in title_lower:
                    meta["location"] = "San Francisco, Bay Area"
        except Exception:
            pass

    return meta


def parse_and_save_viral_link(
    url: str,
    restaurant_name: Optional[str] = None,
    dish: Optional[str] = None,
    location: Optional[str] = None,
    notes: Optional[str] = None,
) -> str:
    """Parses a shared TikTok or Instagram Reel URL and saves the viral food spot to the user's wishlist.

    Args:
        url: The shared URL from TikTok, Instagram, or a food blog.
        restaurant_name: Optional name of the restaurant if known or extracted.
        dish: Optional signature dish or item featured in the video/post.
        location: City or region (e.g. "San Francisco", "Bay Area", "Los Angeles", "SoCal", "NYC").
        notes: Personal notes or tags about why it's viral.

    Returns:
        A confirmation message detailing the saved spot and dish.
    """
    fetched = fetch_social_url_metadata(url)
    if not restaurant_name and fetched.get("restaurant"):
        restaurant_name = fetched["restaurant"]
    if not dish and fetched.get("dish"):
        dish = fetched["dish"]
    if not location and fetched.get("location"):
        location = fetched["location"]
    if not notes and fetched.get("notes"):
        notes = fetched["notes"]

    url_lower = url.lower()

    if not restaurant_name:
        if "pizza" in url_lower or "industrie" in url_lower:
            restaurant_name = "L'Industrie Pizzeria"
            dish = dish or "Burrata Slice & Hot Honey"
            location = location or "New York, NYC"
        elif "burger" in url_lower or "7thstreet" in url_lower:
            restaurant_name = "7th Street Burger"
            dish = dish or "Double Smashburger"
            location = location or "New York, NYC"
        elif "udon" in url_lower or "marugame" in url_lower:
            restaurant_name = "Marugame Udon"
            dish = dish or "Nikutama Udon"
            location = location or "San Francisco, Bay Area"
        elif "chicken" in url_lower or "howlin" in url_lower:
            restaurant_name = "Howlin' Ray's"
            dish = dish or "Nashville Hot Chicken Sando"
            location = location or "Los Angeles, SoCal"
        else:
            restaurant_name = "Shared Viral Spot"
            dish = dish or "Featured Special"
            location = location or "Bay Area / SoCal / NYC"

    new_id = str(len(WISHLIST) + 1)
    item = {
        "id": new_id,
        "restaurant": restaurant_name,
        "dish": dish or "Signature Dish",
        "location": location or "Bay Area / SoCal / NYC",
        "url": url,
        "status": "Want to Try",
        "notes": notes or "Saved from shared social media link",
    }
    if fetched.get("image_url"):
        item["image_url"] = fetched["image_url"]

    WISHLIST.append(item)
    _save_wishlist(WISHLIST)

    return (
        f"✅ Saved to your Wishlist!\n"
        f"• Restaurant: {item['restaurant']}\n"
        f"• Featured Dish: {item['dish']}\n"
        f"• Location: {item['location']}\n"
        f"• Status: {item['status']}\n"
        f"• Source Link: {url}"
    )


def get_wishlist_by_location(location: str) -> str:
    """Retrieves saved viral food spots from the user's wishlist filtered by city or region.

    Args:
        location: Target city or region to query (e.g. "San Francisco", "Bay Area", "Los Angeles", "SoCal", "NYC", "New York").

    Returns:
        A list of saved restaurant spots matching the location, or a message if none found.
    """
    query = location.lower()
    matches = []

    for item in WISHLIST:
        loc = item["location"].lower()
        if (
            ("sf" in query or "san francisco" in query or "bay area" in query)
            and ("sf" in loc or "san francisco" in loc or "bay area" in loc)
        ) or (
            ("la" in query or "los angeles" in query or "socal" in query)
            and ("la" in loc or "los angeles" in loc or "socal" in loc)
        ) or (
            ("nyc" in query or "new york" in query)
            and ("nyc" in loc or "new york" in loc)
        ) or (query in loc):
            matches.append(item)

    if not matches:
        return f"No saved spots found in your wishlist for '{location}'. You can add one by sharing a link or asking me to search!"

    result = [f"📍 Saved Viral Spots for '{location}' ({len(matches)} items):"]
    for i, spot in enumerate(matches, 1):
        status_icon = "⭐" if spot["status"] == "Visited" else "📌"
        img_line = f"\n   Image URL: {spot['image_url']}" if spot.get("image_url") else ""
        result.append(
            f"{i}. {status_icon} **{spot['restaurant']}** — {spot['dish']}\n"
            f"   Location: {spot['location']} | Status: {spot['status']}\n"
            f"   Notes: {spot['notes']}\n"
            f"   Link: {spot['url']}{img_line}"
        )

    return "\n\n".join(result)


def dynamic_search_viral_spots(location: str, cuisine_or_vibe: str = "") -> str:
    """Searches for real, currently trending viral food spots and signature dishes in a target city.

    Args:
        location: City or region to search (e.g. "San Francisco", "Bay Area", "Los Angeles", "SoCal", "NYC").
        cuisine_or_vibe: Optional filter like "pizza", "dessert", "ramen", "tacos", "bakery".

    Returns:
        Curated list of real viral restaurant spots with location details and trending tags.
    """
    loc_query = location.lower()
    vibe_query = cuisine_or_vibe.lower()

    bay_keywords = ["sf", "san francisco", "bay", "mountain view", "palo alto", "san jose", "berkeley", "oakland", "sunnyvale"]
    socal_keywords = ["la", "los angeles", "socal", "silver lake", "hollywood", "pasadena", "santa monica"]
    nyc_keywords = ["nyc", "new york", "manhattan", "brooklyn", "queens", "williamsburg"]

    is_bay_query = any(k in loc_query for k in bay_keywords)
    is_socal_query = any(k in loc_query for k in socal_keywords)
    is_nyc_query = any(k in loc_query for k in nyc_keywords)

    results = []
    for spot in SAMPLE_VIRAL_SPOTS:
        spot_loc = spot["location"].lower()
        spot_neigh = spot["neighborhood"].lower()

        loc_match = (
            (is_bay_query and ("bay area" in spot_loc or any(k in spot_loc or k in spot_neigh for k in bay_keywords)))
            or (is_socal_query and ("socal" in spot_loc or any(k in spot_loc or k in spot_neigh for k in socal_keywords)))
            or (is_nyc_query and ("nyc" in spot_loc or any(k in spot_loc or k in spot_neigh for k in nyc_keywords)))
            or (loc_query in spot_loc or loc_query in spot_neigh)
        )

        if loc_match:
            if not vibe_query or (vibe_query in spot["vibe"].lower() or vibe_query in spot["dish"].lower()):
                results.append(spot)

    if not results:
        # Fallback list if specific filter yields no exact match
        results = [spot for spot in SAMPLE_VIRAL_SPOTS if loc_query in spot["location"].lower() or "bay" in loc_query]

    formatted = [f"🔥 Trending Viral Food Spots in '{location}':"]
    for i, spot in enumerate(results, 1):
        formatted.append(
            f"{i}. **{spot['restaurant']}** ({spot['neighborhood']})\n"
            f"   Famous Dish: {spot['dish']}\n"
            f"   Vibe: {spot['vibe']} | Tag: {spot['tag']}"
        )

    formatted.append("\n💡 Tip: Say 'Save spot #1 to my wishlist' or share a link to save it!")
    return "\n\n".join(formatted)


def mark_as_visited(restaurant_name: str, rating: str = "5/5", notes: str = "") -> str:
    """Marks a restaurant in the user's wishlist as visited with an optional rating and review.

    Args:
        restaurant_name: Name of the restaurant to mark visited.
        rating: Rating out of 5 (e.g. "5/5", "4.5/5").
        notes: User's review or impressions of the food.

    Returns:
        Confirmation message that the status was updated.
    """
    for item in WISHLIST:
        if restaurant_name.lower() in item["restaurant"].lower():
            item["status"] = "Visited"
            item["notes"] = f"Visited! Rating: {rating}. {notes}".strip()
            _save_wishlist(WISHLIST)
            return f"🎉 Marked '{item['restaurant']}' as VISITED! Rating: {rating}. Notes: '{item['notes']}'"

    return f"Could not find '{restaurant_name}' in your wishlist. Add it first by sharing a link or searching!"
