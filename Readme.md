# Stock Insight Agents

Stock Insight Agents is a multi-agent system that leverages advanced language models to analyze financial data, review market news, and provide predictions on company stock performance. This system is built using the `autogen` library to manage interactions between multiple agents, each with a specific role in processing financial information and making predictions.

## Project Structure

The project consists of the following components:

- **Financial Assistant**: Analyzes stock data for a specific company and reviews recent performance.
- **Research Assistant**: Fetches and processes recent market news related to the company.
- **Financial Expert**: Makes predictions about the company's future stock performance based on data and news analysis.

## Features

- Retrieves current stock prices for a given company.
- Analyzes stock performance over the past month.
- Gathers relevant market news using DuckDuckGo search API.
- Provides predictions on stock movement (growth, decline, or stagnation).
- Supports integration with external APIs for real-time data retrieval.

## Requirements

To run the project, you will need:

- Python 3.x
- Required Python libraries:
  - `autogen`
  - `duckduckgo_search`
  
You can install the dependencies by running:

```bash
pip install -r requirements.txt
```
## Usage

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/stock-insight-agents.git
    cd stock-insight-agents
    ```

2. Prepare the configuration file `OAI_CONFIG_LIST.json` with your model configurations.

3. Run the project:

    ```bash
    python main.py
    ```

    You will be prompted to enter a company name, after which the system will analyze stock data, retrieve market news, and provide a prediction about the company's stock performance.

## Contributing

Feel free to submit issues or pull requests if you find any bugs or have suggestions for improvements!
