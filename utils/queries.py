from gql import gql  # pylint: disable=import-error

def get_job_group(name):
    query = f'''
    query{{
        jobGroup(name:"{name}"){{
            edges{{
                node{{
                    id
                    name
                    description
                }}
            }}
        }}
    }}
    '''

    return gql(query)


def get_ppe():
    body = '''
    ```
Está é a consulta para pesquisar os equipamentos de proteção individual cadastrados no sistema.

! Lembre-se, você pode usar o filtro passando o sinal de "()" entre o personalProtectiveEquipment e a chave.
! Caso não saiba os filtros que existem, entre no insomnia e digite CTRL + espaço entre "(" e ")" que ele irá te mostrar.


    query{
        personalProtectiveEquipment{
            edges{
                node{
                    id
                    name
                    equipmentModel
                    serialNumber
                    description
                }
            }
        }
    }
    ```
    '''

    return body


def get_job_equipment(name):
    query = '''
    query{
        jobEquipment{
            edges{
                node{
                    id
                    name
                    equipmentModel
                    serialNumber
                    description
                }
            }
        }
    }
    '''

    return gql(query)
