import io

import pdfrw
from reportlab.pdfgen import canvas

import os

def run(c):
    if os.path.isfile('merged.pdf'):
        os.remove('merged.pdf')
    canvas_data = get_overlay_canvas(c)
    form = merge(canvas_data, template_path='./char_sheet_canvas.pdf')
    save(form, filename='merged.pdf')
    os.startfile('merged.pdf')

    if os.path.isfile('merged2.pdf'):
        os.remove('merged2.pdf')
    canvas_data2 = get_overlay_canvas2(c)
    form2 = merge(canvas_data2, template_path='./char_sheet_canvas2.pdf')
    save(form2, filename='merged2.pdf')  
    os.startfile('merged2.pdf')


def get_overlay_canvas(c) -> io.BytesIO:
    ##

    DEFAULT = 12

    char_name = [55, 713]
    char_class = [270, 730]
    race = [270, 705]
    align = [380, 705]
    background = [380, 730]
    player_name = [480, 730]
    hit_point = [300, 585]
    speed = [355, 630]
    armor_class = [240, 630]
    initiative = [300, 630]
    prof_bonus = [100, 605]
    hit_dice = [260, 465]
    pass_wisdom = [35, 191]

    str_skill = [40, 610]
    dex_skill = [40, 540]
    con_skill = [40, 470]
    int_skill = [40, 400]
    wis_skill = [40, 330]
    cha_skill = [40, 260]

    str_mod = [55, 593]
    dex_mod = [55, 523]
    con_mod = [55, 453]
    int_mod = [55, 380]
    wis_mod = [55, 310]
    cha_mod = [55, 235]

    acr_mod = [114, 465]
    an_mod = [114, 450]
    arc_mod = [114, 436]
    ath_mod = [114, 421]
    dec_mod = [114, 409]
    hist_mod = [114, 395]
    ins_mod = [114, 381]
    in_mod = [114, 367]
    inv_mod = [114, 355]
    med_mod = [114, 340]
    nat_mod = [114, 327]
    perc_mod = [114, 315]
    perf_mod = [114, 301]
    pers_mod = [114, 289]
    rel_mod = [114, 274]
    sl_mod = [114, 260]
    ste_mod = [114, 245]
    sur_mod = [114, 232]

    s_throw = [118, 576]
    d_throw = [118, 563]
    c_throw = [118, 550]
    i_throw = [118, 537]
    w_throw = [118, 525]
    ch_throw = [118, 512]

    sav_thr = [576, 563, 550, 537, 525, 512]
    sk = [464,450,436,421,409,395,381,367,355,340,327,315,301,289,274,260,245,232]

    armor = [290, 190]
    wep1 = [290, 170]
    wep2 = [290, 150]
    # stats at + 60
    # larger y number = closer to top of page

    data = io.BytesIO()
    pdf = canvas.Canvas(data)
    pdf.setFontSize(25)
    pdf.setFont("Times-BoldItalic", 25)
    pdf.drawString(x=char_name[0], y=char_name[1], text=c.name_character)
    pdf.setFont("Courier", DEFAULT)
    pdf.drawString(x=char_class[0], y=char_class[1], text=c.class_type+" 1")
    pdf.drawString(x=race[0], y=race[1], text=c.race)
    pdf.drawString(x=align[0], y=align[1], text=c.alignment)
    pdf.drawString(x=background[0], y=background[1], text=c.background)
    pdf.drawString(x=player_name[0], y=player_name[1], text=c.name_player)
    pdf.drawString(x=hit_point[0], y=hit_point[1], text=str(c.hit_point))
    pdf.drawString(x=speed[0], y=speed[1], text=str(c.speed))
    pdf.drawString(x=prof_bonus[0], y=prof_bonus[1], text="+2")
    pdf.drawString(x=hit_dice[0], y=hit_dice[1], text="1d"+str(c.hit_die))
    pdf.drawString(x=armor[0], y=armor[1], text=c.armor)
    pdf.drawString(x=wep1[0], y=wep1[1], text=c.weapon[0])
    pdf.drawString(x=wep2[0], y=wep2[1], text=c.weapon[1])
    pdf.drawString(x=armor_class[0], y=armor_class[1], text=str(c.armor_class))
    pdf.drawString(x=initiative[0], y=initiative[1], text=str(c.stats[1].modifier))
    x = int(c.stats[1].modifier)+10
    pdf.drawString(x=pass_wisdom[0], y=pass_wisdom[1], text=str(x))

    ### Modifiers ###
    pdf.setFontSize(25)
    pdf.drawString(x=str_skill[0], y=str_skill[1], text=str(c.stats[0].ability_score))
    pdf.drawString(x=dex_skill[0], y=dex_skill[1], text=str(c.stats[1].ability_score))
    pdf.drawString(x=con_skill[0], y=con_skill[1], text=str(c.stats[2].ability_score))
    pdf.drawString(x=int_skill[0], y=int_skill[1], text=str(c.stats[3].ability_score))
    pdf.drawString(x=wis_skill[0], y=wis_skill[1], text=str(c.stats[4].ability_score))
    pdf.drawString(x=cha_skill[0], y=cha_skill[1], text=str(c.stats[5].ability_score))
    pdf.setFontSize(DEFAULT)
    pdf.setFontSize(10)
    pdf.drawString(x=str_mod[0], y=str_mod[1], text=str(c.stats[0].modifier))
    pdf.drawString(x=dex_mod[0], y=dex_mod[1], text=str(c.stats[1].modifier))
    pdf.drawString(x=con_mod[0], y=con_mod[1], text=str(c.stats[2].modifier))
    pdf.drawString(x=int_mod[0], y=int_mod[1], text=str(c.stats[3].modifier))
    pdf.drawString(x=wis_mod[0], y=wis_mod[1], text=str(c.stats[4].modifier))
    pdf.drawString(x=cha_mod[0], y=cha_mod[1], text=str(c.stats[5].modifier))
    pdf.drawString(x=acr_mod[0], y=acr_mod[1], text=str(c.skills_mod[0]))
    pdf.drawString(x=an_mod[0], y=an_mod[1], text=str(c.skills_mod[1]))
    pdf.drawString(x=arc_mod[0], y=arc_mod[1], text=str(c.skills_mod[2]))
    pdf.drawString(x=ath_mod[0], y=ath_mod[1], text=str(c.skills_mod[3]))
    pdf.drawString(x=dec_mod[0], y=dec_mod[1], text=str(c.skills_mod[4]))
    pdf.drawString(x=hist_mod[0], y=hist_mod[1], text=str(c.skills_mod[5]))
    pdf.drawString(x=ins_mod[0], y=ins_mod[1], text=str(c.skills_mod[6]))
    pdf.drawString(x=in_mod[0], y=in_mod[1], text=str(c.skills_mod[7]))
    pdf.drawString(x=inv_mod[0], y=inv_mod[1], text=str(c.skills_mod[8]))
    pdf.drawString(x=med_mod[0], y=med_mod[1], text=str(c.skills_mod[9]))
    pdf.drawString(x=nat_mod[0], y=nat_mod[1], text=str(c.skills_mod[10]))
    pdf.drawString(x=perc_mod[0], y=perc_mod[1], text=str(c.skills_mod[11]))
    pdf.drawString(x=perf_mod[0], y=perf_mod[1], text=str(c.skills_mod[12]))
    pdf.drawString(x=pers_mod[0], y=pers_mod[1], text=str(c.skills_mod[13]))
    pdf.drawString(x=rel_mod[0], y=rel_mod[1], text=str(c.skills_mod[14]))
    pdf.drawString(x=sl_mod[0], y=sl_mod[1], text=str(c.skills_mod[15]))
    pdf.drawString(x=ste_mod[0], y=ste_mod[1], text=str(c.skills_mod[16]))
    pdf.drawString(x=sur_mod[0], y=sur_mod[1], text=str(c.skills_mod[17]))

    pdf.drawString(x=s_throw[0], y=s_throw[1], text=str(c.stats[0].saving_throw))
    pdf.drawString(x=d_throw[0], y=d_throw[1], text=str(c.stats[1].saving_throw))
    pdf.drawString(x=c_throw[0], y=c_throw[1], text=str(c.stats[2].saving_throw))
    pdf.drawString(x=i_throw[0], y=i_throw[1], text=str(c.stats[3].saving_throw))
    pdf.drawString(x=w_throw[0], y=w_throw[1], text=str(c.stats[4].saving_throw))
    pdf.drawString(x=ch_throw[0], y=ch_throw[1], text=str(c.stats[5].saving_throw))

    x_value = 101
    for i in range(0, 6):
        if c.ab_bon[i] != 0:
            y_value = sav_thr[i]
            pdf.drawString(x=x_value, y=y_value, text="X")

    for i in range(0, 18):
        if c.skills[i] == c.prof1 or c.skills[i] == c.prof2:
            y_value = sk[i]

            pdf.drawString(x=x_value, y=y_value, text="X")

    pdf.save()
    data.seek(0)
    return data


def get_overlay_canvas2(c) -> io.BytesIO:
    DEFAULT = 12
    data = io.BytesIO()
    pdf = canvas.Canvas(data)
    pdf.setFontSize(25)
    pdf.setFont("Times-BoldItalic", 25)

    char_name = [55, 713]
    age = [270, 730]
    eyes = [270, 705]
    skin = [380, 705]
    height = [380, 730]
    hair = [480, 705]

    pdf.setFont("Times-BoldItalic", 25)
    pdf.drawString(x=char_name[0], y=char_name[1], text=c.name_character)
    pdf.setFont("Courier", DEFAULT)
    pdf.drawString(x=age[0], y=age[1], text=str(c.age))
    pdf.drawString(x=eyes[0], y=eyes[1], text=c.eyes)
    pdf.drawString(x=skin[0], y=skin[1], text=c.skin)
    pdf.drawString(x=height[0], y=height[1], text=c.size)
    pdf.drawString(x=hair[0], y=hair[1], text=c.hair)


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
        print("writing!")
        f.write(form.read())
