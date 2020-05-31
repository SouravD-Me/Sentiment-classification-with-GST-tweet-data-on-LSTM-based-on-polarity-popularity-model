import csv
new_dict = {}

filename = "sentiments.csv"
complist, orglist = [],[]
org = open ("Occured Words.csv", "wb")
org_writer = csv.writer(org)
for s in complist:
    for xs in orglist:
        if xs in s:
            print(org,xs)
filename = 'Final Occured Words.csv'    
with open(filename, "r") as fp:
    for line in fp:
        words = line.split()

        for word in words:
            word = word.lower()

            if word not in new_dict:
                new_dict[word] = 1
            else:
                new_dict[word] += 1

total_words = sum(new_dict.values(sentiments))
output_file = 'Final Occured Words.csv'
with open(output_file, "w") as fs:
    for key, value in sorted(new_dict.items()):
        sentimentsInString = str(sentiments)
        probability = value / total_words(sentiments)
        fs.write(key + ": " + str(probability) + str(popularity) + "\n") #sentiment_probability and popularity
