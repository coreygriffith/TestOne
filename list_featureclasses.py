import os, arcpy

i_fgdb=r""

arcpy.env.workspace=i_fgdb

def main():
    for fc in arcpy.ListFeatureClasses():
        print(fc)

if __name__=='__main__':
    main()