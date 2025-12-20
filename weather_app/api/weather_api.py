import aiohttp

API_URL ="https://api.open-meteo.com/v1/forecast?latitude=41.01&longitude=28.97&current_weather=true"

async def fetch_weather():
    async with aiohttp.ClientSession() as session:
        async with session.get(API_URL) as resp:
            data = await resp.json()
            w =data["current_weather"]
            return{
                "temperature":w["temperature"],
                "description":"Clear"
            }