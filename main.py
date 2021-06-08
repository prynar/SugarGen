from bitcoinutils.setup import setup
from bitcoinutils.keys import P2pkhAddress, PrivateKey, PublicKey
from bitcoinutils.setup import setup
from bitcoinutils.script import Script
from bitcoinutils.keys import P2wpkhAddress, P2wshAddress, P2shAddress, PrivateKey, PublicKey
from bitcoinutils import constants
import requests
import json
from colorama import Fore, Back, Style
import threading
def runner():
    while True:
        main()

def main():
    # always remember to setup the network
    constants.NETWORK_SEGWIT_PREFIXES["mainnet"] = "sugar"
    setup('mainnet')


    # create a private key (deterministically)
    priv = PrivateKey(secret_exponent = 0)

    # compressed is the default
    wifka=priv.to_wif(compressed=True)
    # could also instantiate from existing WIF key
    #priv = PrivateKey.from_wif('KwDiBf89qGgbjEhKnhxjUh7LrciVRzI3qYjgd9m7Rfu73SvHnOwn')

    # get the public key
    pub = priv.get_public_key()

    # compressed is the default

    # get address from public key
    address = pub.get_segwit_address()

    # print the address and hash160 - default is compressed address
    addresss=address.to_string()
    #print("Hash160:", address.to_hash160())
    a=requests.get(f'https://api.sugarchain.org/balance/{addresss}')
    a=a.content.decode('utf-8')
    a=json.loads(a)
    balanc=a['result']['balance']
    recived=a['result']['received']
    print(Fore.RED+f'[SugarGen] WIF: {wifka} | Address: {addresss} | Balance: {balanc} | Recived: {recived}')
    if int(balanc) > 0:
        print(Fore.GREEN+'Wow! Balance is good! We found VALID account')
    if int(recived) > 0:
        print('Wow! Recived is good! We found ACTIVED account')

if __name__ == "__main__":
    for i in range(10000):
        my_thread = threading.Thread(target=runner, args=())
        my_thread.start()
