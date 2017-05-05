# Planet Pipeline GUI
The Planet Pipeline GUI came from the actual cli (command line interface tools) to enable the use of tools required to access control and 

![GUI](http://i.imgur.com/pEaFzKL.gif)
## Table of contents
* [Installation](#installation)
* [Getting started](#getting-started)
    * [Planet Key](#planet-key)
    * [AOI JSON](#aoi-json)
    * [Activate or Check Asset](#activate-or-check-asset)
    * [Download Asset](#download-asset)
	* [Metadata Parser](#metadata-parser)
* [Credits](#credits)
## Installation
We assume Planet Python API is installed you can install by simply running 
```
pip install planet
```
Further instructions can be found [here](https://www.planet.com/docs/api-quickstart-examples/cli/) 

To install the tool:
```
git clone https://github.com/samapriya/Planet-Pipeline-GUI.git
cd Planet-Pipeline-GUI && pip install .
```

The application can be also run directly by executing PlanetPipe_GUI.pyc script. 
You require two important packages for this to run
```
WxPython(which is what the GUI is built on)
for windows(Tested in Windows 10)
https://wxpython.org/download.php

for linux(Tested in Ubuntu 16)
sudo add-apt-repository "deb http://archive.ubuntu.com/ubuntu utopic main restricted universe"  
sudo apt-get update
apt-cache search python-wxgtk3.0
sudo apt-get install python-wxgtk3.0
```

## Getting started
This should be pretty simple on windows systems with python >=2.7.13 you can just double click the PlanetPipe_GUI.pyc for linux user python PlanetPipe_GUI.pyc

### Planet Key
This tool basically asks you to input your Planet API Key using a password prompt this is then used for all subsequent tools

![planet_key](http://i.imgur.com/YwQGbi5.jpg)

If using on a private machine the Key is saved as a csv file for all future runs of the tool.
 
### AOI JSON
The aoijson tab within the toolset allows you to create filters and structure your existing input file to that which can be used with Planet's API. The tool requires inputs with start and end date, along with cloud cover. You can choose from multiple input files types such as KML, Zipped Shapefile, GeoJSON, WKT or even Landsat Tiles based on PathRow numbers. The geo option asks you to select existing files which will be converted into formatted JSON file called aoi.json. If using WRS as an option just type in the 6 digit PathRow combination and it will create a json file for you.

![aoijson](http://i.imgur.com/UB6nlmu.jpg)

### Activate or Check Asset
The activatepl tab allows the users to either check or activate planet assets, in this case only PSOrthoTile and REOrthoTile are supported because I was only interested in these two asset types for my work but can be easily extended to other asset types. This tool makes use of an existing json file sturctured for use within Planet API or the aoi.json file created earlier

![activatepl](http://i.imgur.com/nmK9gdb.gif)

### Download Asset
Having metadata helps in organising your asstets, but is not mandatory - you can skip it.
The downloadpl tab allows the users to download assets. The platform can download Asset or Asset_XML which is the metadata file to desired folders.One again I was only interested in these two asset types(PSOrthoTile and REOrthoTile) for my work but can be easily extended to other asset types.

![downloadpl](http://i.imgur.com/8dvZtpp.gif)

### Metadata Parser
The metadata tab is a more powerful tool and consists of metadata parsing for PlanetScope OrthoTile RapiEye OrthoTile along with Digital Globe MultiSpectral and DigitalGlobe PanChromatic datasets. This was developed as a standalone to process xml metadata files from multiple sources and is important step is the user plans to upload these assets to Google Earth Engine. The combine Planet-GEE Pipeline tool will be made available soon for testing.

![metadata](http://i.imgur.com/R3BlsiG.gif)

# Credits
[JetStream](https://jetstream-cloud.org/) A portion of the work is suported by JetStream Grant TG-GEO160014.

Also supported by [Planet Labs Ambassador Program](https://www.planet.com/markets/ambassador-signup/)
