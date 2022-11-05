import discord
from discord.ext import commands
import os
import pickle
import random
import asyncio
import json
from discord.ext.commands import (
    has_permissions,
    MissingPermissions,
    has_role,
    MissingRole,
    cooldown,
    BucketType,
    NotOwner,
    CommandNotFound,
    MissingRequiredArgument,
)

arr = "<a:right:1028269253285122068>"
comp = "<a:upvote:1028269240844816505>"
sold = "<:Soldier_Buzz:966705306342129704>"
res = "<:Resources:994990321240912052>"
tank = "<:tank:994712805448093696>"
strike = "<:strike:1025877750298452028>"
wall = "<:wall:1006892740375760959>"
data_filename = "currency files/data.pickle"
green = 0x567d46
red = 0xFF0000
yellow = 0xFFD700

class Data:
      def __init__(self, resources, soldiers, tanks, spy, wall, strikes):
        self.resources = resources
        self.soldiers = soldiers
        self.tanks = tanks
        self.spy = spy
        self.wall = wall
        self.strikes = strikes
        
        

class clans(commands.Cog):
    def __init__(self, client): 
        self.client = client


    





def setup(client):
    client.add_cog(clans(client))   

def load_data():
        if os.path.isfile(data_filename):
            with open(data_filename, "rb") as file:
              return pickle.load(file)
        else:
            return dict()


def load_member_data(member_ID):
    data = load_data()

    if member_ID not in data:
        return Data(0, 0, 0, 0, 0, 0)

    return data[member_ID]

def save_member_data(member_ID, member_data):
    data = load_data()

    data[member_ID] = member_data

    with open(data_filename, "wb") as file:
        pickle.dump(data, file)