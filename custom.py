from util import *
import os

TOPIC = 'SendFlag'


# HTTP or WebSocket connection, url, chainId, isPoA
def get_url():
    return True, "http://eth", 97, True


def check(acct, tx_hash, cont_if):
    return check_if_has_topic(acct.address, tx_hash, cont_if, TOPIC)


# public = False : Deploy
# public = True : Preview the source code
def code(public=True):
    if(public):
        # return ""
        # If you don't want user to see the source code, just return ""
        with open('./eth.sol', 'r') as f:
            SRC_TEXT = f.read()
            source = SRC_TEXT.replace(
                '$RAND_INT$', '0')
    else:
        with open('./eth.sol', 'r') as f:
            SRC_TEXT = f.read()
            source = SRC_TEXT.replace(
                '$RAND_INT$', str(int.from_bytes(os.urandom(16), 'little')))
    return source
