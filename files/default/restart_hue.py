#!/usr/bin/env python
import sys
from cm_api.api_client import ApiResource
from cm_api.api_client import ApiException

CMD_TIMEOUT = 180

manager_host = sys.argv[1]
cluster_name = sys.argv[2]

api = ApiResource(manager_host, username="admin", password="admin", use_tls=False, version=4)
cluster = api.get_cluster(cluster_name)

try:
    hue = cluster.get_service("hue1")
except ApiException:
    raise Exception("Failed to obtain service hue1")

cmd = hue.restart()
if not cmd.wait(CMD_TIMEOUT).success:
    raise Exception('Failed to start Hue service.')
