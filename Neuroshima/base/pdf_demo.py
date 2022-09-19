import os

try:
    GTK_FOLDER = r'C:\Program Files\GTK3-Runtime Win64\bin'
    os.environ['PATH'] = GTK_FOLDER + os.pathsep + os.environ.get('PATH', '')
except:
    pass

from weasyprint import HTML, CSS

def generate_pdf(url, pdf_file):
    """ Generowanie doumentu PDF na podstawie stronyz podanego adresu URL """
    css = CSS(string='body{ font-size: 8px; }')
    HTML(url).write_pdf(pdf_file, stylesheets=[css])

if __name__ == '__main__':
    url = 'http://text.npr.org'
    pdf_file = 'demo_page.pdf'
    generate_pdf(url, pdf_file)