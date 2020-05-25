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


def get_ppe(name):
    query = f'''
    query{{
        personalProtectiveEquipment(name:"{name}"){{
            edges{{
                node{{
                    id
                    name
                    equipmentModel
                    serialNumber
                    description
                }}
            }}
        }}
    }}
    '''

    return gql(query)
