from bs4 import BeautifulSoup
import re
import pandas
import collections
collections.Callable = collections.abc.Callable

# with open('/Users/rohhaechang/testfolder0/sample.html', "r", encoding="utf-8") as f:
#     ht = f.read()


def revise_table(data):
    # soup = BeautifulSoup(html, "html.parser")

    # data = soup.find("table")

    tr_tags = data.find_all('tr')

    tr_list = []

    for tr_tag in tr_tags:
        t_list = []
        td_tags = tr_tag.find_all('td')
        for td_tag in td_tags:
            if td_tag.text.strip() == "":
                td_tag.decompose()
            else:
                p_tags = td_tag.find_all("p")
                if p_tags:
                    text = ''
                    for p_tag in p_tags:
                        text += p_tag.get_text(separator=' ', strip=True)
                        if "$" in text:
                            text = text.replace("$", "")
                        t_list.append(re.sub(r'\s+', ' ', text))

                else:
                    text = ''
                    one_p_tag = td_tag.find("p")
                    if one_p_tag:
                        print('p 태그 하나')
                    else:
                        text += td_tag.get_text(separator=' ', strip=True)
                        if "$" in text:
                            text = text.replace("$", "")
                        t_list.append(re.sub(r'\s+', ' ', text))

        tr_list.append(t_list)

    tr_list = [item for item in tr_list if item != []]

    for i in range(len(tr_list)):
        tr_list[i] = [ele for ele in tr_list[i] if ele != '']

    max_length = max(len(arr) for arr in tr_list)

    for arr in tr_list:
        if len(arr) != 1:
            while len(arr) < max_length:
                arr.insert(0, None)

    df = pandas.DataFrame(tr_list)
    print(df)
