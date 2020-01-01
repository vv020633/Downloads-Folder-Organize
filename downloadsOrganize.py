#! /usr/bin/python3

# This program is intended to search the file in my downloads folder and organize them into relevant
# Sub-folders for later retrieval

import os
import re
import time
import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logging.debug('Start of progam')
loop = True


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


'''    def regexMissing(downloads_list, video_matches, document_matches, image_matches, exec_matches, compressed_matches, photo_matches, app_image_matches):
        non_matches = []
        collective_matches = video_matches + document_matches + image_matches + exec_matches + compressed_matches + photo_matches
        for file in downloads_list:
            for matches in collective_matches:
                if file not in collective_matches:
                    non_matches.append(file)
        return non_matches '''


def regexSearch(downloads_list, filetypes):

    matched_filetypes = []

    for type in filetypes:
       for file in downloads_list:
           regex_match = re.compile(r"." + re.escape(type) + r"*$", re.I)
           #logging.debug('File is: %s' % (file))
           if regex_match.search(file):
               matched_filetypes.append(file)
               print(matched_filetypes)
    logging.debug('matched_types equal to: %s ' % str((matched_filetypes)))
    return matched_filetypes


# Function which sets the current directory to downloads if it isn't already in downloads
def setDirectory(path):
    current_directory = os.getcwd()
    if current_directory != path:
        os.chdir(path)
    return os.getcwd()


# Function to move specified filetypes into relevant folders. If folder doesn't exist - create folder and then move file
def moveFile(matched_filetypes):

    isExist = False
    # Check this line if error occurs
    #while isExist == False:

    if matched_filetypes == photo_match:
        isExist = os.path.exists(picture_downloads_path)

        if not isExist:
            os.makedirs(picture_downloads_path)

        elif isExist:
            for file in matched_filetypes:
                origin_path = path + "/" + file
                photo_destination_path = picture_downloads_path + "/" + file
                os.replace(origin_path, photo_destination_path)

    elif matched_filetypes == video_match:
        isExist = os.path.exists(video_downloads_path)

        if not isExist:
            os.makedirs(video_downloads_path)

        elif isExist:
            for file in matched_filetypes:
                origin_path = path + "/" + file
                video_destination_path = video_downloads_path + "/" + file
                os.replace(origin_path, video_destination_path)

    elif matched_filetypes == document_match:
        isExist = os.path.exists(documents_downloads_path)

        if not isExist:
            os.makedirs(documents_downloads_path)

        elif isExist:
            for file in matched_filetypes:
                origin_path = path + "/" + file
                documents_destination_path = documents_downloads_path + "/" + file
                os.replace(origin_path, documents_destination_path)

    elif matched_filetypes == exec_match:
        isExist = os.path.exists(exec_downloads_path)

        if not isExist:
            os.makedirs(exec_downloads_path)

        elif isExist:
            for file in matched_filetypes:
                origin_path = path + "/" + file
                exec_destination_path = exec_downloads_path + "/" + file
                os.replace(origin_path, exec_destination_path)

    elif matched_filetypes == compressed_match:
        isExist = os.path.exists(compressed_downloads_path)

        if not isExist:
            os.makedirs(compressed_downloads_path)

        elif isExist:
            for file in matched_filetypes:
                origin_path = path + "/" + file
                compressed_destination_path = compressed_downloads_path + "/" + file
                os.replace(origin_path, compressed_destination_path)

    elif matched_filetypes == image_match:
        isExist = os.path.exists(image_downloads_path)

        if not isExist:
            os.makedirs(image_downloads_path)

        elif isExist:
            for file in matched_filetypes:
                origin_path = path + "/" + file
                image_destination_path = image_downloads_path + "/" + file
                os.replace(origin_path, image_destination_path)

    elif matched_filetypes == app_image_match:
        isExist = os.path.exists(app_image_downloads_path)

        if not isExist:
            os.makedirs(app_image_downloads_path)

        elif isExist:
            for file in matched_filetypes:
                origin_path = path + "/" + file
                app_image_destination_path = app_image_downloads_path + "/" + file
                os.replace(origin_path, app_image_destination_path)

    '''elif matched_filetypes == regex_missing:
        isExist = os.path.exists(regex_missing_downloads_path)

        if not isExist:
            os.makedirs(regex_missing_downloads_path)

        elif isExist:
            for file in matched_filetypes:
                origin_path = path + "/" + file
                regex_missing_destination_path = image_downloads_path + "/" + file
                os.replace(origin_path, regex_missing_destination_path)'''


while loop:

    time.sleep(5)
    # Variable for the downloads path
    path = '/home/chiefchas/Downloads'

    # Variables for download folder paths
    picture_downloads_path = '/home/chiefchas/Pictures/Downloads'
    video_downloads_path = '/home/chiefchas/Videos/Downloads'
    documents_downloads_path = '/home/chiefchas/Documents'
    exec_downloads_path = '/home/chiefchas/Downloads/Executables'
    compressed_downloads_path = '/home/chiefchas/Downloads/Compressed_Files'
    image_downloads_path = '/home/chiefchas/Downloads/ISO_Images'
    app_image_downloads_path = '/home/chiefchas/Downloads/App_Images'
    # regex_missing_downloads_path = '/home/chiefchas/Downloads/Unsorted'

    ''' Function which searches the current working directory for files and folders.
     If it is a directory, the program continues to the end of the loops.
     If it is a file the program will return false and break the loop,
     thus returning one value'''

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
    exec_filetypes = ['0xe', '73k', '89k', '8ck', 'a6p', 'apk', 'app', 'air', 'acr', 'applescript', 'ba_', 'bat', 'bin', 'cmd', 'coffee', 'command',
                      'csh', 'deb', 'e_e', 'ear', 'esh$exe$', 'exe1', 'fxp', 'ham', 'jar', 'ksh', 'mac', 'mam', 'mem',  'mlx', 'ps1', 'pyc', 'pyo', 'rgs', 'run', 'scr',
                      'seed', 'sct', 'udf', 'vbe', 'vxp', 'ws', 'wsf', 'x86', 'xlm', 'xbap']

    # Creating list to match compressed filetypes

    compressed_filetypes = ['zip', 'rar', 'tar', '7z', 'tar.gz', 'tgz', 'tar.z', 'tar.bz2', 'tbz2', 'tar.lzma']

    # Creating list to match image filetypes
    disk_image_filetypes = ['bif', 'dcf', 'img', 'iso']

    # AppImage
    app_image_filetypes = ['appimage']

    setDirectory(path)
    files = directoryCheck()

    # Regex searches for different filetypes
    video_match = regexSearch(files, video_filetypes)
    document_match = regexSearch(files, document_filetypes)
    exec_match = regexSearch(files, exec_filetypes)
    compressed_match = regexSearch(files, compressed_filetypes)
    image_match = regexSearch(files, disk_image_filetypes)
    photo_match = regexSearch(files, image_filetypes)
    app_image_match = regexSearch(files, app_image_filetypes)
    #print(files)
    #print('photo_match: ' + str(photo_match))
    #print('exec_match: ' + str(exec_match))

    # Search for values in the downloads folder that don't match anything
    # regex_missing = regexMissing(files, video_match, document_match, exec_match, compressed_match, image_match, photo_match, app_image_match)

    # If a match exists for a specific filetype, the function to move the files is called

    if video_match:
        moveFile(video_match)

    elif document_match:
        moveFile(document_match)

    elif compressed_match:
        moveFile(compressed_match)

    elif image_match:
        moveFile(image_match)

    elif photo_match:
        moveFile(photo_match)

    elif app_image_match:
        moveFile(app_image_match)

    elif exec_match:
        moveFile(exec_match)

    # Missing regex/Last resort conditional. If regex_missing is true, move file into "unsorted" folder
    # elif regex_missing:
    #    moveFile(regex_missing)
