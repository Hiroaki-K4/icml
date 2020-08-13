import csv
from tqdm import tqdm








def main():
    with open('/home/hiroaki-k4/icml.csv') as f:
        reader = csv.reader(f)
        all_list = [row for row in reader]
        
    all_paper_list = []
    for paper in tqdm(all_list):
        if paper[1] == 'https://proceedings.ICML.cc/static/paper_files/icml/2020/None-Paper.pdf':
            continue
        else:
            all_paper_list.append(paper)

    with open('/home/hiroaki-k4/icml_edit.csv', 'w') as file:
        writer = csv.writer(file, lineterminator='\n')
        writer.writerows(all_paper_list)
        





if __name__ == '__main__':
    main()