# KML Polygon Extractor

This tool is designed to extract polygon coordinates from KML files. KML (Keyhole Markup Language) files are XML-based and often used for geographical data. This script parses these files to find and extract coordinates of enclosed polygons, particularly useful for polygons drawn in Google Earth.

## Features

- Extracts coordinates of polygons from KML files.
- Outputs coordinates as a JavaScript variable.
- Automatically copies the output to the clipboard for easy use.

## Installation

1. Clone this repository. `git clone https://github.com/patpragman/shapefl.git` and navigate to the newly created directory
2. Create a virtual environment named `venv` on linux:  `python3 -m venv venv`.
3. Install the required dependencies. `pip install -r requirements.txt`

## Usage

Run the script using the following command:

`source geoconf.bash --input_file /path/to/kml_file.kml`


The script will output the coordinates as a JavaScript variable and copy them to the clipboard.

## Example Output

```javascript
var roi = ee.Geometry.Polygon([  [[-122.45, 37.74], [-122.45, 37.8], 
   [-122.4, 37.8], [-122.4, 37.74], [-122.45, 37.74]]
]);
```

## Limitations

The script is designed for simple polygons. It might not work as expected with complex topologies.

## Acknowledgements

Thanks to ChatGPT for assistance in understanding KML structures and initial code generation.

## Author

* Pat Pragman

Feel free to contribute, report issues, or suggest improvements.