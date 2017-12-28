import csv

def csv_dict_reader(file_obj):
    """
    Read a CSV file using csv.DictReader
    """
    reader = csv.DictReader(file_obj, delimiter=',')
    for line in reader:
        print(line['first_name'], line['last_name'])

if __name__ == '__main__':
    csv_path = "data.csv"
    with open(csv_path, 'r') as f_obj:
        csv_dict_reader(f_obj)