import discord  # pylint: disable=import-error
from discord.ext import commands  # pylint: disable=import-error
from settings.common import API_URL  # pylint: disable=import-error, no-name-in-module
from utils.tools import get_gql_client  # pylint: disable=import-error
from utils.queries import get_job_group  # pylint: disable=import-error
from os import system as sys

# Módulo principal do bot.

client = commands.Bot(command_prefix='--')

@client.event
async def on_ready():
    sys('clear')
    print('<----------On---------->')


@client.command()
async def h(bot):
    """
    Informa os comandos para consultas, cadastro e criações.
    """
    username = '<@!' + str(bot.author.id) + '>'

    body = (f'''
        Olá {username}, em que posso ajuda-lo?

        --job_group : <name> : Mostra as informações do grupo informado.
    ''')

    return await bot.send(body)

@client.command()
async def job_group(bot, _input):
    """
    Mostra o job group pelo nome.
    """
    username = '<@!' + str(bot.author.id) + '>'
    payload = get_job_group(_input)
    api_client = get_gql_client(API_URL)
    response = api_client.execute(payload)

    if not _input:
        return await bot.send(f'É necessário o nome grupo de atividades!')
    
    else:
        edges = response['jobGroup']['edges']
        node = edges[0].get('node') if edges else None
        job_name = node.get('name') if node else None
        job_description = node.get('description') if node else None

        embed = discord.Embed(color=0x8F2B10, type='rich')
        embed.add_field(name=f'{job_name}', value=f'{job_description}', inline=False)

        description = f'{username}, aqui está:'

        return await bot.send(description, embed=embed)
