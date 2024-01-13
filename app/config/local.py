class Config:
    SQLALCHEMY_DATABASE_URI = "sqlite:///prello.db"
    JWT_SECRET_KEY = "super-secret"
    SECRET_KEY = "super-secret"
    JWT_TOKEN_LOCATION = 'cookies'
    JWT_COOKIE_CSRF_PROTECT = True
    JWT_CSRF_CHECK_FORM = True
    DEBUG = True
