import os

SECRET_KEY = 'comictales'



SQLALCHEMY_DATABASE_URI = \
    '{SGBD}://{usuario}:{senha}@{servidor}/{database}'.format(
        SGBD='mysql+mysqlconnector',
        usuario='root',
        senha='4100.143',
        servidor='127.0.0.1',
        database='comictales'
    ) 