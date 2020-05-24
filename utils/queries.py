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
