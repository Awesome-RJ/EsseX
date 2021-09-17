class Config(object):
    LOGGER = True
    API_ID = 2528049
    API_HASH = "49dd6c481ec8e40daf7be44a4ed33200"
    TOKEN = "1461817097:AAFLpVeTvZ_r02_voW0LdPTzRG-d_Wo-5yA"
    DB_URI = "postgres://cqmbulme:WJy6maWsIi5E6BoTP2IsRT6dFk0N0RjB@queenie.db.elephantsql.com:5432/cqmbulme"
    LOG_CHANNEL = 0 # if you want a logging channel you can add this, else logs will go into Owner's PM

class Development(Config):
    TEST_DEVELOP = True
    LOGGER = True
