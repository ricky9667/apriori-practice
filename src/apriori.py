def generate_base_set(dataset):
    base_set = set()
    for itemset in dataset:
        for item in itemset:
            if item not in base_set:
                base_set.add(item)
    return [{item} for item in list(base_set)]


def calculate_item_appear_times(dataset, itemsets):
    appear_dict = []
    for index, itemset in enumerate(itemsets):
        appear_dict.append(0)

    for subset in dataset:
        for index, itemset in enumerate(itemsets):
            if itemset.difference(subset) == set():
                appear_dict[index] += 1

    return appear_dict


def filter_by_min_support(itemsets, appear_times, min_support):
    for index in range(len(itemsets)-1, -1, -1):
        if appear_times[index] < min_support:
            itemsets.pop(index)
            appear_times.pop(index)
    return itemsets


def generate_next_itemsets(filtered_itemsets):
    dataset = []
    for i, itemset1 in enumerate(filtered_itemsets):
        for j, itemset2 in enumerate(filtered_itemsets):
            if j <= i:
                continue
            if len(itemset1.difference(itemset2)) == 1:
                new_itemset = itemset1.union(itemset2)
                if new_itemset not in dataset:
                    dataset.append(new_itemset)
    return dataset


def apriori(dataset, itemsets, min_support):
    appear_times = calculate_item_appear_times(dataset, itemsets)

    filtered_itemsets = filter_by_min_support(itemsets, appear_times, min_support)
    if len(filtered_itemsets) <= 1:
        return []

    next_dataset = generate_next_itemsets(filtered_itemsets)

    frequent_itemsets = apriori(dataset, next_dataset, min_support)
    frequent_itemsets.insert(0, filtered_itemsets)
    return frequent_itemsets


def find_frequent_itemsets(dataset, min_support):
    base_itemset = generate_base_set(dataset)
    return apriori(dataset, base_itemset, min_support)
