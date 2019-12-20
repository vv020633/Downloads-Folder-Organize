#! /usr/bin/python3

# This program is intended to search the file in my downloads folder and organize them into relevant
# Sub-folder for later retrieval

import os
import re
path = '/home/chiefchas/Downloads'

# function which sets the current directory to downloads if it isn't already in downloads


def setDirectory(path):
    current_directory = os.getcwd()
    if current_directory != path:
        os.chdir(path)
    return os.getcwd()


''' Function which searches the current working direcotory for files and folders.
 If it is a directory, the program continues to the end of the loops.
 If it is a file the program will return false and break the loop,
 thus returning one value'''


def directoryCheck():
    files = []
    path = os.getcwd()
    directory_contents = os.listdir(path)

    for content in directory_contents:
        isdir = os.path.isdir(content)
        if isdir:
            continue
        else:
            files.append(content)
    return files


def regexSearch(downloads_list, filetypes):
    match_type = []
    for type in filetypes:
        regex_match = re.compile(r"." + re.escape(type) + r"*$")
        for file in downloads_list:
            search = regex_match.search(file)
            if search:
                match_type.append(file)
            else:
                continue

    return match_type


# Creating list to match photo filetypes

image_filetypes = ['png', 'jpeg', 'exif', 'tiff', 'gif', 'png', 'ppm', 'pgm', 'pbm', 'pnm', 'hdr', 'bpg', 'cgm', 'svg', 'raw']

# Creating list to match video filetypes
video_filetypes = ['mp4', 'm4a', 'm4v', 'f4v', 'f4a', 'm4b', 'm4r', 'f4b', 'mov', '3pg',
                   '3gp2', '3g2', '3gps', '3gpp2', 'ogg', 'oga', 'ogv', 'ogx', 'wmv', 'wma', 'asf', 'web',
                   'flv', 'avi', 'mov', 'hdv', 'mpeg', 'wav', 'lxf', 'gxf', 'vob']

# Creating list to match document filetypes)
document_filetypes = ['doc', 'htm', 'html', 'docx', 'odt', 'pdf',
                      'xls', 'xlsx', 'ods', 'ppt', 'pptx', 'txt']


# Creating list to match executable filetypes
exec_filetypes = ['0xe', '73k', '89k', '8ck', 'a6p', 'apk', 'app', 'appimage', 'air', 'acr', 'applescript', 'ba_', 'bat', 'bin', 'cmd', 'coffee', 'command'
                  'csh', 'e_e', 'ear', 'esh$exe$', 'exe1', 'fxp', 'ham', 'jar', 'ksh', 'mac', 'mam', 'mem',  'mlx', 'ps1', 'pyc', 'pyo', 'rgs', 'run', 'scr',
                  'seed', 'sct', 'udf', 'vbe', 'vxp', 'ws', 'wsf', 'x86', 'xlm', 'xbap']


# Creating list to match compressed filetypes

compressed_filetypes = ['zip', 'rar', 'tar', '7z', 'tar.gz', 'tgz', 'tar.z', 'tar.bz2', 'tbz2', 'tar.lzma']

# Creating list to match image filetypes
disk_image_filetypes = ['bif', 'dcf', 'img', 'iso']


setDirectory(path)
files = directoryCheck()
print(regexSearch(files, video_filetypes))
print(regexSearch(files, document_filetypes))
print(regexSearch(files, exec_filetypes))
print(regexSearch(files, compressed_filetypes))
print(regexSearch(files, disk_image_filetypes))
