#! /usr/bin/env python

import argparse,os,subprocess
from gooey import Gooey, GooeyParser
from gooey import GooeyParser
from message import display_message
from cli_aoi2json import aoijson
import getpass,csv,re,time,sys

os.chdir(os.path.dirname(os.path.realpath(__file__)))
def planet_key_entry():
    planethome=expanduser("~/.config/planet/")
    if not os.path.exists(planethome):
        os.mkdir(planethome)
    print("Enter your Planet API Key")
    password=getpass.getpass()
    os.chdir(planethome)
    with open("pkey.csv",'w') as completed:
        writer=csv.writer(completed,delimiter=',',lineterminator='\n')
        writer.writerow([password])
def planet_key_from_parser(args):
    planet_key_entry()

def aoijson_from_parser(args):
    aoijson(start=args.start,end=args.end,cloud=args.cloud,inputfile=args.inputfile,geo=args.geo,loc=args.loc)
def metadata_from_parser(args):
    metadata(asset=args.asset,mf=args.mf,mfile=args.mfile,errorlog=args.errorlog)
def activatepl_from_parser(args):
    aoi_json=str(args.aoi)
    action_planet=str(args.action)
    asset_type=str(args.asst)
    try:
        os.system("python ./download.py --query "+args.aoi+" --"+args.action+" "+asset_type)
    except Exception:
        print(' ')
def space_from_parser(args):
    aoi=args.aoi
    local=str(args.local)
    asset=str(args.asset)
    inlet='"'+local+'"'+" "+asset
    try:
        os.system('python download.py --query '+aoi+' --size '+inlet)
    except Exception:
        print(' ')

def downloadpl_from_parser(args):
    aoi_json=str(args.aoi)
    planet_pathway=str(args.pathway)
    asset_type=str(args.asst)
    try:
        os.system("python download.py --query "+args.aoi+" --download"+" "+args.pathway+" "+asset_type)
    except Exception:
        print(' ')
spacing="                               "
from gooey import Gooey, GooeyParser
@Gooey(dump_build_config=True, program_name="Planet and EE Pipeline")
def main(args=None):
    parser = GooeyParser(description='Planet and EE Pipeline')
    subparsers = parser.add_subparsers()
    nonbuffered_stdout = os.fdopen(sys.stdout.fileno(), 'w', 0)
    sys.stdout = nonbuffered_stdout

    parser_planet_key = subparsers.add_parser('planet_key', help='Enter your planet API Key')
    parser_planet_key.set_defaults(func=planet_key_from_parser)
    
    parser_aoijson=subparsers.add_parser('aoijson',help='Convert KML/SHP/WKT/GeoJSON file to aoi.json file with structured query for use with Planet API 1.0')
    parser_aoijson.add_argument('--start', default='Start date in YYYY-MM-DD',help='Start date in YYYY-MM-DD?',widget='DateChooser')
    parser_aoijson.add_argument('--end', default='End date in YYYY-MM-DD',help='End date in YYYY-MM-DD?',widget='DateChooser')
    parser_aoijson.add_argument('--cloud', default='Maximum Cloud Cover(0-1)',help='Maximum Cloud Cover(0-1) representing 0-100')
    parser_aoijson.add_argument('--inputfile',default='Choose a KML/SHP/geojson/WKT file or Landsat WRS',choices=['KML', 'SHP','GJSON','WKT','WRS'],help='Choose a KML/SHP/geojson/WKT file or Landsat WRS')
    parser_aoijson.add_argument('--geo', default='map.geojson/aoi.kml/aoi.shp/aoi.wkt file or 6 digit WRS PathRow',help='map.geojson/aoi.kml/aoi.shp/aoi.wkt file',widget="MultiFileChooser")
    parser_aoijson.add_argument('--loc', help='Location where aoi.json file is to be stored',widget="MultiDirChooser")
    parser_aoijson.set_defaults(func=aoijson_from_parser)

    parser_activatepl=subparsers.add_parser('activatepl',description='Tool to query and/or activate Planet Assets')
    parser_activatepl.add_argument('--aoi',default='Choose JSON file to be used with Planet API/Created Earlier',help='Choose JSON file created earlier',widget="MultiFileChooser")
    parser_activatepl.add_argument('--action',choices=['check', 'activate'],help='Check/activate')
    parser_activatepl.add_argument('--asst',choices=['PSOrthoTile analytic','PSOrthoTile analytic_dn','PSOrthoTile visual','PSScene4Band analytic','PSScene4Band analytic_dn','PSScene3Band analytic','PSScene3Band analytic_dn','PSScene3Band visual','REOrthoTile analytic','REOrthoTile visual'],help='PSOrthoTile analytic,PSOrthoTile analytic_dn,PSOrthoTile visual,PSScene4Band analytic,PSScene4Band analytic_dn,PSScene3Band analytic,PSScene3Band analytic_dn,PSScene3Band visual,REOrthoTile analytic,REOrthoTile visual')
    parser_activatepl.set_defaults(func=activatepl_from_parser)

    parser_space=subparsers.add_parser('space',help='Tool to query total download size of activated assets & local space left for download')
    parser_space.add_argument('--aoi', help='Choose aoi.json file created earlier',widget="MultiFileChooser")
    parser_space.add_argument('--local', help='local path where you are downloading assets',widget="MultiDirChooser")
    parser_space.add_argument('--asset',choices=['PSOrthoTile analytic','PSOrthoTile analytic_dn','PSOrthoTile visual','PSScene4Band analytic','PSScene4Band analytic_dn','PSScene3Band analytic','PSScene3Band analytic_dn','PSScene3Band visual','REOrthoTile analytic','REOrthoTile visual'],help='Choose between planet asset types (PSOrthoTile analytic/PSOrthoTile analytic_dn/PSOrthoTile visual/PSScene4Band analytic/PSScene4Band analytic_dn/PSScene3Band analytic/PSScene3Band analytic_dn/PSScene3Band visual/REOrthoTile analytic/REOrthoTile visual')
    parser_space.set_defaults(func=space_from_parser)

    parser_downloadpl=subparsers.add_parser('downloadpl',help='Tool to download Planet Assets')
    parser_downloadpl.add_argument('--aoi', default='Choose JSON file to be used with Planet API/Created Earlier',help='Choose JSON file created earlier',widget="MultiFileChooser")
    parser_downloadpl.add_argument('--action', default='download',help='choose download')
    parser_downloadpl.add_argument('--asst',choices=['PSOrthoTile analytic','PSOrthoTile analytic_dn','PSOrthoTile visual','PSScene4Band analytic','PSScene4Band analytic_dn','PSScene3Band analytic','PSScene3Band analytic_dn','PSScene3Band visual','REOrthoTile analytic','REOrthoTile visual','PSOrthoTile analytic_xml','PSOrthoTile analytic_dn_xml','PSOrthoTile visual_xml','PSScene4Band analytic_xml','PSScene4Band analytic_dn_xml','PSScene3Band analytic_xml','PSScene3Band analytic_dn_xml','PSScene3Band visual_xml','REOrthoTile analytic_xml','REOrthoTile visual_xml'],help='PSOrthoTile analytic,PSOrthoTile analytic_dn,PSOrthoTile visual,PSScene4Band analytic,PSScene4Band analytic_dn,PSScene3Band analytic,PSScene3Band analytic_dn,PSScene3Band visual,REOrthoTile analytic,REOrthoTile visual')
    parser_downloadpl.add_argument('--pathway',default='Folder where you want to save assets',help='Folder Path where PlanetAssets are saved example ./PlanetScope ./RapidEye',widget="MultiDirChooser")
    parser_downloadpl.set_defaults(func=downloadpl_from_parser)

    args = parser.parse_args()

    args.func(args)

if __name__ == '__main__':
  main()
