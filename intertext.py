from bs4 import BeautifulSoup
from pathlib import Path
import re

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
    elements_to_append = dest.find_all("p")
    root_elem = src.find("text")
    root_elem.extend(elements_to_append)
    return soup_src


def get_sources_files(file):
    file_name = Path(file).name
    ex = re.match("(.*)\.(.*)\.(.*)\..*",file_name)
    com_name = ex.group(1)
    src_file = ex.group(2)
    dest_file = ex.group(3)
    bo_file = f"./xml/{com_name}.{src_file}.xml"
    cn_file = f"./xml{com_name}.{dest_file}.xml"
    return bo_file,cn_file


def main(intextext_merged_files):
    bo_files,cn_files = [],[]
    for intextext_merged_file in intextext_merged_files:
        bo_file,cn_file = get_sources_files(intextext_merged_file)
        bo_files.append(bo_file)
        cn_files.append(cn_file)

    prev_xml_file = ""
    for index,bo_file in enumerate(bo_files):
        if index == 0:
            prev_xml_file = bo_file
            continue
        prev_xml = Path(prev_xml_file).read_text(encoding="utf-8")
        cur_xml = Path(bo_file).read_text(encoding="utf-8")
        soup_prev = BeautifulSoup(prev_xml,"xml")
        soup_cur = BeautifulSoup(cur_xml,"xml")
        prev_xml = merge(soup_prev,soup_cur)


if __name__ == "__main__":
    main()