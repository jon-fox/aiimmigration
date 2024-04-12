import fitz  # PyMuPDF dependency
from data_objects.person import get_closest_method_name
from data_objects.person import setup_person

def fill_pdf(file_path, person):
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
                # print(widget.field_name.split('.')[-1].split('_')[-1][:-3] + " | " + widget.field_label)
                # print(widget.field_label)
                field_name = widget.field_name.split('.')[-1].split('_')[-1][:-3]
                # print(field_name + " | " + widget.field_label + " | " + widget.field_value + " | eol")
                # print(widget.xref)
                # print(dir(widget))
                # if field_name == 'SSN':
                #     widget.field_value = '123456789'
                #     widget.update()
                #     print(field_name + " | " + widget.field_label + " | " + widget.field_value + " | eol")
                #     break

                # print("Field name " + field_name)
                if field_name == get_closest_method_name(person, field_name):
                    print("Match with field name " + field_name)
                # field_name = annot.info["title"]
                # print(field_name)
                # if field_name in form_data:
                #     annot.set_text(form_data[field_name])
                # if field['type'] == 'text':
                #     # Fill in the field
                #     field_value = f"We're testing here"  # The text you want to enter
                #     doc[field['name']] = field_value
    # return text
        doc.save("../documents/i-130-test.pdf", incremental=False, encryption=fitz.PDF_ENCRYPT_KEEP)

# Specify the path to your PDF file
file_path = "../documents/i-130.pdf"
new_person = setup_person()
print(f"Created person: {new_person.first_name} {new_person.last_name}")
text = fill_pdf(file_path, new_person)
# print(text)
