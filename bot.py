from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, CallbackQueryHandler, ContextTypes, filters

TOKEN = "7762921178:AAFyQTYd3ZUTfpYVNeRHEdiwHaLMuflL2S0"

# Mensaje multilanguage
def get_mensaje(idioma='es'):
    if idioma == 'en':
        return (
            "📊 *Access to 7 Exclusive Picks*\n"
            "Minimum odds of 1.58 with high probability.\n"
            "Get your predictions now!\n\n"
            "ℹ️ *Frequently Asked Questions*\n\n"
            "*Are they 100% safe?*\n"
            "No prediction is 100% guaranteed, but what you get is highly probable using my verified method. "
            "Check my results at [www.sureyh.com](https://www.sureyh.com).\n\n"
            "*How much should I bet?*\n"
            "I recommend betting the same amount on each pick to balance wins and losses mathematically. Stay consistent!\n\n"
            "*How to pay?*\n"
            "You can pay via PayPal or credit card. Contact me below for the payment link.\n\n"
            "📩 *Ready to pay?* Message @yh043 and I'll send you the custom payment link."
        )
    else:
        return (
            "📊 *Acceso a 7 Picks Exclusivos*\n"
            "Cuotas mínimas de 1.58 altamente probables.\n"
            "¡Consigue tus pronósticos ahora!\n\n"
            "ℹ️ *Preguntas Frecuentes*\n\n"
            "*¿Son 100% seguros?*\n"
            "Ningún pronóstico en el mundo es 100% seguro, pero lo que obtienes tiene probabilidades altísimas. "
            "Usan mi método verificado, consulta mi histórico en [www.sureyh.com](https://www.sureyh.com).\n\n"
            "*¿Cuánto apuesto?*\n"
            "Mi recomendación es que apuestes la misma cantidad en cada pick. Así, matemáticamente ganarás en proporción a lo que puedas llegar a perder. "
            "Apuesta con cabeza. Por ejemplo, si apuestas $100 por pick, no tendría sentido después perder $500 apostando más en otro pick. ¡Mantén tu estrategia constante!\n\n"
            "*¿Cómo pagar?*\n"
            "Al ingresar al enlace, aunque es PayPal (si deseas puedes pagar por PayPal), también encuentras la opción de pagar con tarjeta si te es más cómodo.\n\n"
            "📩 *¿Listo para pagar?* Manda mensaje a @yh043 y te enviaré la liga de pago personalizada."
        )

# Paso 1: Mostrar botones de inicio
async def inicio(update: Update, context: ContextTypes.DEFAULT_TYPE):
    botones = InlineKeyboardMarkup([
        [InlineKeyboardButton("📥 Obtener información sobre los 7 picks", callback_data="info")],
        [InlineKeyboardButton("💳 Solicitar liga de pago", url="https://t.me/yh043?text=Hola,%20me%20interesa%20me%20puedes%20enviar%20mi%20liga%20de%20pago")],
        [InlineKeyboardButton("📈 Ver historial", url="https://sureyh.com/historial")]
    ])
    await update.message.reply_text("Selecciona una opción:", reply_markup=botones)

# Paso 2: Mostrar información completa
async def mostrar_info(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    idioma = query.from_user.language_code or 'es'
    mensaje = get_mensaje(idioma)

    await query.message.reply_text(mensaje, parse_mode="Markdown")

# Configuración del bot
app = ApplicationBuilder().token(TOKEN).build()

# Handlers
app.add_handler(CommandHandler("start", inicio))
app.add_handler(CommandHandler("ayuda", inicio))
app.add_handler(MessageHandler(filters.TEXT, inicio))
app.add_handler(CallbackQueryHandler(mostrar_info, pattern="^info$"))

print("Bot encendido... Esperando mensajes")
app.run_polling()
