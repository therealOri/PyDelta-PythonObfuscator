import sys
import subprocess

class CodeCompiler:
    @staticmethod
    def compile_code(file_path):
        if sys.platform == 'win32':
            platform_command = ['cmd.exe', '/c', 'nuitka', '--version']
            system_args = ['cmd.exe', '/c', 'nuitka', '--follow-imports', '--remove-output', file_path]
        else:
            platform_command = ['nuitka3', '--version']
            system_args = ['nuitka3', '--follow-imports', '--remove-output', file_path]

        try:
            result_code = subprocess.run(platform_command) #check to see if nuitka is installed.
        except:
            try:
                subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'nuitka'])
            except Exception as e:
                input(f'An error has occured while trying to install the nuitka compiler. You can try to install it manually from pypi by using "pip install nuitka" then try to run this code again.\n\nError: {e}\n\nPress "enter" to skip compilation and exit...')

        args = system_args
        subprocess.check_call(args)
