import requests
from bs4 import BeautifulSoup
import json
import re

base_url = "https://cs.bit.edu.cn/szdw/jsml/index.htm"

url = 'https://cs.bit.edu.cn/szdw/jsml/js/yx_2ffb434c6e114faea9b5114b88321940/index.htm'


def main():
    response = requests.get(base_url)
    soup = BeautifulSoup(response.content, 'html.parser')
    div_teachers = soup.find_all('div', class_='teacher')
    result = {}
    for div_teacher in div_teachers:
        class_name = div_teacher.find('h4').text
        result_list = []
        name_links_dict = {a.text: a['href'] for a in div_teacher.find_all('a')}
        for name, link in name_links_dict.items():
            tearch_result = teacher_crawl(name, link)
            result_list.append(tearch_result)
        result[class_name] = result_list
    with open('teacher_info.json', 'a', encoding='utf-8') as f:
        f.write(json.dumps(result, ensure_ascii=False))
    
    

def teacher_crawl(name, link):
    link = "https://cs.bit.edu.cn/szdw/jsml/" + link
    response = requests.get(link)
    soup = BeautifulSoup(response.content, 'html.parser')
    tmp = soup.find('div', class_='box_list')
    tmp = tmp.find_next('div', class_='xq_teacher')
    basic = tmp.find('div', class_='wz_teacher')
    if basic is None:  # 有些老师没有信息  直接返回空字典
        return {
            '姓名': name
        }
    lt = [lt for lt in basic.text.split('\n') if not re.search(r'^[\s]*$', lt)]
    basic_info_dic = {item.split('：')[0]:  item.split('：')[1] for item in lt}
    print(basic_info_dic)
    
    detail = tmp.find('div', class_='con_teacher')
    detail_info_dic = {}
    for dd in detail.find_all('div', class_='con01_t'):
        title = dd.find('h4').text.strip()
        p_list = [p.text.strip() for p in dd.find_all('p') if p.text != '']
        content = ""
        for p in p_list:
            content += p + "\n"
        detail_info_dic[title] = content
        
    return {**basic_info_dic, 'detail_info': detail_info_dic}

if __name__ == '__main__':
    main()