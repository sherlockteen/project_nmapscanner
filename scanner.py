import nmap3
from colorama import init, Fore, Style


# Initializes Colorama
init(autoreset=True)

print(Style.BRIGHT + Fore.GREEN +
      "[*] Welcome, this is a simple nmap script for my homework")
print(Style.BRIGHT + Fore.GREEN + '<' + '-' * 60 + '>' + '\n')

target = input('[*] Enter target IP:\n')
nmap = nmap3.Nmap()
result = nmap.nmap_version_detection(target)
print(Style.BRIGHT + Fore.RED + '\n[+] Result: \n')


try:
    for i in result[target]['ports']:
        try:
            print('Service Name: ' + i['service']['product'] + ' port: ' + i['portid'] + ' Version: ' +
                  i['service']['version'])
        except KeyError:
            pass
except KeyError:
    print(Style.BRIGHT + Fore.RED + '[-] Confidence in the correct IP')
