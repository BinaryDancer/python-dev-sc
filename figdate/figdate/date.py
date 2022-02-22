from time import gmtime, strftime
from pyfiglet import Figlet


def date(date_format='%Y %d %b, %A', font='graceful'):
    f = Figlet(font=font)
    print(f.renderText(strftime(date_format, gmtime())))