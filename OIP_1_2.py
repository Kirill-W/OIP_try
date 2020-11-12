import pathlib
import shutil
import os
import requests

path = str(pathlib.Path().absolute()) + '\\MODIS-Aqua_Sept'
print(path)

try:
    shutil.rmtree(path)
except OSError:
    print("Deletion of the directory %s failed" % path)
else:
    print("Successfully deleted the directory %s" % path)

try:
    os.mkdir(path)
except OSError:
    print("Creation of the directory %s failed" % path)
else:
    print("Successfully created the directory %s" % path)

names = 'MODIS-Aqua_2020_09_'

imgSize = ['4km', '9km']

for key in imgSize:

    sizePath = path + '\\' + key

    try:
        os.mkdir(sizePath)
    except OSError:
        print("Creation of the directory %s failed" % sizePath)
    else:
        print("Successfully created the directory %s" % sizePath)

    ind = 246

    for n in range(2, 20):

        name = names + str(n) + '_' + key + '.png'
        r = requests.get('https://oceancolor.gsfc.nasa.gov/showimages/MODISA/IMAGES/CHL/L3/2020/' + str(ind) + '/' + 'A2020' + str(ind) + '.L3m_DAY_CHL_chlor_a_' + key + '.nc.png')
        open(sizePath + '/' + name, 'wb').write(r.content)

        ind += 1
