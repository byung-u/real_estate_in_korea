"""real_estate_in_korea trade check command line tool."""
import configparser
from real_estate_in_korea import defaults


class Options:
    """Options collected from input options."""
    def __init__(self) -> None:
        self.gu = None  # type: str
        self.dong = None  # type: str
        self.apt = None  # type: str
        self.size = 0.0  # month range  type: float
        self.month_range = 1  # month range  type: int

        config = configparser.ConfigParser()
        config.readfp(open(defaults.CONFIG_FILE))
        self.url = config.get('TOKEN', 'apt_trade_url')  # type: str
        self.svc_key = config.get('TOKEN', 'apt_key', raw=True)  # type: str
