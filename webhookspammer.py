from colorama import Fore, Back, Style, init
import os
from dhooks import Webhook
init()


                                 
print(Fore.MAGENTA +
"""  

                                    
                                      ╔═╗┌─┐┬┬─┐╔╗ ┬  ┬ ┬┌─┐
                                      ╔═╝├┤ │├┬┘╠╩╗""" + Fore.WHITE + """│  │ │├┤ 
                                      ╚═╝└─┘┴┴└─╚═╝┴─┘└─┘└─┘ """ + Fore.WHITE + """
                         =========="""+ Fore.GREEN + """ Discord Webhook-Spammer """ + Fore.WHITE + """==========""" + Fore.MAGENTA + """
                                    ┌─────────────────────────┐   
                                    │""" + Fore.WHITE + """ by GentilStar with """ + Fore.RED + """<3""" + Fore.MAGENTA + """   │                                
                                    └─────────────────────────┘                                                             """ + Fore.RED + """   """)


print('')
i = input('Webhook: ')
p = input('Message: ')
print(Fore.GREEN + "")

hook = Webhook(i)
while True:
 hook.send(p)
 print(f"[+] {p}")
