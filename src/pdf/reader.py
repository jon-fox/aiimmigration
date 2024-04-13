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
                # print(widget.field_label)
                field_name = widget.field_name.split('.')[-1].split('_')[-1][:-3]
                # print(field_name + " | " + widget.field_label + " | " + widget.field_value + " | eol")
                
                closest_match = get_closest_method_name(person, field_name)
                if closest_match:
                    # method_to_call = getattr(person, closest_match, None)
                    print("Attribute Found " + str(closest_match))
                    attribute_value = getattr(person, closest_match, None)
                    # Check if the retrieved attribute is callable and call it
                    widget.field_value = attribute_value
                    widget.update()  # Assuming this function commits the changes to the widget
        doc.save("../documents/i-130-test.pdf", incremental=False, encryption=fitz.PDF_ENCRYPT_KEEP)

# Specify the path to your PDF file
file_path = "../documents/i-130.pdf"
new_person = setup_person()
print(f"Created person: {new_person.first_name} {new_person.last_name}")
text = fill_pdf(file_path, new_person)
# print(text)
