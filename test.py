import csv

def num2DNA(num):
    array = bin(num)
    if len(array) % 2 == 1:
        array = '0'+array
    i = 0
    DNA = ''
    while i<len(array):
        temp = array[i] + array[i+1]
        if temp == '00':
            DNA += 'A'
        elif temp == '01':
            DNA += 'G'
        elif temp == '10':
            DNA += 'C'
        elif temp == '11':
            DNA += 'T'
        i += 2
    return DNA

def DNA2num(DNA):
    array = ''
    for i in DNA:
        if i == 'A':
            array += '00'
        elif i == 'G':
            array += '01'
        elif i == 'C':
            array += '10'
        elif i == 'T':
            array += '11'
    return int(array, 2)

param = []
DNA_folder = []
with open('message.csv','r') as f:
    f_csv = csv.reader(f)
    for line in f_csv:
        param.append([int(line[0]), int(line[1])])
for pairs in param:
    DNA_folder.append([num2DNA(pairs[0]),num2DNA(pairs[1])])
print(DNA_folder)