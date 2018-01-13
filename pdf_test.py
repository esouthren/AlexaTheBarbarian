import pypdftk as pdf



def main():
    pdf_path = "char_sheet.pdf"
    datas = { "name": "TEST!"}

    #fields = pdf.get_num_pages(pdf_path)
    print(pdf.dump_data_fields(pdf_path))

    #generated_pdf = pdf.fill_form(pdf_path, datas, "out.pdf")
    #out_pdf = pypdftk.merge("/character_sheet_main.pdf", generated_pdf)

if __name__ == '__main__':
    main()