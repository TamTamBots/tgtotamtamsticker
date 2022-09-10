MSG_SET_NOT_FOUND = (
    "There is no pack named '{tg_set_name}' in Telegram 😢\n"
    "Send me another name and let's try again!\n\n"
    "The name of the sticker pack can be obtained by rummaging through the pack in any chat, "
    'for example, to yourself in "Saved messages."\n'
    "You'll get a link like this: https://t.me/addstickers/RickAndMorty, "
    "package name in this case is **RickAndMorty**\n"
    "You can also search here: https://tlgrm.ru/stickers, "
    "In this case, the pack name will be at the end of the browser's address bar, for example, "
    "for https://tlgrm.ru/stickers/GravityFallsUn1 pack name"
    '- **GravityFallsUn1**, not "Gravity Falls"')

MSG_SET_IN_PROGRESS = (
    "One moment, I'm already preparing an archive with stickers from the pack:\n{tg_set_name}: "
    "https://t.me/addstickers/{tg_set_name}")

MSG_WELCOME = ("Hi 👋\nI'll help you download your favorite sticker pack"
               "from Telegram and tell you how to upload it to TamTam.\n"
               "Just send me the name of the sticker pack\n")

MSG_ERROR = (
    "Sorry, something unexpected happened in the process 😢\nTry another pack.\n"
    "I'm still young and trying to get better 😉")

MSG_SUCCESS = (
    "Done   \nTo upload the pack to TamTam, you need to make a couple more clicks:\n"
    "We write to the bot: https://tt.me/stickers\n"
    "We do everything according to the instructions from the bot. Something like this:\n"
    "- create a new pack\n"
    "- send the zip received here with stickers, the bot will reply that everything is ok\n"
    "- if there are several archives, load the next one\n"
    "- ...\n"
    "- PROFIT!\n")

MSG_MANY_STICKERS = (
    "You're a little unlucky, there are more than 50 stickers in the original Telegram pack.\n"
    "TamTam allows you to upload up to 50 pieces in one archive.\n"
    "I will send some archives, they will need to be sent to the bot"
    "(https://tt.me/stickers) one by one, waiting for the previous one to be processed."
)
