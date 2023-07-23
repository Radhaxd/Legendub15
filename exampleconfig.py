from sample_config import Config


class Development(Config):
    # get this values from the my.telegram.org
    APP_ID = 10940339
    API_HASH = "4cdbbcc7a57756127b1f3df13a7ee175"
    # the name to display in your alive message
    ALIVE_NAME = "RadhaUserBot"
    # create any PostgreSQL database (i recommend to use elephantsql) and paste that link here
    DB_URI = "postgres://xhagcmjv:RcihLUmDeUm5X8oZwsr5iaesaVrBxxXi@mahmud.db.elephantsql.com/xhagcmjv"
    # After cloning the repo and installing requirements do python3 telesetup.py an fill th this
    LEGEND_STRING = "1AZWarzYBu1I7L5wVNc_ShdZBulrEMlXTg9gXRZAMA7M4gZsslG2it1dvnvNf2sS9-cXTyuEuaCAG-STLcGg--6BzXzbT0fo2xUfiSAg-XtEvtXkL4CDytFCNAQqrN7uw2FuezdXXwn-Sl5I5HI9TaLBjvNN1e_T5elJt4M741wXvgRyvv3vVMGpr8Tvh6nBz9-KxEiVZ_PQrx8tfGJV17K4uH9aprpeGN4n3uMulmgj6PSmYzKZ56RWoOjK3fCgPfqhl3G7xjlKAqF-7ToqB3j23fnhLJtSaCNO708ntl1lGO5eIhN2_Hoonc2LiyTcQVt8vh4RMBCYE1bL39t9qm-1O8f4u7Jg="
    # create a new bot in @botfather and fill the following vales with bottoken
    BOT_TOKEN = "6012629686:AAHOfgIMs6jvRk360SxLy8jylDQQIJxFA5c"
    # command handler
    HANDLER = "."
    # command hanler for sudo
    SUDO_HANDLER = "."
    # External plugins repo
    EXTERNAL_REPO = True
    EXTERNAL_REPOBRANCH = "main"
    UPSTREAM_REPO = "pro"
    VCMODE = False
    # Your City's TimeZone
    TZ = "Asia/Kolkata"
