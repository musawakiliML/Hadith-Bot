def pattern(value):
    patterns = ['<p>', '</p>','<b>','</b>', '<br/>','<i>','</i>']

    for i in patterns:
        if i in value:
            value = value.replace(i,"")
    return value
