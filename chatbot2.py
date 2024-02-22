import asyncio
import logging

from pymongo import MongoClient
from telegram import Bot


logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# MongoDB connection
mongo_client = MongoClient('mongodb+srv://shaugntan:T0024416z.@flats.dey3g18.mongodb.net/')
db = mongo_client["flats"]
collection = db["flats"]


# Telegram bot setup
telegram_token = "6771753067:AAH-jEcwHYahM1fHFoVUCT4sfKR4yp_HXY8"
telegram_bot = Bot(token=telegram_token)
chat_id = "728452374"

async def send_telegram_message(message):
    await telegram_bot.send_message(chat_id=chat_id, text=message)

async def get_flat_details(change):
    id = change.get('documentKey').get('_id')
    flat_document = collection.find_one({"_id" : id})
    return flat_document

async def taken_message(flat_document):
    block =  flat_document.get("block")
    floor = flat_document.get("floor")
    number = flat_document.get("number")
    return "Flat {} at floor {} has been taken!".format(number, floor)

async def monitor_changes():
    with collection.watch() as stream:
        for change in stream:
            await send_telegram_message(await taken_message(await get_flat_details(change)))

async def main():
    try:
        await monitor_changes()
    except Exception as e:
        print(f"Error: {e}")
    finally:
        mongo_client.close()

if __name__ == "__main__":
    # Create an event loop and run the main function
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
