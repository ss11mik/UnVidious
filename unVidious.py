# UnVidious
# ss11mik 2023

import sys
import json
import re


def recurse_folder(folder):
    try:
        for i in folder['children']:

            # is a folder
            if i['typeCode'] == 2:
                recurse_folder(i)

            else:
                if '/watch?v=' in i['uri'] and 'https://www.youtube.com/watch?v=' not in i['uri']:

                    # change domains to youtube.com
                    i['uri'] = re.sub(r'http(s){0,1}://.*/watch\?v=', 'https://www.youtube.com/watch?v=', i['uri'])

                    # remove the quality parameter
                    i['uri'] = re.sub(r'\&quality=.*\&', '&', i['uri'])

                    # remove the listen=0 parameter
                    i['uri'] = re.sub(r'\&listen=0\&', '&', i['uri'])

                    # for debug
                    # print(i['uri'])

    except KeyError:
        pass


with open(sys.argv[1], 'r') as f_in:
    with open(re.sub(r'\.json$', '', sys.argv[1]) + '_unVidious.json', 'w') as f_out:
        data = json.load(f_in)
        recurse_folder(data)
        json.dump(data, f_out)

