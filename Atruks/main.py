import requests #что делает ключевое слово импорт, что за модуль реквест -> импорт подключает библиотеку requests
import xml.etree.ElementTree as ET #что такое as? as - сокращение alias
from bs4 import BeautifulSoup as bs
import lxml


# url = "https://training.atrucks.su/api/v3/customer/"
#
# auth_key="BMJDi7OUDFF6PTKlC7wGRim12sGIhECoQKdeOsXQXedB7Z8r"
# get_partners = 'get_partners'
#
#
# response = requests.post(f"https://training.atrucks.su/api/v3/customer/{get_partners}?auth_key={auth_key}")
# # print(response)
# with open(fr'D:\PycharmProjects\Python-Core\Atruks\inc_xml/{get_partners}.xml','w',encoding='utf8') as inc_file:
#     xml_file = inc_file.write(response.text)

fd = open('D:\PycharmProjects\Python-Core\Atruks\inc_xml\get_partners.xml','r',encoding='utf8')
xml_file = fd.read()

soup = bs(xml_file,'lxml')

partners = []#что означают квадратные скобки -> пустой список
for tag in soup.find_all('atrucks:partner'):
    partners.append(tag.text)
print(partners[0].split('\n')[1])

for partner_num in range(len(partners)):
    partners[partner_num] = partners[partner_num].split('\n')
    # print(p[partner_num][1])
    del partners[partner_num][0]
    del partners[partner_num][-1]



# names_lst = 'номер запроса,наименование партнера,инн партнера,кпп партнера,название партнера,номер партнера'.split(',')
# values_lst = [j for i in range(len(partners)) for j in partners[i]]
# print(*values_lst)



# print(partners[0][1])
# print(names_lst[0])
# data = {names_lst[i]:f'{p[i][j]}' for i in range(len(p)) for j in range(len(p[i]))}
#

# data_p = {p[i][4]:p[i]for i in range(len(p))}
# print(data_p['Перевозчик(1)'])
