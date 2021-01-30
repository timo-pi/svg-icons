from xml.dom import minidom
import os

global path
path = 'C:\\temp\\svg-icons\\'
export_path = 'C:\\temp\\svg-icons\\export\\'
sc_icons_start_number = 1
lidl_blue = '#0050AA'
schwarz_purple = '#AA1499' # CHECK COLOR !!!!
color = lidl_blue

def saveSvg(rootnode, svg):
    with open(svg, 'w') as f:
        f.write(rootnode.toxml())
        # f.write(adln_presentation.toprettyxml())
        f.close()

def setIDs(rootnode, file):
    object_paths = rootnode.getElementsByTagName('path')
    rootnode.setAttribute('id', 'sc-icons-' + str(sc_icons_start_number))
    print(object_paths[0].getAttribute('d'))
    print(object_paths[0].hasAttribute('id'))
    for o_path in object_paths:
        o_path.setAttribute('id','sc-icon-color')
        o_path.setAttribute('fill', color)
    saveSvg(rootnode, export_path + file)

def parseSvgXml(svg):
    try:
        domtree = minidom.parse(svg)
        rootnode = domtree.documentElement
        return rootnode
    except:
        print("Error parsing svg...")

def deleteGroup(svg):
    try:
        domtree = minidom.parse(export_path + svg)
        rootnode = domtree.documentElement
        # return rootnode
    except:
        print("Error parsing svg for group deletion...")

    all_svg_paths = rootnode.getElementsByTagName('path')
    try:
        group = rootnode.getElementsByTagName('g')
        new_root = rootnode.removeChild(group[0])
        for e in all_svg_paths:
            rootnode.appendChild(e)
        saveSvg(rootnode, export_path + svg)
    except:
        print("no group to delete")


if __name__ == '__main__':
    # check all svg files in directory

    from os import listdir
    from os.path import isfile, join

    all_svg_files = [f for f in listdir(path) if isfile(join(path, f))]
    for file in all_svg_files:
        if file.endswith('.svg'):
            file_path = path + str(file)
            print(file_path)
            rootnode = parseSvgXml(file_path)
            setIDs(rootnode, file)
            deleteGroup(file)
            sc_icons_start_number += 1

    """for folder, subfolders, filenames in os.walk(path, topdown=True):
        for file in filenames:
            print(file)
               if file.endswith('.svg'):
                file_path = path + str(file)
                print(file_path)
                rootnode = parseSvgXml(file_path)
                setIDs(rootnode, file)
                deleteGroup(file)
                sc_icons_start_number += 1
                print(sc_icons_start_number)"""

