import os
import asyncio
from datetime import datetime, timedelta
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, MessageHandler, filters, ContextTypes

# ==================== CONFIGURATION ====================
BOT_TOKEN = "8638835983:AAF7G-AnoysedavWMFMZXiganIPhrwlPj2w"
ADMIN_ID = 5608509069
ADMIN_USERNAME = "bigbuddy07"
UPI_ID = "bigbuddy7@ptyes"
QR_FILE = "qr_default.jpg"

GROUP_CHAT_ID = "-1003641618077"
DEMO_GROUP = "https://t.me/+i3GelbzdjggyMWY1"
FREE_CONTENT = "https://t.me/+JE1Wv1kqJFVhNzM9"
COURSES_GROUP = "https://t.me/+gAGt6pZNOldiNGZl"
YOUTUBE = "https://youtube.com/@dhurvrathimasterclass"

# ==================== MESSAGE IDs ====================
MESSAGE_IDS = {
    "ai_tools_demo": 4, "courses_demo": 2, "softwares_demo": 3,
    "editing_demo": 5, "data_extractor_demo": 5, "whatsapp_demo": 5,
    "marketing_demo": 5, "billing_demo": 5, "pro_software_demo": 5,
    "hacking_demo": 5, "ai_bots_demo": 5, "habit_demo": 6,
    "digital_demo": 10, "hack_mod_demo": 22,
}

# ==================== DATA ====================
AI_BOTS = {
    "Digital Marketing Guru": "https://chatgpt.com/g/g-68ca4ae11ad48191b87b97b164cea9d8-dimarko",
    "Ad Creative Bot": "https://chatgpt.com/g/g-68ca4d8512048191ac93522aa6685f4f-ad-creative-bot",
    "Campaign Analyzer": "https://chatgpt.com/g/g-68ca4e44235c819192830e9888391721-campaign-analyzer-bot",
    "Social Media Planner": "https://chatgpt.com/g/g-68ca4e5f003c81919ca56b5ba2cb152a-social-media-planner-bot",
    "Email Marketing Bot": "https://chatgpt.com/g/g-68ca4e676cd08191863fc7ad01e99715-email-marketing-bot",
    "SEO Content Bot": "https://chatgpt.com/g/g-68ca4e7c58a88191a97b61fc1f22d835-seo-content-bot",
    "Brand Voice Bot": "https://chatgpt.com/g/g-68ca50a635d08191b36682ffe87614c6-brand-voice-bot",
    "Landing Page Copy": "https://chatgpt.com/g/g-68ca50d51ec481918d3dafdb099150de-landing-page-copy-bot",
    "Engagement Booster": "https://chatgpt.com/g/g-68ca50fe95ac8191804dd805977777c4-engagement-booster-bot",
    "Blog Writer Bot": "https://chatgpt.com/g/g-68ca518fcaf481919a48c5b7624c582b-blog-writer-bot",
    "Sales Script Bot": "https://chatgpt.com/g/g-68ca52de80b88191b9d41d9bfd5ba3b7-sales-script-bot",
    "Objection Handler": "https://chatgpt.com/g/g-68ca52dd1920819191ae89dc33e863c7-objection-handler-bot",
    "Content Repurposer": "https://chatgpt.com/g/g-68ca51499b908191a4fad0433165ef54-content-repurposer-bot",
    "Funnel Builder": "https://chatgpt.com/g/g-68ca52dfbc0c819185353a103c750cc8-funnel-builder-bot",
    "Client Onboarding": "https://chatgpt.com/g/g-68ca52e0404c8191ad0e51b184dd7558-client-onboarding-bot",
    "Testimonial Collector": "https://chatgpt.com/g/g-68ca52e0f5c08191bb4b5e4b42b319b9-testimonial-collector-bot",
    "Pricing Strategy": "https://chatgpt.com/g/g-68ca52e19e2481918f4b47ebdb0079af-pricing-strategy-bot",
    "Customer Support": "https://chatgpt.com/g/g-68ca52e208148191b3ea59a68c0d6002-customer-support-bot",
    "Presentation Maker": "https://chatgpt.com/g/g-68ca52e27da88191951798532c781264-presentation-maker-bot",
    "Ad Budget Planner": "https://chatgpt.com/g/g-68ca52e0f5c08191bb4b5e4b42b319b9-testimonial-collector-bot",
    "Copy Polisher": "https://chatgpt.com/g/g-68ca52e37d5c81918f327a9c542a36bc-copy-polisher-bot",
    "Webinar Script": "https://chatgpt.com/g/g-68ca551507d8819198006d6c554eb659-webinar-script-bot",
    "Lead Magnet": "https://chatgpt.com/g/g-68ca551639f4819186f85596237d6335-lead-magnet-bot",
    "Upsell Cross-sell": "https://chatgpt.com/g/g-68ca55162d848191b5f7249fd32387c8-upsell-and-cross-sell-bot",
    "Influencer Outreach": "https://chatgpt.com/g/g-68ca55162a30819199b5fe73e0eaffc0-influencer-outreach-bot",
    "Analytics Tracker": "https://chatgpt.com/g/g-68ca551463d48191bda3dc3a9903fb04-analytics-tracking-bot",
    "Cold Email Bot": "https://chatgpt.com/g/g-68ca565355808191b111976ad9fe7ed9-cold-email-bot",
    "Video Script Bot": "https://chatgpt.com/g/g-68ca5653dacc8191918dd7d4fca9871a-video-script-bot",
    "Offer Builder": "https://chatgpt.com/g/g-68ca565497e881919410a4a38bd92fbd-offer-builder-bot",
    "Course Creator": "https://chatgpt.com/g/g-68ca565493908191923f892195225ceb-course-creator-bot",
}

EDITING_SOFTWARE = {"Final Cut Pro": 299, "Adobe Collection": 699, "Filmora": 299, "DaVinci Resolve": 299,
    "Figma": 299, "Blender": 299, "CapCut Pro": 299, "Canva Pro": 299, "OBS Studio": 299, "CorelDraw": 299}
DATA_EXTRACTOR = {"Google Map Extractor": 199, "Facebook Scrapper": 199, "Justdial Extractor": 199,
    "Bing Data Scrapper": 199, "Trade India Extractor": 199, "India Mart Data": 199, "Zuba Scrapper": 199}
WHATSAPP_TOOLS = {"WhatsApp New AI CRM": 149, "Leadvave": 149, "WaCRM": 149, "WhatBotPlus": 149,
    "Simple Sender": 149, "Wa Filter": 149, "Wa Hammer": 149, "Wa Defender": 149, "Wa Engager": 149, "Bulk Sender": 149}
MARKETING_TOOLS = {"Social Media Auto Poster": 249, "64+ Marketing Tools": 249, "Facebook Audience Blaster": 249, "DRPU Bulk SMS": 249}
PRO_SOFTWARE = ["Bot Master", "Insta Bot Pro", "Twit Bot Pro", "WS Tool", "Spider Annucci", "Euro Pages", "Tex Sender", "Tik Tok Bot", "SMS Blaster"]
HACKING_TOOLS = {"Mobihook": 299, "Craxrat": 299, "Batch Wifi Brut Forcer": 299, "Wifi Cracker Apk": 299,
    "iG Tools": 299, "Chrome Profile Generator": 299, "Backlink Pro": 299, "iMobile Droidkit": 299, "Voice Changer": 299, "Auto Sender": 299}
HABIT_TRACKERS = {"Solo Leveling Tracker": 199, "Daily Habit Booster": 199, "Monthly Tracker": 199, "Goal Planner": 199}
DIGITAL_PRODUCTS = {"13000+ Digital Products": 199, "Mega Bundle": 199, "PB Bundle": 199, "4 TB Bundle": 199,
    "140 Crore Database": 199, "Boost Bundle": 199, "90 Top Courses": 199}

# ==================== STORAGE ====================
user_access = {}
pending_payments = {}
awaiting_screenshot = {}

# ==================== FORWARD DEMO ====================
async def forward_demo(update: Update, context: ContextTypes.DEFAULT_TYPE, demo_key: str):
    query = update.callback_query
    await query.answer()
    message_id = MESSAGE_IDS.get(demo_key, 0)
    if message_id and message_id > 0:
        try:
            await context.bot.forward_message(chat_id=update.effective_chat.id, from_chat_id=GROUP_CHAT_ID, message_id=message_id)
        except:
            await query.message.reply_text(f"Demo video unavailable.\nWatch demo in group:\n{DEMO_GROUP}")
    else:
        await query.message.reply_text(f"Demo Video\n\nWatch demo in group:\n{DEMO_GROUP}")

# ==================== PAYMENT FUNCTIONS ====================
async def send_qr_and_payment(update: Update, context: ContextTypes.DEFAULT_TYPE, item: str, price: int, user_message: str, access_type: str = None, access_value: str = None):
    query = update.callback_query
    user_id = update.effective_user.id
    user_name = update.effective_user.first_name
    user_username = update.effective_user.username or "No username"
    
    pending_payments[user_id] = {
        "item": item, "price": price, "message": user_message,
        "access_type": access_type, "access_value": access_value,
        "user_name": user_name, "user_username": user_username
    }
    asyncio.create_task(payment_timer(user_id))
    
    caption = f"💳 PAYMENT REQUIRED\n\n📦 Item: {item}\n💰 Amount: ₹{price}\n\n🔹 UPI ID: {UPI_ID}\n🔹 Pay to: Sonu\n\n⏰ Timer: 2 minutes\n\nAfter payment, click 'Payment Done'"
    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("✅ Payment Done", callback_data=f"done_{item}_{price}")],
        [InlineKeyboardButton("❌ Cancel", callback_data="main_menu")]
    ])
    
    if os.path.exists(QR_FILE):
        with open(QR_FILE, 'rb') as qr:
            await query.message.reply_photo(photo=qr, caption=caption, reply_markup=keyboard)
    else:
        await query.message.reply_text(caption, reply_markup=keyboard)

async def payment_timer(user_id: int):
    await asyncio.sleep(120)
    if user_id in pending_payments:
        del pending_payments[user_id]

async def payment_done(update: Update, context: ContextTypes.DEFAULT_TYPE, item: str, price: int):
    query = update.callback_query
    user_id = update.effective_user.id
    
    if user_id not in pending_payments:
        await query.message.reply_text("Session expired. Please start again.")
        return
    
    payment_info = pending_payments[user_id]
    awaiting_screenshot[user_id] = {
        "item": item, "price": price, "message": payment_info.get("message", ""),
        "access_type": payment_info.get("access_type"), "access_value": payment_info.get("access_value"),
        "user_name": payment_info.get("user_name"), "user_username": payment_info.get("user_username")
    }
    del pending_payments[user_id]
    await query.message.reply_text(f"📸 SUBMIT SCREENSHOT\n\nSend screenshot of ₹{price} payment for {item}.\n\nAdmin will verify.\n\nContact @{ADMIN_USERNAME}")

async def handle_screenshot(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    if user_id not in awaiting_screenshot:
        await update.message.reply_text("No pending payment.")
        return
    if not update.message.photo:
        await update.message.reply_text("Please send a screenshot image.")
        return
    
    info = awaiting_screenshot[user_id]
    photo = update.message.photo[-1]
    file = await context.bot.get_file(photo.file_id)
    
    # Show user details properly to admin
    user_display = f"@{info['user_username']}" if info['user_username'] != "No username" else f"{info['user_name']}"
    
    caption = f"🔔 NEW PAYMENT VERIFICATION\n\n"
    caption += f"👤 User: {user_display}\n"
    caption += f"🆔 User ID: {user_id}\n"
    caption += f"📦 Item: {info['item']}\n"
    caption += f"💰 Amount: ₹{info['price']}\n"
    caption += f"📅 Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n"
    caption += f"Click Approve to grant access, then DM the user."
    
    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("✅ Approve & Notify User", callback_data=f"approve_{user_id}_{info['item']}")],
        [InlineKeyboardButton("❌ Reject", callback_data=f"reject_{user_id}")]
    ])
    
    await context.bot.send_photo(chat_id=ADMIN_ID, photo=file.file_id, caption=caption, reply_markup=keyboard)
    del awaiting_screenshot[user_id]
    await update.message.reply_text("✅ Screenshot submitted! Admin will verify and contact you.")

async def approve_payment(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    
    parts = query.data.split("_")
    user_id = int(parts[1])
    item = "_".join(parts[2:])
    
    # Get user info from the message or store it
    await query.message.reply_text(f"✅ APPROVED!\n\nUser ID: {user_id}\nItem: {item}\n\nNow DM this user with access details.")
    
    # Send approval message to user and redirect to admin
    await context.bot.send_message(
        chat_id=user_id,
        text=f"✅ PAYMENT APPROVED!\n\nYour payment for '{item}' has been verified and approved.\n\n📌 Please contact admin @{ADMIN_USERNAME} to receive your access details.\n\nThank you for your purchase! 🎉"
    )
    
    # Send user details to admin for easy contact
    await context.bot.send_message(
        chat_id=ADMIN_ID,
        text=f"📌 USER TO CONTACT\n\nUser ID: {user_id}\nPurchased: {item}\n\nClick to message: tg://user?id={user_id}\n\nPlease DM them the access details."
    )

async def reject_payment(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    user_id = int(query.data.split("_")[1])
    await query.message.reply_text(f"❌ REJECTED for user {user_id}")
    await context.bot.send_message(chat_id=user_id, text="❌ PAYMENT REJECTED!\n\nYour payment could not be verified.\nPlease contact @{ADMIN_USERNAME} for assistance.")

# ==================== MENU FUNCTIONS ====================
def get_main_menu():
    keyboard = [
        [InlineKeyboardButton("🌟 ALL ACCESS - ₹1999", callback_data="all_access")],
        [InlineKeyboardButton("🤖 100 AI TOOLS", callback_data="menu_ai_tools_100")],
        [InlineKeyboardButton("🤖 30 AI MONEY BOTS", callback_data="menu_ai_bots")],
        [InlineKeyboardButton("📚 10K COURSES", callback_data="menu_courses")],
        [InlineKeyboardButton("💻 SOFTWARES", callback_data="menu_softwares")],
        [InlineKeyboardButton("📊 HABIT TRACKER", callback_data="menu_habit")],
        [InlineKeyboardButton("📦 DIGITAL PRODUCTS", callback_data="menu_digital")],
        [InlineKeyboardButton("🔓 HACK MOD APPS", callback_data="menu_hacking")],
        [InlineKeyboardButton("🎁 MAKE COMBO BUNDLE", callback_data="combo_bundle")],
        [InlineKeyboardButton("👥 DEMO GROUP", url=DEMO_GROUP)],
        [InlineKeyboardButton("🎁 FREE CONTENT", callback_data="free_content")],
        [InlineKeyboardButton("ℹ️ YOU WANT INFO ME", callback_data="want_info")],
        [InlineKeyboardButton("🆘 SUPPORT", callback_data="support")],
    ]
    return InlineKeyboardMarkup(keyboard)

# ==================== MAIN HANDLERS ====================
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🌟 WELCOME TO BIG BUDDY WORLD 🌟\n\nSelect an option below:",
        reply_markup=get_main_menu()
    )

async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    data = query.data
    await query.answer()
    
    if data == "main_menu":
        await query.message.reply_text("Main Menu:", reply_markup=get_main_menu())
    
    elif data == "all_access":
        await send_qr_and_payment(update, context, "ALL ACCESS BUNDLE", 1999, "Give me ALL ACCESS", "all_access", "all")
    
    # 100 AI TOOLS
    elif data == "menu_ai_tools_100":
        keyboard = [
            [InlineKeyboardButton("🎥 Demo Video", callback_data="demo_ai_tools")],
            [InlineKeyboardButton("📅 1 Month - ₹99", callback_data="pay_100ai_1m")],
            [InlineKeyboardButton("📅 6 Months - ₹199", callback_data="pay_100ai_6m")],
            [InlineKeyboardButton("📅 1 Year - ₹399", callback_data="pay_100ai_1y")],
            [InlineKeyboardButton("♾️ Lifetime - ₹499", callback_data="pay_100ai_life")],
            [InlineKeyboardButton("🔙 Main Menu", callback_data="main_menu")],
        ]
        await query.message.reply_text("🤖 100 AI TOOLS\n\nChoose validity:", reply_markup=InlineKeyboardMarkup(keyboard))
    
    elif data.startswith("pay_100ai_"):
        validity = data.split("_")[2]
        price = 99 if validity == "1m" else 199 if validity == "6m" else 399 if validity == "1y" else 499
        await send_qr_and_payment(update, context, f"100 AI Tools", price, "Give me 100 AI Tools access", "ai_tools_100", validity)
    
    # 30 AI BOTS
    elif data == "menu_ai_bots":
        keyboard = [[InlineKeyboardButton("🤖 Demo Video", callback_data="demo_ai_bots")],
                    [InlineKeyboardButton("🤖 All 30 AI Bots - ₹399", callback_data="buy_all_ai_bots")]]
        for bot in list(AI_BOTS.keys())[:15]:
            keyboard.append([InlineKeyboardButton(f"🤖 {bot[:20]} - ₹49", callback_data=f"buy_ai_bot_{bot}")])
        keyboard.append([InlineKeyboardButton("📋 More Bots", callback_data="ai_bots_more")])
        keyboard.append([InlineKeyboardButton("🔙 Main Menu", callback_data="main_menu")])
        await query.message.reply_text("🤖 30 AI MONEY BOTS\n\nAll Bots: ₹399\nIndividual: ₹49", reply_markup=InlineKeyboardMarkup(keyboard))
    
    elif data == "ai_bots_more":
        keyboard = []
        for bot in list(AI_BOTS.keys())[15:30]:
            keyboard.append([InlineKeyboardButton(f"🤖 {bot[:20]} - ₹49", callback_data=f"buy_ai_bot_{bot}")])
        keyboard.append([InlineKeyboardButton("🔙 Back", callback_data="menu_ai_bots")])
        await query.message.reply_text("🤖 More AI Bots", reply_markup=InlineKeyboardMarkup(keyboard))
    
    elif data == "buy_all_ai_bots":
        await send_qr_and_payment(update, context, "All 30 AI Bots", 399, "Give me All AI Bots access", "ai_bot", "all")
    
    elif data.startswith("buy_ai_bot_"):
        bot = data.replace("buy_ai_bot_", "")
        await send_qr_and_payment(update, context, bot, 49, f"Give me {bot} access", "ai_bot", bot)
    
    # COURSES
    elif data == "menu_courses":
        keyboard = [
            [InlineKeyboardButton("🎥 Demo Video", callback_data="demo_courses")],
            [InlineKeyboardButton("📅 1 Month - ₹499", callback_data="pay_courses_1m")],
            [InlineKeyboardButton("📅 6 Months - ₹599", callback_data="pay_courses_6m")],
            [InlineKeyboardButton("♾️ Lifetime - ₹999", callback_data="pay_courses_life")],
            [InlineKeyboardButton("📚 Courses List Group", url=COURSES_GROUP)],
            [InlineKeyboardButton("🔙 Main Menu", callback_data="main_menu")],
        ]
        await query.message.reply_text("📚 10K COURSES\n\nChoose validity:", reply_markup=InlineKeyboardMarkup(keyboard))
    
    elif data.startswith("pay_courses_"):
        validity = data.split("_")[2]
        price = 499 if validity == "1m" else 599 if validity == "6m" else 999
        await send_qr_and_payment(update, context, f"10K Courses", price, "Give me Courses access", "courses", validity)
    
    # SOFTWARES MAIN MENU
    elif data == "menu_softwares":
        keyboard = [
            [InlineKeyboardButton("🎥 Demo Video", callback_data="demo_softwares")],
            [InlineKeyboardButton("🎬 Editing Software", callback_data="sub_editing")],
            [InlineKeyboardButton("📊 Data Extractor", callback_data="sub_data_extractor")],
            [InlineKeyboardButton("💬 WhatsApp API", callback_data="sub_whatsapp")],
            [InlineKeyboardButton("📢 Marketing Tools", callback_data="sub_marketing")],
            [InlineKeyboardButton("💰 Billing Software", callback_data="sub_billing")],
            [InlineKeyboardButton("🔧 Pro Software", callback_data="sub_pro")],
            [InlineKeyboardButton("🔓 Hacking Tools", callback_data="sub_hacking")],
            [InlineKeyboardButton("🔙 Main Menu", callback_data="main_menu")],
        ]
        await query.message.reply_text("💻 SOFTWARES\n\nChoose category:", reply_markup=InlineKeyboardMarkup(keyboard))
    
    # EDITING SOFTWARE
    elif data == "sub_editing":
        keyboard = [[InlineKeyboardButton("🎬 Demo Video", callback_data="demo_editing")],
                    [InlineKeyboardButton("🎬 All Software Combo - ₹1299", callback_data="buy_all_editing")]]
        for sw, price in EDITING_SOFTWARE.items():
            keyboard.append([InlineKeyboardButton(f"🎬 {sw} - ₹{price}", callback_data=f"buy_edit_{sw}")])
        keyboard.append([InlineKeyboardButton("🔙 Back", callback_data="menu_softwares")])
        await query.message.reply_text("🎬 EDITING SOFTWARE\n\nSelect:", reply_markup=InlineKeyboardMarkup(keyboard))
    
    elif data == "buy_all_editing":
        await send_qr_and_payment(update, context, "All Editing Software", 1299, "Give me All Editing Software access", "editing", "all")
    
    elif data.startswith("buy_edit_"):
        sw = data.replace("buy_edit_", "")
        price = EDITING_SOFTWARE.get(sw, 299)
        await send_qr_and_payment(update, context, sw, price, f"Give me {sw} access", "editing", sw)
    
    # DATA EXTRACTOR
    elif data == "sub_data_extractor":
        keyboard = [[InlineKeyboardButton("📊 Demo Video", callback_data="demo_data")]]
        for tool, price in DATA_EXTRACTOR.items():
            keyboard.append([InlineKeyboardButton(f"📊 {tool} - ₹{price}", callback_data=f"buy_data_{tool}")])
        keyboard.append([InlineKeyboardButton("🔙 Back", callback_data="menu_softwares")])
        await query.message.reply_text("📊 DATA EXTRACTOR - ₹199 each", reply_markup=InlineKeyboardMarkup(keyboard))
    
    elif data.startswith("buy_data_"):
        tool = data.replace("buy_data_", "")
        await send_qr_and_payment(update, context, tool, 199, f"Give me {tool} access", "data", tool)
    
    # WHATSAPP API
    elif data == "sub_whatsapp":
        keyboard = [[InlineKeyboardButton("💬 Demo Video", callback_data="demo_whatsapp")],
                    [InlineKeyboardButton("💬 All WhatsApp Tools - ₹999", callback_data="buy_all_whatsapp")]]
        for tool, price in WHATSAPP_TOOLS.items():
            keyboard.append([InlineKeyboardButton(f"💬 {tool} - ₹{price}", callback_data=f"buy_wa_{tool}")])
        keyboard.append([InlineKeyboardButton("🔙 Back", callback_data="menu_softwares")])
        await query.message.reply_text("💬 WHATSAPP API\n\nAll Tools: ₹999\nIndividual: ₹149", reply_markup=InlineKeyboardMarkup(keyboard))
    
    elif data == "buy_all_whatsapp":
        await send_qr_and_payment(update, context, "All WhatsApp Tools", 999, "Give me All WhatsApp access", "whatsapp", "all")
    
    elif data.startswith("buy_wa_"):
        tool = data.replace("buy_wa_", "")
        await send_qr_and_payment(update, context, tool, 149, f"Give me {tool} access", "whatsapp", tool)
    
    # MARKETING TOOLS
    elif data == "sub_marketing":
        keyboard = [[InlineKeyboardButton("📢 Demo Video", callback_data="demo_marketing")],
                    [InlineKeyboardButton("📢 All Marketing Tools - ₹499", callback_data="buy_all_marketing")]]
        for tool, price in MARKETING_TOOLS.items():
            keyboard.append([InlineKeyboardButton(f"📢 {tool} - ₹{price}", callback_data=f"buy_mkt_{tool}")])
        keyboard.append([InlineKeyboardButton("🔙 Back", callback_data="menu_softwares")])
        await query.message.reply_text("📢 MARKETING TOOLS\n\nAll Tools: ₹499\nIndividual: ₹249", reply_markup=InlineKeyboardMarkup(keyboard))
    
    elif data == "buy_all_marketing":
        await send_qr_and_payment(update, context, "All Marketing Tools", 499, "Give me All Marketing access", "marketing", "all")
    
    elif data.startswith("buy_mkt_"):
        tool = data.replace("buy_mkt_", "")
        await send_qr_and_payment(update, context, tool, 249, f"Give me {tool} access", "marketing", tool)
    
    # BILLING SOFTWARE
    elif data == "sub_billing":
        keyboard = [
            [InlineKeyboardButton("💰 Demo Video", callback_data="demo_billing")],
            [InlineKeyboardButton("💰 Both Billing Software - ₹399", callback_data="buy_billing_both")],
            [InlineKeyboardButton("💰 POS Billing - ₹249", callback_data="buy_billing_pos")],
            [InlineKeyboardButton("💰 POS 2 Pro - ₹249", callback_data="buy_billing_pos2")],
            [InlineKeyboardButton("🔙 Back", callback_data="menu_softwares")],
        ]
        await query.message.reply_text("💰 BILLING SOFTWARE", reply_markup=InlineKeyboardMarkup(keyboard))
    
    elif data == "buy_billing_both":
        await send_qr_and_payment(update, context, "Both Billing Software", 399, "Give me Both Billing access", "billing", "both")
    elif data == "buy_billing_pos":
        await send_qr_and_payment(update, context, "POS Billing Software", 249, "Give me POS Billing access", "billing", "pos")
    elif data == "buy_billing_pos2":
        await send_qr_and_payment(update, context, "POS 2 Pro", 249, "Give me POS 2 Pro access", "billing", "pos2")
    
    # PRO SOFTWARE
    elif data == "sub_pro":
        keyboard = [[InlineKeyboardButton("🔧 Demo Video", callback_data="demo_pro")]]
        for sw in PRO_SOFTWARE:
            keyboard.append([InlineKeyboardButton(f"🔧 {sw} - ₹299", callback_data=f"buy_pro_{sw}")])
        keyboard.append([InlineKeyboardButton("🔙 Back", callback_data="menu_softwares")])
        await query.message.reply_text("🔧 PRO SOFTWARE - ₹299 each", reply_markup=InlineKeyboardMarkup(keyboard))
    
    elif data.startswith("buy_pro_"):
        sw = data.replace("buy_pro_", "")
        await send_qr_and_payment(update, context, sw, 299, f"Give me {sw} access", "pro", sw)
    
    # HACKING TOOLS
    elif data == "sub_hacking":
        keyboard = [[InlineKeyboardButton("🔓 Demo Video", callback_data="demo_hacking")],
                    [InlineKeyboardButton("🔓 All Hacking Tools - ₹699", callback_data="buy_all_hacking")]]
        for tool, price in HACKING_TOOLS.items():
            keyboard.append([InlineKeyboardButton(f"🔓 {tool} - ₹{price}", callback_data=f"buy_hack_{tool}")])
        keyboard.append([InlineKeyboardButton("🔙 Back", callback_data="menu_softwares")])
        await query.message.reply_text("🔓 HACKING TOOLS\n\nAll Tools: ₹699\nIndividual: ₹299", reply_markup=InlineKeyboardMarkup(keyboard))
    
    elif data == "buy_all_hacking":
        await send_qr_and_payment(update, context, "All Hacking Tools", 699, "Give me All Hacking access", "hacking", "all")
    
    elif data.startswith("buy_hack_"):
        tool = data.replace("buy_hack_", "")
        await send_qr_and_payment(update, context, tool, 299, f"Give me {tool} access", "hacking", tool)
    
    # HABIT TRACKER
    elif data == "menu_habit":
        keyboard = [[InlineKeyboardButton("📊 Demo Video", callback_data="demo_habit")],
                    [InlineKeyboardButton("📊 All Trackers - ₹399", callback_data="buy_all_habits")]]
        for tracker, price in HABIT_TRACKERS.items():
            keyboard.append([InlineKeyboardButton(f"📊 {tracker} - ₹{price}", callback_data=f"buy_habit_{tracker}")])
        keyboard.append([InlineKeyboardButton("🔙 Main Menu", callback_data="main_menu")])
        await query.message.reply_text("📊 HABIT TRACKER\n\nAll Trackers: ₹399\nIndividual: ₹199", reply_markup=InlineKeyboardMarkup(keyboard))
    
    elif data == "buy_all_habits":
        await send_qr_and_payment(update, context, "All Habit Trackers", 399, "Give me All Habit access", "habit", "all")
    
    elif data.startswith("buy_habit_"):
        tracker = data.replace("buy_habit_", "")
        await send_qr_and_payment(update, context, tracker, 199, f"Give me {tracker} access", "habit", tracker)
    
    # DIGITAL PRODUCTS
    elif data == "menu_digital":
        keyboard = [[InlineKeyboardButton("📦 Demo Video", callback_data="demo_digital")],
                    [InlineKeyboardButton("📦 All Digital Products - ₹499", callback_data="buy_all_digital")]]
        for product, price in DIGITAL_PRODUCTS.items():
            keyboard.append([InlineKeyboardButton(f"📦 {product} - ₹{price}", callback_data=f"buy_digital_{product}")])
        keyboard.append([InlineKeyboardButton("🔙 Main Menu", callback_data="main_menu")])
        await query.message.reply_text("📦 DIGITAL PRODUCTS\n\nAll Products: ₹499\nIndividual: ₹199", reply_markup=InlineKeyboardMarkup(keyboard))
    
    elif data == "buy_all_digital":
        await send_qr_and_payment(update, context, "All Digital Products", 499, "Give me All Digital access", "digital", "all")
    
    elif data.startswith("buy_digital_"):
        product = data.replace("buy_digital_", "")
        await send_qr_and_payment(update, context, product, 199, f"Give me {product} access", "digital", product)
    
    # HACK MOD APPS
    elif data == "menu_hacking":
        keyboard = [
            [InlineKeyboardButton("🔓 Demo Video", callback_data="demo_hack_mod")],
            [InlineKeyboardButton("🔓 Get Access - ₹299", callback_data="buy_hack_mod")],
            [InlineKeyboardButton("🔙 Main Menu", callback_data="main_menu")],
        ]
        await query.message.reply_text("🔓 HACK MOD APPS\n\nLifetime: ₹299", reply_markup=InlineKeyboardMarkup(keyboard))
    
    elif data == "buy_hack_mod":
        await send_qr_and_payment(update, context, "Hack Mod Apps", 299, "Give me Hack Mod access", "hack_mod", "all")
    
    # COMBO BUNDLE
    elif data == "combo_bundle":
        keyboard = [[InlineKeyboardButton("📞 Contact Admin", callback_data="contact_admin")]]
        await query.message.reply_text("🎁 MAKE COMBO BUNDLE\n\nMessage admin with your list for discount.", reply_markup=InlineKeyboardMarkup(keyboard))
    
    # FREE CONTENT
    elif data == "free_content":
        await query.message.reply_text(f"🎁 FREE CONTENT\n\n🔗 Join: {FREE_CONTENT}\n📺 YouTube: {YOUTUBE}")
    
    elif data == "want_info":
        keyboard = [[InlineKeyboardButton("📞 Contact Admin", callback_data="contact_admin")]]
        await query.message.reply_text("ℹ️ Need something not in bot? Contact admin.", reply_markup=InlineKeyboardMarkup(keyboard))
    
    elif data == "support":
        await query.message.reply_text(f"🆘 SUPPORT\n\n📞 Telegram: @{ADMIN_USERNAME}\n💬 WhatsApp: wa.me/9116300585")
    
    elif data == "contact_admin":
        await query.message.reply_text(f"📞 Contact Admin: @{ADMIN_USERNAME}")
    
    # DEMO VIDEOS
    elif data == "demo_ai_tools":
        await forward_demo(update, context, "ai_tools_demo")
    elif data == "demo_courses":
        await forward_demo(update, context, "courses_demo")
    elif data == "demo_softwares":
        await forward_demo(update, context, "softwares_demo")
    elif data == "demo_editing":
        await forward_demo(update, context, "editing_demo")
    elif data == "demo_data":
        await forward_demo(update, context, "data_extractor_demo")
    elif data == "demo_whatsapp":
        await forward_demo(update, context, "whatsapp_demo")
    elif data == "demo_marketing":
        await forward_demo(update, context, "marketing_demo")
    elif data == "demo_billing":
        await forward_demo(update, context, "billing_demo")
    elif data == "demo_pro":
        await forward_demo(update, context, "pro_software_demo")
    elif data == "demo_hacking":
        await forward_demo(update, context, "hacking_demo")
    elif data == "demo_ai_bots":
        await forward_demo(update, context, "ai_bots_demo")
    elif data == "demo_habit":
        await forward_demo(update, context, "habit_demo")
    elif data == "demo_digital":
        await forward_demo(update, context, "digital_demo")
    elif data == "demo_hack_mod":
        await forward_demo(update, context, "hack_mod_demo")
    
    # PAYMENT HANDLERS
    elif data.startswith("done_"):
        parts = data.split("_")
        item = "_".join(parts[1:-1])
        price = int(parts[-1])
        await payment_done(update, context, item, price)
    
    elif data.startswith("approve_"):
        await approve_payment(update, context)
    
    elif data.startswith("reject_"):
        await reject_payment(update, context)

# ==================== MAIN ====================
def main():
    print("=" * 60)
    print("🌟 BIG BUDDY WORLD BOT - FINAL")
    print("=" * 60)
    print(f"✅ UPI: {UPI_ID}")
    print(f"✅ QR: {QR_FILE}")
    print(f"✅ Admin: @{ADMIN_USERNAME}")
    print("=" * 60)
    print("Bot is running...")
    
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button_handler))
    app.add_handler(MessageHandler(filters.PHOTO, handle_screenshot))
    app.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == "__main__":
    main()