import re

import re
def extract_image_links(html_text):
    temp_pattern = "https?[:][/][/]\w*[.]com[/]\w*[.]"
    pattern = '('
    for i in range(len(type_pic)):
        pattern = pattern + temp_pattern + type_pic[i] + '|'
    pattern = pattern[:-1] +')'
    return re.findall(pattern, html_text)


type_pic = ['jpg', 'jpeg', 'png', 'gif']
sample_html = "<img src='https://example.com/image1.jpg'> <img src='http://example.com/image2.png'> <img src='https://example.com/image3.gif'>"

image_links = extract_image_links(sample_html)
if image_links:
    for image_link in image_links:
        print(image_link)
else:
    print("Нет ссылок с картинками в HTML тексте.")

