# OS-Project

## Overview
This project monitors CPU usage, balances server loads, and visualizes CPU performance over time. It includes modules for load monitoring, load balancing, and data visualization.

## Prerequisites
- Python 3.8 or higher
- Required Python packages (see `requirements.txt`)

## Setup Instructions

1. **Clone the Repository**
   ```bash
   git clone <repository-url>
   cd OS-Project
   ```

2. **Install Dependencies**
   Use `pip` to install the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Application**
   Execute the main script:
   ```bash
   python src/main.py
   ```

4. **Log Files**
   - `main.log`: Logs the main program's execution flow.
   - `cpu_monitor.log`: Logs CPU load monitoring data.
   - `visualization.log`: Logs the visualization process.

## Project Structure
```
OS-Project/
├── requirements.txt       # List of dependencies
├── README.md              # Project documentation
├── src/
│   ├── main.py            # Main entry point
│   ├── load_monitor.py    # CPU load monitoring module
│   ├── load_balancer.py   # Server load balancing module
│   ├── visualization.py   # CPU usage visualization module
```

## Features
- **CPU Monitoring**: Logs CPU usage at regular intervals.
- **Load Balancing**: Distributes tasks across servers using round-robin and least-loaded strategies.
- **Visualization**: Plots CPU usage over time using Matplotlib.

## License
This project is licensed under the MIT License.