# assuming transcript is a string

transcript = "This is a string to hold the spoken transcript from Assembly AI"
passage = "This is a string to hold the selected passage"

transcript_list = transcript.split()
passage_list = passage.split()
wrong_words = {}

count = 0

for word in passage_list:
    if count > len(passage):
        print("Spoken transcript exceeds word count of passage")
        break

    if word !=transcript_list[count]:
        wrong_words[word] = [transcript_list[count], count]

    count += 1

print(wrong_words)



