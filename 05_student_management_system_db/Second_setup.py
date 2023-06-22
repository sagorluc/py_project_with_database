from cx_Freeze import setup, Executable
import sys

include_file = ['stu.ico']
exclude = []
packages = []
base = None

if sys.platform == 'win32':
    base = 'Win32GUI'

shortcut_table = [
    (
        'DesktopShortcut',  # Shortcut
        'DesktopFolder',  # Directory
        'First_page',  # Name
        'TARGETDIR',  # Component
        '[TARGETDIR]\First_page.exe',  # Target
        None,  # Argument
        None,  # Description
        None,  # Hotkey
        None,  # Icon
        None,  # IconIndex
        None,  # ShowCmd
        'TARGETDIR',  # Wkdir
    )
]

msi_data = {'shortcut': shortcut_table}

bdist_msi_options = {'data': msi_data}
setup(
    version='0.1',
    description='Student Management System Developed by sagor ahmed',
    author='sagor ahmed',
    name='Student Management System',
    options={'build_exe': {'include_files': include_file}, 'bdist_msi_options': bdist_msi_options},
    executables=[
        Executable(
            script='First_page.py',
            base=base,
            icon='stu.ico',
        )
    ]
)
