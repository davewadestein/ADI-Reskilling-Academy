import re

def pluralize(noun):          
    if re.search('[sxz]$', noun):     
        return noun + 'es'
    elif re.search('[^aeioudgkprt]h$', noun):
        return noun + 'es'
    elif re.search('[^aeiou]y$', noun):      
        return re.sub('y$', 'ies', noun)     
    else:
        return noun + 's'
