## Create Folders
mkdir -p ~/Documents/creds/imp1
mkdir -p ~/Documents/creds/imp2

## Copy over Voltage Credentials
mv tls.cert ~/Documents/creds/imp1
mv admin.macaroon ~/Documents/creds/imp1
ls ~/Documents/creds/imp1

mv tls.cert ~/Documents/creds/imp2
mv admin.macaroon ~/Documents/creds/imp2
ls ~/Documents/creds/imp2

# Install IMP GRPC Client
python3 -m venv env
. env/bin/activate
pip install imp-grpc-client

# Impervious Client
wget https://github.com/imperviousai/imp-releases/releases/download/v0.1.3/impervious-v0.1.3-linux-amd64.tar.gz
tar xzvf impervious-v0.1.3-linux-amd64.tar.gz

## Make config folders
mdkir ~/Documents/imp/imp1
mdkir ~/Documents/imp/imp2

## Create config files
touch ~/Documents/imp/imp1/config.yml
touch ~/Documents/imp/imp2/config.yml

## In two shells

### Shell 1
cd ~/Documents/imp/imp1
export LND_NODE_IP=imp1.t.voltageapp.io
export LND_CRED_PATH=~/Documents/creds/imp1
../impervious -config config.yml


### Shell 2
cd ~/Documents/imp/imp2
export LND_NODE_IP=imp2.t.voltageapp.io
export LND_CRED_PATH=~/Documents/creds/imp2
../impervious -config config.yml