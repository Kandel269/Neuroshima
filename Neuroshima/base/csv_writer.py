import csv

def write_csv(filename, header, data):
    """ Zapis do pliku CSV
     str filename. Nazwa pliku w ktorym nalezy zapisac dane.
     list header. Nagłówek kolumny w pliku csv.
     list data. Zagnieżdżona lista mapująca wartości na kolumny.

     """
    try:
        with open(filename, "w") as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow(header)
            for record in data:
                csv_writer.writerow(record)
    except (IOError, OSError) as csv_file_error:
        print(f"Nie można zapisać danych w pliku csv. Wyjątek {csv_file_error}")

if __name__ == '__main__':
    header = ['name','age','gender']
    data = [['Dominik','32','M'], ['Ania','23','K'], ['Zbycho','44','M']]
    filename = 'sample_output.csv'
    write_csv(filename,header,data)

