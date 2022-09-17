import csv

def read_csv(filename):
    """ Wczytywanie i wyswietalnie danych z pliku CSV """
    try:
        with open(filename, newline='') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for record in csv_reader:
                print(record)
    except(IOError, OSError) as file_read_error:
        print(f"Nie można otworzyć pliku csv. Wyjątek: {file_read_error}")

if __name__ == '__main__':
    read_csv('market_cap.csv')