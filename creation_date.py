#####################################################################
'''Script for getting the creation data in the metadata of a video'''
#####################################################################

from hachoir.parser import createParser
from hachoir.metadata import extractMetadata

def creation_date(filename):
    parser = createParser(filename)
    metadata = extractMetadata(parser)
    return metadata.get('creation_date')

print(creation_date('videos_ODK/20210428_140233.mp4'))
print(creation_date('videos_ODK/20210413_0030.MOV'))