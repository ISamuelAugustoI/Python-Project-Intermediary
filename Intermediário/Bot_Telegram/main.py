# Importando Bibliotecas:
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

# Função de boas-vindas ao Bot:
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Welcome to the Samuel Bot! Type /help to help.')

# Função que exibe os comandos disponíveis:
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    commands = (
        '/start - Start the bot\n'
        '/help - Show this help message\n'
        '/echo <message> - I will repeat your message'
    )
    await update.message.reply_text(f'Here are the commands you can use:\n{commands}')

# Função que responde a mensagens de texto:
async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if context.args:
        user_message = ' '.join(context.args)
        await update.message.reply_text(f'You said: {user_message}')
    else:
        await update.message.reply_text('Please provide a message to echo. Example: /echo Hello!')

# Configuração Principal do Bot:
def main():
    TOKEN = '7800848537:AAFLhrIv-W_qkHsrW_H1j7IGbTAbmwo4POI'

    # Configurar o Bot com o ApplicationBuilder:
    application = ApplicationBuilder().token(TOKEN).build()

    # Adicionar Comandos e Handlers:
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("echo", echo))

    # Iniciando o Bot:
    print('Bot is running...')
    application.run_polling()

if __name__ == '__main__':
    main()

# 7800848537:AAFLhrIv-W_qkHsrW_H1j7IGbTAbmwo4POI