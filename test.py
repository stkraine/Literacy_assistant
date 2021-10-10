truth = "dog is fat"
error = "My cat fat"

l1 = truth.split()
l2 = error.split()

error_words = []
offset = 0
for i, word in enumerate(l1):
    try:
        if word == l2[i+offset]:
            continue
        elif l2[i+offset+1] == word:
            offset = offset - 1
            continue

        elif l2[i+offset+2] == word:
            offset = offset - 2
            continue
        
        else:
            error_words.append(word)

    except Exception as e:
        error_words.append(word)
    
print(error_words)

