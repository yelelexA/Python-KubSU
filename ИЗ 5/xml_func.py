import xml.dom.minidom
from xml.dom import minidom

def qualification_xml_get(file):
 res_list = []
 dom = xml.dom.minidom.parse(file)
 dom.normalize()

 qualification_list = dom.getElementsByTagName("qualification")[0]
 element_list = qualification_list.getElementsByTagName("element")

 for el in element_list:
    res_list.append(el.childNodes[0].nodeValue)

 return res_list

def qualification_xml_to_str(file):
    res_lst = qualification_xml_get(file)
    str = """<?xml version="1.0" encoding="UTF-8"?>
    <test>
   <qualification>"""
    for el in res_lst:
        str += "\n      <element>"+el + "</element>"
    str += """\n   </qualification>
</test>"""
    return str

def qualification_xml_set(value):

    file = qualification_xml_to_str("qualification.xml")
    root = minidom.parseString(file)

    ins_tag = root.createElement("element")
    htext = root.createTextNode(value)

    ins_tag.appendChild(htext)
    items = root.getElementsByTagName("qualification")
    item = items[0]
    item_chidren = item.childNodes
    item.insertBefore(ins_tag, item_chidren[0])

    f = open("qualification.xml", "w", encoding="utf-8")
    f.writelines(root.toxml())
    f.close()

def patient_xml_get():
 res_list = []
 dom = xml.dom.minidom.parse("patient_import.xml")
 dom.normalize()
 element_list = dom.getElementsByTagName("element")

 for el in element_list:
    qualification_list = []
    qualification_list.append(el.getElementsByTagName("fio")[0].childNodes[0].nodeValue)
    qualification_list.append(el.getElementsByTagName("birth_date")[0].childNodes[0].nodeValue)
    qualification_list.append(el.getElementsByTagName("place_of_living")[0].childNodes[0].nodeValue)
    qualification_list.append(el.getElementsByTagName("blood_type")[0].childNodes[0].nodeValue)
    qualification_list.append(el.getElementsByTagName("diagnosis")[0].childNodes[0].nodeValue)
    res_list.append(qualification_list)

 return res_list

def patient_xml_to_str():
    res_lst = patient_xml_get()
    str = """<?xml version="1.0" encoding="UTF-8"?>
<patient>"""
    for el in res_lst:
     str += "\n      <element>"
     str += "\n         <fio>"+el[0]+"</fio>"
     str += "\n         <birth_date>"+el[1]+"</birth_date>"
     str += "\n         <place_of_living>"+el[2]+"</place_of_living>"
     str += "\n         <blood_type>"+el[3]+"</blood_type>"
     str += "\n         <diagnosis>"+el[4]+"</diagnosis>"
     str += "\n      </element>"

    str += """\n</patient>"""
    return str

def patient_xml_set(value):

    root = minidom.parse("patient_export.xml").documentElement
    b = root.childNodes[root.childNodes.length - 1]

    c = minidom.parseString("\n\n    <element>"+
    "\n        <id>"+str(value[0])+"</id>"
      "\n        <fio>"+value[1]+"</fio>"
      "\n        <birth_date>"+value[2]+"</birth_date>"
      "\n        <place_of_living>"+value[3]+"</place_of_living>"
      "\n        <blood_type>"+str(value[4])+"</blood_type>"
      "\n        <diagnosis>"+value[5]+"</diagnosis>"+
      "\n  </element>").documentElement
    root.insertBefore(c, b)

    f = open("patient_export.xml", "w", encoding="utf-8")
    f.writelines(root.toxml())
    f.close()

