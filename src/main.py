import csv
import os

csv_path = "/Users/jungmo/Documents/github/csv2libsvm/csv/"
libsvm_savepath = "/Users/jungmo/Documents/github/csv2libsvm/libsvm/"

csv_array=[]

for csv_filename in os.listdir(csv_path):

    libsvm_filename = os.path.splitext(csv_filename)[0]+".txt"

    csv_fp = open(csv_path+csv_filename,'rb')
    libsvm_fp = open(libsvm_savepath+libsvm_filename,'w')

    csvReader = csv.reader(csv_fp)

    print csvReader
    for row in csvReader:
        print row
        num_class = len(row) - 1
        print num_class
        break

    for line in csvReader:
        libsvm_fp.write(line[0]+" ")

        for eachClass in range(0,num_class) :
            libsvm_fp.write(str(eachClass)+":"+line[eachClass+1]+" ")

        libsvm_fp.write("\n")

    libsvm_fp.close()
    csv_fp.close()
