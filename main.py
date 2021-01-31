from xml.dom import minidom
from os import listdir
from os.path import isfile, join

global path
path = 'C:\\Users\\timop\\Downloads\\Icons-Schwarz\\20190701_Icons\\SVG\\angepasst_ttkf\\' #'C:\\Users\\timop\Downloads\\Icons-Lidl-Beispiele\\angepasst_ttkf\\'
export_path = 'C:\\Users\\timop\\Downloads\\Icons-Schwarz\\20190701_Icons\\SVG\\angepasst_ttkf\\umbenannt\\'

sc_icons_start_number = 1
# CHOOSE FILL-COLOR BEFORE EXECUTION
lidl_blue = '#0050AA'
schwarz_purple = '#8A2093'
black = '#000000'
color = schwarz_purple
valid_file = True

def saveSvg(rootnode, svg_id):
    print('SVG_ID: ' + svg_id)
    filename = export_path + 'sc-icons-' + str(sc_icons_start_number) + '.svg'
    with open(filename, 'w') as f:
        f.write(rootnode.toxml())
        # f.write(adln_presentation.toprettyxml())
        f.close()

def setIDs(rootnode, file):
    try:
        global valid_file
        valid_file = True
        object_paths = rootnode.getElementsByTagName('path')
        svg_id = 'sc-icons-' + str(sc_icons_start_number)
        rootnode.setAttribute('id', svg_id)
        print(object_paths[0].getAttribute('d'))
        print(object_paths[0].hasAttribute('id'))
        for o_path in object_paths:
            o_path.setAttribute('id','sc-icon-color')
            o_path.setAttribute('fill', color)
        #saveSvg(rootnode, export_path + file)
        saveSvg(rootnode, svg_id)
        return svg_id
    except:
        valid_file = False
        print('STRANGE FILE FORMAT... ATTRIBUTES NOT CHANGED!')

def parseSvgXml(svg):
    try:
        domtree = minidom.parse(svg)
        rootnode = domtree.documentElement
        return rootnode
    except:
        print("Error parsing svg...")

def deleteGroup(svg_id):
    try:
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        print(export_path + svg_id + '.svg')
        domtree = minidom.parse(export_path + svg_id + '.svg')
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
        saveSvg(rootnode, export_path + svg_id + '.svg')
    except:
        print("no group to delete")


if __name__ == '__main__':
    # check all svg files in directory
    all_svg_files = [f for f in listdir(path) if isfile(join(path, f))]
    f = open(export_path + "svg-report.txt", "w")
    for file in all_svg_files:
        if file.endswith('.svg'):
            file_path = path + str(file)
            print(file_path)
            rootnode = parseSvgXml(file_path)
            svg_id = setIDs(rootnode, file)
            if valid_file:
                deleteGroup(svg_id)
                sc_icons_start_number += 1
                # Write Report
                f.write(svg_id + ';')
                f.write(file_path + ';' + '\n')
            else:
                f.write('*** INVALID FILE: ' + file_path + ';' + '\n')
    f.close()


