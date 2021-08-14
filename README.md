# lndgrpc
A python grpc client for Impervious Network ⚡⚡⚡

This is a wrapper around the default grpc interface that handles setting up credentials (including macaroons). An async client is also available to do fun async stuff like listening for invoices in the background. 

## Dependencies
- Python 3.6+
- Working LND lightning node, take note of its ip address.
- Copy your admin.macaroon and tls.cert files from your node to a directoy on your machine. 


## Installation
```bash
pip install imp-grpc-client
```



### Environment Variables

These environment variables are only used when testing node connectivity and/or correct module installation from the command line. This library is primarily used through Python scripting.

```bash
export CRED_PATH=/path/to/macaroon/and/tls/cert
export LND_NODE_IP=192.168.1.xx

python3 -m lndgrpc

# You should expect to see:
#
# .....
# .....
# .....
# lndgrpc package is installed... Wow it works!
```

## Basic Usage
The api mirrors the underlying lnd grpc api (http://api.lightning.community/) but methods will be in pep8 style. ie. `.GetInfo()` becomes `.get_info()`.

```python
```

### Specifying Macaroon/Cert files
By default the client will attempt to lookup the `readonly.macaron` and `tls.cert` files in the mainnet directory. 
However if you want to specify a different macaroon or different path you can pass in the filepath explicitly.

```python
lnd = LNDClient(
    macaroon_filepath='~/.lnd/invoice.macaroon', 
    cert_filepath='path/to/tls.cert'
)
```

## Generating LND Proto Files
```bash
virtualenv lnd
source lnd/bin/activate
pip install grpcio grpcio-tools googleapis-common-protos sh
git clone https://github.com/lightningnetwork/lnd.git
mkdir genprotos
git clone https://github.com/googleapis/googleapis.git
```


```python
from pathlib import Path
import shutil
import sh

for proto in list(Path("../imp-releases/proto").rglob("*.proto")):
    shutil.copy(proto, Path.cwd().joinpath("impgrpc/compiled"))

protos = list(Path(".").joinpath("impgrpc/compiled").glob("**/*.proto"))

args = [
    "-m",
    "grpc_tools.protoc",
    # "--proto_path=../imp-releases/proto/:.",
    # "--proto_path=../imp-releases/proto/google/api:.",
    # "--proto_path=../imp-releases/proto/protoc-gen-openapiv2/options:.",
    # "--proto_path=impgrpc/compiled/:.",
    # "--proto_path=impgrpc/compiled/protoc-gen-openapiv2/:.",
    "--proto_path=impgrpc/compiled/",
    # "--proto_path=.:.",
    "--python_out=impgrpc/compiled",
    "--grpc_python_out=impgrpc/compiled",
]

for protofile in protos:
        args.append(str(protofile) )

# Generate the compiled protofiles
sh.python(args)
```

Last Step:
In File: verrpc_pb2_grpc.py
Change:
import verrpc_pb2 as verrpc__pb2
To:
from lndgrpc import verrpc_pb2 as verrpc__pb2

## Deploy to Test-PyPi
```bash
poetry build
twine check dist/*
twine upload --repository-url https://test.pypi.org/legacy/ dist/*
```