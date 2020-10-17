"""
application
that takes an ingame name like Gin Barlow,
and finds the equipped main hand weapon of that char

"""

# https://xivapi.com/item/1676
import requests

names = ["Gin Barlow", "Akashi Hikari", "Galford Shimazu"]

for name in names:
    server = "Omega"  # maybe also chaos, or omega
    search_for_gin = "https://xivapi.com/character/search?name="+name+"&server="+server
    response = requests.get(search_for_gin).json()
    gins_id = response['Results'][0]['ID']
    # print("gins id: ", gins_id)

    # need to get something like
    # https://xivapi.com/character/31066505
    character_lookup = "https://xivapi.com/character/" + str(gins_id)
    response = requests.get(character_lookup).json()
    mainhand_id = response["Character"]["GearSet"]["Gear"]["MainHand"]["ID"]
    # print("mainhand id: ", mainhand_id)

    # lookup weapon
    weapon_lookup = "https://xivapi.com/item/" + str(mainhand_id)
    response = requests.get(weapon_lookup).json()
    print(name, "has a", response['Name'], "as a mainhand weapon")
