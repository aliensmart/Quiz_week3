from .orm import ORM

class TSLA(ORM):
    dbpath = ""
    tablename = "tsla"
    fields = ["open", "high", "low", "close", "adjust_close", "volume"]

    def __init__(self, **kwargs):
        self.pk = kwargs.get('pk')
        self.open = kwargs.get('open')
        self.high = kwargs.get('high')
        self.low = kwargs.get('low')
        self.close = kwargs.get('close')
        self.adjust_close = kwargs.get('adjust_close')
        self.volume = kwargs.get('volume')


