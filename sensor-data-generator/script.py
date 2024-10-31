import time
import numpy as np
import pandas as pd

# Environmental Monitoring Data Generator
def generate_environmental_data(num_samples=1000, interval=5):
    data = []
    for _ in range(num_samples):
        temperature = np.random.normal(22, 2)  # Mean 22°C, std dev 2
        humidity = np.random.normal(50, 5)     # Mean 50%, std dev 5
        air_quality = np.random.normal(200, 20) # Mean AQI 200, std dev 20
        data.append({
            "timestamp": pd.Timestamp.now(),
            "temperature": temperature,
            "humidity": humidity,
            "air_quality": air_quality
        })
        time.sleep(interval)  # Wait for specified interval
    return pd.DataFrame(data)

# Predictive Maintenance Data Generator
def generate_maintenance_data(num_samples=1000, interval=0.1):
    data = []
    for i in range(num_samples):
        vibration = np.random.normal(0.5, 0.1)  # Mean vibration 0.5, std dev 0.1
        sound_level = np.random.normal(70, 5)   # Mean sound level 70 dB, std dev 5
        # Add occasional spikes for anomaly simulation
        if i % 100 == 0:
            vibration += np.random.normal(0.3, 0.1)
        if i % 150 == 0:
            sound_level += np.random.normal(10, 5)
        data.append({
            "timestamp": pd.Timestamp.now(),
            "vibration": vibration,
            "sound_level": sound_level
        })
        time.sleep(interval)  # Wait for specified interval
    return pd.DataFrame(data)

# Activity Recognition Data Generator
def generate_activity_data(num_samples=1000, interval=0.02):
    data = []
    # Simulate different activity levels
    for i in range(num_samples):
        if i < num_samples // 3:
            acceleration = np.random.normal(1, 0.2)  # Idle
            gyroscope = np.random.normal(0.5, 0.1)
        elif i < 2 * num_samples // 3:
            acceleration = np.random.normal(2, 0.5)  # Walking
            gyroscope = np.random.normal(1, 0.3)
        else:
            acceleration = np.random.normal(5, 1)    # Running
            gyroscope = np.random.normal(3, 0.5)
        data.append({
            "timestamp": pd.Timestamp.now(),
            "acceleration": acceleration,
            "gyroscope": gyroscope
        })
        time.sleep(interval)  # Wait for specified interval
    return pd.DataFrame(data)

# Main function to start generating data
def main():
    print("Starting synthetic data generation on Raspberry Pi...")
    while True:
        env_data = generate_environmental_data(num_samples=10)
        maintenance_data = generate_maintenance_data(num_samples=10)
        activity_data = generate_activity_data(num_samples=10)
        print("Environmental Data:\n", env_data.head())
        print("Maintenance Data:\n", maintenance_data.head())
        print("Activity Data:\n", activity_data.head())
        # Here you could write data to files, databases, or stream it to Fluvio
        time.sleep(10)  # Interval between batches

if __name__ == "__main__":
    main()
