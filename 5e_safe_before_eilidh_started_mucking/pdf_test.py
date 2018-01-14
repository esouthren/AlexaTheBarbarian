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
    os.startfile('merged.pdf')


def get_overlay_canvas() -> io.BytesIO:
    ##
    c = CharacterClass()

    char_name = [60, 720]
    char_class = [280, 730]
    race = [280, 705]
    align = [390, 705]
    background = [390, 730]
    player_name = [480, 730]

    str_skill = [52, 620]
    dex_skill = [52, 550]
    con_skill = [52, 480]
    int_skill = [52, 410]
    wis_skill = [52, 340]
    cha_skill = [52, 270]

    str_mod = [55, 593]
    dex_mod = [55, 523]
    con_mod = [55, 453]
    int_mod = [55, 380]
    wis_mod = [55, 305]
    cha_mod = [55, 235]
    print(c.stats[0].modifier)

    # stats at + 60
    # larger y number = closer to top of page

    data = io.BytesIO()
    pdf = canvas.Canvas(data)
    pdf.drawString(x=char_name[0], y=char_name[1], text=c.name_character)
    pdf.drawString(x=char_class[0], y=char_class[1], text=c.class_type)
    pdf.drawString(x=race[0], y=race[1], text=c.race)
    pdf.drawString(x=align[0], y=align[1], text=c.alignment)
    pdf.drawString(x=background[0], y=background[1], text=c.background)
    pdf.drawString(x=player_name[0], y=player_name[1], text=c.name_player)


    ### Modifiers ###
    pdf.drawString(x=str_skill[0], y=str_skill[1], text=str(c.stats[0].ability_score))
    pdf.drawString(x=dex_skill[0], y=dex_skill[1], text=str(c.stats[1].ability_score))
    pdf.drawString(x=con_skill[0], y=con_skill[1], text=str(c.stats[2].ability_score))
    pdf.drawString(x=int_skill[0], y=int_skill[1], text=str(c.stats[3].ability_score))
    pdf.drawString(x=wis_skill[0], y=wis_skill[1], text=str(c.stats[4].ability_score))
    pdf.drawString(x=cha_skill[0], y=cha_skill[1], text=str(c.stats[5].ability_score))
    pdf.drawString(x=str_mod[0], y=str_mod[1], text=str(c.stats[0].modifier))
    pdf.drawString(x=dex_mod[0], y=dex_mod[1], text=str(c.stats[1].modifier))
    pdf.drawString(x=con_mod[0], y=con_mod[1], text=str(c.stats[2].modifier))
    pdf.drawString(x=int_mod[0], y=int_mod[1], text=str(c.stats[3].modifier))
    pdf.drawString(x=wis_mod[0], y=wis_mod[1], text=str(c.stats[4].modifier))
    pdf.drawString(x=cha_mod[0], y=cha_mod[1], text=str(c.stats[5].modifier))



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