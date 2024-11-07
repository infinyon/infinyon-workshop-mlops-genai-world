EDGEHOME = edge1-home.json
HOME_CLUSTER = mlcore
EDGE_CLUSTER = local
FL_VERSION = 0.13.0-dev-3

INPUT_TOPIC=input-labels 
OUTPUT_TOPIC=edge-outputs



connect-home:
	fluvio --profile $(EDGE_CLUSTER) home connect --file $(EDGEHOME)

edge1-status:
	fluvio --profile $(EDGE_CLUSTER) home status

list-edge1-topics:
	fluvio --profile $(EDGE_CLUSTER) topic list

input_mouse:
	fluvio --profile $(EDGE_CLUSTER) produce input-objects --file capture/mouse.json --raw

input_person:
	fluvio --profile $(EDGE_CLUSTER) produce input-objects --file capture/person.json --raw