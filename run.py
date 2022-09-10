import logging
import os
import sys

from tt_bot import TamTamBot

logging.basicConfig(format="%(asctime)s %(levelname)s %(message)s")
log = logging.getLogger()
logging.getLogger("PIL").setLevel(logging.INFO)
logging.getLogger("urllib3").setLevel(logging.INFO)
log.setLevel(logging.INFO)


def run():
    tg_token = os.environ.get("TELEGRAM_BOT_TOKEN")
    if tg_token is None:
        print("env var TELEGRAM_BOT_TOKEN must be set")
        sys.exit(1)

    tt_token = os.environ.get("TAMTAM_BOT_TOKEN")
    if tt_token is None:
        print("env var TAMTAM_BOT_TOKEN must be set")
        sys.exit(1)
    log.info("starting bot...")
    tt_bot = TamTamBot(tt_token, tg_token)
    tt_bot.run()


run()
