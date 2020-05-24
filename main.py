from settings.common import TOKEN  # pylint: disable=no-name-in-module
from aiwendil.aiwendil import client


if __name__ == '__main__':
    client.run(TOKEN)

