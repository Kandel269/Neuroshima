import csv

def write_csv(filename, header, data):
    """ Zapis do pliku CSV
     str filename. Nazwa pliku w ktorym nalezy zapisac dane.
     list header. Nagłówek kolumny w pliku csv.
     list data. Zagnieżdżona lista mapująca wartości na kolumny.

     """
    try:
        with open(filename, "w") as csv_file:
            csv_writer = csv.DictWriter(csv_file, fieldnames=header)
            csv_writer.writeheader()
            csv_writer.writerows(data)
    except (IOError, OSError) as csv_file_error:
        print(f"Nie można zapisać danych w pliku csv. Wyjątek {csv_file_error}")

if __name__ == '__main__':
    header = ['name','age','gender']
    data = [{'name':'Dominik','age':'32','gender':'M'},
            {'name':'Ania','age':'23','gender':'K'},
          {'name':'Zbycho','age':'44','gender':'M'}]
    filename = 'sample_output.csv'
    write_csv(filename,header,data)

## Jakos dziwnie to zapisuje, moze kwestia tego, ze mam wersje probna excela i zle zaczytuje, nwm