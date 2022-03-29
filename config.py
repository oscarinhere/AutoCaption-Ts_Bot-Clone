import os



class Config(object):
      BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "5255784985:AAEnonBIW-x8fn6xAJiNRVequMhQ8cyVGU8")
      API_ID = int(os.environ.get("APP_ID", 14372439))
      API_HASH = os.environ.get("API_HASH", 6641f7d2fcb6380e4f64ffa4a38a09ac))
      CAPTION_POSITION = os.environ.get("CAPTION_POSITION", "nil")
      ADMIN_USERNAME = os.environ.get("ADMIN_USERNAME", "Ts_Bots")
      ADMIN_ID = int(os.environ.get("ADMIN_ID", 1363227841 )) 
      DB_URL = os.environ.get("DATABASE_URL", "postgres://ghdbftiq:HbQZU1clfNyL_n_8HSu1rThQrvAXv34i@jelani.db.elephantsql.com/ghdbftiq ")
