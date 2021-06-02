#!/usr/bin/env python3
import subprocess
import argparse
import re
import pyperclip

arg_parser = argparse.ArgumentParser(description="copy ip address to the clipboard")
arg_parser.add_argument('interface',help='interface to show its ip')
args = arg_parser.parse_args()

def regex_ip(text):
	pattern = '(?:(?:2(?:[0-4][0-9]|5[0-5])|[0-1]?[0-9]?[0-9])\.){3}(?:(?:2([0-4][0-9]|5[0-5])|[0-1]?[0-9]?[0-9]))'
	return re.search(pattern,text.decode('utf-8'))

def text_interface(interface):
	proc = subprocess.run(['ip', 'add','show',interface],check=True,stdout=subprocess.PIPE)
	return proc

if __name__ == '__main__':
	interface_output = text_interface(args.interface).stdout
	ip = regex_ip(interface_output).group()
	pyperclip.copy(ip)
	print('[+] {0}'.format(ip))