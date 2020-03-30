import telebot
from telebot import types

bot = telebot.TeleBot('855299931:AAE31jofHPMcRX2SLfMOAHwURaW7kieQBuc')


@bot.message_handler(commands=['start'])
def start_message(message):
    # keyboard
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("/help")
    item2 = types.KeyboardButton("/circle")
    item3 = types.KeyboardButton('/key')
    item4 = types.KeyboardButton('/p_chords')
    item5 = types.KeyboardButton('/g_chords')
    item6 = types.KeyboardButton('/p_intervals')
    item7 = types.KeyboardButton('/g_intervals')

    markup.add(item1, item2, item3, item4, item5, item6, item7)

    bot.send_message(message.chat.id,
                     'Оу, привет, <b>{0.first_name}</b>! Добро пожаловать!\n\nИспользуйте /help для получения списка команд.'.format(
                         message.from_user, bot.get_me()),
                     parse_mode='html', reply_markup=markup)

@bot.message_handler(commands=['help'])
def help_rus(message):
    bot.send_message(message.chat.id,
                     'Список команд:\n/circle - Кварто-квинтовый круг\n/key - Выберите тональность, которая Вам нужна 🎼\n/p_chords - Аппликатура аккодра для ПИАНИНО 🎹\n/p_interval - Аппликатура интервалов для ПИАНИНО 🎹\n/g_interval - Аппликатура интервалов для ГИТАРЫ 🎸\n/g_chords - Аппликатура аккодра для ГИТАРЫ 🎸(В РАЗРАБОТКЕ)')


@bot.message_handler(commands=['circle'])
def circle_rus(message):
    bot.send_message(message.chat.id, 'Вот Кварто-квинтовый круг')
    circle = open('bot_files/circle.png', 'rb')
    bot.send_photo(message.chat.id, circle)
    circle.close()


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
def help_rus(message):
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


@bot.callback_query_handler(func=lambda call: True)
def key_callback(call):
    if call.message:
        if call.data == 'A':
            bot.send_message(call.message.chat.id, 'Вы выбрали А (Ля)')

            bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                                      text="Вы выбрали А (Ля)")

            Amodemarkup = types.InlineKeyboardMarkup(row_width=2)
            Amode1 = types.InlineKeyboardButton("Major", callback_data="MajorA")
            Amode2 = types.InlineKeyboardButton("Minor", callback_data="MinorA")

            Amodemarkup.add(Amode1, Amode2)

            bot.send_message(call.message.chat.id, 'Выберите лад', reply_markup=Amodemarkup)

        if call.message:
            if call.data == 'MajorA':
                bot.send_message(call.message.chat.id, 'Вы выбрали А major (Ля мажор)')
                bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                                          text="Вы выбрали А major (Ля мажор)")

                amaj = open('bot_files/keys/Major/A.png', 'rb')

                bot.send_photo(call.message.chat.id, amaj)
                amaj.close()

        if call.message:
            if call.data == 'MinorA':
                bot.send_message(call.message.chat.id, 'Вы выбрали А minor (Ля минор)')
                bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                                          text="Вы выбрали А minor (Ля минор)")

                am = open('bot_files/keys/Minor/Am.png', 'rb')

                bot.send_photo(call.message.chat.id, am)
                am.close()

    if call.data == 'A#':
        bot.send_message(call.message.chat.id, 'Вы выбрали А#\Bb (Ля диез \ Си бемоль)')

        bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                                  text="Вы выбрали А#\Bb (Ля диез\Си бемоль)")

        Bbmodemarkup = types.InlineKeyboardMarkup(row_width=2)
        Bbmode1 = types.InlineKeyboardButton("Major", callback_data="MajorBb")
        Bbmode2 = types.InlineKeyboardButton("Minor", callback_data="MinorBb")

        Bbmodemarkup.add(Bbmode1, Bbmode2)

        bot.send_message(call.message.chat.id, 'Выберите лад', reply_markup=Bbmodemarkup)

    if call.message:
        if call.data == 'MajorBb':
            bot.send_message(call.message.chat.id, 'Вы выбрали А#\Bb major (Ля диез \ Си бемоль)')
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                                      text="Вы выбрали А#\Bb major (Ля диез \ Си бемоль мажор)")

            Bbmaj = open('bot_files/keys/Major/Bb_A#.png', 'rb')

            bot.send_photo(call.message.chat.id, Bbmaj)
            Bbmaj.close()

    if call.message:
        if call.data == 'MinorBb':
            bot.send_message(call.message.chat.id, 'Вы выбрали А#\Bb minor (Ля диез \ Си бемоль минор)')
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                                      text="Вы выбрали А#\Bb minor (Ля диез \ Си бемоль минор)")

            Bbm = open('bot_files/keys/Minor/Bbm.png', 'rb')

            bot.send_photo(call.message.chat.id, Bbm)
            Bbm.close()

    if call.data == 'B':
        bot.send_message(call.message.chat.id, 'Вы выбрали B (Си)')

        bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                                  text="Вы выбрали B (Си)")

        Bmodemarkup = types.InlineKeyboardMarkup(row_width=2)
        Bmode1 = types.InlineKeyboardButton("Major", callback_data="MajorB")
        Bmode2 = types.InlineKeyboardButton("Minor", callback_data="MinorB")

        Bmodemarkup.add(Bmode1, Bmode2)

        bot.send_message(call.message.chat.id, 'Выберите лад', reply_markup=Bmodemarkup)

    if call.message:
        if call.data == 'MajorB':
            bot.send_message(call.message.chat.id, 'Вы выбрали B major (Си мажор)')
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                                      text="Вы выбрали B major (Си мажор)")

            Bmaj = open('bot_files/keys/Major/B.png', 'rb')

            bot.send_photo(call.message.chat.id, Bmaj)
            Bmaj.close()

    if call.message:
        if call.data == 'MinorB':
            bot.send_message(call.message.chat.id, 'Вы выбрали B minor (Си минор)')
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                                      text="Вы выбрали B minor (Си минор)")
            Bm = open('bot_files/keys/Minor/Bm.png', 'rb')

            bot.send_photo(call.message.chat.id, Bm)
            Bm.close()

    if call.data == 'C':
        bot.send_message(call.message.chat.id, 'Вы выбрали C (До)')

        bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                                  text="Вы выбрали C (До)")

        Cmodemarkup = types.InlineKeyboardMarkup(row_width=2)
        Cmode1 = types.InlineKeyboardButton("Major", callback_data="MajorC")
        Cmode2 = types.InlineKeyboardButton("Minor", callback_data="MinorC")

        Cmodemarkup.add(Cmode1, Cmode2)
        bot.send_message(call.message.chat.id, 'Выберите лад', reply_markup=Cmodemarkup)

    if call.message:
        if call.data == 'MajorC':
            bot.send_message(call.message.chat.id, 'Вы выбрали C major (До мажор)')
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                                      text="Вы выбрали C major (До минор)")

            Cmaj = open('bot_files/keys/Major/C.png', 'rb')

            bot.send_photo(call.message.chat.id, Cmaj)
            Cmaj.close()

    if call.message:
        if call.data == 'MinorC':
            bot.send_message(call.message.chat.id, 'Вы выбрали C minor (До минор)')
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                                      text="Вы выбрали C minor (До минор)")
            Cm = open('bot_files/keys/Minor/Cm.png', 'rb')

            bot.send_photo(call.message.chat.id, Cm)
            Cm.close()

    if call.data == 'C#':
        bot.send_message(call.message.chat.id, 'Вы выбрали C#\Db (До диез\Ре бемоль)')

        bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                                  text="Вы выбрали ноту C#\Db (До диез\Ре бемоль)")

        Dbmodemarkup = types.InlineKeyboardMarkup(row_width=2)
        Dbmode1 = types.InlineKeyboardButton("Major", callback_data="MajorDb")
        Dbmode2 = types.InlineKeyboardButton("Minor", callback_data="MinorDb")

        Dbmodemarkup.add(Dbmode1, Dbmode2)
        bot.send_message(call.message.chat.id, 'Выберите лад', reply_markup=Dbmodemarkup)

    if call.message:
        if call.data == 'MajorDb':
            bot.send_message(call.message.chat.id, 'Вы выбрали C#\Db major (До диез мажор \ Ре бемоль мажор)')
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                                      text="Вы выбрали C# major\Db major (До диез минор \ Ре бемоль минор)")

            Dbmaj = open('bot_files/keys/Major/C#.png', 'rb')

            bot.send_photo(call.message.chat.id, Dbmaj)
            Dbmaj.close()

    if call.message:
        if call.data == 'MinorDb':
            bot.send_message(call.message.chat.id, 'Вы выбрали C#\Db minor (До диез минор \ Ре бемоль минор)')
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                                      text="Вы выбрали C#\Db minor (До диез минор \ Ре бемоль минор)")
            Dbm = open('bot_files/keys/Minor/C#m.png', 'rb')

            bot.send_photo(call.message.chat.id, Dbm)
            Dbm.close()

    if call.data == 'D':
        bot.send_message(call.message.chat.id, 'Вы выбрали D (Ре)')

        bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                                  text="Вы выбрали D (Ре)")

        Dmodemarkup = types.InlineKeyboardMarkup(row_width=2)
        Dmode1 = types.InlineKeyboardButton("Major", callback_data="MajorD")
        Dmode2 = types.InlineKeyboardButton("Minor", callback_data="MinorD")

        Dmodemarkup.add(Dmode1, Dmode2)
        bot.send_message(call.message.chat.id, 'Выберите лад', reply_markup=Dmodemarkup)

    if call.message:
        if call.data == 'MajorD':
            bot.send_message(call.message.chat.id, 'Вы выбрали D major (Ре мажор)')
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                                      text="Вы выбрали D major (Ре минор)")

            Dmaj = open('bot_files/keys/Major/D.png', 'rb')

            bot.send_photo(call.message.chat.id, Dmaj)
            Dmaj.close()

    if call.message:
        if call.data == 'MinorD':
            bot.send_message(call.message.chat.id, 'Вы выбрали D minor (Ре минор)')
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                                      text="Вы выбрали D minor (Ре бемоль минор)")

            Dm = open('bot_files/keys/Minor/Dm.png', 'rb')

            bot.send_photo(call.message.chat.id, Dm)
            Dm.close()

    if call.data == 'D#':
        bot.send_message(call.message.chat.id, 'Вы выбрали D#\Eb (Ре диез \ Ми бемоль)')

        bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                                  text="Вы выбрали D#\Eb (Ре диез\Ми бемоль)")

        Ebmodemarkup = types.InlineKeyboardMarkup(row_width=2)
        Ebmode1 = types.InlineKeyboardButton("Major", callback_data="MajorEb")
        Ebmode2 = types.InlineKeyboardButton("Minor", callback_data="MinorEb")

        Ebmodemarkup.add(Ebmode1, Ebmode2)
        bot.send_message(call.message.chat.id, 'Выберите лад', reply_markup=Ebmodemarkup)

    if call.message:
        if call.data == 'MajorEb':
            bot.send_message(call.message.chat.id, 'Вы выбрали D#\Eb major (Ре диез \ Ми бемоль мажор)')
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                                      text="Вы выбрали D#\Eb major (Ре диез \ Ми бемоль мажор)")

            Ebmaj = open('bot_files/keys/Major/D#.png', 'rb')

            bot.send_photo(call.message.chat.id, Ebmaj)
            Ebmaj.close()

    if call.message:
        if call.data == 'MinorEb':
            bot.send_message(call.message.chat.id, 'Вы выбрали D#\Eb minor (Ре диез \ Ми бемоль минор)')
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                                      text="Вы выбрали D#\Eb minor (Ре диез \ Ми бемоль минор)")
            Ebm = open('bot_files/keys/Minor/D#m.png', 'rb')

            bot.send_photo(call.message.chat.id, Ebm)
            Ebm.close()

    if call.data == 'E':
        bot.send_message(call.message.chat.id, 'Вы выбрали E (Ми)')

        bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                                  text="Вы выбрали E (Ми)")

        Emodemarkup = types.InlineKeyboardMarkup(row_width=2)
        Emode1 = types.InlineKeyboardButton("Major", callback_data="MajorE")
        Emode2 = types.InlineKeyboardButton("Minor", callback_data="MinorE")

        Emodemarkup.add(Emode1, Emode2)
        bot.send_message(call.message.chat.id, 'Выберите лад', reply_markup=Emodemarkup)

    if call.message:
        if call.data == 'MajorE':
            bot.send_message(call.message.chat.id, 'Вы выбрали E major (Ми мажор)')
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                                      text="Вы выбрали E major (Ми мажор)")

            Emaj = open('bot_files/keys/Major/E.png', 'rb')

            bot.send_photo(call.message.chat.id, Emaj)
            Emaj.close()

    if call.message:
        if call.data == 'MinorE':
            bot.send_message(call.message.chat.id, 'Вы выбрали E minor (Ми минор)')
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                                      text="Вы выбрали E minor (Ми минор)")
            Em = open('bot_files/keys/Minor/Em.png', 'rb')

            bot.send_photo(call.message.chat.id, Em)
            Em.close()

    if call.data == 'F':
        bot.send_message(call.message.chat.id, 'Вы выбрали F (Фа)')

        bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                                  text="Вы выбрали F (Фа)")

        Fmodemarkup = types.InlineKeyboardMarkup(row_width=2)
        Fmode1 = types.InlineKeyboardButton("Major", callback_data="MajorF")
        Fmode2 = types.InlineKeyboardButton("Minor", callback_data="MinorF")

        Fmodemarkup.add(Fmode1, Fmode2)
        bot.send_message(call.message.chat.id, 'Выберите лад', reply_markup=Fmodemarkup)

    if call.message:
        if call.data == 'MajorF':
            bot.send_message(call.message.chat.id, 'Вы выбрали F major (Фа мажор)')
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                                      text="Вы выбрали F major (Фа мажор)")

            Fmaj = open('bot_files/keys/Major/F.png', 'rb')

            bot.send_photo(call.message.chat.id, Fmaj)
            Fmaj.close()

    if call.message:
        if call.data == 'MinorF':
            bot.send_message(call.message.chat.id, 'Вы выбрали F minor (Фа минор)')
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                                      text="Вы выбрали F minor (Фа минор)")
            Fm = open('bot_files/keys/Minor/Fm.png', 'rb')

            bot.send_photo(call.message.chat.id, Fm)
            Fm.close()

    if call.data == 'F#':
        bot.send_message(call.message.chat.id, 'Вы выбрали F#\Gb (Фа диез \ Соль бемоль)')

        bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                                  text="Вы выбрали F#\Gb (Фа диез\Соль бемоль)")

        Gbmodemarkup = types.InlineKeyboardMarkup(row_width=2)
        Gbmode1 = types.InlineKeyboardButton("Major", callback_data="MajorGb")
        Gbmode2 = types.InlineKeyboardButton("Minor", callback_data="MinorGb")

        Gbmodemarkup.add(Gbmode1, Gbmode2)
        bot.send_message(call.message.chat.id, 'Выберите лад', reply_markup=Gbmodemarkup)

    if call.message:
        if call.data == 'MajorGb':
            bot.send_message(call.message.chat.id, 'Вы выбрали F#\Gb major (Фа диез \ Соль бемоль мажор)')
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                                      text="Вы выбрали F#\Gb major (Фа диез \ Соль бемоль мажор)")

            Gbmaj = open('bot_files/keys/Major/F#.png', 'rb')

            bot.send_photo(call.message.chat.id, Gbmaj)
            Gbmaj.close()

    if call.message:
        if call.data == 'MinorGb':
            bot.send_message(call.message.chat.id, 'Вы выбрали F#\Gb minor (Фа диез \ Соль бемоль минор)')
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                                      text="Вы выбрали F# minor (Фа диез \ Соль бемоль минор)")
            Gbm = open('bot_files/keys/Minor/F#m.png', 'rb')

            bot.send_photo(call.message.chat.id, Gbm)
            Gbm.close()

    if call.data == 'G':
        bot.send_message(call.message.chat.id, 'Вы выбрали G (Соль)')

        bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                                  text="Вы выбрали G (Соль)")

        Gmodemarkup = types.InlineKeyboardMarkup(row_width=2)
        Gmode1 = types.InlineKeyboardButton("Major", callback_data="MajorG")
        Gmode2 = types.InlineKeyboardButton("Minor", callback_data="MinorG")

        Gmodemarkup.add(Gmode1, Gmode2)
        bot.send_message(call.message.chat.id, 'Выберите лад', reply_markup=Gmodemarkup)

    if call.message:
        if call.data == 'MajorG':
            bot.send_message(call.message.chat.id, 'Вы выбрали G major (Соль мажор)')
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                                      text="Вы выбрали G major (Соль мажор)")

            Gmaj = open('bot_files/keys/Major/G.png', 'rb')

            bot.send_photo(call.message.chat.id, Gmaj)
            Gmaj.close()

    if call.message:
        if call.data == 'MinorG':
            bot.send_message(call.message.chat.id, 'Вы выбрали G minor (Соль минор)')
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                                      text="Вы выбрали G minor (Соль минор)")
            Gm = open('bot_files/keys/Minor/Gm.png', 'rb')

            bot.send_photo(call.message.chat.id, Gm)
            Gm.close()

    if call.data == 'G#':
        bot.send_message(call.message.chat.id, 'Вы выбрали G#\Ab (Соль диез \ Ля бемоль)')

        bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                                  text="Вы выбрали G#\Ab (Соль диез \ Ля бемоль)")

        Abmodemarkup = types.InlineKeyboardMarkup(row_width=2)
        Abmode1 = types.InlineKeyboardButton("Major", callback_data="MajorAb")
        Abmode2 = types.InlineKeyboardButton("Minor", callback_data="MinorAb")

        Abmodemarkup.add(Abmode1, Abmode2)
        bot.send_message(call.message.chat.id, 'Выберите лад', reply_markup=Abmodemarkup)

    if call.message:
        if call.data == 'MajorAb':
            bot.send_message(call.message.chat.id, 'Вы выбрали G#\Ab major (Соль диез \ Ля бемоль мажор)')
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                                      text="Вы выбрали G#\Ab major (Соль диез\Ля бемоль мажор)")

            Abmaj = open('bot_files/keys/Major/G#.png', 'rb')

            bot.send_photo(call.message.chat.id, Abmaj)
            Abmaj.close()

    if call.message:
        if call.data == 'MinorAb':
            bot.send_message(call.message.chat.id, 'Вы выбрали G#\Ab minor (Соль диез \ Ля бемоль минор)')
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                                      text="Вы выбрали G#\Ab minor (Соль диез \ Ля бемоль минор)")
            Abm = open('bot_files/keys/Minor/G#m.png', 'rb')

            bot.send_photo(call.message.chat.id, Abm)
            Abm.close()





# Аккорды для пианино

@bot.message_handler(commands=['p_chords'])
def p_chord(message):

    chordmarkup = types.InlineKeyboardMarkup(row_width=3)
    key1p = types.InlineKeyboardButton('A', callback_data='Ap')
    key2p = types.InlineKeyboardButton('A#/Bb', callback_data='A#p')
    key3p = types.InlineKeyboardButton('B', callback_data='Bp')
    key4p = types.InlineKeyboardButton('C', callback_data='Cp')
    key5p = types.InlineKeyboardButton('C#/Db', callback_data='C#p')
    key6p = types.InlineKeyboardButton('D', callback_data='Dp')
    key7p = types.InlineKeyboardButton('D#/Eb', callback_data='D#p')
    key8p = types.InlineKeyboardButton('E', callback_data='Ep')
    key9p = types.InlineKeyboardButton('F', callback_data='Fp')
    key10p = types.InlineKeyboardButton('F#/Gb', callback_data='F#p')
    key11p = types.InlineKeyboardButton('G', callback_data='Gp')
    key12p = types.InlineKeyboardButton('G#/Ab', callback_data='G#p')

    chordmarkup.add(key1p, key2p, key3p, key4p, key5p, key6p, key7p, key8p, key9p, key10p, key11p, key12p)

    bot.send_message(message.chat.id, 'Выберите тонику аккорда:', reply_markup=chordmarkup)


@bot.callback_query_handler(func=lambda call: True)
def p_chord_callback(call):
    if call.message:
        if call.data == 'Ap':
            bot.send_message(call.message.chat.id, 'Вы выбрали А (Ля)')

            bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                                      text="Вы выбрали А (Ля)")

            Apmodemarkup = types.InlineKeyboardMarkup(row_width=1)
            Apmode1 = types.InlineKeyboardButton("A", callback_data="Ap")
            Apmode2 = types.InlineKeyboardButton("A5", callback_data="A5")
            Apmode3 = types.InlineKeyboardButton("A6", callback_data="A6")
            Apmode4 = types.InlineKeyboardButton("A6/9", callback_data="A6_9")
            Apmode5 = types.InlineKeyboardButton("A7", callback_data="A7")
            Apmode6 = types.InlineKeyboardButton("A7-5", callback_data="A7-5")
            Apmode7 = types.InlineKeyboardButton("A7+5", callback_data="A7+5")
            Apmode8 = types.InlineKeyboardButton("A9", callback_data="A9")
            Apmode9 = types.InlineKeyboardButton("A11", callback_data="A11")
            Apmode10 = types.InlineKeyboardButton("A13", callback_data="A13")
            Apmode11 = types.InlineKeyboardButton("A add2", callback_data="A_add2")
            Apmode12 = types.InlineKeyboardButton("A add9", callback_data="A_add9")
            Apmode13 = types.InlineKeyboardButton("A Aug", callback_data="A_aug")
            Apmode14 = types.InlineKeyboardButton("A Aug7", callback_data="A_aug7")
            Apmode15 = types.InlineKeyboardButton("A dim", callback_data="A_dim")
            Apmode16 = types.InlineKeyboardButton("A dim7", callback_data="A_dim7")
            Apmode17 = types.InlineKeyboardButton("A maj7", callback_data="A_maj7")
            Apmode18 = types.InlineKeyboardButton("A maj9", callback_data="A_maj9")
            Apmode19 = types.InlineKeyboardButton("Am", callback_data="MinorAp")
            Apmode20 = types.InlineKeyboardButton("Am6", callback_data="Am6")
            Apmode21 = types.InlineKeyboardButton("Am7", callback_data="Am7")
            Apmode22 = types.InlineKeyboardButton("Am7(b5)", callback_data="Am7b5")
            Apmode23 = types.InlineKeyboardButton("Am9", callback_data="Am9")
            Apmode24 = types.InlineKeyboardButton("Am11", callback_data="Am11")
            Apmode25 = types.InlineKeyboardButton("Am13", callback_data="Am13")
            Apmode26 = types.InlineKeyboardButton("Am maj7", callback_data="Am_maj7")
            Apmode27 = types.InlineKeyboardButton("A sus2", callback_data="A_sus2")
            Apmode28 = types.InlineKeyboardButton("A sus4", callback_data="A_sus4")

            Apmodemarkup.add(Apmode1, Apmode2, Apmode3, Apmode4, Apmode5, Apmode6, Apmode7, Apmode8, Apmode9, Apmode10,
                             Apmode11, Apmode12, Apmode13, Apmode14, Apmode15, Apmode16, Apmode17, Apmode18, Apmode19,
                             Apmode20, Apmode21, Apmode22, Apmode23, Apmode24, Apmode24, Apmode25,
                             Apmode26, Apmode27, Apmode28)

            bot.send_message(call.message.chat.id, 'Выберите аккорд', reply_markup=Apmodemarkup)

        if call.message:
            if call.data == 'Ap':
                bot.send_message(call.message.chat.id, 'Вы выбрали А (Ля мажор)')
                bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                                          text="Вы выбрали А (Ля мажор)")

                apmaj = open('bot_files/p_chords/A/a.png', 'rb')

                bot.send_photo(call.message.chat.id, apmaj)
                apmaj.close()

        if call.message:
            if call.data == 'MinorA':
                bot.send_message(call.message.chat.id, 'Вы выбрали А minor (Ля минор)')
                bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                                          text="Вы выбрали А minor (Ля минор)")

                am = open('bot_files/keys/Minor/Am.png', 'rb')

                bot.send_photo(call.message.chat.id, am)
                am.close()




@bot.message_handler(commands=['g_chords'])
def g_chord_rus(message):
    bot.send_message(message.chat.id, 'Функция находится в разработке')


bot.polling(none_stop=True)
