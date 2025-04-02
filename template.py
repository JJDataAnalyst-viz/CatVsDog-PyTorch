import os
import pathlib


project_name = 'PetVision'

list_of_files = [
       ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/entity/config_entity.py",
    f"src/{project_name}/constants/__init__.py",
    'data/',
    "config/config.yaml",
    "params.yaml",
    "schema.yaml",
    "main.py",
    "Dockerfile",
    "setup.py",
    "research/research.ipynb",
    "templates/index.html",
    "app.py",
    'requirements.txt',
    '.gitignore'
]


for file in list_of_files:
    filepath = pathlib.Path(file)

    dirs,filename = os.path.split(filepath)

    if dirs != None and len(dirs) != 0:
        os.makedirs(dirs,exist_ok=True)

    print(filepath)

    if os.path.exists(dirs):
        print(f'{dirs} already exists')

        
    if not filepath.exists():
        with open(filepath,'w') as f:
                continue
    else: 
         print('already is')