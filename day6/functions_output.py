# Functions with output

def title(first_name, last_name):
    if first_name == "" or last_name == "":
        return "You didn't provide valid inputs."
    else:
        return first_name[0].upper() + first_name[1:].lower() + " " + last_name[0].upper() + last_name[1:].lower()


formatted_string = title("Giovanni", "")
print(formatted_string)
