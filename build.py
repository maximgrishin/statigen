import glob
import os
import shutil
import subprocess


currentDirectory = os.path.dirname(__file__)

for txtname in glob.glob(os.path.join('posts', '*')):
    htmlname = os.path.splitext(os.path.basename(txtname))[0] + '.html'
    with open(txtname) as source:
        with open(htmlname, 'w') as html:
            subprocess.run(['python3', os.path.join(currentDirectory, 'mdToHtml.py')],
                stdin=source, stdout=html)

with open('index.html', 'wb') as index:
    subprocess.run(['python3', os.path.join(currentDirectory, 'makeIndex.py')],
        stdout=index)
