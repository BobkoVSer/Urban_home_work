import re

def extract_image_links(html_text):
    sample_html = ["img src='https://example.com/image1.jpg", "img src='http://example.com/image2.png ",
                   "<img src='https://example.com/image3.gif"]
    for file in sample_html:
        match = re.search("\.jpeg$", file)
    if match:
        print("Файлы с расширением jpeg: это", file)