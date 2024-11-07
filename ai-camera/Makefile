EDGEHOME = edge1-home.json
HOME_CLUSTER = mldemo
EDGE_CLUSTER = local

setup_fluvio:
	fluvio topic create objects

download_edge:
	fluvio cloud remote export edge1 --file $(EDGEHOME)

connect-home:
	fluvio --profile $(EDGE_CLUSTER) home connect --file $(EDGEHOME)



setup_python:
	python3 -m venv fluvio --system-site-packages
	source fluvio/bin/activate
	pip install fluvio 


create-cloud-cluster:
	fluvio cloud cluster create mldemo --version 0.13.0-dev-2

setup-home:
	fluvio --profile $(HOME_CLUSTER) remote register edge1

exp-remote:
	fluvio cloud remote export edge1  --file edge1-home.json


create-home-topics:
	fluvio --profile $(HOME_CLUSTER) topic create input-labels --mirror-apply mirror.json --home-to-remote
	fluvio --profile $(HOME_CLUSTER) topic create output-labels --mirror-apply mirror.json



demo:
	source fluvio/bin/activate
	python demo.py
