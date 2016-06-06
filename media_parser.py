__author__ = 'Bogdan'
__email__ = 'evstrat.bg@gmail.com'

import requests
from lxml.html import parse
from bs4 import BeautifulSoup
from random import choice
from grab import Grab

class Movie(object):
    def __init__(self):
        self.name = ''
        self.year = ''
        self.adr = ''
        self.email = []
        self.mobile = ''


user_agents = ['Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)',
               'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)',
               'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT 5.0 )',
               'Mozilla/4.0 (compatible; MSIE 5.5; Windows 98; Win 9x 4.90)',
               'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.1) Gecko/2008070208 Firefox/3.0.1',
               'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.14) Gecko/20080404 Firefox/2.0.0.14',
               'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/525.13 (KHTML, like Gecko) Chrome/0.2.149.29 Safari/525.13',
               'Mozilla/4.8 [en] (Windows NT 6.0; U)',
               'Mozilla/4.8 [en] (Windows NT 5.1; U)',
               'Opera/9.25 (Windows NT 6.0; U; en)',
               'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0; en) Opera 8.0',
               'Opera/7.51 (Windows NT 5.1; U) [en]',
               'Opera/7.50 (Windows XP; U)',
               'Avant Browser/1.2.789rel1 (http://www.avantbrowser.com)',
               'Mozilla/5.0 (Windows; U; Win98; en-US; rv:1.4) Gecko Netscape/7.1 (ax)',
               'Mozilla/5.0 (Windows; U; Windows XP) Gecko MultiZilla/1.6.1.0a',
               'Opera/7.50 (Windows ME; U) [en]',
               'Mozilla/3.01Gold (Win95; I)',
               'Mozilla/2.02E (Win95; U)',
               'Mozilla/5.0 (Macintosh; U; PPC Mac OS X; en) AppleWebKit/125.2 (KHTML, like Gecko) Safari/125.8',
               'Mozilla/5.0 (Macintosh; U; PPC Mac OS X; en) AppleWebKit/125.2 (KHTML, like Gecko) Safari/85.8',
               'Mozilla/4.0 (compatible; MSIE 5.15; Mac_PowerPC)',
               'Mozilla/5.0 (Macintosh; U; PPC Mac OS X Mach-O; en-US; rv:1.7a) Gecko/20050614 Firefox/0.9.0+',
               'Mozilla/5.0 (Macintosh; U; PPC Mac OS X; en-US) AppleWebKit/125.4 (KHTML, like Gecko, Safari) OmniWeb/v563.15',
               'Mozilla/5.0 (X11; U; Linux; i686; en-US; rv:1.6) Gecko Debian/1.6-7',
               'Mozilla/5.0 (X11; U; Linux; i686; en-US; rv:1.6) Gecko Epiphany/1.2.5',
               'Mozilla/5.0 (X11; U; Linux i586; en-US; rv:1.7.3) Gecko/20050924 Epiphany/1.4.4 (Ubuntu)',
               'Mozilla/5.0 (compatible; Konqueror/3.5; Linux) KHTML/3.5.10 (like Gecko) (Kubuntu)',
               'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1.19) Gecko/20081216 Ubuntu/8.04 (hardy) ',
               'Firefox/2.0.0.19',
               'Mozilla/5.0 (X11; U; Linux; i686; en-US; rv:1.6) Gecko Galeon/1.3.14',
               'Konqueror/3.0-rc4; (Konqueror/3.0-rc4; i686 Linux;;datecode)',
               'Mozilla/5.0 (compatible; Konqueror/3.3; Linux 2.6.8-gentoo-r3; X11;',
               'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.6) Gecko/20050614 Firefox/0.8',
               'ELinks/0.9.3 (textmode; Linux 2.6.9-kanotix-8 i686; 127x41)',
               'ELinks (0.4pre5; Linux 2.6.10-ac7 i686; 80x33)',
               'Links (2.1pre15; Linux 2.4.26 i686; 158x61)',
               'Links/0.9.1 (Linux 2.4.24; i386;)',
               'MSIE (MSIE 6.0; X11; Linux; i686) Opera 7.23',
               'Opera/9.52 (X11; Linux i686; U; en)',
               'Lynx/2.8.5rel.1 libwww-FM/2.14 SSL-MM/1.4.1 GNUTLS/0.8.12',
               'w3m/0.5.1',
               'Links (2.1pre15; FreeBSD 5.3-RELEASE i386; 196x84)',
               'Mozilla/5.0 (X11; U; FreeBSD; i386; en-US; rv:1.7) Gecko',
               'Mozilla/4.77 [en] (X11; I; IRIX;64 6.5 IP30)',
               'Mozilla/4.8 [en] (X11; U; SunOS; 5.7 sun4u)',
               'Mozilla/3.0 (compatible; NetPositive/2.1.1; BeOS)',
               'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)',
               'Googlebot/2.1 (+http://www.googlebot.com/bot.html)',
               'msnbot/1.0 (+http://search.msn.com/msnbot.htm)',
               'msnbot/0.11 (+http://search.msn.com/msnbot.htm)',
               'Mozilla/5.0 (compatible; Yahoo! Slurp; http://help.yahoo.com/help/us/ysearch/slurp)',
               'Mozilla/2.0 (compatible; Ask Jeeves/Teoma)',
               'Mozilla/5.0 (compatible; ScoutJet; +http://www.scoutjet.com/)',
               'Gulper Web Bot 0.2.4 (www.ecsl.cs.sunysb.edu/~maxim/cgi-bin/Link/GulperBot)',
               'EmailWolf 1.00',
               'grub-client-1.5.3; (grub-client-1.5.3; Crawl your own stuff with http://grub.org)',
               'Download Demon/3.5.0.11',
               'OmniWeb/2.7-beta-3 OWF/1.0',
               'SearchExpress',
               'Microsoft URL Control - 6.00.8862']

proxies = []
pr = open('proxies.txt', 'r', encoding='utf8')
for line in pr:
    proxies.append(line.rstrip('\n'))


def collect_urls():
    deep_urls = []
    urls = []
    url = 'http://www.kinopoisk.ru/s/type/film/list/1/order/rating/m_act%5Bfrom_year%5D/2010/m_act%5Bto_year%5D/2015/m_act%5Bcountry%5D/2/m_act%5Btype%5D/film/page/'
    for i in range(1, 25):
        new_url = url + str(i) + '/'
        urls.append(new_url)
    for u in urls:
        data = parse(u)
        for element in data.findall('//*[@class="info"]'):
            children = element.getchildren()
            for el in children[0]:
                if el.attrib.values()[0] != 'year':
                    deep_urls.append('http://www.kinopoisk.ru' + el.attrib.values()[0])
    f = open('urls.txt', 'w', encoding='utf8')
    for u in deep_urls:
        f.write(u + '\r\n')
    return deep_urls


def parsing_html(url):
    collected_data = []
    print(url)
    print({'http': 'http://' + choice(proxies)})
    try:
        page = requests.get(url, headers={'User-Agent': choice(user_agents)}, proxies={'http': 'http://189.218.106.135:10000'}).content.decode('cp1251')
    except:
        page = requests.get(url, headers={'User-Agent': choice(user_agents)}, proxies={'http': 'http://220.248.224.243:8089'}).content.decode('cp1251')
    soup = BeautifulSoup(page, 'lxml')
    print(soup)
    #print(soup.findAll('div', id="photoInfoTable"))
    print('----------------')

    movie_name = soup.findAll('h1', itemprop="name")
    actors = soup.findAll('li', itemprop="actors")
    director = soup.findAll('td', itemprop="director")
    producer = soup.findAll('td', itemprop="producer")
    cost = soup.findAll('dd')
    if len(cost) > 3:
        cost = soup.findAll('dd')[2]
    else:
        cost = 'Нет данных'
    composer = soup.findAll('td', itemprop="musicBy")
    genre = soup.findAll('span', itemprop="genre")
    #print(cost)
    collected_data.append((movie_name[0], actors, director[0], producer, cost, composer, genre))
    return collected_data


def write_out():
    arr_urls = []
    urls = open('urls.txt', 'r', encoding='utf8')
    for u in urls:
        arr_urls.append(u.strip('\n'))
    c = 100
    with open('out_data.csv', 'a', encoding='utf8') as f:
        for ur in arr_urls[101:]:
            s = ''
            for element in parsing_html(ur):
                for el in element:
                    s += str(el)
                    s += ';'
            c += 1
            print('ИСПОЛЬЗОВАННЫЕ ССЫЛКИ -------' + str(c))

            #print(s.replace('\n', '').replace('[', '').replace(']', ''))
            f.write(s.replace('\n', '').replace('[', '').replace(']', '') + '\r\n')

write_out()
