# My agent: ScrollToBite
One-liner: A conversational food concierge that lets you paste/share TikTok & Instagram links while doom scrolling, extracts restaurant & dish details, saves them to your wishlist, and notifies you of saved spots whenever you visit a city (Bay Area, SoCal, NYC).

Tool coverage:
- Memory: Saved wishlist (shared links, spot name, dish, location, status) and user's preferred regions.
- Tools: 
  - parse_and_save_viral_link(url) - Extracts restaurant, dish, and city from shared TikTok/IG URLs and saves to wishlist.
  - get_wishlist_by_location(city_or_region) - Retrieves saved spots when user asks "I'm in LA today, what's on my list?".
  - dynamic_search_viral_spots(location, query) - Discovers new trending spots dynamically on demand.
  - mark_as_visited(spot_id, rating) - Updates wishlist status.
- Catalog/UI: Collection of saved viral spots rendered as rich restaurant cards with dish photos and original video links.
- Image gen: Generates food artwork or menu previews.
- Sandbox: Bill/tip splitting and route distance calculations.

Core rails (everyone): memory, tools, eval, deploy, frontend
My stretch menu (pick later): A2UI restaurant cards, link extraction, Imagen food visuals, Code Sandbox bill calculator.
First eval question: "I'm visiting San Francisco today — do I have any saved viral spots on my wishlist for SF?"
