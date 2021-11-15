from src.apriori import find_frequent_itemsets
from src.converter import generate_dataset_from_csv
from datasets.sample import dataset1, dataset2, dataset3, dataset4


def main():
    # print("dataset1 = " + str(dataset1))
    # frequent_itemsets = find_frequent_itemsets(dataset=dataset1, min_support=2)
    # for frequent_itemset in frequent_itemsets:
    #     print(frequent_itemset)

    dataset = generate_dataset_from_csv('datasets/my_movies.csv')
    frequent_itemsets = find_frequent_itemsets(dataset=dataset[0:500], min_support=2)
    for frequent_itemset in frequent_itemsets:
        print(frequent_itemset)


if __name__ == '__main__':
    main()
