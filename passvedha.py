#!/usr/bin/env python3
"""
PassVedha - Password Breach & Strength Checker
Author: 0x13
GitHub: https://github.com/muhammedismailsalim
"""

import argparse
import hashlib
import requests
import os
import sys

try:
    from colorama import Fore, Style, init
except ImportError:
    print("[-] colorama not installed. Run: pip install colorama")
    sys.exit(1)

init(autoreset=True)

# -------------------------------------------------
# Banner
# -------------------------------------------------
def print_banner():
    banner = r"""
   ______                           _ _           
   | ___ \                         | | |          
   | |_/ /_ _ ___ _____   _____  __| | |__   __ _ 
   |  __/ _` / __/ __\ \ / / _ \/ _` | '_ \ / _` |
   | | | (_| \__ \__ \\ V /  __/ (_| | | | | (_| |
   \_|  \__,_|___/___/ \_/ \___|\__,_|_| |_|\__,_|
                                                  
                                                  
    """
    print(Fore.CYAN + banner)
    print(Fore.GREEN + "PassVedha - Password Breach & Strength Checker")
    print(Fore.YELLOW + "Author: 0x13reaker")
    print(Fore.YELLOW + "GitHub: https://github.com/0x13reaker\n" + Style.RESET_ALL)

# -------------------------------------------------
# HIBP breach check
# -------------------------------------------------
def check_pwned(password: str) -> int:
    sha1pwd = hashlib.sha1(password.encode("utf-8")).hexdigest().upper()
    prefix, suffix = sha1pwd[:5], sha1pwd[5:]
    url = f"https://api.pwnedpasswords.com/range/{prefix}"

    try:
        res = requests.get(url, timeout=5)
        if res.status_code != 200:
            return -1
        hashes = (line.split(":") for line in res.text.splitlines())
        for h, count in hashes:
            if h == suffix:
                return int(count)
        return 0
    except Exception:
        return -1


# -------------------------------------------------
# Local password list check
# -------------------------------------------------
def check_in_passlist(password: str, passlist: str) -> bool:
    try:
        with open(passlist, "r", encoding="latin-1", errors="ignore") as f:
            for line in f:
                if password.strip() == line.strip():
                    return True
        return False
    except FileNotFoundError:
        print(Fore.YELLOW + f"[!] Password list {passlist} not found.")
        return False


# -------------------------------------------------
# Password strength suggestion
# -------------------------------------------------
def password_strength(password: str) -> str:
    suggestions = []
    if len(password) < 12:
        suggestions.append("Use at least 12 characters.")
    if password.lower() == password:
        suggestions.append("Add uppercase letters.")
    if password.upper() == password:
        suggestions.append("Add lowercase letters.")
    if not any(c.isdigit() for c in password):
        suggestions.append("Add numbers.")
    if not any(c in "!@#$%^&*()-_=+[]{};:,.<>?/|\\`~" for c in password):
        suggestions.append("Add special characters.")

    if not suggestions:
        return Fore.GREEN + "✔ Strong password!"
    return Fore.YELLOW + "⚠ Suggestions: " + " ".join(suggestions)


# -------------------------------------------------
# Main function
# -------------------------------------------------
def main():
    parser = argparse.ArgumentParser(
        description="PassVedha - Password Breach & Strength Checker"
    )
    parser.add_argument("-p", "--password", required=True, help="Password to check")
    parser.add_argument(
        "-l", "--list", help="Optional password list (e.g. rockyou.txt)"
    )
    args = parser.parse_args()

    password = args.password
    passlist = args.list

    print_banner()
    print(Fore.CYAN + "=== PassVedha - Password Checker ===\n")

    # HIBP check
    count = check_pwned(password)
    if count == -1:
        print(Fore.RED + "[!] Error checking HIBP API.")
    elif count == 0:
        print(Fore.GREEN + "[+] Password not found in known breaches.")
    else:
        print(
            Fore.RED
            + f"[!] Password appeared {count:,} times in data breaches. DO NOT USE."
        )

    # Local list check
    if passlist:
        found = check_in_passlist(password, passlist)
        if found:
            print(Fore.RED + f"[!] Password found in {passlist}. Very unsafe.")
        else:
            print(Fore.GREEN + f"[+] Password not found in {passlist}.")
    else:
        print(Fore.YELLOW + "[*] No password list provided (skipping local check).")

    # Strength suggestions
    print("\n" + password_strength(password) + "\n")


if __name__ == "__main__":
    main()