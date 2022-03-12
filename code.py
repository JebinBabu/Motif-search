print('Locate Motif')
print('--------------------')

#gathering inputs
f = input('Enter .fasta file of the genome: ')
m = input('Motif to search for: ')
s = input('% Similarity: ')

print('\nThis would be a good time to check your messages!!!\n')


# preparing inputs
file = open(f,'r')
content = file.readlines()
file.close()

genome = ''
motif = m
motifSize = len(motif)
similarity = int(s)/100

def searchForMotif(genome):

    si = 0

    result = ['#','\t','Location','\t','Motif','\t','Similarity %','\n']

    #print(genome.count('CAACGGTTCC')) # == 2
    #print(genome.count('CAACGGTTGC')) # == 9

    for baseID,base in enumerate(genome):

        

        end = baseID + motifSize

        unkMotif = ''

        similar = motifSize

        for unkBaseID,unkBase in enumerate(genome[baseID:end]):

            if unkBase == motif[unkBaseID]:

                unkMotif += unkBase

            else:

                similar -= 1

                unkMotif += unkBase




        if (similar >= similarity * motifSize) and (len(unkMotif) == motifSize):

            si += 1
            percSimilarity = int((similar/motifSize)*100)

            result += [str(si),'\t',str(baseID + 1),'\t',str(unkMotif),'\t',str(percSimilarity),'\n']

    
    print('Done')
    return result



def resultFile(data):

    newData = ''.join(data)
    result = open('result.txt','w')
    result.write(newData)
    print('Data saved as \'result.txt\' file.\n')


for line in content[1::]:

    newArr = ''

    for el in line:

        if el == '\n':
            continue
        else:
            newArr += el

    genome += ''.join(newArr)


# finding similar motifs
result = searchForMotif(genome)

#saving result as result.txt file
resultFile(result)


x = input('Press Enter to exit')