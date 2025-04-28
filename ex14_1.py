#! python3

# write the contents of the infile into the outfile
# in the outfile, look for the indexstring, and replace each instance of it with the replstring

import fileinput

def sed(indexstring, replstring, infile, outfile):
    
    try:
        fileout = open(outfile, 'w')
    except:
        print("Something went wrong with the outfile file.")

    try:
        filein = open(infile, 'r')
    except:
        print("There\'s a problem with the input file.")

    try:
        for line in filein:
            fileout.write(line)
    except:
        print("Writing between the files didn\'t work.")

    filein.close()
    fileout.close()

    try:
        with open(outfile, 'r') as text_file:
            texts = text_file.read()
        with open(outfile, 'w') as file:
            texts = texts.replace(indexstring, replstring)
            file.write(texts)
        #fileout.close()
    except:
        print("Something about the string replacement didn\'t work.")

sed('working man', 'sovereign man', 'ex14_1.txt', 'ex14_1_out.txt')