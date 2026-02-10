import os
from telegram import Update
from telegram.ext import Application, MessageHandler, filters, ContextTypes
import yt_dlp

TOKEN = os.getenv("8486924160:AAHWMD-lNgTWPo_3Qd6lM5Keqls29Ewl3y4")

async def download_video(update: Update, context: ContextTypes.DEFAULT_TYPE):
    url = update.message.text
    if "instagram.com" in url:
        await update.message.reply_text("در حال بررسی و دانلود... لطفا صبر کنید.")
        
        # تنظیمات دانلود
        ydl_opts = {'format': 'best', 'outtmpl': 'video.mp4'}
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        
        # ارسال ویدیو برای کاربر
        await update.message.reply_video(video=open('video.mp4', 'rb'))
        os.remove('video.mp4') # پاک کردن فایل برای پر نشدن حافظه
    else:
        await update.message.reply_text("لطفاً یک لینک معتبر اینستاگرام بفرستید.")

if __name__ == '__main__':
    app = Application.builder().token(TOKEN).build()
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, download_video))
    app.run_polling()
