import glob

files = glob.glob('txt/*.txt')

with open('output.txt', 'w', encoding='utf-8') as outfile:
    for file in files:
        #print(file)
        with open(file, encoding='utf-8') as infile:
            #test = infile.read()
            #print(test[:100])
            print('reading' + file)
            contents = infile.read()
            outfile.write(contents)
    #outfile.close()

#with open('txt/miracle-mile.txt', encoding='utf8') as file:
    #text = file.read()
    #print(text[:100])
