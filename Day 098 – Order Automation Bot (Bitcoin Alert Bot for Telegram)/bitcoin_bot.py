import time, threading, requests
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import *

TOKEN = "BOT TOKEN HERE"
alerts = {}
CHOOSING, PRICE = range(2)

def btc_price():
    try:
        url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd"
        return requests.get(url, timeout=10).json()["bitcoin"]["usd"]
    except Exception:
        return None

async def start(update, context):
    await update.message.reply_text(
        "🤖 Bitcoin Alert Bot\n\n"
        "/price - current BTC price\n"
        "/alert - set alert\n"
        "/my_alerts - view alerts"
    )

async def price(update, context):
    p = btc_price()
    await update.message.reply_text(
        f"💰 BTC Price: ${p:,.2f}" if p else "❌ Could not fetch price"
    )

async def alert(update, context):
    kb = [["Above"], ["Below"], ["Cancel"]]
    await update.message.reply_text(
        "Choose alert type:",
        reply_markup=ReplyKeyboardMarkup(kb, one_time_keyboard=True)
    )
    return CHOOSING

async def choose(update, context):
    text = update.message.text.lower()
    if text == "cancel":
        await update.message.reply_text("Cancelled", reply_markup=ReplyKeyboardRemove())
        return ConversationHandler.END
    if text not in ["above", "below"]:
        await update.message.reply_text("Type Above or Below")
        return CHOOSING
    context.user_data["type"] = text
    await update.message.reply_text("Enter target price:", reply_markup=ReplyKeyboardRemove())
    return PRICE

async def save(update, context):
    try:
        target = float(update.message.text)
        uid = update.effective_user.id
        typ = context.user_data["type"]
        alerts.setdefault(uid, []).append({"type": typ, "price": target})
        await update.message.reply_text(f"✅ Alert set: {typ.title()} ${target:,.2f}")
        return ConversationHandler.END
    except:
        await update.message.reply_text("Enter a valid number")
        return PRICE

async def my_alerts(update, context):
    uid = update.effective_user.id
    if uid not in alerts or not alerts[uid]:
        await update.message.reply_text("No alerts set. Use /alert")
        return
    msg = "\n".join(
        f"{i+1}. {a['type'].title()} ${a['price']:,.2f}"
        for i, a in enumerate(alerts[uid])
    )
    await update.message.reply_text("📋 Your alerts:\n" + msg)

def send_msg(uid, text):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    requests.post(url, json={"chat_id": uid, "text": text})

def monitor():
    while True:
        p = btc_price()
        if p:
            for uid, user_alerts in list(alerts.items()):
                for a in user_alerts[:]:
                    hit = a["type"] == "above" and p >= a["price"] or a["type"] == "below" and p <= a["price"]
                    if hit:
                        send_msg(uid, f"🚨 BTC Alert!\nCurrent: ${p:,.2f}\nTarget: {a['type'].title()} ${a['price']:,.2f}")
                        user_alerts.remove(a)
        time.sleep(30)

def main():
    app = Application.builder().token(TOKEN).build()

    conv = ConversationHandler(
        entry_points=[CommandHandler("alert", alert)],
        states={
            CHOOSING: [MessageHandler(filters.TEXT & ~filters.COMMAND, choose)],
            PRICE: [MessageHandler(filters.TEXT & ~filters.COMMAND, save)],
        },
        fallbacks=[]
    )

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("price", price))
    app.add_handler(CommandHandler("my_alerts", my_alerts))
    app.add_handler(conv)

    threading.Thread(target=monitor, daemon=True).start()
    app.run_polling()

if __name__ == "__main__":
    main()
