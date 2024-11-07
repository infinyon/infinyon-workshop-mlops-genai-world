#!/usr/bin/env python
import time
import json
from datetime import datetime
from fluvio import Fluvio
from ai_camera import IMX500Detector

camera = IMX500Detector()

TOPIC_NAME = "input-objects"
PARTITION = 0

fluvio = Fluvio.connect()
print(f"Connected to fluvio")
producer = fluvio.topic_producer(TOPIC_NAME)
print(f"Created fluvio producer to: {TOPIC_NAME}")

# Start the detector with preview window
camera.start(show_preview=True)

# Main loop
while True:
    # Get the latest detections
    detections = camera.get_detections()
    
    # Get the labels for reference
    labels = camera.get_labels()
    
    # Process each detection
    for detection in detections:
        label = labels[int(detection.category)]
        confidence = detection.conf

        event_time  = datetime.now().isoformat()
        record = {
            "label": label,
            "confidence": float(confidence),
            "time": event_time
        }

        output = json.dumps(record)

        producer.send_string(output)
        producer.flush()


    
    # Small delay to prevent overwhelming the system
    time.sleep(0.1)
