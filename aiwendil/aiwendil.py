import discord  # pylint: disable=import-error
from discord.ext import commands  # pylint: disable=import-error
from os import system as sys
from settings.common import API_URL  # pylint: disable=import-error, no-name-in-module
from utils.tools import get_gql_client, decode_b64  # pylint: disable=import-error
from utils.queries import get_job_group, get_ppe  # pylint: disable=import-error


# Módulo principal do bot.

client = commands.Bot(command_prefix='>> ')
API = get_gql_client(API_URL)
DA ='<@'
FUCK = '>' 

@client.event
async def on_ready():
    sys('clear')
    print('''
      ______   __                                          __  __  __ 
     /      \ |  \                                        |  \|  \|  |
    |  $$$$$$\| $$ __   __   __   ______   _______    ____| $$| $$| $$
    | $$__| $$| $$|  \ |  \ |  \ /      \ |       \  /      $$| $$| $$
    | $$    $$| $$| $$ | $$ | $$|  $$$$$$\| $$$$$$$\|  $$$$$$$| $$| $$
    | $$$$$$$$| $$| $$ | $$ | $$| $$    $$| $$  | $$| $$  | $$| $$| $$
    | $$  | $$| $$| $$_/ $$_/ $$| $$$$$$$$| $$  | $$| $$__| $$| $$| $$
    | $$  | $$| $$ \$$   $$   $$ \$$     \| $$  | $$ \$$    $$| $$| $$
     \$$   \$$ \$$  \$$$$$\$$$$   \$$$$$$$ \$$   \$$  \$$$$$$$ \$$ \$$
                                                                    
    ''')

@client.command()
async def h(bot):
    """
    Informa os comandos para consultas, cadastro e criações.
    """
    username = DA + str(bot.author.id) + FUCK

    body = (f'''
    Olá {username}, em que posso ajuda-lo? Logo digo, ">> " é meu prefixo!

        ```
    mithrandir : <string> : Retorna informações sobre a EPI informada.

    h : Mostra essa mensagem.

        ```
    ''')

    return await bot.send(body)


@client.command()
async def b64d(bot, _input):
    """
    Trás informações sobre a API mithrandir.
    """
    username = DA + str(bot.author.id) + FUCK

    try:
        response = decode_b64(_input)

        return await bot.send(f'''
{username}, aqui está meu caro amigo!

`{response}`
        ''')

    except:
        return await bot.send(f'''
       
{username}, se quer meu conselho parar usar aquele seu "fumo de corda"!

`Você está me passando um valor inválido!`

        ''')


@client.command()
async def mithrandir(bot, *_input):
    """
    Trás informações sobre a API mithrandir.
    """
    username = DA + str(bot.author.id) + FUCK
    command = ' '.join(_input)
    if not _input:

        return await bot.send(f'''
        Olá {username}, estou aqui para te ajudar com questões sobre a API mithrandir!
        Para obter a informação desejada informe o comando `>> mithrandir -comando`.


        ```
        -eq : Trás a query usada para obter informações sobre equipamentos de proteção individual!
        ```
        ''')
    
    if command == '-eq':
        return await bot.send(get_ppe())

    return await bot.send(f'''
    Ai ai ai, meu caro {username}, tá usando drogas de novo né!?

    Sua entrada foi {command}
    ''')
