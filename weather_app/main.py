import asyncio

from database import Base, engine
from repository.weather_repository import WeatherRepository
from services.weather_service import WeatherService

Base.metadata.create_all(bind=engine)


async def run():
    service = WeatherService(WeatherRepository())
    print("Hava durumu aliniyor")
    await service.fetch_and_save("istanbul")

    print("\nkayitli hava durumu verileri:")
    for w in service.list_records():
        print(f"{w.city} - {w.temperature} - {w.description} ")


asyncio.run(run())
