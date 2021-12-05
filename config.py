class Config:
    pass

class DevConfig(Config):
    SECRET_KEY = b'\xcc^\x91\xea\x17-\xd0W\x03\xa7\xf8J0\xac8\xc5'
    SESSION_COOKIE_HTTPONLY = False
    SESSION_COOKIE_SECURE = True