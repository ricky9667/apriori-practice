from apriori import find_frequent_item_sets
from test_data import dataset1


def main():
    print("dataset1 = " + str(dataset1))
    frequent_item_sets = find_frequent_item_sets(dataset=dataset1, min_support=2)

    # print("dataset2 = " + str(dataset2))
    # frequent_item_sets = find_frequent_item_sets(dataset=dataset2, min_support=2)

    # print("dataset3 = " + str(dataset3))
    # frequent_item_sets = find_frequent_item_sets(dataset=dataset3, min_support=2)

    # print("dataset4 = " + str(dataset4))
    # frequent_item_sets = find_frequent_item_sets(dataset=dataset4, min_support=2)

    for frequent_item_set in frequent_item_sets:
        print(frequent_item_set)


if __name__ == '__main__':
    main()
