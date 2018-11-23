const TeleBot = require('telebot');
var TOKEN = ""

if(TOKEN == "")
{
    TOKEN = process.env.TOKEN
}

const bot = new TeleBot(TOKEN);
const log = console.log
const dataFile = require('./data')
const data = dataFile.Data
const length = data.length


// Generate a random Integer.
function getRandomInt(max) 
{
    return Math.floor(Math.random() * Math.floor(max));
}

bot.on(['/start'], (msg) => {
    const userID = msg.from.id
    TEXT = "我是一个骚话机器人，专门收集NB的骚话。\n - 回复 /yiyan 来随机抽取一句骚话作为今日一言。"
    bot.sendMessage(userID,TEXT);
});

bot.on(['/yiyan','/sao'], (msg) => {
    TEXT = data[getRandomInt(length)]
    console.log("Send ----> " + TEXT)
    return bot.sendMessage(msg.chat.id, TEXT, { replyToMessage: msg.message_id });
});



bot.start();
