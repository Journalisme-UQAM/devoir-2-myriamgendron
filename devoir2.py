#!/usr/bin/env python
# coding: utf-8 

import csv

#Code trouvé pour traduire les chiffres romains
table=[['M',1000],['CM',900],['D',500],['CD',400],['C',100],['XC',90],['L',50],['XL',40],['X',10],['IX',9],['V',5],['IV',4],['I',1]]
def rom_to_int(string):
    result = 0
    for letter, value in table:
        while string.startswith(letter):
            result += value
            string = string[len(pairs[0]):]
    return result





donnees = []
with open('concordia1.csv', 'r') as f:
  reader = csv.reader(f)
  donnees = list(reader)


for index in range(len(donnees)):
    if index == 0:
        donnees[index].append('longTitre')
        donnees[index].append('type')
        donnees[index].append('nbPages')
    else:
        #Longueur du titre
        donnees[index].append(len(donnees[index][2]))
        #Doctorat ou Maitrise
        if 'Ph.D.' in donnees[index][6]:
            donnees[index].append('Thèse')
        else:
            donnees[index].append('Mémoire')
        # Calcul page
        nb_pages = 0
        tab_pages_aac = donnees[index][5].split(',')

        if 'leaves' in tab_pages_aac[0] or 'l.' in tab_pages_aac[0] or 'p.' in tab_pages_aac[0]:
            nb_pages = int(tab_pages_aac[0].lstrip().split(' ')[0])
        elif 'photo' in tab_pages_aac[1].lstrip().split(' ')[0]:
            nb_pages = 0
        else:
            nb1 = rom_to_int(tab_pages_aac[0])
            nb2 = tab_pages_aac[1].lstrip().split(' ')[0]
            if '-' in nb2:
                tab_nombres = tab_pages_aac[1].lstrip().split(' ')[0].split('-')
                nb2 = int(tab_nombres[0]) + int(tab_nombres[1])
            elif 'leaves' in nb2:
                nb2 = 0
            elif 'l' in nb2:
                nb2 = int(nb2.replace('l', '1'))
            nb_pages = nb1 + int(nb2)
        donnees[index].append(nb_pages)
        #print
        nom_complet = donnees[index][1] + ' ' + donnees[index][0]
        print('La %s de %s compte %d pages. Son titre est %s (%s caractères).' % \
                (donnees[index][8], nom_complet, nb_pages, donnees[index][2], donnees[index][7]))

with open('resultat.csv', 'wb') as myfile:
    wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
    wr.writerows(donnees)

