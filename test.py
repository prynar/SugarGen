from bitcoinutils.setup import setup
from bitcoinutils.script import Script
from bitcoinutils.keys import P2wpkhAddress, P2wshAddress, P2shAddress, PrivateKey, PublicKey
from bitcoinutils import constants
import hashlib
def main():
    constants.NETWORK_SEGWIT_PREFIXES["mainnet"] = "sugar"
    # always remember to setup the network
    setup('mainnet')
    private = PrivateKey.from_wif('KwDiBf89QgGbjEhKnhXJuH7LrciVrZi3qYjgd9M7rFU73sVHnoWn')
    public = private.get_public_key()
    segwit = public.get_segwit_address()
    address = segwit.to_string()
    wif = private.to_wif()
    print(wif,address)
main()
