
from sites import site

__all__ = ('site',)

VERSION = "0.1.4"

def autodiscover():
    from autoload import autodiscover as discover
    discover("dynamic_actions")
