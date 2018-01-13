import io
from CharacterClass import *
import pdfrw
from reportlab.pdfgen import canvas
import os



def run():
    if os.path.isfile('merged.pdf'):
        os.remove('merged.pdf')
    canvas_data = get_overlay_canvas()
    form = merge(canvas_data, template_path='./char_sheet_canvas.pdf')
    save(form, filename='merged.pdf')


def get_overlay_canvas() -> io.BytesIO:
    ##
    c = CharacterClass()
d = {
    char_name : [60,720]
    char_class : [300, 750]
}

    # stats at + 60
    # larger y number = closer to top of page

    data = io.BytesIO()
    pdf = canvas.Canvas(data)
    pdf.drawString(x=d[char_name][0], y=char_name[1], text=(c.name_character))

    pdf.save()
    data.seek(0)
    return data


def merge(overlay_canvas: io.BytesIO, template_path: str) -> io.BytesIO:
    template_pdf = pdfrw.PdfReader(template_path)
    overlay_pdf = pdfrw.PdfReader(overlay_canvas)
    for page, data in zip(template_pdf.pages, overlay_pdf.pages):
        overlay = pdfrw.PageMerge().add(data)[0]
        pdfrw.PageMerge(page).add(overlay).render()
    form = io.BytesIO()
    pdfrw.PdfWriter().write(form, template_pdf)
    form.seek(0)
    return form


def save(form: io.BytesIO, filename: str):
    with open(filename, 'wb') as f:
        f.write(form.read())

if __name__ == '__main__':
    run()