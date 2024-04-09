import fitz  # PyMuPDF dependency

def read_pdf(file_path):
    # open pdf file
    with fitz.open(file_path) as doc:
        # text = ""
        # Iterate through each page in the PDF
        for page in doc:
            # print(page.get_text())
            widgets = page.widgets()
            for widget in widgets:
                # print(f"Field Name: {field['name']}, Field Type: {field['type']}")
                # Extract text from the current page
                # print(widget.field_name)
                print(widget.field_name.split('.')[-1].split('_')[-1][:-3] + " | " + widget.field_label)
                # print(widget.field_label)
                # print(widget.field_value)
                # print(widget.xref)
                # print(dir(widget))
                if widget.field_name == 'Field I am looking for':
                    widget.field_value = 'My new value'
                    widget.update()
                # field_name = annot.info["title"]
                # print(field_name)
                # if field_name in form_data:
                #     annot.set_text(form_data[field_name])
                # if field['type'] == 'text':
                #     # Fill in the field
                #     field_value = f"We're testing here"  # The text you want to enter
                #     doc[field['name']] = field_value
    # return text

# Specify the path to your PDF file
file_path = "../../documents/i-130.pdf"
text = read_pdf(file_path)
print(text)
