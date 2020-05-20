from random import randint

def random_next_hope():
        octets = []
        octets.append(str(randint(0,223)))
        for x in range(1,4):
            octets.append(str(randint(0,255)))
        return '.'.join(octets)


def random_destination():
    octets = []
    for x in range(4):
        octets.append(str(randint(0, 224)))
    return '.'.join(octets)

#--generer addresse suivant la classe------------
def randomIp(classe):
    if(classe =='A'):
        octets = []
        octets.append(str(randint(0, 127)))
        for x in range(3):
            octets.append('0')
        prefix='{:08b}'.format(int(octets[0]))

        return ('.'.join(octets)+"\t\t"+"255.0.0.0"+"\t\t"+
                                prefix+"\t\t"+random_next_hope()+"\t\t"+"S"+str(randint(1,4))+"\t\t"+str(randint(1,16)))
    elif(classe == 'B'):
        octets = []
        octets.append(str(randint(128, 191)))
        octets.append(str(randint(0, 255)))
        for x in range(0,2):
            octets.append('0')
        prefix = '{:08b}'.format(int(octets[0]))+'{:08b}'.format(int(octets[1]))
        return ('.'.join(octets)+"\t\t"+"255.255.0.0"+"\t\t"+prefix+
                                    "\t\t"+random_next_hope()+"\t\t"+"S"+str(randint(1,4))+"\t\t"+str(randint(1,16)))
    elif (classe == 'C'):
        octets = []
        octets.append(str(randint(192, 223)))
        octets.append(str(randint(0, 255)))
        octets.append(str(randint(0, 255)))
        octets.append('0')

        prefix = '{:08b}'.format(int(octets[0])) + '{:08b}'.format(int(octets[1]))+'{:08b}'.format(int(octets[2]))
        return ('.'.join(octets)+"\t\t"+"255.255.255.0"+"\t\t"+prefix+
                                "\t\t"+random_next_hope()+"\t\t"+"S"+str(randint(1,4))+"\t\t"+str(randint(1,16)))
    elif (classe == 'D'):
        octets = []
        octets.append(str(randint(224, 239)))
        for x in range(3):
            octets.append(str(randint(0, 255)))
        prefix = '{:08b}'.format(int(octets[0])) + '{:08b}'.format(int(octets[1])) + '{:08b}'.format(int(octets[2]))
        return ('.'.join(octets) +"\t\t"+ "255.255.255.0" + "\t\t" +prefix+
                                "\t\t" + random_next_hope() + "\t\t" + "S" + str(randint(1, 4)) + "\t\t" + str(randint(1, 16)))

#--------remplir la table--------------
def generateTable(file):
    f = open(file,'w')
    f.write('0.0.0.0\t\t0.0.0.0\t\t*\t\t192.168.1.1\t\tS3\t\t1\n')
    for i in range(0,500):
        f.write(randomIp(('A')) + '\n')
    for i in range(0,300):
        f.write(randomIp(('B')) + '\n')
    for i in range(0,200):
        f.write(randomIp(('C')) + '\n')
    f.close()

def generateDestinations(file):
    f = open(file, 'w')
    for i in range(0, 100):
        f.write(random_destination()+'\n')
    f.close()

generateTable('table_routage.txt')
generateDestinations('destinations.txt')