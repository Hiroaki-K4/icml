import os
import csv
import tempfile
from google.cloud import storage
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]='/home/hiroaki-k4/Downloads/first-penguin-284413-5b7ff1cd5e53.json'





def main():
    with tempfile.TemporaryDirectory() as temp_path:
        write_path = temp_path + '/icml_edit.csv'
        client = storage.Client()
        bucket_name = "penguin-first"
        bucket = client.get_bucket(bucket_name)
        blob = bucket.get_blob('icml_edit.csv')
        blob.download_to_filename(write_path)
        with open(write_path) as f:
            reader = csv.reader(f)
            word_list = [row for row in reader]
        print(word_list)
        input()





if __name__ == '__main__':
    main()