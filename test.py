from bitcoinutils.setup import setup
from bitcoinutils.script import Script
from bitcoinutils.keys import P2wpkhAddress, P2wshAddress, P2shAddress, PrivateKey, PublicKey
from bitcoinutils import constants
import base58
import hashlib
def priv2WIF(h, compressed = False, testnet = False):
    #uncompressed: 0x80 + [32-byte secret] + [4 bytes of Hash() of previous 33 bytes], base58 encoded
    #compressed: 0x80 + [32-byte secret] + 0x01 + [4 bytes of Hash() previous 34 bytes], base58 encoded
    prefix = b'\x80'
    if testnet:
        prefix = b'\xef'
    h = prefix + h
    if compressed: h += b'\x01'
    h += hashlib.sha256(hashlib.sha256(h).digest()).digest()[:4]
    return base58.b58encode(h).decode('utf-8')
def main():
    constants.NETWORK_SEGWIT_PREFIXES["mainnet"] = "sugar"
    # always remember to setup the network
    setup('mainnet')
    kavo=priv2WIF(b'KxRMt7KypfEsLNSikhxTPYepDMBizHNmH5Bii3wssgesxrkHNJg6')
    print(kavo)
    private = PrivateKey.from_wif('KwDiBf89QgGbjEhKnhXJuH7LrciVrZi3qYjgd9M7rFU73sVHnoWn')
    public = private.get_public_key()
    segwit = public.get_segwit_address()
    address = segwit.to_string()
    wif = private.to_wif()
    print(wif,address)
main()
