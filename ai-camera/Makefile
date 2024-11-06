EDGEHOME = edge1-home.json	

setup_fluvio:
	fluvio topic create objects

download_edge:
	fluvio cloud remote export edge1 --file $(EDGEHOME)

connect-home:
	fluvio home connect --file $(EDGEHOME)

setup_python:
	python3 -m venv fluvio --system-site-packages
	source fluvio/bin/activate
	pip install fluvio 





demo:
	source fluvio/bin/activate
	python demo.py
