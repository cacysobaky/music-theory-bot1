# -*- coding: utf8 -*-
import telebot
from telebot import types
from telebot.types import InlineKeyboardMarkup

bot = telebot.TeleBot('855299931:AAE31jofHPMcRX2SLfMOAHwURaW7kieQBuc')

@bot.message_handler(commands=['start'])
def start_message(message):
    # keyboard
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("/help")
    item2 = types.KeyboardButton("/circle")
    item3 = types.KeyboardButton('/key')
    item4 = types.KeyboardButton('/pent')
    item5 = types.KeyboardButton('/p_chords')
    item6 = types.KeyboardButton('/g_chords')
    item7 = types.KeyboardButton('/p_intervals')
    item8 = types.KeyboardButton('/g_intervals')
    item9 = types.KeyboardButton('/start')


    markup.add(item1, item2, item3, item4, item5, item6, item7, item8, item9)

    bot.send_message(message.chat.id,
                     'Оу, привет, <b>{0.first_name}</b>! Добро пожаловать!\n\nИспользуйте /help для получения списка команд.'.format(
                         message.from_user, bot.get_me()),
                     parse_mode='html', reply_markup=markup)

# /help
@bot.message_handler(commands=['help'])
def help1(message):
    bot.send_message(message.chat.id,
                     'Список команд:\n/circle - Кварто-квинтовый круг\n/key - Выберите тональность, которая Вам нужна 🎼\n/pent - Выберите пентатонику, которая Вам нужна 🎼\n/p_chords - Аппликатура аккодров для ПИАНИНО 🎹\n/p_interval - Аппликатура интервалов для ПИАНИНО 🎹\n/g_interval - Аппликатура интервалов для ГИТАРЫ 🎸\n/g_chords - Аппликатура аккодров для ГИТАРЫ 🎸(В РАЗРАБОТКЕ)')


# Кварто-квинтовый круг
@bot.message_handler(commands=['circle'])
def circle(message):
    bot.send_message(message.chat.id, 'Вот Кварто-квинтовый круг')
    ccircle = open('bot_files/circle.png', 'rb')
    bot.send_photo(message.chat.id, ccircle)
    ccircle.close()

@bot.message_handler(commands=['p_intervals'])
def p_intervals_rus(message):
    bot.send_message(message.chat.id, 'Вот аппликатура интервалов для Пианино 🎹')
    interv1 = open('bot_files/piano_intervals_rus.png', 'rb')
    interv2 = open('bot_files/piano_intervals.png', 'rb')
    bot.send_photo(message.chat.id, interv1)
    bot.send_photo(message.chat.id, interv2)
    interv1.close()
    interv2.close()


@bot.message_handler(commands=['g_intervals'])
def g_intervals_rus(message):
    bot.send_message(message.chat.id, 'Вот аппликатура интервалов для Гитары 🎸')
    interv3 = open('bot_files/guitar_intervals_rus.png', 'rb')
    bot.send_photo(message.chat.id, interv3)
    interv3.close()


# Тональности
@bot.message_handler(commands=['key'])
def key(message):
    keymarkup = types.InlineKeyboardMarkup(row_width=3)
    key1 = types.InlineKeyboardButton('A', callback_data='A')
    key2 = types.InlineKeyboardButton('A#/Bb', callback_data='A#')
    key3 = types.InlineKeyboardButton('B', callback_data='B')
    key4 = types.InlineKeyboardButton('C', callback_data='C')
    key5 = types.InlineKeyboardButton('C#/Db', callback_data='C#')
    key6 = types.InlineKeyboardButton('D', callback_data='D')
    key7 = types.InlineKeyboardButton('D#/Eb', callback_data='D#')
    key8 = types.InlineKeyboardButton('E', callback_data='E')
    key9 = types.InlineKeyboardButton('F', callback_data='F')
    key10 = types.InlineKeyboardButton('F#/Gb', callback_data='F#')
    key11 = types.InlineKeyboardButton('G', callback_data='G')
    key12 = types.InlineKeyboardButton('G#/Ab', callback_data='G#')

    keymarkup.add(key1, key2, key3, key4, key5, key6, key7, key8, key9, key10, key11, key12)

    bot.send_message(message.chat.id, 'Выберите тонику:', reply_markup=keymarkup)


@bot.message_handler(commands=['p_chords'])
def p_chords(message):
    chordsnotemarkup = types.InlineKeyboardMarkup(row_width=3)
    note1 = types.InlineKeyboardButton("A ", callback_data="Ap")
    note2 = types.InlineKeyboardButton("A#/Bb ", callback_data="A#p")
    note3 = types.InlineKeyboardButton("B ", callback_data="Bp")
    note4 = types.InlineKeyboardButton("C ", callback_data="Cp")
    note5 = types.InlineKeyboardButton("C#/Db ", callback_data="C#p")
    note6 = types.InlineKeyboardButton("D ", callback_data="Dp")
    note7 = types.InlineKeyboardButton("D#/Eb ", callback_data="D#p")
    note8 = types.InlineKeyboardButton("E ", callback_data="Ep")
    note9 = types.InlineKeyboardButton("F ", callback_data="Fp")
    note10 = types.InlineKeyboardButton("F#/Gb ", callback_data="F#p")
    note11 = types.InlineKeyboardButton("G ", callback_data="Gp")
    note12 = types.InlineKeyboardButton("G#/Ab ", callback_data="G#p")

    chordsnotemarkup.add(note1, note2, note3, note4, note5, note6, note7, note8, note9, note10, note11, note12)

    bot.send_message(message.chat.id, 'Выберите тонику аккорда:', reply_markup=chordsnotemarkup)

@bot.message_handler(commands=['pent'])
def pent_rus(message):
    pentmarkup = types.InlineKeyboardMarkup(row_width=3)
    pent1 = types.InlineKeyboardButton('A', callback_data='Apt')
    pent2 = types.InlineKeyboardButton('A#/Bb', callback_data='A#pt')
    pent3 = types.InlineKeyboardButton('B', callback_data='Bpt')
    pent4 = types.InlineKeyboardButton('C', callback_data='Cpt')
    pent5 = types.InlineKeyboardButton('C#/Db', callback_data='C#pt')
    pent6 = types.InlineKeyboardButton('D', callback_data='Dpt')
    pent7 = types.InlineKeyboardButton('D#/Eb', callback_data='D#pt')
    pent8 = types.InlineKeyboardButton('E', callback_data='Ept')
    pent9 = types.InlineKeyboardButton('F', callback_data='Fpt')
    pent10 = types.InlineKeyboardButton('F#/Gb', callback_data='F#pt')
    pent11 = types.InlineKeyboardButton('G', callback_data='Gpt')
    pent12 = types.InlineKeyboardButton('G#/Ab', callback_data='G#pt')

    pentmarkup.add(pent1, pent2, pent3, pent4, pent5, pent6, pent7, pent8, pent9, pent10, pent11, pent12)

    bot.send_message(message.chat.id, 'Выберите тонику:', reply_markup=pentmarkup)

# Функция выбора нот
# @bot.callback_query_handler()
@bot.callback_query_handler(func=lambda call: True)
def keys_callback(call):
    # Функция выбора нот ТОНАЛЬНОСТЕЙ и загрузки картинок
    def scales(note):

        if call.message:
            if call.data == note:
                bot.send_message(call.message.chat.id, f'Вы выбрали {note}')
                bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                                          text=f'Вы выбрали {note}')

                modemarkup: InlineKeyboardMarkup = types.InlineKeyboardMarkup(row_width=2)
                mode1 = types.InlineKeyboardButton("Major", callback_data=f"Major{note}")
                mode2 = types.InlineKeyboardButton("Minor", callback_data=f"Minor{note}")
                modemarkup.add(mode1, mode2)

                bot.send_message(call.message.chat.id, 'Выберите лад', reply_markup=modemarkup)

            if call.message:
                if call.data == f'Major{note}':
                    bot.send_message(call.message.chat.id, f'Вы выбрали {note} major')
                    bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                                              text=f'Вы выбрали {note} major')

                    majorK = open(f'bot_files/keys/Major/{note}.png', 'rb')

                    bot.send_photo(call.message.chat.id, majorK)
                    majorK.close()

            if call.message:
                if call.data == 'Minor' + note:
                    bot.send_message(call.message.chat.id, f'Вы выбрали {note} minor')
                    bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                                              text=f'Вы выбрали {note} minor')

                    minorK = open(f'bot_files/keys/Minor/{note}m.png', 'rb')

                    bot.send_photo(call.message.chat.id, minorK)
                    minorK.close()

    # Piano chords

    def chord(P_note):
        if call.message:
            if call.message:
                if call.data == f'{P_note}p':
                    bot.send_message(call.message.chat.id, f'Вы выбрали {P_note}')

                    bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                                              text=f"Вы выбрали {P_note}")

                    chordsmarkup = types.InlineKeyboardMarkup(row_width=3)

                    chord1 = types.InlineKeyboardButton(f"{P_note}", callback_data=f"{P_note}_major")
                    chord2 = types.InlineKeyboardButton(f"{P_note}m", callback_data=f"{P_note}_minor")
                    chord3 = types.InlineKeyboardButton(f"{P_note}5", callback_data=f"{P_note}5")
                    chord4 = types.InlineKeyboardButton(f"{P_note}6", callback_data=f"{P_note}6")
                    chord5 = types.InlineKeyboardButton(f"{P_note}6 add9", callback_data=f"{P_note}6_9")
                    chord6 = types.InlineKeyboardButton(f"{P_note}7", callback_data=f"{P_note}7")
                    chord7 = types.InlineKeyboardButton(f"{P_note} maj7", callback_data=f"{P_note}_maj7")
                    chord8 = types.InlineKeyboardButton(f"{P_note} maj9", callback_data=f"{P_note}_maj9")
                    chord9 = types.InlineKeyboardButton(f"{P_note}7-5", callback_data=f"{P_note}7-5")
                    chord10 = types.InlineKeyboardButton(f"{P_note}7+5", callback_data=f"{P_note}7+5")
                    chord11 = types.InlineKeyboardButton(f"{P_note}9", callback_data=f"{P_note}9")
                    chord12 = types.InlineKeyboardButton(f"{P_note}11", callback_data=f"{P_note}11")
                    chord13 = types.InlineKeyboardButton(f"{P_note}13", callback_data=f"{P_note}13")
                    chord14 = types.InlineKeyboardButton(f"{P_note} aug", callback_data=f"{P_note}_aug")
                    chord15 = types.InlineKeyboardButton(f"{P_note} aug7", callback_data=f"{P_note}_aug7")
                    chord16 = types.InlineKeyboardButton(f"{P_note} dim", callback_data=f"{P_note}_dim")
                    chord17 = types.InlineKeyboardButton(f"{P_note} dim7", callback_data=f"{P_note}_dim7")
                    chord18 = types.InlineKeyboardButton(f"{P_note}m6", callback_data=f"{P_note}m6")
                    chord19 = types.InlineKeyboardButton(f"{P_note}m7", callback_data=f"{P_note}m7")
                    chord20 = types.InlineKeyboardButton(f"{P_note}m7(b5)", callback_data=f"{P_note}m7b5")
                    chord21 = types.InlineKeyboardButton(f"{P_note}m9", callback_data=f"{P_note}m9")
                    chord22 = types.InlineKeyboardButton(f"{P_note}m11", callback_data=f"{P_note}m11")
                    chord23 = types.InlineKeyboardButton(f"{P_note}m13", callback_data=f"{P_note}m13")
                    chord24 = types.InlineKeyboardButton(f"{P_note}m maj7", callback_data=f"{P_note}m_maj7")
                    chord25 = types.InlineKeyboardButton(f"{P_note} add2", callback_data=f"{P_note}_add2")
                    chord26 = types.InlineKeyboardButton(f"{P_note} add9", callback_data=f"{P_note}_add9")
                    chord27 = types.InlineKeyboardButton(f"{P_note} sus2", callback_data=f"{P_note}_sus2")
                    chord28 = types.InlineKeyboardButton(f"{P_note} sus4", callback_data=f"{P_note}_sus4")

                    chordsmarkup.add(chord1, chord2, chord3, chord4, chord5, chord6, chord7, chord8, chord9, chord10,
                                     chord11,
                                     chord12,
                                     chord13, chord14, chord15, chord16, chord17, chord18, chord19, chord20, chord21,
                                     chord22,
                                     chord23,
                                     chord24, chord25, chord26, chord27, chord28)

                    bot.send_message(call.message.chat.id, 'Выберите аккорд:', reply_markup=chordsmarkup)
            if call.message:
                if call.data == f'{P_note}_major':
                    bot.send_message(call.message.chat.id, f'Вы выбрали {P_note} major')
                    bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                                              text=f"Вы выбрали {P_note} major")

                    Pmajor = open(f'bot_files/p_chords/{P_note}/{P_note}.png', 'rb')

                    bot.send_photo(call.message.chat.id, Pmajor)
                    Pmajor.close()

            if call.message:
                if call.data == f'{P_note}_minor':
                    bot.send_message(call.message.chat.id, f'Вы выбрали {P_note} minor')
                    bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                                              text=f"Вы выбрали {P_note} minor (Ля минор)")

                    Pminor = open(f'bot_files/p_chords/{P_note}/{P_note}m.png', 'rb')

                    bot.send_photo(call.message.chat.id, Pminor)
                    Pminor.close()

            if call.message:
                if call.data == f'{P_note}5':
                    bot.send_message(call.message.chat.id, f'Вы выбрали {P_note}5')
                    bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                                              text=f"Вы выбрали {P_note}5")

                    a5p = open(f'bot_files/p_chords/{P_note}/{P_note}5.png', 'rb')

                    bot.send_photo(call.message.chat.id, a5p)
                    a5p.close()

            if call.message:
                if call.data == f'{P_note}6':
                    bot.send_message(call.message.chat.id, f'Вы выбрали {P_note}6')
                    bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                                              text=f"Вы выбрали {P_note}6")

                    a6p = open(f'bot_files/p_chords/{P_note}/{P_note}6.png', 'rb')

                    bot.send_photo(call.message.chat.id, a6p)
                    a6p.close()

            if call.message:
                if call.data == f'{P_note}6_9':
                    bot.send_message(call.message.chat.id, f'Вы выбрали {P_note}6add9')
                    bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                                              text="Вы выбрали A6add9")

                    a6_9p = open(f'bot_files/p_chords/{P_note}/{P_note}6_9.png', 'rb')

                    bot.send_photo(call.message.chat.id, a6_9p)
                    a6_9p.close()

            if call.message:
                if call.data == f'{P_note}7':
                    bot.send_message(call.message.chat.id, f'Вы выбрали {P_note}7')
                    bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                                              text=f"Вы выбрали {P_note}7")

                    a7p = open(f'bot_files/p_chords/{P_note}/{P_note}7.png', 'rb')

                    bot.send_photo(call.message.chat.id, a7p)
                    a7p.close()

            if call.message:
                if call.data == f'{P_note}_maj7':
                    bot.send_message(call.message.chat.id, f'Вы выбрали {P_note} maj7')
                    bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                                              text="Вы выбрали A maj7")

                    a_maj7p = open(f'bot_files/p_chords/{P_note}/{P_note}maj7.png', 'rb')

                    bot.send_photo(call.message.chat.id, a_maj7p)
                    a_maj7p.close()

            if call.message:
                if call.data == f'{P_note}_maj9':
                    bot.send_message(call.message.chat.id, f'Вы выбрали {P_note} maj9')
                    bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                                              text=f"Вы выбрали {P_note} maj9")

                    a_maj9p = open(f'bot_files/p_chords/{P_note}/{P_note}maj9.png', 'rb')

                    bot.send_photo(call.message.chat.id, a_maj9p)
                    a_maj9p.close()

            if call.message:
                if call.data == f'{P_note}7-5':
                    bot.send_message(call.message.chat.id, f'Вы выбрали {P_note}7-5')
                    bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                                              text=f"Вы выбрали {P_note}7-5")

                    a7minus5p = open(f'bot_files/p_chords/{P_note}/{P_note}7minus5.png', 'rb')

                    bot.send_photo(call.message.chat.id, a7minus5p)
                    a7minus5p.close()

            if call.message:
                if call.data == f'{P_note}7+5':
                    bot.send_message(call.message.chat.id, f'Вы выбрали {P_note}7+5')
                    bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                                              text=f"Вы выбрали {P_note}7+5")

                    a7plus5p = open(f'bot_files/p_chords/{P_note}/{P_note}7plus5.png', 'rb')

                    bot.send_photo(call.message.chat.id, a7plus5p)
                    a7plus5p.close()

            if call.message:
                if call.data == f'{P_note}9':
                    bot.send_message(call.message.chat.id, f'Вы выбрали {P_note}9')
                    bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                                              text=f"Вы выбрали {P_note}9")

                    a9p = open(f'bot_files/p_chords/{P_note}/{P_note}9.png', 'rb')

                    bot.send_photo(call.message.chat.id, a9p)
                    a9p.close()

            if call.message:
                if call.data == f'{P_note}11':
                    bot.send_message(call.message.chat.id, f'Вы выбрали {P_note}11')
                    bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                                              text=f"Вы выбрали {P_note}7")

                    a11p = open(f'bot_files/p_chords/{P_note}/{P_note}11.png', 'rb')

                    bot.send_photo(call.message.chat.id, a11p)
                    a11p.close()

            if call.message:
                if call.data == f'{P_note}13':
                    bot.send_message(call.message.chat.id, f'Вы выбрали {P_note}13')
                    bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                                              text=f"Вы выбрали {P_note}13")

                    a13p = open(f'bot_files/p_chords/{P_note}/{P_note}13.png', 'rb')

                    bot.send_photo(call.message.chat.id, a13p)
                    a13p.close()

            if call.message:
                if call.data == f'{P_note}_aug':
                    bot.send_message(call.message.chat.id, f'Вы выбрали {P_note} aug')
                    bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                                              text=f"Вы выбрали {P_note} aug")

                    a_augp = open(f'bot_files/p_chords/{P_note}/{P_note}aug.png', 'rb')

                    bot.send_photo(call.message.chat.id, a_augp)
                    a_augp.close()

            if call.message:
                if call.data == f'{P_note}_aug7':
                    bot.send_message(call.message.chat.id, f'Вы выбрали {P_note} aug7')
                    bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                                              text=f"Вы выбрали {P_note} aug7")

                    a_aug7p = open(f'bot_files/p_chords/{P_note}/{P_note}aug7.png', 'rb')

                    bot.send_photo(call.message.chat.id, a_aug7p)
                    a_aug7p.close()

            if call.message:
                if call.data == f'{P_note}_dim':
                    bot.send_message(call.message.chat.id, f'Вы выбрали {P_note} dim')
                    bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                                              text=f"Вы выбрали {P_note} dim")

                    a_dimp = open(f'bot_files/p_chords/{P_note}/{P_note}dim.png', 'rb')

                    bot.send_photo(call.message.chat.id, a_dimp)
                    a_dimp.close()

            if call.message:
                if call.data == f'{P_note}_dim7':
                    bot.send_message(call.message.chat.id, f'Вы выбрали {P_note} dim7')
                    bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                                              text=f"Вы выбрали {P_note} dim7")

                    a_dim7p = open(f'bot_files/p_chords/{P_note}/{P_note}dim7.png', 'rb')

                    bot.send_photo(call.message.chat.id, a_dim7p)
                    a_dim7p.close()

            if call.message:
                if call.data == f'{P_note}m6':
                    bot.send_message(call.message.chat.id, f'Вы выбрали {P_note}m6')
                    bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                                              text=f"Вы выбрали {P_note}m6")

                    am6p = open(f'bot_files/p_chords/{P_note}/{P_note}m6.png', 'rb')

                    bot.send_photo(call.message.chat.id, am6p)
                    am6p.close()

            if call.message:
                if call.data == f'{P_note}m7':
                    bot.send_message(call.message.chat.id, f'Вы выбрали {P_note}m7')
                    bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                                              text=f"Вы выбрали {P_note}m7")

                    am7p = open(f'bot_files/p_chords/{P_note}/{P_note}m7.png', 'rb')

                    bot.send_photo(call.message.chat.id, am7p)
                    am7p.close()

            if call.message:
                if call.data == f'{P_note}m7b5':
                    bot.send_message(call.message.chat.id, f'Вы выбрали {P_note}m7(b5) ({P_note}m7-5) ')
                    bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                                              text=f"Вы выбрали {P_note}m7(b5)")

                    am7b5p = open(f'bot_files/p_chords/{P_note}/{P_note}m7b5.png', 'rb')

                    bot.send_photo(call.message.chat.id, am7b5p)
                    am7b5p.close()

            if call.message:
                if call.data == f'{P_note}m9':
                    bot.send_message(call.message.chat.id, f'Вы выбрали {P_note}m9')
                    bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                                              text=f"Вы выбрали {P_note}m9")

                    am9p = open(f'bot_files/p_chords/{P_note}/{P_note}m9.png', 'rb')

                    bot.send_photo(call.message.chat.id, am9p)
                    am9p.close()

            if call.message:
                if call.data == f'{P_note}m11':
                    bot.send_message(call.message.chat.id, f'Вы выбрали {P_note}m11')
                    bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                                              text=f"Вы выбрали {P_note}m11")

                    am11p = open(f'bot_files/p_chords/{P_note}/{P_note}m11.png', 'rb')

                    bot.send_photo(call.message.chat.id, am11p)
                    am11p.close()

            if call.message:
                if call.data == f'{P_note}m13':
                    bot.send_message(call.message.chat.id, f'Вы выбрали {P_note}m13')
                    bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                                              text=f"Вы выбрали {P_note}m13")

                    am13p = open(f'bot_files/p_chords/{P_note}/{P_note}m13.png', 'rb')

                    bot.send_photo(call.message.chat.id, am13p)
                    am13p.close()

            if call.message:
                if call.data == f'{P_note}m_maj7':
                    bot.send_message(call.message.chat.id, f'Вы выбрали {P_note}m maj7')
                    bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                                              text=f"Вы выбрали {P_note}m maj7")

                    am_maj7p = open(f'bot_files/p_chords/{P_note}/{P_note}minmaj7.png', 'rb')

                    bot.send_photo(call.message.chat.id, am_maj7p)
                    am_maj7p.close()

            if call.message:
                if call.data == f'{P_note}_add2':
                    bot.send_message(call.message.chat.id, f'Вы выбрали {P_note} add2 ({P_note}2)')
                    bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                                              text=f"Вы выбрали {P_note} add2 ({P_note}2)")

                    a_add2p = open(f'bot_files/p_chords/{P_note}/{P_note}add2.png', 'rb')

                    bot.send_photo(call.message.chat.id, a_add2p)
                    a_add2p.close()

            if call.message:
                if call.data == f'{P_note}_add9':
                    bot.send_message(call.message.chat.id, f'Вы выбрали {P_note}_add9')
                    bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                                              text=f"Вы выбрали {P_note}_add9")

                    a_add9p = open(f'bot_files/p_chords/{P_note}/{P_note}add9.png', 'rb')

                    bot.send_photo(call.message.chat.id, a_add9p)
                    a_add9p.close()

            if call.message:
                if call.data == f'{P_note}_sus2':
                    bot.send_message(call.message.chat.id, f'Вы выбрали {P_note} sus2')
                    bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                                              text=f"Вы выбрали {P_note} sus2")

                    a_sus2p = open(f'bot_files/p_chords/{P_note}/{P_note}sus2.png', 'rb')

                    bot.send_photo(call.message.chat.id, a_sus2p)
                    a_sus2p.close()

            if call.message:
                if call.data == f'{P_note}_sus4':
                    bot.send_message(call.message.chat.id, f'Вы выбрали {P_note} sus4')
                    bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                                              text=f"Вы выбрали {P_note} sus4")

                    a_sus4p = open(f'bot_files/p_chords/{P_note}/{P_note}sus4.png', 'rb')

                    bot.send_photo(call.message.chat.id, a_sus4p)
                    a_sus4p.close()

    def pent(Pt_note):
        if call.message:
            if call.data == f'{Pt_note}pt':
                bot.send_message(call.message.chat.id, f'Вы выбрали {Pt_note}')

                bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                                          text=f'Вы выбрали {Pt_note}')

                Pentmarkup = types.InlineKeyboardMarkup(row_width=2)
                Pent1 = types.InlineKeyboardButton("Major", callback_data=f"Major{Pt_note}pt")
                Pent2 = types.InlineKeyboardButton("Minor", callback_data=f"Minor{Pt_note}pt")

                Pentmarkup.add(Pent1, Pent2)

                bot.send_message(call.message.chat.id, 'Выберите лад', reply_markup=Pentmarkup)

        if call.message:
            if call.data == f'Major{Pt_note}pt':
                bot.send_message(call.message.chat.id, f'Вы выбрали {Pt_note} major')
                bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                                          text=f"Вы выбрали {Pt_note} major")

                majpt1 = open(f'bot_files/pentatonics/p_pent/{Pt_note} major pent.png', 'rb')
                majpt2 = open(f'bot_files/pentatonics/g_pent/{Pt_note} Major Pentatonic.png', 'rb')
                bot.send_photo(call.message.chat.id, majpt1)
                bot.send_photo(call.message.chat.id, majpt2)
                majpt1.close()
                majpt2.close()

        if call.message:
            if call.data == f'Minor{Pt_note}pt':
                bot.send_message(call.message.chat.id, f'Вы выбрали {Pt_note} minor')
                bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                                          text=f"Вы выбрали {Pt_note} minor")

                minpt1 = open(f'bot_files/pentatonics/p_pent/{Pt_note} minor pent.png', 'rb')
                minpt2 = open(f'bot_files/pentatonics/g_pent/{Pt_note} Minor Pentatonic.png', 'rb')
                bot.send_photo(call.message.chat.id, minpt1)
                bot.send_photo(call.message.chat.id, minpt2)
                minpt1.close()
                minpt2.close()

    # Вызов функций
    # keys Тональности
    if call.message:
        scales('A')
        scales('A#')
        scales('B')
        scales('C')
        scales('C#')
        scales('D')
        scales('D#')
        scales('E')
        scales('F')
        scales('F#')
        scales('G')
        scales('G#')

    # Piano chords Акоорды
    if call.message:
        chord('A')
        chord('A#')
        chord('B')
        chord('C')
        chord('C#')
        chord('D')
        chord('D#')
        chord('E')
        chord('F')
        chord('F#')
        chord('G')
        chord('G#')

    if call.message:
        pent('A')
        pent('A#')
        pent('B')
        pent('C')
        pent('C#')
        pent('D')
        pent('D#')
        pent('E')
        pent('F')
        pent('F#')
        pent('G')
        pent('G#')


bot.polling(none_stop=True)
