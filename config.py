import os
basedir=os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY=os.environ.get('SECRET_KEY') or 'hard to guess string'
    MAIL_SERVER=os.environ.get('MAIL_SERVER','smtp.googlemail.com')
    MAIL_PORT=int(os.environ.get('MAIL_PORT','587'))
    MAIL_USE_TLS=os.environ.get('MAIL_USE_TLS','true').lower() in ['true','on','1']
    MAIL_USERNAME=os.environ.get('MAIL_USERNAME') or 'Ray'
    MAIL_PASSWORD=os.environ.get('MAIL_PASSWORD') or 'ray123'
    FLASKY_MAIL_SUBJECT_PREFIX='[Flasky]'
    FLASKY_MAIL_SENDER='Flasky Admin<flasky@example.com>'
    FLASKY_ADMIN=os.environ.get('FLASKY_ADMIN') or 'FLASKY_ADMIN'
    SQLALCHEMY_COMMIT_ON_TEARDOWN=True
    SQLALCHEMY_TRACK_MODIFICATIONS=False
    FLASKY_POSTS_PER_PAGE=10
    FLASKY_COMMENTS_PER_PAGE=10

    @staticmethod
    def init_app(app):
        pass

class DevelopmentConfig(Config):
    DEBUG=True
    SQLALCHEMY_DATABASE_URI=os.environ.get('DEV_DATABASE_URL') or 'mysql://root:2014051903@localhost/flasky_dev'

class TestConfig(Config):
    TESTING=True
    SQLALCHEMY_DATABASE_URI=os.environ.get('TEST_DATABASE_URL') or 'mysql://root:2014051903@localhost/flasky_test'

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI=os.environ.get('DATABASE_URL') or 'mysql://root:2014051903@localhost/flasky'

config={
        'development':DevelopmentConfig,
        'testing':TestConfig,
        'production':ProductionConfig,

        'default':DevelopmentConfig
        }
