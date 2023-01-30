from bs4 import BeautifulSoup
from pathlib import Path


def update_xml(prev_xml,cur_xml):
    p_last = int(prev_xml.find_all("p")[-1].get("id"))
    cur_paras = cur_xml.find_all("p")
    for cur_para in cur_paras:
        sentences = cur_para.find_all("s")
        p_last+=1
        cur_para.attrs['id'] = p_last
        update_sentence(sentences,p_last)



def update_sentence(sentences,cur_par_id):
    cur_sentence_count =1
    for sentence in sentences:
        sentence.attrs['id'] = f"{cur_par_id}:{cur_sentence_count}"
        cur_sentence_count+=1


def merge(src,dest):

    update_xml(src,dest)
    elements_to_append = src.find_all("p")
    root_elem = src.find("text")
    root_elem.extend(elements_to_append)
    return soup_src



if __name__ == "__main__":
    bo_text = Path("./dmk-t341-t0202-08-padma-20221217.bo.xml").read_text(encoding="utf-8")
    bo_text2 = Path("./dmk-t341-t0202-09-JC-20221210.bo.xml").read_text(encoding="utf-8")
    soup_src = BeautifulSoup(bo_text,"xml")
    soup_dest = BeautifulSoup(bo_text2,"xml")
    xml = merge(soup_src,soup_dest)
    print(xml.prettify())