#!/usr/bin/env python3

import os
import sys
import urllib.parse

def clear_screen():
    os.system('clear' if os.name == 'posix' else 'cls')

def center_text(text, width=80):
    lines = text.split('\n')
    centered = []
    for line in lines:
        spaces = (width - len(line.replace('\033[0m', '').replace('\033[1m', '').replace('\033[91m', '').replace('\033[92m', '').replace('\033[93m', '').replace('\033[94m', '').replace('\033[95m', '').replace('\033[96m', ''))) // 2
        centered.append(' ' * max(0, spaces) + line)
    return '\n'.join(centered)

def display_banner():
    banner = """
\033[96m██████╗ \033[95m██╗██████╗ \033[96m████████╗██╗  ██╗██████╗  \033[95m█████╗ ██╗   ██╗
\033[96m██╔══██╗\033[95m██║██╔══██╗\033[96m╚══██╔══╝██║  ██║██╔══██╗\033[95m██╔══██╗╚██╗ ██╔╝
\033[96m██████╔╝\033[95m██║██████╔╝\033[96m   ██║   ███████║██║  ██║\033[95m███████║ ╚████╔╝ 
\033[96m██╔══██╗\033[95m██║██╔══██╗\033[96m   ██║   ██╔══██║██║  ██║\033[95m██╔══██║  ╚██╔╝  
\033[96m██████╔╝\033[95m██║██║  ██║\033[96m   ██║   ██║  ██║██████╔╝\033[95m██║  ██║   ██║   
\033[96m╚═════╝ \033[95m╚═╝╚═╝  ╚═╝\033[96m   ╚═╝   ╚═╝  ╚═╝╚═════╝ \033[95m╚═╝  ╚═╝   ╚═╝   
                                                                  
\033[95m██╗    ██╗\033[96m██╗███████╗██╗  ██╗
\033[95m██║    ██║\033[96m██║██╔════╝██║  ██║
\033[95m██║ █╗ ██║\033[96m██║███████╗███████║
\033[95m██║███╗██║\033[96m██║╚════██║██╔══██║
\033[95m╚███╔███╔╝\033[96m██║███████║██║  ██║
\033[95m ╚══╝╚══╝ \033[96m╚═╝╚══════╝╚═╝  ╚═╝\033[0m"""
    
    print(center_text(banner))
    print(center_text("\033[93m" + "─" * 60 + "\033[0m"))
    print(center_text("\033[95mCreated by: \033[96mRoot Nexus | \033[91m CYBER SENTINEL BANGLADESH - CSB\033[0m"))
    print(center_text("\033[93mVersion: 1.0\033[0m"))
    print(center_text("\033[93m" + "─" * 60 + "\033[0m"))

def display_menu():
    menu_text = """
\033[92m╔═════════════════════════════════════╗
║         \033[1m\033[96mSELECT TEMPLATE\033[0m\033[92m             ║
╠═════════════════════════════════════╣
║                                     ║
║    \033[93m[1]\033[0m \033[96m▸ Template One\033[92m               ║
║    \033[93m[2]\033[0m \033[95m▸ Template Two\033[92m               ║
║    \033[93m[3]\033[0m \033[94m▸ Template Three\033[92m             ║
║    \033[91m[0]\033[0m \033[91m▸ Exit\033[92m                       ║
║                                     ║
╚═════════════════════════════════════╝\033[0m"""
    print(center_text(menu_text))

def get_input_with_prompt(prompt):
    print(center_text(prompt), end='')
    user_input = input()
    return user_input.strip()

def animated_loading():
    print(center_text("\033[92m✓ Generating your birthday wish link...\033[0m"))

def main():
    TEMPLATES = {
        "1": "https://birthday-template-1.vercel.app",
        "2": "https://birthday-template-2.vercel.app",
        "3": "https://birthday-template-3.vercel.app"
    }
    
    while True:
        clear_screen()
        display_banner()
        display_menu()
        
        choice = get_input_with_prompt("\n\033[96m╔═▸ Select Option: \033[0m")
        
        if choice == "0":
            clear_screen()
            print(center_text("\033[91m╔════════════════════════════════╗"))
            print(center_text("\033[91m║     EXITING BIRTHDAY WISH      ║"))
            print(center_text("\033[91m║          Goodbye!              ║"))
            print(center_text("\033[91m╚════════════════════════════════╝\033[0m"))
            sys.exit(0)
        
        if choice not in ["1", "2", "3"]:
            print(center_text("\n\033[91m⚠ Invalid selection! Please choose 1-3 or 0 to exit.\033[0m"))
            input(center_text("\033[93mPress Enter to continue...\033[0m"))
            continue
        
        clear_screen()
        display_banner()
         
        print(center_text("\033[95m╔════════════════════════════════════╗"))
        print(center_text("\033[95m║     PERSONALIZE YOUR WISH          ║"))
        print(center_text("\033[95m╚════════════════════════════════════╝\033[0m"))
        print()
        
        name = get_input_with_prompt("\033[96m╔═▸ Enter birthday person's name: \033[0m")
        
        if not name:
            print(center_text("\n\033[91m⚠ Name cannot be empty!\033[0m"))
            input(center_text("\033[93mPress Enter to continue...\033[0m"))
            continue
        
        encoded_name = urllib.parse.quote(name)
        final_link = f"{TEMPLATES[choice]}?name={encoded_name}"
        
        print()
        animated_loading()
        print()
        print(center_text("\033[92m" + "═" * 60 + "\033[0m"))
        print(center_text("\033[1m\033[96mYour Birthday Wish Link:\033[0m"))
        print(center_text("\033[93m" + final_link + "\033[0m"))
        print(center_text("\033[92m" + "═" * 60 + "\033[0m"))
        print()
        print(center_text("\033[95m╔════════════════════════════════════╗"))
        print(center_text("\033[95m║  \033[93m[1]\033[0m \033[96mCreate Another\033[95m                ║"))
        print(center_text("\033[95m║  \033[91m[0]\033[0m \033[91mExit\033[95m                          ║"))
        print(center_text("\033[95m╚════════════════════════════════════╝\033[0m"))
        
        next_action = get_input_with_prompt("\n\033[96m╔═▸ Select: \033[0m")
        
        if next_action == "0":
            clear_screen()
            print(center_text("\033[92m╔════════════════════════════════╗"))
            print(center_text("\033[92m║   Thank you for using          ║"))
            print(center_text("\033[92m║     Birthday Wish!             ║"))
            print(center_text("\033[92m╚════════════════════════════════╝\033[0m"))
            sys.exit(0)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n" + center_text("\033[91mOperation cancelled by user\033[0m"))
        sys.exit(0)
    except Exception as e:
        print(center_text(f"\033[91mError: {e}\033[0m"))
        sys.exit(1)