from os import system

from colorama import Fore

from plugin import Plugin

# import socket


class IP(Plugin):
    """
    Display local and public ip address
    """
    def __init__(self):    
        self._local_ip = "ifconfig -a"

        self._public_ip = "timeout 10 curl ifconfig.co"  # 10 second time out if not connected to internet
        super(Plugin, self).__init__()

    def require(self):
        pass

    def complete(self):
        pass

    def alias(self):
        pass

    def run(self, jarvis, s):
        self._get_local_ip(jarvis)
        jarvis.say("")
        self._get_public_ip(jarvis)

    def _get_local_ip(self, jarvis):
        jarvis.say("List of local ip addresses :", Fore.BLUE)
        system(self._local_ip)

    def _get_public_ip(self, jarvis):
        jarvis.say("Public ip address :", Fore.BLUE)
        system(self._public_ip)
