import aiohttp
from sqlalchemy.testing import assert_warnings

SPELLER_URL = 'https://speller.yandex.net/services/spellservice.json/checkText'


async def speller_query(text: str) -> dict:
    async with aiohttp.ClientSession() as session:
        async with session.get(SPELLER_URL, params={
            'text': text
        }) as response:
            return await response.json()
