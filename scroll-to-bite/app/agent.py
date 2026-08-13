# ruff: noqa
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

from a2ui.basic_catalog.provider import BasicCatalog
from a2ui.schema.manager import A2uiSchemaManager
from google.adk.agents import Agent
from google.adk.apps import App
from google.adk.models import Gemini
from google.genai import types

from app.a2ui_utils import a2ui_callback
from app.tools import (
    dynamic_search_viral_spots,
    get_wishlist_by_location,
    mark_as_visited,
    parse_and_save_viral_link,
)

MODEL = "gemini-3.6-flash"

schema_manager = A2uiSchemaManager(
    version="0.8",
    catalogs=[BasicCatalog.get_config("0.8")],
)

a2ui_instruction = schema_manager.generate_system_prompt(
    role_description=(
        "You are ScrollToBite, a savvy food concierge for Bay Area, SoCal, and NYC foodies. "
        "You help users save viral food spots from shared TikTok/Instagram links, retrieve saved wishlist "
        "items whenever they visit a city (SF/Bay Area, LA/SoCal, NYC), discover trending viral dishes, "
        "and track visited restaurants. "
        "You remember the user's home city, dietary restrictions, favorite cuisines, and preferences "
        "across sessions to personalize your recommendations."
    ),
    workflow_description="Analyze the user's request, run appropriate tools, and return structured A2UI cards when presenting restaurant spots or wishlists.",
    ui_description=(
        "Keep every surface tiny and flat: ONE Card > ONE Column > a few Text rows and an Image if available. "
        "Never nest a Card inside a Card. "
        "Use ONLY these components: Card, Column, Row, Text, and Image. "
        "When returning restaurant spots or saved wishlist items, ALWAYS render an A2UI Card for each spot. "
        "ALWAYS include an Image component if an image_url or Image URL is provided in the tool output. "
        "Set the Image url property to that exact https link. "
        "No markdown in text; use usageHint ('h1', 'h2', 'body', 'caption') for formatting. "
        "Output ONLY the raw A2UI JSON array when returning UI components."
    ),
    include_schema=True,
    include_examples=True,
)


root_agent = Agent(
    name="scroll_to_bite_agent",
    model=Gemini(
        model=MODEL,
        retry_options=types.HttpRetryOptions(attempts=3),
    ),
    instruction=a2ui_instruction,
    tools=[
        parse_and_save_viral_link,
        get_wishlist_by_location,
        dynamic_search_viral_spots,
        mark_as_visited,
    ],
    after_model_callback=a2ui_callback,
)

app = App(
    root_agent=root_agent,
    name="app",
)
