from dotenv import load_dotenv
import os 
import telepot

load_dotenv()


class Telegram():
     def __init__(self):
         my_token = os.environ.get('BOT_TOKEN') # 봇파더에서 얻은 토큰값을 입력합니다.
         self.bot = telepot.Bot(token=my_token)

     def sendMessage(self, message):
         self.bot.sendMessage("6707224567", message, parse_mode="Markdown")

     def getUpdates(self):
         return self.bot.getUpdates()
    #  print(getUpdates()) # 내 ID 확인하는 방법


if __name__ == '__main__':  
     bot = Telegram()
    #  msg = "테스트메시지"
     print(bot.getUpdates()) # 내 ID 확인하는 방법
    #  bot.sendMessage(msg)