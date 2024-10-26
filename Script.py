class script(object):
    START_TXT = """👋🏻 ʜᴇʟʟᴏ ᴛʜᴇʀᴇ {}.
ɪ ᴀᴍ ʜᴇʀᴇ ᴛᴏ ᴘʀᴏᴠɪᴅᴇ ʙᴏᴏᴋꜱ ɪɴ ᴠᴀʀɪᴏᴜꜱ ꜰᴏʀᴍᴀᴛꜱ ᴀꜱ ꜱᴏᴏɴ ᴀꜱ ᴍᴇᴍʙᴇʀꜱ ᴍᴀᴋᴇ ᴛʜᴇɪʀ ʀᴇQᴜᴇꜱᴛꜱ.\n\nᴡᴀɴᴛ ᴍʏ ʜᴇʟᴘ ɪɴ ᴀ ɢʀᴏᴜᴘ? ᴊᴜꜱᴛ ᴀᴅᴅ ᴍᴇ, <i>ᴘʀᴏᴍᴏᴛᴇ ᴍᴇ ᴛᴏ ᴀᴅᴍɪɴ</i>, ᴀɴᴅ ᴡᴀᴛᴄʜ ᴍᴇ ʜᴀɴᴅʟᴇ ʙᴏᴏᴋ ʀᴇQᴜᴇꜱᴛꜱ ᴅɪʀᴇᴄᴛʟʏ ɪɴ ᴛʜᴇ ɢʀᴏᴜᴘ.\n\nʟᴇᴛ’ꜱ ᴍᴀᴋᴇ ʀᴇᴀᴅɪɴɢ ᴇᴀꜱɪᴇʀ ᴀɴᴅ ᴍᴏʀᴇ ꜰᴜɴ ᴛᴏɢᴇᴛʜᴇʀ!

©️ ᴍᴀɪɴᴛᴀɪɴᴇᴅ ʙʏ @infohub_updates"""
    HELP_TXT = """
    🙋🏻‍♂️   ʜᴇʟʟᴏ ᴛʜᴇʀᴇ  {} 🤓

○ ᴀᴠᴀɪʟᴀʙʟᴇ ᴄᴏᴍᴍᴀɴᴅꜱ
     
 /start - ᴄʜᴇᴄᴋ ɪꜰ ɪ'ᴍ ᴀʟɪᴠᴇ
 /status - ᴍʏ ᴄᴜʀʀᴇɴᴛ ꜱᴛᴀᴛᴜꜱ
 /info - ɢᴇᴛ ɪɴꜰᴏʀᴍᴀᴛɪᴏɴ ᴀʙᴏᴜᴛ ꜱᴏᴍᴇᴏɴᴇ
 /id - ʏᴏᴜʀ ᴅᴇᴛᴀɪʟꜱ
 /stats - ᴅᴀᴛᴀʙᴀꜱᴇ'ꜱ ᴄᴜʀʀᴇɴᴛ ꜱᴛᴀᴛᴜꜱ
 /broadcast - ʙʀᴏᴀᴅᴄᴀꜱᴛ ꜱᴏᴍᴇᴛʜɪɴɢ (ᴏᴡɴᴇʀ ᴏɴʟʏ)


○ ᴘʟᴇᴀꜱᴇ ᴅᴏ ɴᴏᴛ ꜱᴘᴀᴍ ᴍᴇ 🙂
○ ᴜꜱᴇ ᴍᴇ ʀᴇꜱᴘᴏɴꜱɪʙʟʏ 🎀
"""
    ABOUT_TXT = """<b>◎ Nᴀᴍᴇ: 𝕐𝕠𝕦𝕣 𝔹𝕠𝕠𝕜𝕤
◎ Cʀᴇᴀᴛᴏʀ: <a href=https://t.me/infohubupdates>ɪɴꜰᴏʜᴜʙ ᴜᴘᴅᴀᴛᴇꜱ</a>
◎ Lᴀɴɢᴜᴀɢᴇ: Pʏᴛʜᴏɴ 3
◎ Dᴀᴛᴀ Bᴀsᴇ: Mᴏɴɢᴏ DB
◎ Bᴏᴛ Sᴇʀᴠᴇʀ: ʜᴇʀᴏᴋᴜ</b>"""
    SOURCE_TXT = """<b>NOTE:</b>
- 𝕐𝕠𝕦𝕣 𝔹𝕠𝕠𝕜𝕤 ɪꜱ ɴᴏᴛ ᴀɴ ᴏᴘᴇɴ ꜱᴏᴜʀᴄᴇ ᴘʀᴏᴊᴇᴄᴛ. 

<b>DEVS:</b>
- <a href=https://t.me/infohub_updates>ɪɴꜰᴏʜᴜʙ ᴜᴘᴅᴀᴛᴇꜱ🌈</a>"""
    MANUELFILTER_TXT = """Help: <b>Filters</b>
- Filter is the feature were users can set automated replies for a particular keyword and the bot will respond whenever a keyword is matched
<b>NOTE:</b>
1. This Bot should have admin privillage.
2. only admins can add filters in a chat.
3. alert buttons have a limit of 64 characters.

<b>Commands and Usage:</b>
• /filter - <code>add a filter in chat</code>
• /filters - <code>list all the filters of a chat</code>
• /del - <code>delete a specific filter in chat</code>
• /delall - <code>delete the whole filters in a chat (chat owner only)</code>"""
    BUTTON_TXT = """Help: <b>Buttons</b>

- This bot supports both url and alert inline buttons.

<b>NOTE:</b>
1. Telegram will not allow you to send buttons without any content, so content is mandatory.
2. This Bot supports buttons with any telegram media type.
3. Buttons should be properly parsed as markdown format

<b>URL buttons:</b>
<code>[Button Text](buttonurl:https://t.me/infohub_updates)</code>

<b>Alert buttons:</b>
<code>[Button Text](buttonalert:This is an alert message)</code>"""
    AUTOFILTER_TXT = """Help: <b>Auto Filter</b>

<b>NOTE:</b>
1. Make me the admin of your channel if it's private.
2. make sure that your channel does not contain porn and/or fake files.
3. Forward the last message to me with quotes.
 I'll add all the files in that channel to my db."""
    CONNECTION_TXT = """Help: <b>Connections</b>

- Used to connect bot to PM for managing filters 
- it helps to avoid spamming in groups.

<b>NOTE:</b>
1. Only admins can add a connection.
2. Send <code>/connect</code> for connecting me to ur PM

<b>Commands and Usage:</b>
• /connect  - <code>connect a particular chat to your PM</code>
• /disconnect  - <code>disconnect from a chat</code>
• /connections - <code>list all your connections</code>"""
    EXTRAMOD_TXT = """Help: <b>Extra Modules</b>

<b>NOTE:</b>
these are the extra features of Eva Maria

<b>Commands and Usage:</b>
• /id - <code>get id of a specified user.</code>
• /info  - <code>get information about a user.</code>
"""
    ADMIN_TXT = """Help: <b>Admin mods</b>

<b>NOTE:</b>
This module only works for my admins

<b>Commands and Usage:</b>
• /logs - <code>to get the rescent errors</code>
• /stats - <code>to get status of files in db.</code>
• /delete - <code>to delete a specific file from db.</code>
• /users - <code>to get list of my users and ids.</code>
• /chats - <code>to get list of the my chats and ids </code>
• /leave  - <code>to leave from a chat.</code>
• /disable  -  <code>do disable a chat.</code>
• /ban  - <code>to ban a user.</code>
• /unban  - <code>to unban a user.</code>
• /channel - <code>to get list of total connected channels</code>
• /broadcast - <code>to broadcast a message to all users</code>"""
    STATUS_TXT = """★ 𝚃𝙾𝚃𝙰𝙻 𝙵𝙸𝙻𝙴𝚂: <code>{}</code>
★ 𝚃𝙾𝚃𝙰𝙻 𝚄𝚂𝙴𝚁𝚂: <code>{}</code>
★ 𝚃𝙾𝚃𝙰𝙻 𝙲𝙷𝙰𝚃𝚂: <code>{}</code>
★ 𝚄𝚂𝙴𝙳 𝚂𝚃𝙾𝚁𝙰𝙶𝙴: <code>{}</code> 
★ 𝙵𝚁𝙴𝙴 𝚂𝚃𝙾𝚁𝙰𝙶𝙴: <code>{}</code> """
    LOG_TEXT_G = """#NewGroup
Group = {}(<code>{}</code>)
Total Members = <code>{}</code>
Added By - {}
"""
    RESULT_TXT="""ᴄᴏɴɢʀᴀᴛᴜʟᴀᴛɪᴏɴꜱ! 🎉🎉 ᴛʜɪꜱ ᴀʀᴇ ᴛʜᴇ ʀᴇꜱᴜʟᴛꜱ ꜰʀᴏᴍ ᴍʏ ᴅᴀᴛᴀʙᴀꜱᴇ ᴛʜᴀᴛ ᴍᴀᴛᴄʜ ʏᴏᴜʀ QᴜᴇʀʏEᴅᴀᴀ Mᴏɴᴇʜ I Fᴏᴜɴᴅ Iɴ Mʏ Dʙ Fᴏʀ Yᴏᴜʀ Qᴜᴇʀʏ {}"""

    CUSTOM_FILE_CAPTION = """<b>📂Fɪʟᴇɴᴀᴍᴇ : {file_name}
FɪʟᴇSɪᴢᴇ : {file_size}

╔════ ᴊᴏɪɴ ᴡɪᴛʜ ᴜs ════╗
▫️<a href=https://t.me/Bookslibraryofficial> Pages & Voices </a>
╚════ ᴊᴏɪɴ ᴡɪᴛʜ ᴜs ════╝</b>"""

    
    RESTART_TXT = """
<b>𝖡𝗈𝗍 𝖱𝖾𝗌𝗍𝖺𝗋𝗍𝖾𝖽 !</b>
𝕐𝕠𝕦𝕣 𝔹𝕠𝕠𝕜𝕤
**@readbooks_robot**

📅 𝖣𝖺𝗍𝖾 : <code>{}</code>
⏰ 𝖳𝗂𝗆𝖾 : <code>{}</code>
🌐 𝖳𝗂𝗆𝖾𝗓𝗈𝗇𝖾 : <code>Asia/Kolkata</code>
🛠️ 𝖡𝗎𝗂𝗅𝖽 𝖲𝗍𝖺𝗍𝗎𝗌 : <code>𝗏1 [ 𝖲𝗍able 😁 ]</code></b>"""
    
    LOG_TEXT_P = """#NewUser
ID - <code>{}</code>
Name - {}
"""
    SPOLL_NOT_FND="""Eᴅᴀᴀ Mᴏɴᴇʜ🤚🏻
I couldn't find anything related to your request. 😵
Try reading the instruction below 👇🏼
    """
#SPELL CHECK LANGUAGES TO KNOW callback
    ENG_SPELL="""Please Note Below📓
1️⃣Ask in Correct Spelling
2️⃣Don't ask Books which are not Realased yet

    """
    MAL_SPELL="""ദയവായി താഴെ ശ്രദ്ധിക്കുക📓
1️⃣ശരിയായ അക്ഷരവിന്യാസത്തിൽ ചോദിക്കുക
2️⃣OTT പ്ലാറ്റ്‌ഫോമുകളിൽ റിലീസ് ചെയ്യാത്ത സിനിമകൾ ചോദിക്കരുത്

    """
    HIN_SPELL="""कृपया नीचे ध्यान दें📓
1️⃣सही वर्तनी में पूछें
2️⃣उन फिल्मों के बारे में न पूछें जो ओटीटी प्लेटफॉर्म पर रिलीज नहीं हुई हैं
3️⃣संभव है पूछें [मूवी का नाम भाषा] इस तरह या [मूवी वर्ष]
    """
    TAM_SPELL="""கீழே கவனிக்கவும்📓
1️⃣சரியான எழுத்துப்பிழையில் கேளுங்கள்
2️⃣வெளியாகாத திரைப்படங்களைக் கேட்காதீர்கள்
3️⃣இந்த வடிவத்தில் கேளுங்கள் [திரைப்படத்தின் பெயர், ஆண்டு]
    """

    CHK_MOV_ALRT="""♻️ ᴄʜᴇᴄᴋɪɴɢ ꜰɪʟᴇ ᴏɴ ᴍʏ ᴅᴀᴛᴀʙᴀꜱᴇ... ♻️"""
    
    OLD_MES=""" 𝐘𝐨𝐮 𝐚𝐫𝐞 𝐮𝐬𝐢𝐧𝐠 𝐨𝐧𝐞 𝐨𝐟 𝐦𝐲 𝐨𝐥𝐝 𝐦𝐞𝐬𝐬𝐚𝐠𝐞𝐬🤔, 𝐩𝐥𝐞𝐚𝐬𝐞 𝐬𝐞𝐧𝐝 𝐭𝐡𝐞 𝐫𝐞𝐪𝐮𝐞𝐬𝐭 𝐚𝐠𝐚𝐢𝐧"""
    
    MOV_NT_FND="""<b> Tʜɪs ʙᴏᴏᴋ Is Nᴏᴛ Yᴇᴛ Rᴇᴀʟᴇsᴇᴅ Oʀ Aᴅᴅᴇᴅ Tᴏ DB</b>
Report To ADMIN - @infohubsupport_robot
"""
    RESTART_GC_TXT = """
<b><u>𝖡𝗈𝗍 𝖱𝖾𝗌𝗍𝖺𝗋𝗍𝖾𝖽 ✅</u></b>"""

