"""
I didn't know how to parse .kml files to get exactly what I wanted, so I had chatgpt explain the structure to me, it
only hallucinated a little bit, and after some coaxing I was able to get it to extract polygon coordinates from the .kml
files - apparently they're just some horrendous XML tree.  This code finds all of the points in an enclosed polygon,
if it breaks because you tried to do some crazy topology - sorry, but for simple polygons you draw in google earth then
save it works pretty well for me.

After chatgpt generated some code, I used it to build a quick CLI to run it wrote a little code to get it to spit out
some javascript then finally copy it to the clipboard.

install works like this:
clone the repository
make a virtual environment called venv
install the requirements
then run the following bash command:

source geoconf.bash --input_file /path/to/kml_file.kml

it will output the text as a javascript variable and copy it to the clipboard for you.  I hope it helps.
-pat
"""

import argparse
import xml.etree.ElementTree as ET
import pyperclip
from pprint import pformat

def extract_polygon_coords(kml_file):
    # Parse the KML file
    tree = ET.parse(kml_file)
    root = tree.getroot()

    # KML namespaces
    ns = {'kml': 'http://www.opengis.net/kml/2.2'}

    # Find all coordinates in the KML file
    coordinates = []
    # this is actually PFM to me - it appears that it's finding all the coordinates - and so far it's been fine but
    # admittedly, I don't understand the lower level details of the xml tree structure here, but it is generating
    # precisely the output I want.  ChatGPT says it's searching through the structure of the xml tree and returning
    # the appropriate information.  Specifically it says when I asked it to explain it to me:
    """In summary, this line searches the entire XML tree starting from the root element for all occurrences of 
    coordinates elements that are situated within the specific hierarchy of Polygon -> outerBoundaryIs -> LinearRing. 
    These coordinates elements are typically used in KML to define the vertices of a polygon, and the returned list 
    will contain all such elements found in the document. """

    for coord in root.findall(".//kml:Polygon/kml:outerBoundaryIs/kml:LinearRing/kml:coordinates", namespaces=ns):
        # once we've got them all, iterate through them, convert them to floats and add them the list we're going to
        # return
        coords = coord.text.strip().split(" ")
        for c in coords:
            lon, lat, _ = c.split(",")
            coordinates.append((float(lon), float(lat)))

    return coordinates


def main():
    parser = argparse.ArgumentParser(description='Convert KML to Shapefile using GeoPandas')
    parser.add_argument('--input_file', '-i', help='Input KML file')
    args = parser.parse_args()

    coords = extract_polygon_coords(args.input_file)

    """ example of what the output should look like
    var roi = ee.Geometry.Polygon([
  [[-122.45, 37.74], [-122.45, 37.8], 
   [-122.4, 37.8], [-122.4, 37.74], [-122.45, 37.74]]
]);
    """

    output = rf"""
var roi = ee.Geometry.Polygon([
{",".join([pformat(list(coord)) for coord in coords])}
])
    """
    pyperclip.copy(output)
    print(output)
    print('to the clipboard')



if __name__ == '__main__':
    main()
