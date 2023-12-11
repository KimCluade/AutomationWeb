from config.default import *

SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(os.path.join(BASE_DIR, 'pybo.db'))
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = b'\x19\xd3\xe4\x94_\xfb8\xe0\xdc\x9b\x04\xdc\xfb\xd0I\xc0'
