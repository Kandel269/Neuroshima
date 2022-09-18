import os

GTK_FOLDER = r'C:\Program Files\GTK3-Runtime Win64\bin'
os.environ['PATH'] = GTK_FOLDER + os.pathsep + os.environ.get('PATH', '')

from weasyprint import HTML

def generate_pdf(url, pdf_file):
    """ Generowanie doumentu PDF na podstawie stronyz podanego adresu URL """
    print("Generowanie dokumentu PDF...")
    HTML(url).write_pdf(pdf_file)

if __name__ == '__main__':
    url = 'http://text.npr.org'
    pdf_file = 'demo_page.pdf'
    generate_pdf(url, pdf_file)