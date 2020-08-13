import os
import csv
import time
import random
import tempfile
import slackweb
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
        attachments_title = []
        attachments_contents = []
        paper_title = {"title": word[0],
                "text": word[1]}
        paper_contents = {"title": word[2],
                "text": word[3]}
        attachments_title.append(paper_title)
        attachments_contents.append(paper_contents)
        slack = slackweb.Slack(url="https://hooks.slack.com/services/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")
        slack.notify(attachments=attachments_title)
        slack.notify(attachments=attachments_contents)
        time.sleep(1)

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
