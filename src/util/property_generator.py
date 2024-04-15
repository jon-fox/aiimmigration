def generate_property_methods_from_file(file_path, output):
    lines = []
    try:
        with open(file_path, 'r') as file:
            attributes = [line.strip() for line in file if line.strip()]
    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
        return ""
    except Exception as e:
        print(f"An error occurred: {e}")
        return ""

    for attr in attributes:
        # Generate the getter method
        lines.append(f"@property")
        lines.append(f"def {attr}(self):")
        lines.append(f"    return self._{attr}")
        lines.append("")

        # Generate the setter method
        lines.append(f"@{attr}.setter")
        lines.append(f"def {attr}(self, value):")
        lines.append(f"    self._{attr} = value")
        lines.append("")
    
    try:
        with open(output, 'w') as file:
            file.write("\n".join(lines))
        print(f"Successfully written to {output}")
    except Exception as e:
        print(f"Failed to write to file: {e}")


    # return "\n".join(lines)

# Usage example
file_path = './properties.txt'
output = './properties-output.txt'
property_code = generate_property_methods_from_file(file_path, output)
# print(property_code)
