from gql import gql  # pylint: disable=import-error


def create_login(username, email, password, cpf):
    mutation = f'''
    mutation login{{
        createLogin(input:{{
            username:"{username}",
            email:"{email}",
            password:"{password}",
            cpf:"{cpf}",
        }}){{
            user{{
            id
            username
            email
            password
            cpf
            }}
        }}
    }}
    '''
    return gql(mutation)
