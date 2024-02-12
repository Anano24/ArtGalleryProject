from os import path


class Config:
    BASE_DIRECTORY = path.abspath(path.dirname(__file__))
    UPLOAD_PATH = path.join(BASE_DIRECTORY, "static", "img")
    SECRET_KEY = "abjdlhrjekls78akkjluiillakqawss"
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + path.join(BASE_DIRECTORY, "database.db")
    FLASK_ADMIN_SWATCH = "Journal"


