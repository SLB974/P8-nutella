"""Config variables"""

from decouple import config

SECRET_KEY = config("SECRET_KEY")
DEBUG=config("DEBUG", default=False)
BDD_PASSW=config('BDD_PASSW')
