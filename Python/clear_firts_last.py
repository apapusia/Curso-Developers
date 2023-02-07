html=['<h1>', 'some content','</h1>']

def remove_first_and_last(list_to_clean):
    if  len(list_to_clean)<=2:
        print('El código HTML está vacio')
    else:
        _, *content, _=list_to_clean
        return content

print (remove_first_and_last(html))