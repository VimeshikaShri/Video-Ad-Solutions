import xml.etree.ElementTree as ET
import sys

# Load the XML file passed as a command-line argument
filename = sys.argv[1]
with open(filename) as f:
    xml_string = f.read()

# Parse the XML
root = ET.fromstring(xml_string)

# Check the root element
print(f"Root element: {root.tag}")
print(f"VAST version: {root.attrib.get('version', 'NOT FOUND')}")