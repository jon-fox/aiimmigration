import fitz  # PyMuPDF dependency
from data_objects.person import get_closest_method_name
from data_objects.person import setup_person
from data_objects.person import Person
import re
import yaml
from pprint import pprint


def input_with_validation(prompt, type_=None, min_=None, max_=None, range_=None):
    """Generic input function that includes validation."""
    while True:
        try:
            value = input(prompt)
            if type_ is not None:
                value = type_(value)
            if min_ is not None and value < min_:
                raise ValueError(f"Value must be at least {min_}.")
            if max_ is not None and value > max_:
                raise ValueError(f"Value must be no more than {max_}.")
            if range_ is not None and value not in range_:
                raise ValueError(f"Value must be within {range_}.")
            return value
        except ValueError as ve:
            print(ve)
            continue


def fill_pdf(file_path, person):
    special_case_like_barcode = []
    with open('config/i_130.yml', 'r') as file:
        i_130 = yaml.safe_load(file)

    # pprint.pprint(i_130)
    # open pdf file
    with fitz.open(file_path) as doc:
        # text = ""
        # Iterate through each page in the PDF
        for page in doc:
            # print(page.get_text())
            widgets = page.widgets()
            for widget in widgets:
                # print(widget.field_label)
                
                # print(field_name + " | " + widget.field_label + " | " + widget.field_value + " | eol")
                # print(widget.field_name)
                part_number = widget.field_name.split('.')[-1].split('_')[0].split('Line')[0].lower()
                field_numeral = widget.field_name.split('.')[-1].split('_')[0].split('Line')[-1]
                field_name = widget.field_name.split('.')[-1].split('_')[-1][:-3]
                if re.search(r'\[.*\]', field_numeral):
                    special_case_like_barcode.append(field_numeral)
                
                # print(widget.field_name)
                # print(f"Field Name: {field_name}")
                # print(f"Field Numeral: {field_numeral}")
                # print(f"Part Number: {part_number}")
                if part_number in i_130:
                    # print(f"INSIDE THE DICT!!")
                    if field_numeral in i_130[part_number]:
                        # print(f"INSIDE THE DICT!!")
                        field = i_130[part_number][field_numeral][0]
                        # print(field_name)
                        # print(field)
                        # print(widget.field_type_string)
                        if widget.field_type_string.lower() == 'combobox':
                            pprint(widget.choice_values)
                            count = 0
                            # widget.field_value = {'1B1': '1B1 - H-1B1 SPECIALITY OCCUPATION'}
                            # widget.field_value = "1B1 - H-1B1 SPECIALITY OCCUPATION"
                            print("Please select a value:")
                            for i, value in enumerate(widget.choice_values, 1):
                                print(f"{i}. {value}")

                            # Get the user's selection
                            selection = int(input("Enter the number of your selection: ")) - 1

                            # Check if the selection is valid
                            if 0 <= selection < len(widget.choice_values):
                                selected_value = widget.choice_values[selection]
                                print(f"You selected: {selected_value}")
                                print(f"Field label: {widget.field_label}")
                                if 'Select State' in widget.field_label:
                                    widget.field_value = selected_value[0]
                                else:
                                    widget.choice_values = (selected_value)
                                widget.update()
                                import time
                                time.sleep(5)
                                widget.update()
                            else:
                                print("Invalid selection")
                            # if count < 1:
                            #     # widget.field_value = 4
                            #     widget.choice_values = (('1B1', '1B1 - H-1B1 SPECIALITY OCCUPATION'))
                            #     count += 1
                            #     widget.update()
                            # else:
                            #     # widget.field_value = 'WY'
                            #     widget.choice_values = (('WY', 'WY'))
                            #     widget.update()
                        else:
                            # field_value = input_with_validation(f"Enter {field}: ", type_=str)
                            field_value = 'blah'
                            widget.field_value = field_value
                            widget.update()

                # print(widget.field_label + " | ")
                # closest_match = get_closest_method_name(person, field_name)
                # if closest_match:
                #     # method_to_call = getattr(person, closest_match, None)
                #     # print("Attribute Found " + str(closest_match))
                #     attribute_value = getattr(person, closest_match, None)
                #     # Check if the retrieved attribute is callable and call it
                #     widget.field_value = attribute_value
                #     widget.update()  # Assuming this function commits the changes to the widget
        doc.save("../documents/i-130-test.pdf", incremental=False, encryption=fitz.PDF_ENCRYPT_KEEP)

# Specify the path to your PDF file
file_path = "../documents/i-130.pdf"
# new_person = setup_person()
new_person = Person(first_name="blah", last_name="blah", employment="shallam", address="shallam")
print(f"Created person: {new_person.first_name} {new_person.last_name}")
text = fill_pdf(file_path, new_person)
# print(text)
