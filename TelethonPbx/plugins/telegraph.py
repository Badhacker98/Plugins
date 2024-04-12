import datetime
import os
import random
import string

from PIL import Image
from TelethonPbx.plugins import *

from telegraph import Telegraph, exceptions, upload_file

telegraph = Telegraph()
account = telegraph.create_account(short_name=Config.TELEGRAPH_NAME)
auth_url = account["auth_url"]

def resize_image(image):
    im = Image.open(image)
    im.save(image, "PNG")


@Pbx_cmd(pattern="t(m|t)(?:\s|$)([\s\S]*)")
async def _(event):
    if not os.path.isdir(Config.TMP_DOWNLOAD_DIRECTORY):
        os.makedirs(Config.TMP_DOWNLOAD_DIRECTORY)
    lists = event.text.split(" ", 1)
    optional_title = None
    if len(lists) == 2:
        optional_title = lists[1].strip()
    Pbx = await eor(event, "Making Telegraph Link....")
    _, _, Pbx_mention = await client_id(event)
    reply = await event.get_reply_message()
    if reply:
        start = datetime.datetime.now()
        input_str = lists[0][2:3]
        if input_str == "m":
            downloaded_file_name = await event.client.download_media(
                reply, Config.TMP_DOWNLOAD_DIRECTORY
            )
            end = datetime.datetime.now()
            ms = (end - start).seconds
            await Pbx.edit(
                f"Downloaded to  {downloaded_file_name}  in  {ms}  seconds. \nMaking Telegraph Link....."
            )
            if downloaded_file_name.endswith((".webp")):
                resize_image(downloaded_file_name)
            try:
                start = datetime.datetime.now()
                media_urls = upload_file(downloaded_file_name)
            except exceptions.TelegraphException as exc:
                await parse_error(Pbx, exc)
                os.remove(downloaded_file_name)
            else:
                end = datetime.datetime.now()
                ms_two = (end - start).seconds
                os.remove(downloaded_file_name)
                await Pbx.edit(
                    "✓ [File uploaded to telegraph](https://te.legra.ph{}) \n✓ Time Taken: {} secs \n✓ By: {} \n✓  https://te.legra.ph{}".format(
                        media_urls[0],
                        (ms + ms_two),
                        Pbx_mention,
                        media_urls[0],
                    ),
                    link_preview=True,
                )
        elif input_str == "t":
            user_object = await event.client.get_entity(reply.sender_id)
            title_of_page = user_object.first_name
            if optional_title:
                title_of_page = optional_title
            page_content = reply.message
            if reply.media:
                return await Pbx.edit(f"Media aren't supported for Text Telegraph")
            page_content = page_content.replace("\n", "<br>")
            try:
                response = telegraph.create_page(title_of_page, html_content=page_content)
            except Exception as e:
                title_of_page = "".join(
                    random.choice(list(string.ascii_lowercase + string.ascii_uppercase))
                    for _ in range(16)
                )
                response = telegraph.create_page(title_of_page, html_content=page_content)
            end = datetime.datetime.now()
            ms = (end - start).seconds
            await Pbx.edit(
                f"✓ [Pasted to telegraph](https://te.legra.ph/{response['path']}) \n✓ Time Taken: {ms} secs\n✓ By:  {Pbx_mention} \n✓  https://te.legra.ph/{response['path']}",
                link_preview=True,
            )
    else:
        await eod(Pbx, "Reply to a message to get a permanent telegra.ph link.")


@Pbx_cmd(pattern="tgraph(?:\s|$)([\s\S]*)")
async def _(event):
    Pbx = await eor(event, "Making telegraph post ...")
    reply = await event.get_reply_message()
    lists = event.text.split(" ", 1)
    if not reply:
        return await parse_error(event, "Nothing given to paste on telegraph.")
    if not len(lists) == 2:
        return await parse_error(event, "Give a title for the telegraph page!")
    query = lists[1].split("|", 2)
    title = None
    auth = "[ ♡³_🫧𝆺꯭𝅥˶֟፝͟͝β𝝰꯭‌𝞉 ꯭𝝡꯭𝞄꯭𝞌𝞉꯭𝝺꯭𝆺꯭𝅥🍷┼❤️// ]"
    url = "https://t.me/ll_BAD_BBY_ll"
    content = reply.message
    if len(query) == 3:
        title = query[0].strip()
        auth = query[1].strip()
        url = query[2].strip()
    else:
        title = query[0].strip()
    link = await telegraph_paste(title, content, auth, url)
    await Pbx.edit(f"Created telegraph post! \n\n◈ Title: {title} 


CmdHelp("telegraph").add_command(
    "tt", "<reply to text message>", "Uploads the replied text message to telegraph making a short telegraph link"
).add_command(
    "tm", "<reply to media>", "Uploads the replied media (sticker/ gif/ video/ image) to telegraph and gives a short telegraph link"
).add_command(
    "tgraph", "<reply to a text> <title|author|authorlink>", "Makes a telegraph page of replied content using html parser."
).add_info(
    "Make Telegraph Links."
).add_warning(
    "✅ Harmless Module."
).add()
    
