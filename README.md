# Apriori Algorithm

Practice Apriori algorithm and test with some datasets.

## How to run

### Get Python

This algorithm requires Python, first you have to install [here](https://www.python.org/downloads/) for Windows or run the following command for Linux/macOS:

```shell=
# macOS
brew install python

# Linux
apt install python
```

> Note: macOS is required to install [Homebrew](https://brew.sh) before running the command above

### Run Apriori

There are some easy datasets saved in `./test_data.py`, to run them with Apriori simply run:

```python=
# import our example datasets
from test_data import dataset1

# get frequent itemsets by Apriori, you will get a list of itemsets during the process of the algorithm
frequent_itemsets = find_frequent_itemsets(dataset=dataset1, min_support=2)

# show results
for itemset in itemsets:
    print(itemset)
```

