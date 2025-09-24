import asyncio
import logging
from aiocoap import *

logging.basicConfig(level=logging.INFO)

async def main():
    protocol = await Context.create_client_context()

    request = Message(code=GET, uri="coap://localhost/temperature")

    try:
        response = await protocol.request(request).response
    except Exception as e:
        print("Failed to fetch resource:")
        print(e)
    else:
        print("Response Code:", response.code)
        print("Payload:", response.payload.decode())

if __name__ == "__main__":
    asyncio.run(main())
