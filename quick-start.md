
mkdir -p ~/Documents/creds/imp1
mkdir -p ~/Documents/creds/imp2


mv tls.cert ~/Documents/creds/imp1
mv admin.macaroon ~/Documents/creds/imp1
ls ~/Documents/creds/imp1

mv tls.cert ~/Documents/creds/imp2
mv admin.macaroon ~/Documents/creds/imp2
ls ~/Documents/creds/imp2


python3 -m venv env
. env/bin/activate
pip install lnd-grpc-client

## In two shells

### Shell 1
export LND_NODE_IP=imp1.t.voltageapp.io
export LND_CRED_PATH=~/Documents/creds/imp1


### Shell 2
export LND_NODE_IP=imp2.t.voltageapp.io
export LND_CRED_PATH=~/Documents/creds/imp2