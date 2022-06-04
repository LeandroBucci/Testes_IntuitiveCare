import csv
import os


def file_cleaner(file_name):

    file = open(file_name, "r", encoding="Latin-1")
    basename = os.path.basename(file_name).split('.')[0]
    print(basename)
    outfile = open(basename+' Cleaned'+'.csv', "w+")
    outfile.write(file.readline())
    for line in file.readlines():
        if 'EVENTOS/ SINISTROS CONHECIDOS OU AVISADOS  DE ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR' in line and '0,00' not in line:
            outfile.write(line)

    file.close()


    if(os.path.basename(file_name) == '4T2021.csv'):
        file = open(file_name, "r", encoding="utf8")
        for line in file.readlines():
            if 'EVENTOS/ SINISTROS CONHECIDOS OU AVISADOS  DE ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR' in line and (line.count('0,00') != 2):
                    outfile.write(line)
                
            
            
    
        file.close()
    outfile.close()

def main():

    path = os.path.dirname(__file__)
    folder_list = ['2020', '2021']   
    file_list = [['1T2020.csv','2T2020.csv','3T2020.csv','4T2020.csv'],['1T2021.csv','2T2021.csv','3T2021.csv','4T2021.csv']]

    
    for i, folder in enumerate(folder_list):
        for file in file_list[i]:
            npath = os.path.join(path,folder, file)
            print(npath)
            file_cleaner(npath)
        
        
            


main()

