import textwrap

def wrap(string, max_width):
    modified_string=""
    len_string=len(string)
    # modulo=len(string)%max_width
    for i in range(0,len_string,max_width):
        modified_string+=string[i:i+max_width]+'\n'
    return modified_string