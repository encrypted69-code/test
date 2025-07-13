from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes
import qrcode
from io import BytesIO
import os
from datetime import datetime

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Send me any text and I will send you a QR code!')

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    # Generate QR code
    qr = qrcode.make(text)
    # Save to images/ with a unique name
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    filename = f'images/qr_{timestamp}.png'
    os.makedirs('images', exist_ok=True)
    qr.save(filename, 'PNG')
    # Also send as photo
    with open(filename, 'rb') as photo:
        await update.message.reply_photo(photo=photo, caption="Here is your QR code!")

app = ApplicationBuilder().token('8161625128:AAH-s6KpjGEWWwMxaZofy2eik2nJtx4yNCw').build()
app.add_handler(CommandHandler('start', start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
app.run_polling()
