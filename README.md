# Country Data Visualization

This repository contains Python scripts to fetch and visualize country data using various APIs.

## Files

- `country_data.py`: This script fetches country data from the "restcountries.com" API and saves it in JSON format.
- `visualize_population.py`: This script reads the country data from the JSON file and visualizes the population of the top 20 countries using matplotlib and seaborn libraries.
- `wiki_data.py`: This script fetches additional data from the Wikipedia API and prints it to the console.

## Dependencies

To run the scripts in this repository, you need to have the following dependencies installed:

- Python 3
- requests
- json
- pandas
- matplotlib
- seaborn

## Usage

1. Clone the repository:

<pre><code>```bash
git clone https://github.com/your-username/country-data-visualization.git
```
</code></pre>

2. Install the required dependencies:
<pre><code>```bash
pip install -r requirements.txt
```
</code></pre>

3. Run the scripts:

To fetch country data and create a JSON file:
<pre><code>```bash
python country_data.py
```
</code></pre>

To visualize the population of the top 20 countries:
<pre><code>```bash
python visualize_population.py
```
</code></pre>
To fetch additional data from Wikipedia:
pre><code>```bash
python wiki_data.py
```
</code></pre>
Feel free to explore and modify the scripts to suit your needs.
