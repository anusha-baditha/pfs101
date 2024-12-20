from itsdangerous import URLSafeTimedSerializer
from key import salt
def encode(data):
    serializer=URLSafeTimedSerializer('Codegnan@123') #sdfghj
    return serializer.dumps(data,salt=salt)
def decode(data):
    serializer=URLSafeTimedSerializer('Codegnan@123')
    return serializer.loads(data,salt=salt)  #123
