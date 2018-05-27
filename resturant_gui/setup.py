from cx_Freeze import setup, Executable

base = None    

executables = [Executable("Maa_resturant.py", base=base)]

packages = ["idna"]
options = {
    'build_exe': {    
        'packages':packages,
    },    
}

setup(
    name = "<Maa_resturant>",
    options = options,
    version = "<1.1>",
    description = '<by deep>',
    executables = executables
)