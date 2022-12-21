# input sentence
sentc = input("Input sentence: ")
# split sentence
sentc = sentc.replace(',', '').lower().split()
# special char
spc = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '~', ':', "'", '+', '[', '\\', '@', '^', '{', '%', '(', '"', '*', '|', ',', '&', '<', '`', '}', '_', '=', ']', '!', '>', ';', '#', '$', ')', '/']

# filter sentence
fil_sentc = [x for x in sentc if
              all(y not in x for y in spc)]

count = len(fil_sentc)
print(count)