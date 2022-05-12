import json
import csv
from csv import DictWriter

def get_my_key(obj):
  return obj['Recurrence Count']

if __name__ == "__main__":
    with open('feed.json','r') as file:
       data = json.load(file)

    entries = data['entries']

    all_data = []
    str_list = []
    for item in entries:
        content = item['content']

        str = content['title'].lower()
        str_list.extend(str.split())

    # print(str_list)
    total_data_count = 0
    for item in entries:
        content = item['content']
        str = content['title'].lower()
        single_str_list = str.split()
        unique_words = set(single_str_list)

        recurrence_count = 0

        for words in unique_words:
            # print(words)
            # print(str_list.count(words))
            if str_list.count(words) > 1:
                recurrence_count += 1

        img_list = []

        for img_url in content['images']:
            img_list.append(img_url['url'])


        content_obj = {
            'Guid': content['guid'],
            'Title': content['title'],
            'Related Image Urls': img_list,
            'Publish Date': content['published_at'],
            'Creation Date': content['created_at'],
            'Recurrence Count': recurrence_count
        }
        all_data.append(content_obj)
        total_data_count += 1
        # all_data.append(article(content['guid'], content['title'], img_list, content['published_at'], content['created_at'], recurrence_count))
        # break

    all_data.sort(key = get_my_key, reverse=True)
    # total_data_count = count(all_data)
    # print(total_data_count)
    cnt = 0
    check = 0
    field_names = ['Guid', 'Title', 'Related Image Urls', 'Publish Date', 'Creation Date', 'Recurrence Count']

    with open('event.csv', 'w') as f_object:
        dictwriter_object = DictWriter(f_object, fieldnames=field_names)
        dictwriter_object.writeheader()
        for item in all_data:
            if cnt > 3:
                if item['Recurrence Count'] != check:
                    f_object.close()
                    break
            dictwriter_object.writerow(item)
            cnt += 1
            check = item['Recurrence Count']

            if cnt >= total_data_count:
                f_object.close()
                break
