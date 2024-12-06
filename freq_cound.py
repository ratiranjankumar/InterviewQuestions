def freq_cout(text):
    freq  = {}
    # Split the text into words
    new_lst = text.split(" ")
    for word in new_lst:
         # If the word is already in the dictionary, increment its count
        if word in freq:
            freq[word] += 1
        else:
             # Otherwise, add the word to the dictionary with a count of 1
            freq[word] = 1
    # Sort the dictionary by key (word) 
    freq = dict(sorted(freq.items()))
    return freq

#input text
input_text = "which is better python 2 or python 3"

# pass the input text to cound  word frequency and print the results
freq = freq_cout(input_text)
for w, f in freq.items():
    print(f"{w} : {f}")

