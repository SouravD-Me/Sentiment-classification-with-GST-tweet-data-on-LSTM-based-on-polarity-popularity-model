sampleFile = open('b.txt','r').read()
splitFile = sampleFile.split('\n')

for eachLine in splitFile:
    x = eachLine.encode('utf-8')
    print (x.decode('unicode-escape'))






