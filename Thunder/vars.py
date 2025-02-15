# Thunder/vars.py

import os
from dotenv import load_dotenv
from typing import Set, Optional

load_dotenv()


def str2bool(value: str) -> bool:
    """
    Convert a string to a boolean.

    Args:
        value (str): The string to convert.

    Returns:
        bool: The converted boolean value.
    """
    return value.lower() in ('true', '1', 'yes', 'y', 't')


class Var:
    """
    Configuration variables for the bot.
    """
    # Telegram API credentials
    API_ID: int = int(os.getenv('API_ID', '10660564'))
    API_HASH: str = os.getenv('API_HASH', '527e6297989f4e7cda5091f5bf41d0e4')

    # Bot token
    BOT_TOKEN: str = os.getenv('BOT_TOKEN', '7239597095:AAEISDjMXXH5kE-bx9R6sUnms4toZWQuTEw')

    # Bot name
    NAME: str = os.getenv('NAME', 'Radhaji_FileStream_Bot')

    # Sleep threshold
    SLEEP_THRESHOLD: int = int(os.getenv('SLEEP_THRESHOLD', '60'))

    # Number of workers
    WORKERS: int = int(os.getenv('WORKERS', '8'))

    # Channel ID where files are stored
    BIN_CHANNEL: int = int(os.getenv('BIN_CHANNEL', '-1002416466147'))

    # Web server configurations
    PORT: int = int(os.getenv('PORT', '8080'))
    BIND_ADDRESS: str = os.getenv('WEB_SERVER_BIND_ADDRESS', '0.0.0.0')
    PING_INTERVAL: int = int(os.getenv('PING_INTERVAL', '1200'))  # 20 minutes
    NO_PORT: bool = str2bool(os.getenv('NO_PORT', 'True'))

    # Owner details
    OWNER_ID: Set[int] = set(int(x) for x in os.getenv('OWNER_ID', '7737048829').split() if x.isdigit())
    OWNER_USERNAME: str = os.getenv('OWNER_USERNAME', 'PRESIDENTIND7')

    # Application configurations
    APP_NAME: str = os.getenv('APP_NAME', '')
    ON_HEROKU: bool = 'DYNO' in os.environ

    # Fully Qualified Domain Name
    if ON_HEROKU:
        FQDN: str = os.getenv('FQDN', '') or f"{APP_NAME}.herokuapp.com"
    else:
        FQDN: str = os.getenv('FQDN', BIND_ADDRESS)

    # SSL configuration
    HAS_SSL: bool = str2bool(os.getenv('HAS_SSL', 'True'))
    URL: str = f"https://{FQDN}/" if HAS_SSL else f"http://{FQDN}/"

    # Database URL
    DATABASE_URL: str = os.getenv('DATABASE_URL', 'mongodb+srv://Koi:Lok@cluster0.bt8r7.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0')

    # Updates channel
    UPDATES_CHANNEL: Optional[str] = os.getenv('-1002386857422')

    # Banned channels
    BANNED_CHANNELS: Set[int] = set(
        int(x) for x in os.getenv('BANNED_CHANNELS', '-1002374738987').split() if x.lstrip('-').isdigit()
    )

    # Multi-client support
    MULTI_CLIENT: bool = False
