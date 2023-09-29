import re
import argparse
import csv


def process_args( ):
    parser = argparse.ArgumentParser( prog="UniversalSubstitutionCipher",
                                      description="Loads a file and performs a series of substituions based on the specified configuration file" )
    parser.add_argument( "input_file" )
    parser.add_argument( "config_file" )
    parser.add_argument( "-c", "--case-sensitive" )
    args = parser.parse_args()
    return args


def load_file( file_to_read ):
    f = open( file_to_read, "r" )
    return f


def process_sub( list_sub, input_sub ):
    if len( list_sub ) == 2:
        return  input_sub.replace( list_sub[0], list_sub[1] )


if __name__ == "__main__":
    csv.register_dialect( "usc-config", delimiter=':', doublequote=False, escapechar='\\', lineterminator='\r\n',
                          quotechar='"', quoting=csv.QUOTE_NONE, skipinitialspace=True, strict=False )
    args = process_args()
    input_file = load_file( args.input_file )
    input_txt = input_file.read()
    config_file = load_file( args.config_file )
    config_reader = csv.reader(config_file, dialect="usc-config" )
    running_txt = input_txt
    for config_row in config_reader:
        running_txt = process_sub( config_row, running_txt )
    print( running_txt )


