import requests
url = 'https://zajecia-programowania-xd.pl/flagi'

def web_to_txt(url):
    raw_text = requests.get(url)
    text = raw_text.text
    return text

def links_to_list(text):
    lines = text.split('</p>')
    links = []
    temp = []

    for line in lines:
        link = line.replace('<p>', '')
        link = link.replace('- ', '')
        link = link.replace('.pl.', '.pl')
        link = link.replace('/', '.')
        link = link.strip()

        if ' ' in link or '<' in link:
            continue
        elif len(link) == 0:
            continue
        elif '.' not in link:
            continue

        temp.append(link)

    for i in temp:
        if i not in links:
            links.append(i)

    return links

def link_counter(urls):
    counter = 0

    for i in urls:
        counter += 1

    return counter

def domain_counter(urls):
    counter = 0
    for i in urls:
        if '.com.pl' in i:
            counter += 1

    return counter


text = web_to_txt(url)
list = links_to_list(text)

for i in list:
    print(i)

print(link_counter(list))
print(domain_counter(list))
