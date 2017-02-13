"""real_estate_in_seoul trade check command line tool."""

import configparser


class Options:
    """Options collected from input options."""
    def __init__(self) -> None:
        self.gu = None  # type: str
        self.dong = None  # type: str
        self.apt = None  # type: str
        self.month_range = 1  # month range  type: int

        config = configparser.ConfigParser()
        config.readfp(open('./bot.ini'))
        self.url = config.get('TOKEN', 'apt_trade_url')  # type: str
        self.svc_key = config.get('TOKEN', 'apt_key', raw=True)  # type: str
