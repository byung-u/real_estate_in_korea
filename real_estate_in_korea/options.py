"""real_estate_in_korea trade check command line tool."""
import os


class Options:
    """Options collected from input options."""
    def __init__(self) -> None:
        self.gu = None  # type: str
        self.dong = None  # type: str
        self.apt = None  # type: str
        self.size = 0.0  # month range  type: float
        self.month_range = 1  # month range  type: int
        self.start_month = '0'  # month range  type: str

        self.trade_url = os.environ.get('DATA_APT_TRADE_URL')  # type: str
        self.rent_url = os.environ.get('DATA_APT_RENTE_URL')  # type: str
        self.svc_key = os.environ.get('DATA_APT_API_KEY')  # type: str
        self.mode = 0  # 0: trade, 1: rent type: int
        self.text = False  # test output use
