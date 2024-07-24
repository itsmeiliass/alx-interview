# Project README.md

## Curriculum Project: UTF-8 Validation

### Short Specialization: Algorithm in Python

### Resources

- [UTF-8](https://intranet.alxswe.com/rltoken/oqFi6P1hNvp9aSuNv---IQ)
- [Characters, Symbols, and the Unicode Miracle](https://intranet.alxswe.com/rltoken/d--jVK8sBSlhkosu7pFzdw)

### General Requirements

- **Allowed Editors:** vi, vim, emacs
- **Interpreter/Compiler:** Ubuntu 20.04 LTS using Python3 (version 3.4.3)
- **File Ending:** All files should end with a new line.
- **First Line:** The first line of all files should be exactly `#!/usr/bin/python3`.
- **README.md:** A README.md file at the root of the project folder is mandatory.
- **PEP 8 Style:** Code should adhere to the PEP 8 style (version 1.7.x).
- **File Executability:** All files must be executable.

### Task

#### 0. UTF-8 Validation (mandatory)

Write a method that determines if a given data set represents a valid UTF-8 encoding.

- **Prototype:** `def validUTF8(data)`
- **Return:** True if data is a valid UTF-8 encoding, else return False.
- A character in UTF-8 can be 1 to 4 bytes long.
- The data set can contain multiple characters.
- The data will be represented by a list of integers.
- Each integer represents 1 byte of data, therefore you only need to handle the 8 least significant bits of each integer.

### Example

```python
validUTF8 = __import__('0-validate_utf8').validUTF8

data = [65]
print(validUTF8(data))  # Output: True

data = [80, 121, 116, 104, 111, 110, 32, 105, 115, 32, 99, 111, 111, 108, 33]
print(validUTF8(data))  # Output: True

data = [229, 65, 127, 256]
print(validUTF8(data))  # Output: False
```

### Repository Information

- **GitHub repository:** [alx-interview](https://github.com/mugambi12/0x04-utf8_validation)
- **Directory:** 0x04-utf8_validation
- **File:** 0-validate_utf8.py
