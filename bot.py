from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import requests

# URL to the raw image file in your GitHub repo
QR_IMAGE_URL = "https://raw.githubusercontent.com/encrypted69-code/test/main/qr/qr1.png.jpg"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Send /qr to receive the QR code image.')

async def send_qr(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Download the image from GitHub
    response = requests.get(QR_IMAGE_URL)
    if response.status_code == 200:
        await update.message.reply_photo(photo=response.content, caption="Here is your QR code from GitHub!")
    else:
        await update.message.reply_text("Sorry, could not retrieve the QR code image.")

app = ApplicationBuilder().token('8161625128:AAH-s6KpjGEWWwMxaZofy2eik2nJtx4yNCw').build()
app.add_handler(CommandHandler('start', start))
app.add_handler(CommandHandler('qr', send_qr))
app.run_polling()
