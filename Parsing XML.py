import xml.etree.ElementTree 

tree=xml.etree.ElementTree.parse('compiler.xml') 
root=tree.getroot() 
print(root) 
for element in root.findall("book"): 
    print('\t---------------------------\n') 
    print('     ',element.tag,element.attrib,'\n') 
    for child in element: 
        print('  ',child.tag , ' ==> ', child.text)
