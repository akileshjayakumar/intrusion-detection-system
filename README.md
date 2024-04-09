# Intrusion Detection System (IDS)

This Python script simulates an Intrusion Detection System (IDS) for analyzing activity logs and detecting anomalies. It takes event and statistics data as input, generates activity logs, analyzes them, and flags anomalies if detected.

## Requirements

- Python 3.x

## Features

- Simulates an Intrusion Detection System (IDS) for analyzing activity logs.
- Detects anomalies in the activity logs and provides alerts.
- Generates activity logs based on event and statistics data.
- Calculates baseline statistics for comparison with activity logs.

## Usage

1. **Clone the repository:**

    ```bash
    git clone https://github.com/yourusername/IDS.git
    ```

2. **Navigate to the project directory:**

    ```bash
    cd IDS
    ```

3. **Run the script with the following command:**

    ```bash
    python3 IDS.py <Events file> <Stats file> <Number of Days>
    ```

    Replace `<Events file>`, `<Stats file>`, and `<Number of Days>` with your desired input parameters.

## Inputs

- `<Events file>`: File containing event data.
- `<Stats file>`: File containing statistics data.
- `<Number of Days>`: Number of days for activity simulation.

## Outputs

- `ActivityLogs.txt`: Generated activity logs.
- `BaselineStats.txt`: Output file containing baseline statistics.

## Alerting

The script flags anomalies detected in the activity logs and provides alerts when anomalies are found.
