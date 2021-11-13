from test_data import dataset1, dataset2, dataset3, dataset4
from apriori import find_frequent_itemsets


def main():
    # print("dataset1 = " + str(dataset1))
    # result = find_frequent_itemsets(dataset=dataset1, min_support=2)

    print("dataset2 = " + str(dataset2))
    result = find_frequent_itemsets(dataset=dataset2, min_support=2)

    # print("dataset3 = " + str(dataset3))
    # find_frequent_itemsets(dataset=dataset3, min_support=2)

    # print("dataset4 = " + str(dataset4))
    # find_frequent_itemsets(dataset=dataset4, min_support=2)

    for frequent_itemset in result:
        print(frequent_itemset)


if __name__ == '__main__':
    main()
