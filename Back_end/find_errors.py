def find_errors(truth, transcript):
    '''
    takes in two strings, the truth and the transcripted text, and returns a list of the words that are
    pronounced incorrectly, according to AssemblyAI.
    '''
    l1 = truth.split()
    l2 = transcript.split()
    error_words = [] 
    offset = 0
    for i, word in enumerate(l1):
        try:
            # found word at i + offset
            if word == l2[i + offset]:
                continue

            # start looking ahead (only by 3 words) in case the user missed a word in the passage
            elif word == l2[i + offset + 1]:
                offset += 1
                continue

            elif word == l2[i + offset + 2]:
                offset += 2
                continue

            elif word == l2[i + offset + 3]:
                offset += 3
                continue
            
            # didn't find the word, so call it an error and start looking for the next word from the same point
            else:
                error_words.append(word)
                offset -= 1

        # reached the end of the array and got IndexError, so didn't find the word 
        # so call it an error and start looking for the next word from the same point
        except Exception as e:
            error_words.append(word)
            offset -= 1
        
    return error_words

