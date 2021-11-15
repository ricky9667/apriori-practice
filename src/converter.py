import csv


def generate_dataset_from_csv(file_path):
    dataset = []
    with open(file_path, newline='') as csvfile:
        rows = csv.reader(csvfile)
        for row in rows:
            items = row[0].split(',')
            dataset.append(set(items))
    return dataset
