import os
import json
from datetime import datetime
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, ContextTypes, filters
import matplotlib.pyplot as plt
from fpdf import FPDF

TOKEN = "7603906189:AAFcnPuYWW9c069a9KFAtfdziSdfdn9156I"  # <-- Bot tokeningizni bu yerga qo‘ying
DATA_DIR = "data"

# --- JSON bilan ishlash funksiyalari ---
def get_user_file(user_id):
    os.makedirs(DATA_DIR, exist_ok=True)
    return os.path.join(DATA_DIR, f"{user_id}.json")


def load_data(user_id):
    file_path = get_user_file(user_id)
    if os.path.exists(file_path):
        with open(file_path, "r") as f:
            return json.load(f)
    return {}

def save_data(user_id, data):
    with open(get_user_file(user_id), "w") as f:
        json.dump(data, f)

def add_transaction(user_id, amount, tx_type):
    data = load_data(user_id)
    today = datetime.today()
    month_key = today.strftime("%Y-%m")

    if month_key not in data:
        data[month_key] = {"daromad": 0, "xarajat": 0}

    data[month_key][tx_type] += amount
    save_data(user_id, data)

# --- PDF va grafik yaratish ---
def generate_chart(data, user_id):
    months = list(data.keys())
    daromad = [data[m]["daromad"] for m in months]
    xarajat = [data[m]["xarajat"] for m in months]

    plt.figure()
    x = range(len(months))
    plt.bar(x, daromad, width=0.4, label='Daromad', align='center')
    plt.bar(x, xarajat, width=0.4, label='Xarajat', align='edge')
    plt.xticks(x, months, rotation=45)
    plt.title("Oylik daromad va xarajat (¥)")
    plt.legend()
    chart_path = f"{DATA_DIR}/{user_id}_chart.png"
    plt.tight_layout()
    plt.savefig(chart_path)
    plt.close()
    return chart_path

def generate_pdf(data, chart_path, user_id):
    os.makedirs(DATA_DIR, exist_ok=True)
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=14)
    pdf.cell(200, 10, txt="Oylik hisobot", ln=True, align='C')

    for month, val in data.items():
        balance = val['daromad'] - val['xarajat']
        pdf.cell(200, 10, txt=f"{month}: Daromad = {val['daromad']} ¥, Xarajat = {val['xarajat']} ¥, Balans = {balance} ¥", ln=True)

    # Faqat 1 marta tekshirish va rasm qo‘shish
    if os.path.exists(chart_path):
        pdf.image(chart_path, x=10, y=pdf.get_y(), w=180)
    else:
        pdf.cell(200, 10, txt="Grafik topilmadi", ln=True)

    pdf_path = f"{DATA_DIR}/{user_id}_hisobot.pdf"
    pdf.output(pdf_path)
    return pdf_path

# --- Telegram komandalar ---
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    buttons = [["💰 Daromad qo'shish", "➖ Xarajat qo'shish"], ["📊Balans", "🧾Hisobot (PDF + grafik)"],["🗑Tarixni o'chirish"]]
    await update.message.reply_text(
        "Assalomu alaykum! Xarajat va daromadlarni boshqarish uchun tayyorman.",
        reply_markup=ReplyKeyboardMarkup(buttons, resize_keyboard=True)
    )

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    user_id = update.message.from_user.id

    if text == "💰Daromad qo'shish":
        await update.message.reply_text("Daromad miqdorini yuboring:")
        context.user_data["mode"] = "daromad"
    elif text == "➖ Xarajat qo'shish":
        await update.message.reply_text("Xarajat miqdorini yuboring:")
        context.user_data["mode"] = "xarajat"
    elif text == "📊Balans":
        data = load_data(user_id)
        if not data:
            await update.message.reply_text("Hali hech qanday yozuv yo'q.")
            return
        last_month = sorted(data.keys())[-1]
        d = data[last_month]
        balance = d['daromad'] - d['xarajat']
        await update.message.reply_text(
            f"{last_month} oyi uchun:\nDaromad: {d['daromad']} ¥\nXarajat: {d['xarajat']} ¥\nBalans: {balance} ¥"
        )
    elif text == "🧾Hisobot (PDF + grafik)":
        data = load_data(user_id)
        if not data:
            await update.message.reply_text("Hisobot uchun ma'lumot topilmadi.")
            return
        chart = generate_chart(data, user_id)
        pdf = generate_pdf(data, chart, user_id)
        await update.message.reply_photo(photo=open(chart, 'rb'))
        await update.message.reply_document(document=open(pdf, 'rb'))
    elif "mode" in context.user_data:
        try:
            amount = int(text)
            mode = context.user_data["mode"]
            add_transaction(user_id, amount, mode)
            await update.message.reply_text(f"{amount} ¥ {mode} qo'shildi.")
            context.user_data["mode"] = None
        except ValueError:
            await update.message.reply_text("Faqat raqam kiriting.")
        else:
            await update.message.reply_text("Menyudan biror amalni tanlang.")

    elif text == "🗑Tarixni o'chirish":
         file_path = get_user_file(user_id)
         if os.path.exists(file_path):
            os.remove(file_path)
            await update.message.reply_text("Tarix tozalandi.")
    else:
        await update.message.reply_text("Hech qanday yozuv yo'q edi.")


# --- Botni ishga tushirish ---
async def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    print("Bot ishga tushdi...")
    await app.run_polling()

if __name__ == "__main__":
    import asyncio
    try: 
        asyncio.run(main())
    except RuntimeError:
        import nest_asyncio 
        nest_asyncio.apply()
        loop = asyncio.get_event_loop()
        loop.run_until_complete(main())
