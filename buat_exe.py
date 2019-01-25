import cx_Freeze
import sys

shortcut_table = [
    ("DesktopShortcut",        # Shortcut
     "DesktopFolder",          # Directory_
     "Perizinan Santri PP. Nurul Jadid",           # Name
     "TARGETDIR",              # Component_
     "[TARGETDIR]APerizinan.exe",# Target
     None,                     # Arguments
     None,                     # Description
     None,                     # Hotkey
     None,                     # Icon
     None,                     # IconIndex
     None,                     # ShowCmd
     'TARGETDIR'               # WkDir
     ),
    ("StartupShortcut",        # Shortcut
     "StartupFolder",          # Directory_
     "Perizinan Santri PP. Nurul Jadid",     # Name
     "TARGETDIR",              # Component_
     "[TARGETDIR]APerizinan.exe",   # Target
     None,                     # Arguments
     None,                     # Description
     None,                     # Hotkey
     None,                     # Icon
     None,                     # IconIndex
     None,                     # ShowCmd
     'TARGETDIR'               # WkDir
     ),
    ]

# Now create the table dictionary
msi_data = {"Shortcut": shortcut_table}

# Change some default MSI options and specify the use of the above defined tables
bdist_msi_options = {'data': msi_data}

base = None
if sys.platform == 'win32':
    base = "Win32GUI"

executables = [cx_Freeze.Executable("APerizinan.py", base=base, icon="icon.ico")]#tempat file program python  
cx_Freeze.setup(
    name =  "Perizinan Santri PP. Nurul Jadid", #nama aplikasi
    options = {"build_exe": 
        {
            "packages":["wx","base64","json","requests", "logging", "yaml"],"include_files":["app/"]
        },
        "bdist_msi":bdist_msi_options
        }, #tempat menaruh lib sama file image,dll
    version = "1.0", #versi aplikasi
    description = "Application Developer by Faizul Amaly", #deskripsi
    executables = executables,
    )
