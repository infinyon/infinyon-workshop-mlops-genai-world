#!/usr/bin/env python
import time
import json
from datetime import datetime
from fluvio import Fluvio


TOPIC_NAME = "output-labels"
PARTITION = 0

fluvio = Fluvio.connect()
print(f"Connected to fluvio")
producer = fluvio.topic_producer(TOPIC_NAME)
print(f"Created fluvio producer to: {TOPIC_NAME}")


producer.send_string("hello world")
producer.flush()


