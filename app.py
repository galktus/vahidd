#pip install pyrogram
#pip install tgcrypto
# my.telegram.or 

from pyrogram import Client
api_id = 8600804
api_hash = "b434223c50f512421b86cda44d0a8775"
bot_token = "1982205672:AAEAcAMxcPKQ3DtnIVSOLZa9D_AbtGS35Vo"
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
