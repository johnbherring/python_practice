from typing import get_type_hints


a_string = 'john herring'

print (a_string.count(''))get_type_hints

# print (a_string.capitalize())

print ('Is ' + a_string + ' Title Case? ' + str(a_string.istitle()))

a_string = a_string.title()

print ('The title converted string is: ' + '\"'+ a_string + '\"' + ' Is this title case? ' + str(a_string.istitle())) 