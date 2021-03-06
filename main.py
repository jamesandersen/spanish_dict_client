import logging
import sys
import os

from dotenv import load_dotenv
from pathlib import Path
from spanish_dict.spanish_dict_client import SpanishDictionaryClient
#from techscreen import num_to_words

# Merriam-Webster API
# https://dictionaryapi.com/account/my-keys

def main():
    setup_logging()
    load_dotenv()
    logger = logging.getLogger(__name__)
    logger.info("Starting Spanish Dict program")

    sp_dict_client = SpanishDictionaryClient(os.environ['SPANISH_DICT_API_KEY'])

    result = sp_dict_client.get_spanish_short_definitions("food")
    print(f"food has the following spanish translations: {', '.join(result)}")


def setup_logging():
    logPath = Path(Path.cwd(), "logs")
    logPath.mkdir(exist_ok=True)

    # https://docs.python.org/3/library/logging.html#logrecord-attributes
    #logFormat = "%(asctime)s [%(threadName)-12.12s] [%(name)s] [%(levelname)-5.5s]  %(message)s"
    #logFormat = "%(asctime)s [%(name)s] [%(levelname)-5.5s]  %(message)s"
    logFormat = "[%(levelname)-5.5s]  %(message)s"
    logFormatter = logging.Formatter(logFormat)
    rootLogger = logging.getLogger()
    rootLogger.setLevel(logging.INFO)

    fileHandler = logging.FileHandler("{0}/{1}.log".format(str(logPath), "application"))
    fileHandler.setFormatter(logFormatter)
    rootLogger.addHandler(fileHandler)

    consoleHandler = logging.StreamHandler()
    consoleHandler.setFormatter(logFormatter)
    rootLogger.addHandler(consoleHandler)
    


if __name__ == "__main__":
    main()
