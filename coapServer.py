import asyncio
import logging
import aiocoap.resource as resource
import aiocoap

logging.basicConfig(level=logging.INFO)

class TemperatureResource(resource.Resource):
    async def render_get(self, request):
        payload = b"25"  
        return aiocoap.Message(payload=payload)

async def main():
   
    root = resource.Site()
    root.add_resource(['temperature'], TemperatureResource())

    await aiocoap.Context.create_server_context(root)
    await asyncio.get_running_loop().create_future() 

if __name__ == "__main__":
    asyncio.run(main())