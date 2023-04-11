'''
This module contains the server adapter that lets us use HTTPS with SSL, since
Bottle doesn't support it normally.

Almost completely drawn from [this bottle-ssl template]
(https://github.com/nickbabcock/bottle-ssl/blob/master/main.py).
'''

import ssl
from bottle import ServerAdapter
from cheroot import wsgi
from cheroot.ssl.builtin import BuiltinSSLAdapter


# The certificate and Private Key files.
CERTIFICATE_PATH = "certificate/info2222.a1.crt"
PRIVATE_KEY_PATH = "certificate/info2222.a1.key"


class SSLCherootAdapter(ServerAdapter):
    '''
    An adapter class to set up Bottle to run in a Cheroot server.
    This allows it to use HTTPS.
    '''
    def run(self, handler):
        server = wsgi.Server((self.host, self.port), handler)
        server.ssl_adapter = BuiltinSSLAdapter(CERTIFICATE_PATH, PRIVATE_KEY_PATH)

        # By default, the server will allow negotiations with extremely old protocols
        # that are susceptible to attacks, so we only allow TLSv1.2 or later
        server.ssl_adapter.context.options |= ssl.OP_NO_TLSv1
        server.ssl_adapter.context.options |= ssl.OP_NO_TLSv1_1

        try:
            server.start()
        finally:
            server.stop()
