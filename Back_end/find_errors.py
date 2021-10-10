
def find_errors(truth, transcript):
    '''
    takes in two strings, the truth and the transcripted text, and returns a list of the words that are
    pronounced incorrectly, according to AssemblyAI
    '''
    l1 = truth.split()
    l2 = transcript.split()

    error_words = [] 
    offset = 0
    for i, word in enumerate(l1):
        try:
            if word == l2[i + offset]:
                continue

            elif word == l2[i + offset + 1]:
                offset += 1
                continue

            elif word == l2[i + offset + 2]:
                offset += 2
                continue

            elif word == l2[i + offset + 3]:
                offset += 3
                continue
            
            else:
                error_words.append(word)
                offset -= 1

        except Exception as e:
            error_words.append(word)
            offset -= 1
        
    return error_words

