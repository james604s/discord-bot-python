#導入 Discord.py
import discord
#client 是我們與 Discord 連結的橋樑
client = discord.Client()


# 調用event函式庫
@client.event
# 當機器人完成啟動時
async def on_ready():
    print('目前登入身份：', client.user)
    game = discord.Game('努力學習py中')
    # discord.Status.<狀態>，可以是online,offline,idle,dnd,invisible
    await client.change_presence(status=discord.Status.idle, activity=game)


@client.event
# 當有訊息時
async def on_message(message):
    # 排除自己的訊息，避免陷入無限循環
    if message.author == client.user:
        return
    # 如果以「說」開頭
    if message.content.startswith('Say'):
        # 分割訊息成兩份
        tmp = message.content.split(" ", 2)
        # 如果分割後串列長度只有1
        if len(tmp) == 1:
            await message.channel.send("你要我說什麼啦？")
        else:
            await message.channel.send(tmp[1])
    if message.content.startswith('更改狀態'):
        # 切兩刀訊息
        tmp = message.content.split(" ", 2)
        # 如果分割後串列長度只有1
        if len(tmp) == 1:
            await message.channel.send("你要改成什麼啦？")
        else:
            game = discord.Game(tmp[1])
            # discord.Status.<狀態>，可以是online,offline,idle,dnd,invisible
            await client.change_presence(status=discord.Status.idle, activity=game)


client.run('input your token') #TOKEN 在剛剛 Discord Developer 那邊「BOT」頁面裡面