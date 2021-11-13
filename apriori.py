def generate_base_set(dataset):
    base_set = set()
    for item_set in dataset:
        for item in item_set:
            if item not in base_set:
                base_set.add(item)
    return [{item} for item in list(base_set)]


def calculate_item_appear_times(dataset, item_sets):
    appear_dict = []
    for _ in item_sets:
        appear_dict.append(0)

    for subset in dataset:
        for index, item_set in enumerate(item_sets):
            if item_set.difference(subset) == set():
                appear_dict[index] += 1

    return appear_dict


def filter_by_min_support(item_sets, appear_times, min_support):
    for index in range(len(item_sets) - 1, -1, -1):
        if appear_times[index] < min_support:
            item_sets.pop(index)
            appear_times.pop(index)
    return item_sets


def generate_next_item_sets(filtered_item_sets):
    dataset = []
    for i, item_set1 in enumerate(filtered_item_sets):
        for j, item_set2 in enumerate(filtered_item_sets):
            if j <= i:
                continue
            if len(item_set1.difference(item_set2)) == 1:
                new_item_set = item_set1.union(item_set2)
                if new_item_set not in dataset:
                    dataset.append(new_item_set)
    return dataset


def apriori(dataset, item_sets, min_support):
    appear_times = calculate_item_appear_times(dataset, item_sets)
    filtered_item_sets = filter_by_min_support(item_sets, appear_times, min_support)
    if len(filtered_item_sets) <= 1:
        return []

    next_dataset = generate_next_item_sets(filtered_item_sets)
    frequent_item_sets = apriori(dataset, next_dataset, min_support)
    frequent_item_sets.insert(0, filtered_item_sets)
    return frequent_item_sets


def find_frequent_item_sets(dataset, min_support):
    base_item_set = generate_base_set(dataset)
    return apriori(dataset, base_item_set, min_support)
