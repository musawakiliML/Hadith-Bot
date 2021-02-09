def pattern(value):
    patterns = ['<p>', '</p>','<b>','</b>', '<br/>','<i>','</i>','<br>','<a href="/abudawud/letter">','</a>']

    for i in patterns:
        if i in value:
            value = value.replace(i,"")
    return value
