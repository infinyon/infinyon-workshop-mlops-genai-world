EDGEHOME = edge1-home.json
HOME_CLUSTER = mlcore
EDGE_CLUSTER = local
FL_VERSION = 0.13.0-dev-3

INPUT_TOPIC=input-labels 
OUTPUT_TOPIC=edge-outputs

setup_fluvio:
	fluvio topic create objects

download_edge:
	fluvio cloud remote export edge1 --file $(EDGEHOME)

connect-home:
	fluvio --profile $(EDGE_CLUSTER) home connect --file $(EDGEHOME)

edge-status:
	fluvio --profile $(EDGE_CLUSTER) home status

list-edge-topics:
	fluvio --profile $(EDGE_CLUSTER) topic list


setup_python:
	python3 -m venv fluvio --system-site-packages
	source fluvio/bin/activate
	pip install fluvio 


create-cloud-cluster:
	fluvio cloud cluster create $(HOME_CLUSTER) --version $(FL_VERSION)

setup-home:
	fluvio --profile $(HOME_CLUSTER) remote register edge1

exp-remote:
	fluvio cloud remote export edge1  --file edge1-home.json


create-home-topics:
	fluvio --profile $(HOME_CLUSTER) topic create $(INPUT_TOPIC) --mirror-apply mirror.json --home-to-remote
	fluvio --profile $(HOME_CLUSTER) topic create $(OUTPUT_TOPIC) --mirror-apply mirror.json

list-home-topics:
	fluvio --profile $(HOME_CLUSTER) topic list

clean-home-topics:
	fluvio --profile $(HOME_CLUSTER) topic delete $(INPUT_TOPIC)
	fluvio --profile $(HOME_CLUSTER) topic delete $(OUTPUT_TOPIC)

demo:
	source fluvio/bin/activate
	python demo.py


label_mouse:
	fluvio --profile $(HOME_CLUSTER) produce input-labels --file requests/mouse.json --raw

label_person:
	fluvio --profile $(HOME_CLUSTER) produce input-labels --file requests/person.json --raw


