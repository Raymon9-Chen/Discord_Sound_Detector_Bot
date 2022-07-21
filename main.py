import board
import busio
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn
from time import sleep
import discord 
from discord.ext import commands
from time import sleep
import asyncio


client = discord.Client()
client.post_message = False

i2c = busio.I2C(board.SCL, board.SDA)
ads = ADS.ADS1115(i2c)
pin = AnalogIn(ads, ADS.P3)

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    if pin.voltage > 15000:
        await client.get.user(PERSONAL DISCORD ID HERE).send('Too Loud')
        
#replace placeholder with your discord ID
client.run(placeholder)
