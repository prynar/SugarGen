from bitcoinutils.setup import setup
from bitcoinutils.script import Script
from numba import jit
from bitcoinutils.keys import P2wpkhAddress, P2wshAddress, P2shAddress, PrivateKey, PublicKey
from bitcoinutils import constants
@jit(target ="cuda")
def main():
    constants.NETWORK_SEGWIT_PREFIXES["mainnet"] = "sugar"
    # always remember to setup the network
    setup('mainnet')
    private = PrivateKey.from_wif()
    public = private.get_public_key()
    segwit = public.get_segwit_address()
    address = segwit.to_string()
    wif = private.to_wif()
    print(wif,address)
for i in range(10000):
    main()
