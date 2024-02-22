import json

from Flat import Flat
from init import init
from ranges import ranges
from Block import Block

# Blocks and floors set up here

block_46a = Block("46A", 21, [254, 256, 262, 264])
block_46b = Block("46B", 21, [266, 268, 272, 274, 276, 278, 280])
block_46c = Block("46C", 22, [286, 288, 298, 304])
block_47a = Block("47A", 22, [306, 312, 322, 324])
block_47b = Block("47B", 20, [334, 336, 342, 344])
block_47c = Block("47C", 20, [346, 348, 356, 358])
block_48a = Block("48A", 19, [360, 362, 370, 372])
block_48b = Block("48B", 20, [374, 376, 382, 384])
block_48c = Block("48C", 19, [406, 408, 410, 412, 414])

blocks = [block_46a, block_46b, block_46c, block_47a, block_47b, block_47c, block_48a, block_48b, block_48c]

spreadsheet = "141K-NYQNkHSBeextMZm4-3lLLc1cXvsGYpPM4FIcbuc"


def get_price_and_availibity(range):
    price_and_availability = []
    sheet = service.spreadsheets()

    # Specify the fields parameter to include formatting information
    result = sheet.get(
        spreadsheetId=spreadsheet,
        ranges=[range],
        includeGridData=True
    ).execute()

    row_data = result.get("sheets")[0].get("data")[0].get("rowData")

    for dict in row_data:
        values = dict.get("values")
        price = values[0].get("formattedValue")
        color = list(values[0].get("userEnteredFormat").get("backgroundColor").keys())[0]
        if color == "green":
            price_and_availability.append((price, True))
        elif color == "red":
            price_and_availability.append((price, False))
        else:
            raise ValueError("Cell background cannot be determined")
    return price_and_availability


service = init()

flat_data = []

for block in blocks:
    # Get the flat numbers, then go into ranges to find spreadsheet range
    # Then, append the flats into blocks

    flat_positions = block.positions

    for position in flat_positions:
        floors = block.floors
        spreadsheet_range = ranges.get(position)
        price_and_availibity = get_price_and_availibity(spreadsheet_range)

        for price, availibility in price_and_availibity:
            flat = Flat(position, price, floors, block.block, availibility)
            floors -= 1
            flat_data.append(flat.__dict__)

    with open('flats.json', 'w') as json_file:
        json.dump(flat_data, json_file, indent=2)
