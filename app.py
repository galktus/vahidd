#pip install pyrogram
#pip install tgcrypto
# my.telegram.or 

from pyrogram import Client
api_id = 1074077
api_hash = "d3d3602a5b6c1e2df56183c219816d55"
bot_token = "1918422706:AAH-0K7diUxw2ftkSLVn2XczaN3HuHTYUOs"
app = Client('session_01',api_id=api_id,api_hash=api_hash,bot_token=bot_token)
@app.on_message()
def handel(Client,message):
    print(message)
    if message.reply_to_message :
        text = str(message.text) 
        if text =="ن":
            message.delete()
            spl = str(message.reply_to_message.text).split(' ')
            print(spl)
            app.send_message(message.chat.id,'معامله شد \n  قیمت :'+ str(spl[3])+ "\n خریدار :"+str(message.from_user.first_name)+"\n فروشنده : "+str(message.reply_to_message.from_user.first_name))
app.run()    
