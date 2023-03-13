import sys
final_phrase = ''
for i, arg in enumerate(sys.argv):
    if i == 0:
        final_phrase = ''
    else:
        word = arg
        i = 0
        for x in word:
            i = i + 1
            if i%2 == 1:
                final_phrase = final_phrase + x.upper()
            else:
                final_phrase = final_phrase + x 
        final_phrase = final_phrase +' '
print(final_phrase)
       