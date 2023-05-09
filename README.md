##Creare il wheel
python3 -m build

##sarà egnerata la cartella dist

##upload su server ufficiale pypi
python3 -m twine upload dist/*


##trovare o creare il file ~/.pypirc

[distutils]
index-servers = 

[mdotmupload]
repository = 
username = 
password = 

##Trovare il pip.conf del proprio pip e inserire nel file pip.conf

[global]
timeout = 60
index = 
index-url = 
