import random
from PrimeMega.events import register
from PrimeMega import telethn

APAKAH_STRING = ["Iya", 
                 "Tidak", 
                 "Yes" 
                 "No" 
                 "Mungkin", 
                 "Maybe", 
                 ]


@register(pattern="^/apakah ?(.*)")
async def apakah(event):
    quew = event.pattern_match.group(1)
    if not quew:
        await event.reply('Give me a question 😐')
        return
    await event.reply(random.choice(APAKAH_STRING))
