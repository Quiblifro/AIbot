from aiogram import types, F, Router
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from states import MenuState
from gptcontact import get
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
    if msg.text == "🔰Just started":
        await state.update_data(level=1)
    elif msg.text == "📕 Junior":
        await state.update_data(level=2)
    elif msg.text == "👔 Middle":
        await state.update_data(level=3)
    elif msg.text == "🎩 Senior":
        await state.update_data(level=4)








@router.message(F.text == "📁 Взять задачу из архива")
async def get_1(msg: Message, state : FSMContext):
    ...



    



#