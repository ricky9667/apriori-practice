import csv


def generate_dataset_from_csv(file_path):
    dataset = []
    with open(file_path, newline='') as csvfile:
        rows = csv.reader(csvfile)
        for row in rows:
            subset = set(row)
            dataset.append(subset)
    return dataset
