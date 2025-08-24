# PassVedha: Password Breach & Strength Checker 🔒

![Python Version](https://img.shields.io/badge/python-3.10-blue)
![License](https://img.shields.io/badge/license-MIT-green)

PassVedha is a simple command-line tool designed to help you **verify the security of your passwords**.  
It provides a comprehensive analysis by checking against:
- A **password strength algorithm**  
- A **local password list** (like `rockyou.txt`)  
- The **Have I Been Pwned (HIBP) API** database of compromised passwords  

---

### ✨ Key Features
- **Password Strength Analysis:** Get instant suggestions on how to make your password stronger.  
- **Breach Check:** Securely check if your password has been exposed in a data breach using the HIBP API.  
- **Local Password List Check:** Compare your password against a local list for extra validation.  

---

### 🚀 How to Use

#### Prerequisites
- Python 3 installed.

#### Installation
Clone the repository:

```bash
git clone https://github.com/0x13reaker/PassVedha-Password-Breach-Checker.git

```

Navigate to the project directory:

```Bash

cd PassVedha-Password-Breach-Checker

```
Install the required Python libraries:

```Bash

pip install colorama requests
```
Usage
Once installed, you can run the tool directly from your terminal.

Check a single password:

```Bash

python passvedha.py -p "mySecurePassword123!"
```
Check a password against a local list:

```Bash

python passvedha.py -p "123456" -l rockyou.txt
```
📄 License
This project is licensed under the MIT License - see the LICENSE file for details.

👤 About the Author
0x13reaker

GitHub: https://github.com/0x13reaker
