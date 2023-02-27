import pyfiglet

def banner(text):
    banner = pyfiglet.figlet_format(text,font="block",width=200)
    print(banner)
print("\n"*5)
banner("Observing The World")
print("\n"*5)