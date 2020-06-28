from base64 import b64decode, b64encode
from gql import Client  # pylint: disable=import-error
from gql.transport.requests import RequestsHTTPTransport  # pylint: disable=import-error

def get_gql_client(url, auth=None):
    """
    Retorna um cliente de execução de requisições graphql para acessar mithrandir.
    Param : auth : <str> : hash de autorização.
    """
    if not auth:
        transport = RequestsHTTPTransport(url=url, use_json=True)
    else:
        headers = {
            'content-type': 'application/json',
            'auth': '{}'.format(auth)
        }
        transport = RequestsHTTPTransport(
            url=url,
            use_json=True,
            headers=headers,
        )
    
    client = Client(transport=transport, fetch_schema_from_transport=False)
    return client


def decode_b64(hash):
    response = b64decode(hash).decode('utf-8')

    return response


def encode_b64(to_hash):
    response = b64encode(to_hash)

    return response

