import json
import falcon

__author__ = 'Evren Esat Ozkan'

#
# class SessionMiddleware(object):
#     """
#     just for easier access to session dict
#     """
#     def process_request(self, req, resp):
#         req.session = req.env['session']


ALLOWED_ORIGINS = ['http://127.0.0.1:8080', 'http://127.0.0.1:9001', 'http://104.155.6.147']

class CORS(object):
    """
    allow origins
    """
    def process_response(self, request, response, resource):
        origin = request.get_header('Origin')
        # if origin in ALLOWED_ORIGINS:
        response.set_header(
            'Access-Control-Allow-Origin',
            origin
        )
        response.set_header(
            'Access-Control-Allow-Credentials',
            "true"
        )
        response.set_header(
            'Access-Control-Allow-Headers',
            'Content-Type'
        )
        # This could be overridden in the resource level
        response.set_header(
            'Access-Control-Allow-Methods',
            'OPTIONS'
        )


class RequireJSON(object):
    def process_request(self, req, resp):
        if not req.client_accepts_json:
            raise falcon.HTTPNotAcceptable(
                'This API only supports responses encoded as JSON.',
                href='http://docs.examples.com/api/json')
        if req.method in ('POST', 'PUT'):
            if 'application/json' not in req.content_type and 'text/plain' not in req.content_type:
                raise falcon.HTTPUnsupportedMediaType(
                    'This API only supports requests encoded as JSON.',
                    href='http://docs.examples.com/api/json')


class JSONTranslator(object):
    def process_request(self, req, resp):
        # req.stream corresponds to the WSGI wsgi.input environ variable,
        # and allows you to read bytes from the request body.
        #
        # See also: PEP 3333
        if req.content_length in (None, 0):
            # Nothing to do
            req.context['data'] = {}
            req.context['result'] = {}
            return
        else:
            req.context['result'] = {}

        body = req.stream.read()
        if not body:
            raise falcon.HTTPBadRequest('Empty request body',
                                        'A valid JSON document is required.')

        try:
            req.context['data'] = json.loads(body.decode('utf-8'))

        except (ValueError, UnicodeDecodeError):
            raise falcon.HTTPError(falcon.HTTP_753,
                                   'Malformed JSON',
                                   'Could not decode the request body. The '
                                   'JSON was incorrect or not encoded as '
                                   'UTF-8.')

    def process_response(self, req, resp, resource):
        if 'result' not in req.context:
            return
        req.context['result']['is_login'] = 'user_id' in req.env['session']
        resp.body = json.dumps(req.context['result'])
        resp.status = falcon.HTTP_201
