import discord  # pylint: disable=import-error
from discord.ext import commands  # pylint: disable=import-error
from settings.common import API_URL
from utils.tools import get_gql_client
from utils.queries import get_job_group
from os import system as sys

# Módulo principal do bot.

client = commands.Bot(command_prefix='-')

@client.event()
async def on_ready():
    sys('clear')
    print('<----------On---------->')


@client.command()
async def jobgroup(bot, _input):
    """
    Mostra o job group pelo nome.
    """
    api_client = get_gql_client(API_URL)
    response = api_client.execute(_input)
    user = bot.author.id

    if not _input:
        return await bot.send(f'É necessário o nome grupo de atividades!')
    
    else:
        edges = response['jobGroup']['edges']
        node = edges[0].get('node') if edges else None
        job_name = node.get('name') if node else None
        job_description = node.get('description') if node else None

        embed = discord.Embed(color=0x1B1E94, type='rich')
        embed.add_field(name=f'{job_name}', value=f'{job_description}', inline=False)

        description = f'{user}, aqui está:'

        return await bot.send(description, embed=embed)
