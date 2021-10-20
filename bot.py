#bot.py

import cryptocompare
import discord
from discord.ext import commands
import math
import os
from dotenv import load_dotenv
import json
from web3 import Web3
import etherscan

#just loading shit
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix= '!')

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

#token converts

@bot.command(name='ETH', help='converts eth to usd')
async def ETH(ctx, n:float):
    x = cryptocompare.get_price('ETH', currency='USD')
    usdVal = (x.get('ETH')).get('USD')
    response = str(n) + ' ETH = '+ str(round(float(n*usdVal), 3)) + ' USD'
    embed=discord.Embed(description=response,color=0xfc5356)
    embed.set_footer(text='1 ETH = ' + str(usdVal) + ' USD')
    await ctx.send(embed=embed)

@bot.command(name='EUSD', help='converts usd to eth')
async def EUSD(ctx, n:float):
    x = cryptocompare.get_price('ETH', currency='USD')
    usdVal = (x.get('ETH')).get('USD')
    response = str(n) + ' USD = '+ str(round(float(n/usdVal), 3)) + ' ETH'
    embed=discord.Embed(description=response,color=0xfc5356)
    embed.set_footer(text='1 ETH = ' + str(usdVal) + ' USD')
    await ctx.send(embed=embed)

@bot.command(name='SOL', help='converts sol to usd')
async def SOL(ctx, n:float):
    x = cryptocompare.get_price('SOL', currency='USD')
    usdVal = (x.get('SOL')).get('USD')
    response = str(n) + ' SOL = '+ str(round(float(n*usdVal), 3)) + ' USD'
    embed=discord.Embed(description=response,color=0xfc5356)
    embed.set_footer(text='1 SOL = ' + str(usdVal) + ' USD')
    await ctx.send(embed=embed)

@bot.command(name='SUSD', help='converts usd to sol')
async def SUSD(ctx, n:float):
    x = cryptocompare.get_price('SOL', currency='USD')
    usdVal = (x.get('SOL')).get('USD')
    response = str(n) + ' USD = '+ str(round(float(n/usdVal), 3)) + ' SOL'
    embed=discord.Embed(description=response,color=0xfc5356)
    embed.set_footer(text='1 SOL = ' + str(usdVal) + ' USD')
    await ctx.send(embed=embed)

bot.command(name='eth')(ETH.callback)
bot.command(name='eusd')(EUSD.callback)
bot.command(name='sol')(SOL.callback)
bot.command(name='susd')(SUSD.callback)

#web3 poggers
infura_url = 'https://mainnet.infura.io/v3/11eef71d1caa4dadbd86128029c96f54'

es = etherscan.Client(
    api_key='EVRGAYVAMCTKJG53NV2KYZP8FZYZ5CBZIR',
    cache_expire_after=5,
)

@bot.command(name='bal', help='checks balance of wallet')
async def bal(ctx, w:str):
    num = es.get_eth_balance(w)
    usd = es.get_eth_price()
    val = usd*num
    embed=discord.Embed(title=w, description=str(num) +' ETH', color=0xfc5356)
    embed.set_footer(text ='$'+str(val))


@bot.commmand(name='gas', help='gets current gas in GWEI')
async def gas(ctx):
    result = es.get_gas_price()
    embed=discord.Embed(description=str(result) + ' GWEI', color=0xfc5356)

bot.run(TOKEN)