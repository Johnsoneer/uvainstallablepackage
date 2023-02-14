def space_compress(str_in: str):
    """
    Take a string and return a string with no whitespaces

    Args:
        - str_in(str): string to remove whitespace
    """
    if type(str_in) != str:
        return "Expected string but got {}".format(type(str_in))

    else:
        # replace multiline string with one-line string
        str_out = str_in.replace('\n',"")

        # reduce multiple whitespaces into one white space
        str_out = " ".join(str_in.split())

        return str_out