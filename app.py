#接收 line 的套件
#import ______
#回覆（用line的套件功能）
#send_msg("asdasdasd")
#SDK
#software development kit
#-------------------
#web app
#通常用app.py當主要檔案
#flask(小), django(大)


from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage, StickerSendMessage
)

app = Flask(__name__)

line_bot_api = LineBotApi('Zd8uzUJAp+uWoR1jvqvrmfzAK/7nilyrwGVJpQ6ATTXV0UJzj3OS0u826lVWVneCQIME91GuBZLbrREbBmC5D1hbFlcXPubEUsyL1hkt423HNAGwv3N/8N/L2wDBSqGGtlnvd/euDyl2iqQtSXIbUQdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('ce80ff1fc97ee575c7df19c4fcc3c4b3')
 

@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    msg = event.message.text
    r = "很抱歉，您說什麼?"
    if "給我貼圖" in msg:
        sticker_message = StickerSendMessage(
            package_id='1',
            sticker_id='1'
        )

        line_bot_api.reply_message(
            event.reply_token,
            sticker_message)

        return

    if msg in ["hi", "Hi"]:
        r = "hi!"
    elif msg == "你吃飯了嗎?":
        r = "還沒"
    elif msg == "你是誰?":
        r = "我是機器人"
    elif msg == "你愛我嗎?":
        r = "超愛"
    elif "你女朋是誰" in msg:
        r = "JJ"
    elif msg == "今天好累":
        r = "辛苦啦～早點睡～記得抬腳！" 
    elif "訂位" in msg:
        r = "您想訂位，是嗎?"

    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=r))



if __name__ == "__main__":
    app.run()