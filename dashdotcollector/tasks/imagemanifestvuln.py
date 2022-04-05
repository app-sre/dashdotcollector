import os
import json
from typing import Optional

import requests

from dashdotcollector.core.app import app
from dashdotcollector.utils.oc import OC
from dashdotcollector.tasks.demo import IMAGEMANIFESTVULN
from gql import Client, gql
from gql.transport.requests import RequestsHTTPTransport

ENDPOINT = os.environ['DASHDOTDB_URL']


# CLUSTER_QUERY = """
# {
#   clusters: clusters_v1 {
#     name
#     serverUrl
#     jumpHost {
#       hostname
#       knownHosts
#       user
#       port
#       identity {
#         path
#         field
#         format
#       }
#     }
#     automationToken {
#       path
#       field
#       format
#     }
#     internal
#   }
# }
# """


@app.task
def run():
    # gqlcli = _init_gql_client('http://localhost:4000/graphql', None)
    # result = gqlcli.execute(gql(CLUSTER_QUERY))
    # for cluster in result['data']['clusters']:
    clusters = ['test-cluster-01']
    for cluster in clusters:
        sync.delay(cluster=cluster)

    return f'sync tasks created for: {", ".join(clusters)}'


@app.task
def sync(cluster):
    # oc_creds = OC_CREDS[cluster]
    # oc_cli = OC(server=oc_creds['server'], token=oc_creds['token'])
    # imagemanifestvln = oc_cli.get_all('imagemanifestvuln')
    imagemanifestvln = json.loads(IMAGEMANIFESTVULN)
    endpoint = f'{ENDPOINT}/imagemanifestvuln/{cluster}'
    headers = {'Authorization': f'token: {os.environ["ACCESS_TOKEN"]}'}
    res = requests.post(url=endpoint, json=imagemanifestvln, headers=headers)
    res.raise_for_status()
    return f"cluster {cluster} synced"


def _init_gql_client(url: str, token: Optional[str]) -> Client:
    req_headers = None
    if token:
        # The token stored in vault is already in the format 'Basic ...'
        req_headers = {"Authorization": token}
    # Here we are explicitly using sync strategy
    return Client(transport=RequestsHTTPTransport(url, headers=req_headers))
