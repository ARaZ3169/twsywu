from GPBot import Stark
from telethon import events, Button

PM_START_TEXT = """
**Hi {}**
I am a bot who works for LosAntos_Scam and can detect spammers in groups can protect groups from then

**Click the below button for getting help menu!**
"""

@Stark.on(events.NewMessage(pattern="^[?!/]start$"))
async def start(event):

    if event.is_private:
       await event.reply(PM_START_TEXT.format(event.sender.first_name), buttons=[
        [Button.inline("Help And Commands", data="help")],
        [Button.url("Group Helper", "t.me/LosAntos_Scam")]])
       return

    if event.is_group:
       await event.reply("**I am alive 24/7!**")
       return
