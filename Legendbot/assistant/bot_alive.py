from telethon import Button

from Legendbot import Config, legend, legendversion

from ..core.logger import logging
from ..helpers import reply_id
from ..plugins import mention
from ..sql_helper.bot_blacklists import check_is_black_list
from . import BOTLOG, BOTLOG_CHATID

LOGS = logging.getLogger(__name__)

menu_category = "bot"
botusername = Config.BOT_USERNAME


PM_IMG = "https://te.legra.ph/file/e530e5a3c1fa848c75b7c.jpg"
pm_caption = f"⚜『ʀᴀᴅʜᴀᴜꜱᴇʀʙᴏᴛ†』ɪꜱ ᴏɴʟɪɴᴇ⚜ \n\n"
pm_caption += f"Oᴡɴᴇʀ ~ 『{mention}』\n"
pm_caption += f"**╭───────────**\n"
pm_caption += f"┣Tᴇʟᴇᴛʜᴏɴ ~ `1.15.0` \n"
pm_caption += f"┣『ʀᴀᴅʜᴀᴜꜱᴇʀʙᴏᴛ†』~ `{legendversion}` \n"
pm_caption += f"┣ᴄʜᴀɴɴᴇʟ ~ [Channel](https://t.me/RadhaX2Update)\n"
pm_caption += f"┣**License** ~ [License v3.0](github.com/LEGEND-AI/LEGENBOT/blob/master/LICENSE)\n"
pm_caption += f"┣Copyright ~ By [『ʀᴀᴅʜᴀᴜꜱᴇʀʙᴏᴛ』 ](https://t.me/RadhaX2Support)\n"
pm_caption += f"┣Assistant ~ By [『ʀᴀᴅʜᴀᴜꜱᴇʀʙᴏᴛ』 ](https://t.me/GhostRadha)\n"
pm_caption += f"╰────────────\n"
pm_caption += f"       »»» [『ʀᴀᴅʜᴀᴜꜱᴇʀʙᴏᴛ』](https://t.me/GhostRadha) «««"


@legend.bot_cmd(
    pattern=f"^/alive({botusername})?([\s]+)?$",
    incoming=True,
)
async def bot_start(event):
    chat = await event.get_chat()
    await legend.get_me()
    if check_is_black_list(chat.id):
        return
    reply_to = await reply_id(event)
    buttons = [
        (Button.url("ʀᴇᴩᴏ ⚡", "https://github.com/RADHAK8/RADHA-USERBOT"),),
    ]
    try:
        await event.client.send_file(
            chat.id,
            PM_IMG,
            caption=pm_caption,
            link_preview=False,
            buttons=buttons,
            reply_to=reply_to,
        )
    except Exception as e:
        if BOTLOG:
            await event.client.send_message(
                BOTLOG_CHATID,
                f"**Error**\nThere was a error while using **alive**. `{e}`",
            )
