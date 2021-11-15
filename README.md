# Apriori Practice

Practice Apriori algorithm and test with some datasets.

## How to run

### Get Python

This algorithm requires Python, first you have to install [here](https://www.python.org/downloads/) for Windows or run the following command for Linux/macOS:

```shell=
# macOS
brew install python3

# Linux
apt install python3
```

> Note: macOS is required to install [Homebrew](https://brew.sh) before running the command above

### Run Apriori with raw Python sets

You can add datasets written in Python, the dataset should be a Python list `[]` with sets contains inside.
For example:

```python=
dataset1 = [{1, 3, 4},
            {2, 3, 5},
            {1, 2, 3, 5},
            {2, 5}]
```

> You can check out more examples in `./datasets/sample.py`

Next, try Apriori by running the following code:

```python=
from src.apriori import find_frequent_itemsets
from datasets.sample import dataset1, dataset2, dataset3, dataset4


def main():
    print("dataset1 = " + str(dataset1))
    frequent_itemsets = find_frequent_itemsets(dataset=dataset1, min_support=2)
    for frequent_itemset in frequent_itemsets:
        print(frequent_itemset)


if __name__ == '__main__':
    main()
```

### Run Apriori by importing datasets from CSV file

You can import datasets from csv files, you can check out the sample csv file `./datasets/my_movies.csv`.

You should import the converter that converts the csv file to raw dataset like the following code:

```python=
from src.apriori import find_frequent_itemsets
from src.converter import generate_dataset_from_csv


def main():
    dataset = generate_dataset_from_csv('datasets/my_movies.csv')
    frequent_itemsets = find_frequent_itemsets(dataset=dataset, min_support=2)
    for frequent_itemset in frequent_itemsets:
        print(frequent_itemset)


if __name__ == '__main__':
    main()
```
