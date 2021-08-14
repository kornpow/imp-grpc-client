from pathlib import Path
import json
from pprint import pprint
import os
import base64
from time import sleep
from datetime import datetime, timedelta

# Pip installed Modules
from impgrpc import IMPClient
from protobuf_to_dict import protobuf_to_dict


node_ip = "127.0.0.1"

imp = IMPClient(
	f"{node_ip}:8881"
)


node_ip = "127.0.0.1"

imp = IMPClient(
	f"{node_ip}:9991"
)


for i in imp.subscribe():
	print(f"Amount Spent: {i.amount} \n\n")
	pprint(protobuf_to_dict(i.data))

