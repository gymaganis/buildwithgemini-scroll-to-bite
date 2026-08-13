import asyncio
import os
import uuid
import google.auth
import google.auth.transport.requests
import httpx
from a2a.client import ClientConfig, create_client
from a2a.types import Message, Part, Role, SendMessageRequest

RESOURCE = os.environ.get("AGENT_ENGINE_RESOURCE_NAME", "projects/316809081798/locations/us-east1/reasoningEngines/4986276435871137792")
AGENT_DIRECTORY = os.environ.get("AGENT_DIRECTORY", "app")
LOCATION = RESOURCE.split("/locations/")[1].split("/")[0]

A2A_BASE = (
    f"https://{LOCATION}-aiplatform.googleapis.com/reasoningEngines/v1/"
    f"{RESOURCE}/api/a2a/{AGENT_DIRECTORY}"
)

_creds, _ = google.auth.default(scopes=["https://www.googleapis.com/auth/cloud-platform"])

def _auth_headers() -> dict[str, str]:
    _creds.refresh(google.auth.transport.requests.Request())
    return {
        "Authorization": f"Bearer {_creds.token}",
        "Content-Type": "application/json",
    }

async def main():
    print(f"Connecting to A2A_BASE: {A2A_BASE}")
    async with httpx.AsyncClient(headers=_auth_headers(), timeout=120) as client:
        a2a_client = await create_client(A2A_BASE, client_config=ClientConfig(httpx_client=client))
        msg = Message(
            message_id=str(uuid.uuid4()),
            role=Role.ROLE_USER,
            parts=[Part(text="What are the top viral spots in Mountain View, CA?")],
        )
        send_req = SendMessageRequest(message=msg)
        async for event in a2a_client.send_message(send_req):
            print("EVENT RECVD:", type(event), repr(event))

if __name__ == "__main__":
    asyncio.run(main())
