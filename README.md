# PyDelta

PyDelta is a Python obfuscator script designed to obfuscate Python source code, making it more difficult to understand and reverse-engineer. PyDelta obfuscates your scripts with multiple layers of protection making it extremely hard for someone to deobfuscate.
> The original repo has been archived and won't be maintained anymore so for the time being and the forseeable future, I'll continue making updates here. <3

<br>

## Features:
* Anti-Debugger: Adds anti-debugger code to the source to deter debugging attempts.
* Code Compression and Encryption: Compresses and encrypts the code to make it harder to analyze.
* String Encryption: Encrypts strings within the code to prevent easy extraction of sensitive information.
* Inline Imports: Converts imports to inline imports to reduce readability.
* Name Refactoring: Refactors variable, function and arguments identifiers to further obfuscate the code.
* Code Compilation: Uses Nuitka to compile code to an executable.

<br>

## Usage:
PyDelta was intended to run in a browser but it is indeed possible to run it locally.
> Install PyDelta locally by using the following command: `pip install .`

### Example Usage:
```py
from pydelta import delta_obfuscate

source_code = """
# Your Python source code here
print('Hello')
"""

obfuscated_code = delta_obfuscate(source_code)
with open('my_obf_file.py', 'w') as file:
    file.write(obfuscated_code)
```

Or you can simply run the `pydelta-obfuscate` command.

### Parameters:
* source_code: Source code to obfuscate
* add_anti_dbg: Whether to add anti-debugger code (default: True).
* inline_imports: Whether to convert imports to inline imports (default: True).
* refactor_names: Whether to refactor variable and function names (default: True).
* encrypt_str: Whether to encrypt strings in the code (default: True).
* compress_encrypt: Whether to compress and encrypt the entire code (default: True).
* str_encryption_amount: Number of times to encrypt strings (default: 3).
* compress_encrypt_amount: Number of times to compress and encrypt the code (default: 30).
* compile_code: Whether to compile your code or not. (default: False).


### CLI Arguments:
* no_add_anti_dbg
* no_inline_imports
* no_refactor_names
* no_encrypt_str
* no_compress_encrypt
* code_compile
* str_encryption_amount: Number of times to encrypt strings (default: 3).
* compress_encrypt_amount: Number of times to compress and encrypt the code (default: 30).

<br>

### Notes
* This version of PyDelta is still in development and some features may not be fully functional.
* Runtime code is obfuscated by choice which can make maintaining a little tricky, even if those function will likely remain untouched in future releases a module will be used.

### License
This project is licensed under the MIT License.

<br>
<br>
<br>


### Support  |  Buy me a coffee <3
Donate to me here:
> - Don't have Cashapp? [Sign Up](https://cash.app/app/TKWGCRT)

![image](https://user-images.githubusercontent.com/45724082/158000721-33c00c3e-68bb-4ee3-a2ae-aefa549cfb33.png)
