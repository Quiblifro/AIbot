from aiogram import types, F, Router
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from states import MenuState
from gptcontact import get_task
from callbacks import CallbackFactory
import requests
import asyncio
import kb
router = Router()


#starter
@router.message(Command("start"))
async def start_handler(msg: Message, state : FSMContext):
    await state.clear()
    await msg.answer('Привет, программист! Я подготовил для тебя несколько задач, но также ты можешь сгенерировать задачу нейросетью:', reply_markup=kb.problem_menu)
    await state.set_state(MenuState.isgenerated)


@router.message(MenuState.isgenerated)
async def isgenerated_handler(msg: Message, state : FSMContext):
    if msg.text == "🤖 Сгенерировать задачу":
        await state.update_data(isgenerated=True)
    elif msg.text == "📁 Взять задачу из архива":
        await state.update_data(isgenerated=False)
    await msg.answer(f'🧠 Какой уровень знаний у тебя в python?', reply_markup=kb.level_menu)
    await state.set_state(MenuState.level)


@router.message(MenuState.level)
async def level_handler(msg: Message, state : FSMContext):
    if msg.text == "🔰 Just started":
        await state.update_data(level=1)
        await state.update_data(theme=['none'])
    elif msg.text == "📕 Junior":
        await state.update_data(level=2)
        await state.update_data(theme=['none'])
    elif msg.text == "👔 Middle":
        await state.update_data(level=3)
        await state.update_data(theme=['none'])
    elif msg.text == "🎩 Senior":
        await state.update_data(level=4)
        await state.update_data(theme=['none'])
    elif msg.text == "🔙":
        await start_handler(msg, state)
    data = await state.get_data()
    if data:
        level = data.get("level")
        await msg.answer(get_task(level), reply_markup=kb.problem_nav())
    
@router.callback_query(CallbackFactory.filter(F.action == "next"))
async def next_task(query: types.CallbackQuery, callback_data: CallbackFactory, state: FSMContext):
    print("я работать")
    data = await state.get_data()
    level = data.get("level")
    await query.message.edit_text(get_task(level), reply_markup=kb.problem_nav())

@router.callback_query(CallbackFactory.filter(F.action == "stop"))
async def next_task(query: types.CallbackQuery, callback_data: CallbackFactory, state: FSMContext):
    print("я работать")    
    await start_handler(query.message, state)
    


    

#get_task




    



#