import glob
import requests 
import hashlib
import os 
path =os.getcwd()
print(path)
def getMd5(file_path):
    m = hashlib.md5()
    with open(file_path,'rb') as f:
        lines = f.read()
        m.update(lines)
    md5code = m.hexdigest()
    if md5code!=ena_md5:
        print(f)
file_list = glob.glob("*.fastq.gz")
for f in file_list:
    file_ids=f.split(".fastq.gz")[0]
    file_id=file_ids.split("_")
    part=file_id[1]
    x=requests.get('https://www.ebi.ac.uk/ena/portal/api/filereport?accession='+file_id[0]+'&result=read_run&fields=fastq_md5')
    ena_md5=x.text.splitlines()[1].split('\t')[1].split(";")[int(part)-1]
    file_path=(path+"/"+f)
    getMd5(file_path)

