#!/usr/bin/env python

from ai_camera import IMX500Detector
import time
from fluvio import Fluvio

camera = IMX500Detector()

TOPIC_NAME = "objects"
PARTITION = 0

fluvio = Fluvio.connect()
print(f"Connected to fluvio")
producer = fluvio.topic_producer(TOPIC_NAME)
print(f"Created fluvio producer")

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
        
        # Example: Print when a person is detected with high confidence
        if label == "person" and confidence > 0.4:
            producer.send_string(f"Person detected with {confidence:.2f} confidence!")
            producer.flush()

    
    # Small delay to prevent overwhelming the system
    time.sleep(0.1)
