lines_seen = set() # holds lines already seen
outfile = open("Final POS Tagged.csv", "w")
for line in open("POS Tagged.csv", "r"):
    if line not in lines_seen: # not a duplicate
        outfile.write(line)
        lines_seen.add(line)
outfile.close()
