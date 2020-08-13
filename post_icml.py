import os
import csv
import random
import tempfile
from google.cloud import storage
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]=''



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
        random_list = random.sample(word_list, k=10)
        
    all_message = []
    for word in random_list:
        word_list.remove(word)
        info = {"title": word[0], "text": word[1], "title": word[2], "text": word[3]}
        all_message.append(info)
    slack = slackweb.Slack(url="")
    slack.notify(attachments=all_message)

    with tempfile.TemporaryDirectory() as temp_path:
        write_path = temp_path + '/icml_edit.csv'
        with open(write_path, 'w') as file:
            writer = csv.writer(file, lineterminator='\n')
            writer.writerows(word_list)
        client = storage.Client()
        bucket_name = "penguin-first"
        bucket = client.get_bucket(bucket_name)
        blob = bucket.blob('icml_edit.csv')
        blob.upload_from_filename(filename=write_path)



if __name__ == '__main__':
    main()
