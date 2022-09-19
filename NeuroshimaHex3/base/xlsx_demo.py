import xlsxwriter

def create_workbook(filename):
    """ Tworzenie nowego skoroszytu """
    workbook = xlsxwriter.Workbook(filename)
    return workbook

def create_worksheet(workbook):
    """ Dodawanie nowego arkusza do skoroszytu """
    worksheet = workbook.add_worksheet()
    return worksheet

def write_data(worksheet, data):
    """ Zapisywanie danych w arkuszu """
    for row in range(len(data)):
        for col in range(len(data[row])):
            worksheet.write(row,col, data[row][col])

def close_workbook(workbook):
    """ Zamykanie pliku """
    workbook.close()

if __name__ == '__main__':
    data = [['Zbyszek Samoistny', 38],
            ['Adam Kowalski', 42],
            ['Frodo Poter', 60],
            ['Czlowiek XD', 24]]
    workbook = create_workbook('sample_workbook.xlsx')
    worksheet = create_worksheet(workbook)
    write_data(worksheet, data)
    close_workbook(workbook)

    ## a tu w przeciwienstwie do csv normalnie zaczytuje