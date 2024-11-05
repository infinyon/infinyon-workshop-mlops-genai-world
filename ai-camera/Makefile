setup_fluvio:
	fluvio topic create objects


setup_python:
	python3 -m ven fluvio --system-site-packages
	source fluvio/bin/activate
	pip install fluvio

demo:
	source fluvio/bin/activate
	python demo.py