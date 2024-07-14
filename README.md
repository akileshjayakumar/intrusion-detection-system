# Intrusion Detection System (IDS)

This Python script simulates an Intrusion Detection System (IDS) for analyzing activity logs and detecting anomalies. It takes event and statistics data as input, generates activity logs, analyzes them, and flags anomalies if detected.

## Requirements

- Python 3.x

## Features

- Simulates an Intrusion Detection System (IDS) for analyzing activity logs.
- Detects anomalies in the activity logs and provides alerts.
- Generates activity logs based on event and statistics data.
- Calculates baseline statistics for comparison with activity logs.

## Project Setup

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

## Contributing

Your contributions are welcome! If you have ideas for improvements or new features:

1. **Fork the Repository**
   - Click the "Fork" button at the top right of the repository page to create a copy in your GitHub account.

2. **Create a New Branch**
   - Open your terminal and switch to the repository directory.
   - Create and switch to a new branch:
     ```bash
     git checkout -b feature-branch
     ```

3. **Commit Your Changes**
   - Make your desired changes in the code.
   - Stage and commit your changes with a descriptive message:
     ```bash
     git commit -am 'Add new feature: description'
     ```

4. **Push to the Branch**
   - Push your changes to the newly created branch in your forked repository:
     ```bash
     git push origin feature-branch
     ```

5. **Submit a Pull Request**
   - Go to the original repository and click on the "Pull Requests" tab.
   - Click the "New Pull Request" button.
   - Select your branch and provide a clear description of your changes.

## Contact Information

For more information or if you have any questions, please reach out:

- **Email**: [jayakuma006@mymail.sim.edu.sg](mailto:jayakuma006@mymail.sim.edu.sg)
- **LinkedIn**: [Akilesh Jayakumar on LinkedIn](https://www.linkedin.com/in/akileshjayakumar/)
- **GitHub**: [Akilesh Jayakumar on GitHub](https://github.com/akileshjayakumar)
