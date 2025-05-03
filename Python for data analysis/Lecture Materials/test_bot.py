from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, MessageHandler, filters, ContextTypes, ConversationHandler

TOKEN = 123 # берется из BotFather
user_tasks = {}


async def show_tasks(update, context, user_chat_id: int, delete=False, complete=False) -> None:
    if user_chat_id not in user_tasks:
        await update.message.reply_text("У вас еще нет задач.")
        return ConversationHandler.END
    
    tasks = user_tasks[user_chat_id]
    in_progress = [task for task in tasks if task['status'] == 'В процессе']
    completed = [task for task in tasks if task['status'] == 'Выполнено']

    if delete:
        tasks_list = "\n".join([f"{i + 1}: {task['text']}" for i, task in enumerate(in_progress)])
        await update.message.reply_text(f"Список задач:\n{tasks_list if tasks_list else 'Нет задач для удаления.'}")
        
        await update.message.reply_text("Выберите номер задачи для удаления:")
        context.user_data['action'] = 'delete'
    
    elif complete:
        tasks_list = "\n".join([f"{i + 1}: {task['text']}" for i, task in enumerate(in_progress)])
        await update.message.reply_text(f"Список задач в процессе:\n{tasks_list if tasks_list else 'Нет задач.'}")
        
        await update.message.reply_text("Выберите номер задачи для выполнения:")
        context.user_data['action'] = 'complete'
    else:
        tasks_in_progress = "\n".join([f"{i + 1}: {task['text']}" for i, task in enumerate(in_progress)])
        tasks_completed = "\n".join([f"{i + 1}: {task['text']}" for i, task in enumerate(completed)])
        
        await update.message.reply_text(
            text=f"Задачи в процессе:\n{tasks_in_progress if tasks_in_progress else 'Нет задач.'}\n\nЗадачи выполнены:\n{tasks_completed if tasks_completed else 'Нет задач.'}"
        )


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_chat_id = update.message.chat.id
    if user_chat_id not in user_tasks:
        user_tasks[user_chat_id] = []

    keyboard = [
        [InlineKeyboardButton("Все задачи", callback_data='all_tasks')],
        [InlineKeyboardButton("Добавить задачу", callback_data='add_task'), InlineKeyboardButton("Удалить задачу", callback_data='delete_task')],
        [InlineKeyboardButton("Выполнить задачу", callback_data='complete_task')]
    ]

    await update.message.reply_text(
        text="*Привет!* Я Ваш личный менеджер задач.\nВыберите действие:",
        reply_markup=InlineKeyboardMarkup(keyboard),
        parse_mode='Markdown'
    )
    

async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()

    user_chat_id = query.from_user.id

    if query.data == 'all_tasks':
        # что-то сделать, если была нажата именно кнопка 'all_tasks'
        await show_tasks(query, context, user_chat_id)
    elif query.data == 'add_task':
        # что-то сделать, если была нажата именно кнопка 'add_task'
        await query.edit_message_text("Введите текст задачи:")
        context.user_data['action'] = 'add'
    elif query.data == 'delete_task':
        await show_tasks(query, context, user_chat_id, delete=True)
    elif query.data == 'complete_task':
        await show_tasks(query, context, user_chat_id, complete=True)
    else:
        pass


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_chat_id = update.message.chat.id
    action = context.user_data.get('action')
    if action == 'add':
        task_text = update.message.text
        user_tasks[user_chat_id].append({'text': task_text, 'status': 'В процессе'})
        print(user_tasks)

        await update.message.reply_text("Задача добавлена.")
        context.user_data['action'] = None 
    elif action == 'delete':
        task_index = int(update.message.text) - 1
        if 0 <= task_index < len(user_tasks[user_chat_id]):
            user_tasks[user_chat_id].pop(task_index)
            await update.message.reply_text("Задача удалена.")
        else:
            await update.message.reply_text("Неверный номер задачи.")
        context.user_data['action'] = None
    elif action == 'complete':
        task_index = int(update.message.text) - 1
        if 0 <= task_index < len(user_tasks[user_chat_id]):
            user_tasks[user_chat_id][task_index]['status'] = 'Выполнено'
            await update.message.reply_text("Задача выполнена.")
        else:
            await update.message.reply_text("Неверный номер задачи.")
        context.user_data['action'] = None


def main() -> None:
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button_handler))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    app.run_polling()

if __name__ == '__main__':
    main()