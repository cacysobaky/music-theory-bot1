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
    item8 = types.KeyboardButton('/start')

    markup.add(item1, item2, item3, item4, item5, item6, item7, item8)

    bot.send_message(message.chat.id,
                     'Оу, привет, <b>{0.first_name}</b>! Добро пожаловать!\n\nИспользуйте /help для получения списка команд.'.format(
                         message.from_user, bot.get_me()),
                     parse_mode='html', reply_markup=markup)


@bot.message_handler(commands=['help'])
def help_rus(message):
    bot.send_message(message.chat.id,
                     'Список команд:\n/circle - Кварто-квинтовый круг\n/key - Выберите тональность, которая Вам нужна 🎼\n/p_chords - Аппликатура аккодра для ПИАНИНО 🎹(В РАЗРАБОТКЕ)\n/p_interval - Аппликатура интервалов для ПИАНИНО 🎹\n/g_interval - Аппликатура интервалов для ГИТАРЫ 🎸\n/g_chords - Аппликатура аккодра для ГИТАРЫ 🎸(В РАЗРАБОТКЕ)')


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


@bot.message_handler(commands=['p_chords'])


def p_chords(message):
    chordsnotemarkup = types.InlineKeyboardMarkup(row_width=3)

    note1 = types.InlineKeyboardButton("A ", callback_data="Ap")
    note2 = types.InlineKeyboardButton("A# ", callback_data="A#p")
    note3 = types.InlineKeyboardButton("B ", callback_data="Bp")
    note4 = types.InlineKeyboardButton("C ", callback_data="Cp")
    note5 = types.InlineKeyboardButton("C# ", callback_data="C#p")
    note6 = types.InlineKeyboardButton("D ", callback_data="Dp")
    note7 = types.InlineKeyboardButton("D# ", callback_data="D#p")
    note8 = types.InlineKeyboardButton("E ", callback_data="Ep")
    note9 = types.InlineKeyboardButton("F ", callback_data="Fp")
    note10 = types.InlineKeyboardButton("F# ", callback_data="F#p")
    note11 = types.InlineKeyboardButton("G ", callback_data="Gp")
    note12 = types.InlineKeyboardButton("G# ", callback_data="G#p")

    chordsnotemarkup.add(note1, note2, note3, note4, note5, note6, note7, note8, note9, note10, note11, note12)

    bot.send_message(message.chat.id, 'Выберите тонику аккорда:', reply_markup=chordsnotemarkup)


@bot.callback_query_handler(func=lambda call: True)
def keys_chords_callback(call):
    #keys
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
            bot.send_message(call.message.chat.id, 'Вы выбрали А#\Bb major (Ля диез \ Си бемоль мажор)')
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
    #pianoChords
    #A Chords

    if call.message:
        if call.data == 'Ap':
            bot.send_message(call.message.chat.id, 'Вы выбрали А (Ля)')

            bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                                      text="Вы выбрали А (Ля)")

            chordsmarkup = types.InlineKeyboardMarkup(row_width=3)

            chord1 = types.InlineKeyboardButton("A", callback_data="A_major")
            chord2 = types.InlineKeyboardButton("Am", callback_data="A_minor")
            chord3 = types.InlineKeyboardButton("A5", callback_data="A5")
            chord4 = types.InlineKeyboardButton("A6", callback_data="A6")
            chord5 = types.InlineKeyboardButton("A6 add9", callback_data="A6_9")
            chord6 = types.InlineKeyboardButton("A7", callback_data="A7")
            chord7 = types.InlineKeyboardButton("A maj7", callback_data="A_maj7")
            chord8 = types.InlineKeyboardButton("A maj9", callback_data="A_maj9")
            chord9 = types.InlineKeyboardButton("A7-5", callback_data="A7-5")
            chord10 = types.InlineKeyboardButton("A7+5", callback_data="A7+5")
            chord11 = types.InlineKeyboardButton("A9", callback_data="A9")
            chord12 = types.InlineKeyboardButton("A11", callback_data="A11")
            chord13 = types.InlineKeyboardButton("A13", callback_data="A13")
            chord14 = types.InlineKeyboardButton("A aug", callback_data="A_aug")
            chord15 = types.InlineKeyboardButton("A aug7", callback_data="A_aug7")
            chord16 = types.InlineKeyboardButton("A dim", callback_data="A_dim")
            chord17 = types.InlineKeyboardButton("A dim7", callback_data="A_dim7")
            chord18 = types.InlineKeyboardButton("Am6", callback_data="Am6")
            chord19 = types.InlineKeyboardButton("Am7", callback_data="Am7")
            chord20 = types.InlineKeyboardButton("Am7(b5)", callback_data="Am7b5")
            chord21 = types.InlineKeyboardButton("Am9", callback_data="Am9")
            chord22 = types.InlineKeyboardButton("Am11", callback_data="Am11")
            chord23 = types.InlineKeyboardButton("Am13", callback_data="Am13")
            chord24 = types.InlineKeyboardButton("Am maj7", callback_data="Am_maj7")
            chord25 = types.InlineKeyboardButton("A add2", callback_data="A_add2")
            chord26 = types.InlineKeyboardButton("A add9", callback_data="A_add9")
            chord27 = types.InlineKeyboardButton("A sus2", callback_data="A_sus2")
            chord28 = types.InlineKeyboardButton("A sus4", callback_data="A_sus4")

            chordsmarkup.add(chord1, chord2, chord3, chord4, chord5, chord6, chord7, chord8, chord9, chord10, chord11,
                             chord12,
                             chord13, chord14, chord15, chord16, chord17, chord18, chord19, chord20, chord21, chord22,
                             chord23,
                             chord24, chord25, chord26, chord27, chord28)

            bot.send_message(call.message.chat.id, 'Выберите аккорд:', reply_markup=chordsmarkup)

    if call.message:
        if call.data == 'A_major':
            bot.send_message(call.message.chat.id, 'Вы выбрали A major (Ля мажор)')
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                                      text="Вы выбрали A major (Ля мажор)")

            a_majorp = open('bot_files/p_chords/A/a.png', 'rb')

            bot.send_photo(call.message.chat.id, a_majorp)
            a_majorp.close()

    if call.message:
        if call.data == 'A_minor':
            bot.send_message(call.message.chat.id, 'Вы выбрали A minor (Ля минор)')
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                                      text="Вы выбрали A minor (Ля минор)")

            a_minorp = open('bot_files/p_chords/A/am.png', 'rb')

            bot.send_photo(call.message.chat.id, a_minorp)
            a_minorp.close()

    if call.message:
        if call.data == 'A5':
            bot.send_message(call.message.chat.id, 'Вы выбрали A5')
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                                      text="Вы выбрали A5")

            a5p = open('bot_files/p_chords/A/a5.png', 'rb')

            bot.send_photo(call.message.chat.id, a5p)
            a5p.close()

    if call.message:
        if call.data == 'A6':
            bot.send_message(call.message.chat.id, 'Вы выбрали A6')
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                                      text="Вы выбрали A6")

            a6p = open('bot_files/p_chords/A/a6.png', 'rb')

            bot.send_photo(call.message.chat.id, a6p)
            a6p.close()

    if call.message:
        if call.data == 'A6_9':
            bot.send_message(call.message.chat.id, 'Вы выбрали A6add9')
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                                      text="Вы выбрали A6add9")

            a6_9p = open('bot_files/p_chords/A/a6_9.png', 'rb')

            bot.send_photo(call.message.chat.id, a6_9p)
            a6_9p.close()

    if call.message:
        if call.data == 'A7':
            bot.send_message(call.message.chat.id, 'Вы выбрали A7')
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                                      text="Вы выбрали A7")

            a7p = open('bot_files/p_chords/A/a7.png', 'rb')

            bot.send_photo(call.message.chat.id, a7p)
            a7p.close()

    if call.message:
        if call.data == 'A_maj7':
            bot.send_message(call.message.chat.id, 'Вы выбрали A maj7')
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                                      text="Вы выбрали A maj7")

            a_maj7p = open('bot_files/p_chords/A/amaj7.png', 'rb')

            bot.send_photo(call.message.chat.id, a_maj7p)
            a_maj7p.close()

    if call.message:
        if call.data == 'A_maj9':
            bot.send_message(call.message.chat.id, 'Вы выбрали A maj9')
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                                      text="Вы выбрали A maj9")

            a_maj9p = open('bot_files/p_chords/A/amaj9.png', 'rb')

            bot.send_photo(call.message.chat.id, a_maj9p)
            a_maj9p.close()

    if call.message:
        if call.data == 'A7-5':
            bot.send_message(call.message.chat.id, 'Вы выбрали A7-5')
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                                      text="Вы выбрали A7-5")

            a7minus5p = open('bot_files/p_chords/A/a7minus5.png', 'rb')

            bot.send_photo(call.message.chat.id, a7minus5p)
            a7minus5p.close()

    if call.message:
        if call.data == 'A7+5':
            bot.send_message(call.message.chat.id, 'Вы выбрали A7+5')
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                                      text="Вы выбрали A7+5")

            a7plus5p = open('bot_files/p_chords/A/a7plus5.png', 'rb')

            bot.send_photo(call.message.chat.id, a7plus5p)
            a7plus5p.close()

    if call.message:
        if call.data == 'A9':
            bot.send_message(call.message.chat.id, 'Вы выбрали A9')
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                                      text="Вы выбрали A9")

            a9p = open('bot_files/p_chords/A/a9.png', 'rb')

            bot.send_photo(call.message.chat.id, a9p)
            a9p.close()

    if call.message:
        if call.data == 'A11':
            bot.send_message(call.message.chat.id, 'Вы выбрали A11')
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                                      text="Вы выбрали A7")

            a11p = open('bot_files/p_chords/A/a11.png', 'rb')

            bot.send_photo(call.message.chat.id, a11p)
            a11p.close()

    if call.message:
        if call.data == 'A13':
            bot.send_message(call.message.chat.id, 'Вы выбрали A13')
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                                      text="Вы выбрали A13")

            a13p = open('bot_files/p_chords/A/a13.png', 'rb')

            bot.send_photo(call.message.chat.id, a13p)
            a13p.close()

    if call.message:
        if call.data == 'A_aug':
            bot.send_message(call.message.chat.id, 'Вы выбрали A aug')
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                                      text="Вы выбрали A aug")

            a_augp = open('bot_files/p_chords/A/aaug.png', 'rb')

            bot.send_photo(call.message.chat.id, a_augp)
            a_augp.close()

    if call.message:
        if call.data == 'A_aug7':
            bot.send_message(call.message.chat.id, 'Вы выбрали A aug7')
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                                      text="Вы выбрали A aug7")

            a_aug7p = open('bot_files/p_chords/A/aaug7.png', 'rb')

            bot.send_photo(call.message.chat.id, a_aug7p)
            a_aug7p.close()

    if call.message:
        if call.data == 'A_dim':
            bot.send_message(call.message.chat.id, 'Вы выбрали A dim')
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                                      text="Вы выбрали A dim")

            a_dimp = open('bot_files/p_chords/A/adim.png', 'rb')

            bot.send_photo(call.message.chat.id, a_dimp)
            a_dimp.close()

    if call.message:
        if call.data == 'A_dim7':
            bot.send_message(call.message.chat.id, 'Вы выбрали A dim7')
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                                      text="Вы выбрали A dim7")

            a_dim7p = open('bot_files/p_chords/A/adim7.png', 'rb')

            bot.send_photo(call.message.chat.id, a_dim7p)
            a_dim7p.close()

    if call.message:
        if call.data == 'Am6':
            bot.send_message(call.message.chat.id, 'Вы выбрали Am6')
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                                      text="Вы выбрали Am6")

            am6p = open('bot_files/p_chords/A/am6.png', 'rb')

            bot.send_photo(call.message.chat.id, am6p)
            am6p.close()

    if call.message:
        if call.data == 'Am7':
            bot.send_message(call.message.chat.id, 'Вы выбрали Am7')
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                                      text="Вы выбрали Am7")

            am7p = open('bot_files/p_chords/A/am7.png', 'rb')

            bot.send_photo(call.message.chat.id, am7p)
            am7p.close()

    if call.message:
        if call.data == 'Am7b5':
            bot.send_message(call.message.chat.id, 'Вы выбрали Am7(b5) (Am7-5) ')
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                                      text="Вы выбрали Am7(b5) (Am7-5)")

            am7b5p = open('bot_files/p_chords/A/am7b5.png', 'rb')

            bot.send_photo(call.message.chat.id, am7b5p)
            am7b5p.close()

    if call.message:
        if call.data == 'Am9':
            bot.send_message(call.message.chat.id, 'Вы выбрали Am9')
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                                      text="Вы выбрали Am9")

            am9p = open('bot_files/p_chords/A/am9.png', 'rb')

            bot.send_photo(call.message.chat.id, am9p)
            am9p.close()

    if call.message:
        if call.data == 'Am11':
            bot.send_message(call.message.chat.id, 'Вы выбрали Am11')
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                                      text="Вы выбрали Am11")

            am11p = open('bot_files/p_chords/A/am11.png', 'rb')

            bot.send_photo(call.message.chat.id, am11p)
            am11p.close()

    if call.message:
        if call.data == 'Am13':
            bot.send_message(call.message.chat.id, 'Вы выбрали Am13')
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                                      text="Вы выбрали Am13")

            am13p = open('bot_files/p_chords/A/am13.png', 'rb')

            bot.send_photo(call.message.chat.id, am13p)
            am13p.close()

    if call.message:
        if call.data == 'Am_maj7':
            bot.send_message(call.message.chat.id, 'Вы выбрали Am maj7')
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                                      text="Вы выбрали Am maj7")

            am_maj7p = open('bot_files/p_chords/A/aminmaj7.png', 'rb')

            bot.send_photo(call.message.chat.id, am_maj7p)
            am_maj7p.close()

    if call.message:
        if call.data == 'A_add2':
            bot.send_message(call.message.chat.id, 'Вы выбрали A add2 (A2)')
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                                      text="Вы выбрали A add2 (A2)")

            a_add2p = open('bot_files/p_chords/A/aadd2.png', 'rb')

            bot.send_photo(call.message.chat.id, a_add2p)
            a_add2p.close()

    if call.message:
        if call.data == 'A_add9':
            bot.send_message(call.message.chat.id, 'Вы выбрали A_add9')
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                                      text="Вы выбрали A_add9")

            a_add9p = open('bot_files/p_chords/A/aadd9.png', 'rb')

            bot.send_photo(call.message.chat.id, a_add9p)
            a_add9p.close()

    if call.message:
        if call.data == 'A_sus2':
            bot.send_message(call.message.chat.id, 'Вы выбрали A sus2')
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                                      text="Вы выбрали A sus2")

            a_sus2p = open('bot_files/p_chords/A/asus2.png', 'rb')

            bot.send_photo(call.message.chat.id, a_sus2p)
            a_sus2p.close()

    if call.message:
        if call.data == 'A_sus4':
            bot.send_message(call.message.chat.id, 'Вы выбрали A sus4')
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                                      text="Вы выбрали A sus4")

            a_sus4p = open('bot_files/p_chords/A/asus4.png', 'rb')

            bot.send_photo(call.message.chat.id, a_sus4p)
            a_sus4p.close()

    # A#Chords
    if call.message:
        if call.data == 'A#p':
            bot.send_message(call.message.chat.id, 'Вы выбрали А#/Bb (Ля диез / Си бемоль)')

            bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                                      text="Вы выбрали А#/Bb (Ля диез / Си бемоль)")

            chordsmarkup = types.InlineKeyboardMarkup(row_width=3)

            chord1 = types.InlineKeyboardButton("A#", callback_data="A#_major")
            chord2 = types.InlineKeyboardButton("A#m", callback_data="A#_minor")
            chord3 = types.InlineKeyboardButton("A#5", callback_data="A#5")
            chord4 = types.InlineKeyboardButton("A#6", callback_data="A#6")
            chord5 = types.InlineKeyboardButton("A#6 add9", callback_data="A#6_9")
            chord6 = types.InlineKeyboardButton("A#7", callback_data="A#7")
            chord7 = types.InlineKeyboardButton("A# maj7", callback_data="A#_maj7")
            chord8 = types.InlineKeyboardButton("A# maj9", callback_data="A#_maj9")
            chord9 = types.InlineKeyboardButton("A#7-5", callback_data="A#7-5")
            chord10 = types.InlineKeyboardButton("A#7+5", callback_data="A#7+5")
            chord11 = types.InlineKeyboardButton("A#9", callback_data="A#9")
            chord12 = types.InlineKeyboardButton("A#11", callback_data="A#11")
            chord13 = types.InlineKeyboardButton("A#13", callback_data="A#13")
            chord14 = types.InlineKeyboardButton("A# aug", callback_data="A#_aug")
            chord15 = types.InlineKeyboardButton("A# aug7", callback_data="A#_aug7")
            chord16 = types.InlineKeyboardButton("A# dim", callback_data="A#_dim")
            chord17 = types.InlineKeyboardButton("A# dim7", callback_data="A#_dim7")
            chord18 = types.InlineKeyboardButton("A#m6", callback_data="A#m6")
            chord19 = types.InlineKeyboardButton("A#m7", callback_data="A#m7")
            chord20 = types.InlineKeyboardButton("A#m7(b5)", callback_data="A#m7b5")
            chord21 = types.InlineKeyboardButton("A#m9", callback_data="A#m9")
            chord22 = types.InlineKeyboardButton("A#m11", callback_data="A#m11")
            chord23 = types.InlineKeyboardButton("A#m13", callback_data="A#m13")
            chord24 = types.InlineKeyboardButton("A#m maj7", callback_data="A#m_maj7")
            chord25 = types.InlineKeyboardButton("A# add2", callback_data="A#_add2")
            chord26 = types.InlineKeyboardButton("A# add9", callback_data="A#_add9")
            chord27 = types.InlineKeyboardButton("A# sus2", callback_data="A#_sus2")
            chord28 = types.InlineKeyboardButton("A# sus4", callback_data="A#_sus4")

            chordsmarkup.add(chord1, chord2, chord3, chord4, chord5, chord6, chord7, chord8, chord9, chord10, chord11,
                             chord12,
                             chord13, chord14, chord15, chord16, chord17, chord18, chord19, chord20, chord21, chord22,
                             chord23,
                             chord24, chord25, chord26, chord27, chord28)

            bot.send_message(call.message.chat.id, 'Выберите аккорд:', reply_markup=chordsmarkup)


    if call.message:
        if call.data == 'A#_major':
            bot.send_message(call.message.chat.id, 'Вы выбрали А# / Bb major(Ля диез / Си бемоль мажор)')
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                                      text="Вы выбрали А# / Bb major(Ля диез / Си бемоль мажор)")

            Bb_majorp = open('bot_files/p_chords/A#/a#.png', 'rb')

            bot.send_photo(call.message.chat.id, Bb_majorp)
            Bb_majorp.close()

    if call.message:
        if call.data == 'A#_minor':
            bot.send_message(call.message.chat.id, 'Вы выбрали А# / Bb minor(Ля диез / Си бемоль минор)')
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                                      text="Вы выбрали А# / Bb minor(Ля диез / Си бемоль минор)")

            Bb_minorp = open('bot_files/p_chords/A#/a#m.png', 'rb')

            bot.send_photo(call.message.chat.id, Bb_minorp)
            Bb_minorp.close()

    if call.message:
        if call.data == 'A#5':
            bot.send_message(call.message.chat.id, 'Вы выбрали А#5/Bb5')
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                                      text="Вы выбрали А#5/Bb5")

            Bb5p = open('bot_files/p_chords/A#/b_flat_5.png', 'rb')

            bot.send_photo(call.message.chat.id, Bb5p)
            Bb5p.close()

    if call.message:
        if call.data == 'A#6':
            bot.send_message(call.message.chat.id, 'Вы выбрали А#6/Bb6')
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                                      text="Вы выбрали А#6/Bb6")

            Bb6p = open('bot_files/p_chords/A#/b_flat_6.png', 'rb')

            bot.send_photo(call.message.chat.id, Bb6p)
            Bb6p.close()

    if call.message:
        if call.data == 'A#6_9':
            bot.send_message(call.message.chat.id, 'Вы выбрали А#6 add9/Bb6 add9')
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                                      text="Вы выбрали А#6 add9/Bb6 add9")

            Bb6_9p = open('bot_files/p_chords/A#/b_flat_6_9.png', 'rb')

            bot.send_photo(call.message.chat.id, Bb6_9p)
            Bb6_9p.close()

    if call.message:
        if call.data == 'A#7':
            bot.send_message(call.message.chat.id, 'Вы выбрали А#7/Bb7')
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                                      text="Вы выбрали А#7/Bb7")

            Bb7p = open('bot_files/p_chords/A#/b_flat_7.png', 'rb')

            bot.send_photo(call.message.chat.id, Bb7p)
            Bb7p.close()

    if call.message:
        if call.data == 'A#_maj7':
            bot.send_message(call.message.chat.id, 'Вы выбрали А# maj7/Bb maj7')
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                                      text="Вы выбрали А# maj7/Bb maj7")

            Bb_maj7p = open('bot_files/p_chords/A#/b_flat_maj7.png', 'rb')

            bot.send_photo(call.message.chat.id, Bb_maj7p)
            Bb_maj7p.close()

    if call.message:
        if call.data == 'A#_maj9':
            bot.send_message(call.message.chat.id, 'Вы выбрали А# maj9/Bb maj9')
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                                      text="Вы выбрали А# maj9/Bb maj9")

            Bb_maj9p = open('bot_files/p_chords/A#/b_flat_maj9.png', 'rb')

            bot.send_photo(call.message.chat.id, Bb_maj9p)
            Bb_maj9p.close()

    if call.message:
        if call.data == 'A#7-5':
            bot.send_message(call.message.chat.id, 'Вы выбрали А#7-5/Bb7-5')
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                                      text="Вы выбрали А#7-5/Bb7-5")

            Bb7min5p = open('bot_files/p_chords/A#/b_flat_7minus5.png', 'rb')

            bot.send_photo(call.message.chat.id, Bb7min5p)
            Bb7min5p.close()

    if call.message:
        if call.data == 'A#7+5':
            bot.send_message(call.message.chat.id, 'Вы выбрали А#7+5/Bb7+5')
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                                      text="Вы выбрали А#7+5/Bb7+5")

            Bb7plus5p = open('bot_files/p_chords/A#/b_flat_7plus5.png', 'rb')

            bot.send_photo(call.message.chat.id, Bb7plus5p)
            Bb7plus5p.close()

    if call.message:
        if call.data == 'A#9':
            bot.send_message(call.message.chat.id, 'Вы выбрали А#9/Bb9')
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                                      text="Вы выбрали А#9/Bb9")

            Bb9p = open('bot_files/p_chords/A#/b_flat_9.png', 'rb')

            bot.send_photo(call.message.chat.id, Bb9p)
            Bb9p.close()

    if call.message:
        if call.data == 'A#11':
            bot.send_message(call.message.chat.id, 'Вы выбрали А#11/Bb11')
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                                      text="Вы выбрали А#11/Bb11")

            Bb11p = open('bot_files/p_chords/A#/b_flat_11.png', 'rb')

            bot.send_photo(call.message.chat.id, Bb11p)
            Bb11p.close()

    if call.message:
        if call.data == 'A#13':
            bot.send_message(call.message.chat.id, 'Вы выбрали А#13/Bb13')
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                                      text="Вы выбрали А#13/Bb13")

            Bb13p = open('bot_files/p_chords/A#/b_flat_13.png', 'rb')

            bot.send_photo(call.message.chat.id, Bb13p)
            Bb13p.close()

    if call.message:
        if call.data == 'A#_aug':
            bot.send_message(call.message.chat.id, 'Вы выбрали А# aug/Bb aug')
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                                      text="Вы выбрали А# aug/Bb aug")

            Bb_augp = open('bot_files/p_chords/A#/b_flat_aug.png', 'rb')

            bot.send_photo(call.message.chat.id, Bb_augp)
            Bb_augp.close()

    if call.message:
        if call.data == 'A#_aug7':
            bot.send_message(call.message.chat.id, 'Вы выбрали А# aug7/Bb aug7')
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                                      text="Вы выбрали А# aug7/Bb aug7")

            Bb_aug7p = open('bot_files/p_chords/A#/b_flat_aug7.png', 'rb')

            bot.send_photo(call.message.chat.id, Bb_aug7p)
            Bb_aug7p.close()

    if call.message:
        if call.data == 'A#_dim':
            bot.send_message(call.message.chat.id, 'Вы выбрали А# dim/Bb dim')
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                                      text="Вы выбрали А# dim/Bb dim")

            Bb_dimp = open('bot_files/p_chords/A#/b_flat_dim.png', 'rb')

            bot.send_photo(call.message.chat.id, Bb_dimp)
            Bb_dimp.close()

    if call.message:
        if call.data == 'A#_dim7':
            bot.send_message(call.message.chat.id, 'Вы выбрали А# dim7/Bb dim7')
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                                      text="Вы выбрали А#9/Bb9")

            Bb_dim7p = open('bot_files/p_chords/A#/b_flat_dim7.png', 'rb')

            bot.send_photo(call.message.chat.id, Bb_dim7p)
            Bb_dim7p.close()

    if call.message:
        if call.data == 'A#m6':
            bot.send_message(call.message.chat.id, 'Вы выбрали А#m6/Bbm6')
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                                      text="Вы выбрали А#m6/Bbm6")

            Bbm6p = open('bot_files/p_chords/A#/b_flat_m6.png', 'rb')

            bot.send_photo(call.message.chat.id, Bbm6p)
            Bbm6p.close()

    if call.message:
        if call.data == 'A#m7':
            bot.send_message(call.message.chat.id, 'Вы выбрали А#m7/Bbm7')
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                                      text="Вы выбрали А#m7/Bbm7")

            Bbm7p = open('bot_files/p_chords/A#/b_flat_m7.png', 'rb')

            bot.send_photo(call.message.chat.id, Bbm7p)
            Bbm7p.close()

    if call.message:
        if call.data == 'A#m7b5':
            bot.send_message(call.message.chat.id, 'Вы выбрали А#m7b5/Bbm7b5')
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                                      text="Вы выбрали А#m7b5/Bbm7b5")

            Bbm7b5p = open('bot_files/p_chords/A#/b_flat_m7b5.png', 'rb')

            bot.send_photo(call.message.chat.id, Bbm7b5p)
            Bbm7b5p.close()

    if call.message:
        if call.data == 'A#m9':
            bot.send_message(call.message.chat.id, 'Вы выбрали А#m9/Bbm9')
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                                      text="Вы выбрали А#m9/Bbm9")

            Bbm9p = open('bot_files/p_chords/A#/b_flat_m9.png', 'rb')

            bot.send_photo(call.message.chat.id, Bbm9p)
            Bbm9p.close()

    if call.message:
        if call.data == 'A#m11':
            bot.send_message(call.message.chat.id, 'Вы выбрали А#m11/Bbm11')
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                                      text="Вы выбрали А#m11/Bbm11")

            Bbm11p = open('bot_files/p_chords/A#/b_flat_m11.png', 'rb')

            bot.send_photo(call.message.chat.id, Bbm11p)
            Bbm11p.close()

    if call.message:
        if call.data == 'A#m13':
            bot.send_message(call.message.chat.id, 'Вы выбрали А#m13/Bbm13')
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                                      text="Вы выбрали А#m13/Bbm13")

            Bbm13p = open('bot_files/p_chords/A#/b_flat_m13.png', 'rb')

            bot.send_photo(call.message.chat.id, Bbm13p)
            Bbm13p.close()

    if call.message:
        if call.data == 'A#m_maj7':
            bot.send_message(call.message.chat.id, 'Вы выбрали А#m maj7/Bbm maj7')
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                                      text="Вы выбрали А#m maj7/Bbm maj7")

            Bbm_maj7p = open('bot_files/p_chords/A#/b_flat_minmaj7.png', 'rb')

            bot.send_photo(call.message.chat.id, Bbm_maj7p)
            Bbm_maj7p.close()

    if call.message:
        if call.data == 'A#_add2':
            bot.send_message(call.message.chat.id, 'Вы выбрали А# add2/Bb add2')
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                                      text="Вы выбрали А# add2/Bb add2")

            Bb_add2p = open('bot_files/p_chords/A#/b_flat_add2.png', 'rb')

            bot.send_photo(call.message.chat.id, Bb_add2p)
            Bb_add2p.close()

    if call.message:
        if call.data == 'A#_add9':
            bot.send_message(call.message.chat.id, 'Вы выбрали А# add9/Bb add9')
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                                      text="Вы выбрали А# add9/Bb add9")

            Bb_add9p = open('bot_files/p_chords/A#/b_flat_add9.png', 'rb')

            bot.send_photo(call.message.chat.id, Bb_add9p)
            Bb_add9p.close()

    if call.message:
        if call.data == 'A#_sus2':
            bot.send_message(call.message.chat.id, 'Вы выбрали А# sus2/Bb sus2')
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                                      text="Вы выбрали А# sus2/Bb sus2")

            Bb_sus2p = open('bot_files/p_chords/A#/b_flat_sus2.png', 'rb')

            bot.send_photo(call.message.chat.id, Bb_sus2p)
            Bb_sus2p.close()

    if call.message:
        if call.data == 'A#_sus4':
            bot.send_message(call.message.chat.id, 'Вы выбрали А# sus4/Bb sus4')
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                                      text="Вы выбрали А# sus4/Bb sus4")

            Bb_sus4p = open('bot_files/p_chords/A#/b_flat_sus4.png', 'rb')

            bot.send_photo(call.message.chat.id, Bb_sus4p)
            Bb_sus4p.close()

    #Bchords
    if call.message:
        if call.data == 'Bp':
            bot.send_message(call.message.chat.id, 'Вы выбрали B (Си)')

            bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                                      text="Вы выбрали B (Си)")

            chordsmarkup = types.InlineKeyboardMarkup(row_width=3)

            chord1 = types.InlineKeyboardButton("B", callback_data="B_major")
            chord2 = types.InlineKeyboardButton("Bm", callback_data="B_minor")
            chord3 = types.InlineKeyboardButton("B5", callback_data="B5")
            chord4 = types.InlineKeyboardButton("B6", callback_data="B6")
            chord5 = types.InlineKeyboardButton("B6 add9", callback_data="B6_9")
            chord6 = types.InlineKeyboardButton("B7", callback_data="B7")
            chord7 = types.InlineKeyboardButton("B maj7", callback_data="B_maj7")
            chord8 = types.InlineKeyboardButton("B maj9", callback_data="B_maj9")
            chord9 = types.InlineKeyboardButton("B7-5", callback_data="B7-5")
            chord10 = types.InlineKeyboardButton("B7+5", callback_data="B7+5")
            chord11 = types.InlineKeyboardButton("B9", callback_data="B9")
            chord12 = types.InlineKeyboardButton("B11", callback_data="B11")
            chord13 = types.InlineKeyboardButton("B13", callback_data="B13")
            chord14 = types.InlineKeyboardButton("B aug", callback_data="B_aug")
            chord15 = types.InlineKeyboardButton("B aug7", callback_data="B_aug7")
            chord16 = types.InlineKeyboardButton("B dim", callback_data="B_dim")
            chord17 = types.InlineKeyboardButton("B dim7", callback_data="B_dim7")
            chord18 = types.InlineKeyboardButton("Bm6", callback_data="Bm6")
            chord19 = types.InlineKeyboardButton("Bm7", callback_data="Bm7")
            chord20 = types.InlineKeyboardButton("Bm7(b5)", callback_data="Bm7b5")
            chord21 = types.InlineKeyboardButton("Bm9", callback_data="Bm9")
            chord22 = types.InlineKeyboardButton("Bm11", callback_data="Bm11")
            chord23 = types.InlineKeyboardButton("Bm13", callback_data="Bm13")
            chord24 = types.InlineKeyboardButton("Bm maj7", callback_data="Bm_maj7")
            chord25 = types.InlineKeyboardButton("B add2", callback_data="B_add2")
            chord26 = types.InlineKeyboardButton("B add9", callback_data="B_add9")
            chord27 = types.InlineKeyboardButton("B sus2", callback_data="B_sus2")
            chord28 = types.InlineKeyboardButton("B sus4", callback_data="B_sus4")

            chordsmarkup.add(chord1, chord2, chord3, chord4, chord5, chord6, chord7, chord8, chord9, chord10, chord11,
                             chord12,
                             chord13, chord14, chord15, chord16, chord17, chord18, chord19, chord20, chord21, chord22,
                             chord23,
                             chord24, chord25, chord26, chord27, chord28)

            bot.send_message(call.message.chat.id, 'Выберите аккорд:', reply_markup=chordsmarkup)

    if call.message:
        if call.data == 'B_major':
            bot.send_message(call.message.chat.id, 'Вы выбрали B major (Си мажор)')
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                                      text="Вы выбрали B major (Си мажор)")

            B_majorp = open('bot_files/p_chords/B/b.png', 'rb')

            bot.send_photo(call.message.chat.id, B_majorp)
            B_majorp.close()

    if call.message:
        if call.data == 'B_minor':
            bot.send_message(call.message.chat.id, 'Вы выбрали B minor (Си минор)')
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                                      text="Вы выбрали B minor (Си минор)")

            B_minor = open('bot_files/p_chords/B/bm.png', 'rb')

            bot.send_photo(call.message.chat.id, B_minor)
            B_minor.close()

    if call.message:
        if call.data == 'B5':
            bot.send_message(call.message.chat.id, 'Вы выбрали B5')
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                                      text="Вы выбрали B5")

            B5p = open('bot_files/p_chords/B/b5.png', 'rb')

            bot.send_photo(call.message.chat.id, B5p)
            B5p.close()

    if call.message:
        if call.data == 'B6':
            bot.send_message(call.message.chat.id, 'Вы выбрали B6')
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                                      text="Вы выбрали B6")

            B6p = open('bot_files/p_chords/B/b6.png', 'rb')

            bot.send_photo(call.message.chat.id, B6p)
            B6p.close()

    if call.message:
        if call.data == 'B6_9':
            bot.send_message(call.message.chat.id, 'Вы выбрали B6 add9 ')
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                                      text="Вы выбрали B6 add9")

            B6add9p = open('bot_files/p_chords/B/b6_9.png', 'rb')

            bot.send_photo(call.message.chat.id, B6add9p)
            B6add9p.close()

    if call.message:
        if call.data == 'B7':
            bot.send_message(call.message.chat.id, 'Вы выбрали B7')
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                                      text="Вы выбрали B7")

            B7p = open('bot_files/p_chords/B/b7.png', 'rb')

            bot.send_photo(call.message.chat.id, B7p)
            B7p.close()

    if call.message:
        if call.data == 'B_maj7':
            bot.send_message(call.message.chat.id, 'Вы выбрали B maj7')
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                                      text="Вы выбрали B maj7")

            B_maj7p = open('bot_files/p_chords/B/bmaj7.png', 'rb')

            bot.send_photo(call.message.chat.id, B_maj7p)
            B_maj7p.close()

    if call.message:
        if call.data == 'B_maj9':
            bot.send_message(call.message.chat.id, 'Вы выбрали B maj9')
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                                      text="Вы выбрали B maj9")

            B_maj9p = open('bot_files/p_chords/B/bmaj9.png', 'rb')

            bot.send_photo(call.message.chat.id, B_maj9p)
            B_maj9p.close()

    if call.message:
        if call.data == 'B7-5':
            bot.send_message(call.message.chat.id, 'Вы выбрали B7-5')
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                                      text="Вы выбрали B7-5")

            B7min5p = open('bot_files/p_chords/B/b7minus5.png', 'rb')

            bot.send_photo(call.message.chat.id, B7min5p)
            B7min5p.close()

    if call.message:
        if call.data == 'B7+5':
            bot.send_message(call.message.chat.id, 'Вы выбрали B7+5')
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                                      text="Вы выбрали B7+5")

            B7plus5p = open('bot_files/p_chords/B/b7plus5.png', 'rb')

            bot.send_photo(call.message.chat.id, B7plus5p)
            B7plus5p.close()

    if call.message:
        if call.data == 'B9':
            bot.send_message(call.message.chat.id, 'Вы выбрали B9')
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                                      text="Вы выбрали B9")

            B9p = open('bot_files/p_chords/B/b9.png', 'rb')

            bot.send_photo(call.message.chat.id, B9p)
            B9p.close()

    if call.message:
        if call.data == 'B11':
            bot.send_message(call.message.chat.id, 'Вы выбрали B11')
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                                      text="Вы выбрали B11")

            B11p = open('bot_files/p_chords/B/b11.png', 'rb')

            bot.send_photo(call.message.chat.id, B11p)
            B11p.close()

    if call.message:
        if call.data == 'B13':
            bot.send_message(call.message.chat.id, 'Вы выбрали B13')
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                                      text="Вы выбрали B13")

            B13p = open('bot_files/p_chords/B/b13.png', 'rb')

            bot.send_photo(call.message.chat.id, B13p)
            B13p.close()

    if call.message:
        if call.data == 'B_aug':
            bot.send_message(call.message.chat.id, 'Вы выбрали B aug')
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                                      text="Вы выбрали B aug")

            B_augp = open('bot_files/p_chords/B/baug.png', 'rb')

            bot.send_photo(call.message.chat.id, B_augp)
            B_augp.close()

    if call.message:
        if call.data == 'B_aug7':
            bot.send_message(call.message.chat.id, 'Вы выбрали B_aug7')
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                                      text="Вы выбрали B_aug7")

            B_aug7p = open('bot_files/p_chords/B/baug7.png', 'rb')

            bot.send_photo(call.message.chat.id, B_aug7p)
            B_aug7p.close()

    if call.message:
        if call.data == 'B_dim':
            bot.send_message(call.message.chat.id, 'Вы выбрали B dim')
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                                      text="Вы выбрали B dim")

            B_dimp = open('bot_files/p_chords/B/bdim.png', 'rb')

            bot.send_photo(call.message.chat.id, B_dimp)
            B_dimp.close()

    if call.message:
        if call.data == 'B_dim7':
            bot.send_message(call.message.chat.id, 'Вы выбрали B dim7')
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                                      text="Вы выбрали B dim7")

            B_dim7p = open('bot_files/p_chords/B/bdim7.png', 'rb')

            bot.send_photo(call.message.chat.id, B_dim7p)
            B_dim7p.close()

    if call.message:
        if call.data == 'Bm6':
            bot.send_message(call.message.chat.id, 'Вы выбрали Bm6')
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                                      text="Вы выбрали Bm6")

            Bm6p = open('bot_files/p_chords/B/bm6.png', 'rb')

            bot.send_photo(call.message.chat.id, Bm6p)
            Bm6p.close()

    if call.message:
        if call.data == 'Bm7':
            bot.send_message(call.message.chat.id, 'Вы выбрали Bm7')
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                                      text="Вы выбрали Bm7")

            Bm7p = open('bot_files/p_chords/B/bm7.png', 'rb')

            bot.send_photo(call.message.chat.id, Bm7p)
            Bm7p.close()

    if call.message:
        if call.data == 'Bm7b5':
            bot.send_message(call.message.chat.id, 'Вы выбрали Bm7(b5)')
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                                      text="Вы выбрали Bm7(b5)")

            Bm7b5p = open('bot_files/p_chords/B/bm7b5.png', 'rb')

            bot.send_photo(call.message.chat.id, Bm7b5p)
            Bm7b5p.close()

    if call.message:
        if call.data == 'Bm9':
            bot.send_message(call.message.chat.id, 'Вы выбрали Bm9')
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                                      text="Вы выбрали Bm9")

            Bm9p = open('bot_files/p_chords/B/bm9.png', 'rb')

            bot.send_photo(call.message.chat.id, Bm9p)
            Bm9p.close()

    if call.message:
        if call.data == 'Bm11':
            bot.send_message(call.message.chat.id, 'Вы выбрали Bm11')
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                                      text="Вы выбрали Bm11")

            Bm11p = open('bot_files/p_chords/B/bm11.png', 'rb')

            bot.send_photo(call.message.chat.id, Bm11p)
            Bm11p.close()

    if call.message:
        if call.data == 'Bm13':
            bot.send_message(call.message.chat.id, 'Вы выбрали Bm13')
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                                      text="Вы выбрали Bm13")

            Bm13p = open('bot_files/p_chords/B/bm13.png', 'rb')

            bot.send_photo(call.message.chat.id, Bm13p)
            Bm13p.close()

    if call.message:
        if call.data == 'Bm_maj7':
            bot.send_message(call.message.chat.id, 'Вы выбрали Bm maj7')
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                                      text="Вы выбрали Bm maj7")

            Bm_maj7p = open('bot_files/p_chords/B/bminmaj7.png', 'rb')

            bot.send_photo(call.message.chat.id, Bm_maj7p)
            Bm_maj7p.close()

    if call.message:
        if call.data == 'B_add2':
            bot.send_message(call.message.chat.id, 'Вы выбрали B add2')
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                                      text="Вы выбрали B add2")

            B_add2p = open('bot_files/p_chords/B/badd2.png', 'rb')

            bot.send_photo(call.message.chat.id, B_add2p)
            B_add2p.close()

    if call.message:
        if call.data == 'B_add4':
            bot.send_message(call.message.chat.id, 'Вы выбрали B add4')
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                                      text="Вы выбрали B add4")

            B_add4p = open('bot_files/p_chords/B/badd4.png', 'rb')

            bot.send_photo(call.message.chat.id, B_add4p)
            B_add4p.close()

    if call.message:
        if call.data == 'B_sus2':
            bot.send_message(call.message.chat.id, 'Вы выбрали B sus2')
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                                      text="Вы выбрали B sus2")

            B_sus2p = open('bot_files/p_chords/B/bsus2.png', 'rb')

            bot.send_photo(call.message.chat.id, B_sus2p)
            B_sus2p.close()

    if call.message:
        if call.data == 'B_sus4':
            bot.send_message(call.message.chat.id, 'Вы выбрали B sus4')
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                                      text="Вы выбрали B sus4")

            B_sus4p = open('bot_files/p_chords/B/bsus4.png', 'rb')

            bot.send_photo(call.message.chat.id, B_sus4p)
            B_sus4p.close()

#Cchords
    if call.message:
        if call.data == 'Cp':
            bot.send_message(call.message.chat.id, 'Вы выбрали C (До)')

            bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                                      text="Вы выбрали C (До)")

            chordsmarkup = types.InlineKeyboardMarkup(row_width=3)

            chord1 = types.InlineKeyboardButton("C", callback_data="C_major")
            chord2 = types.InlineKeyboardButton("Cm", callback_data="C_minor")
            chord3 = types.InlineKeyboardButton("C5", callback_data="C5")
            chord4 = types.InlineKeyboardButton("C6", callback_data="C6")
            chord5 = types.InlineKeyboardButton("C6 add9", callback_data="C6_9")
            chord6 = types.InlineKeyboardButton("C7", callback_data="C7")
            chord7 = types.InlineKeyboardButton("C maj7", callback_data="C_maj7")
            chord8 = types.InlineKeyboardButton("C maj9", callback_data="C_maj9")
            chord9 = types.InlineKeyboardButton("C7-5", callback_data="C7-5")
            chord10 = types.InlineKeyboardButton("C7+5", callback_data="C7+5")
            chord11 = types.InlineKeyboardButton("C9", callback_data="C9")
            chord12 = types.InlineKeyboardButton("C11", callback_data="C11")
            chord13 = types.InlineKeyboardButton("C13", callback_data="C13")
            chord14 = types.InlineKeyboardButton("C aug", callback_data="C_aug")
            chord15 = types.InlineKeyboardButton("C aug7", callback_data="C_aug7")
            chord16 = types.InlineKeyboardButton("C dim", callback_data="C_dim")
            chord17 = types.InlineKeyboardButton("C dim7", callback_data="C_dim7")
            chord18 = types.InlineKeyboardButton("Cm6", callback_data="Cm6")
            chord19 = types.InlineKeyboardButton("Cm7", callback_data="Cm7")
            chord20 = types.InlineKeyboardButton("Cm7(b5)", callback_data="Cm7b5")
            chord21 = types.InlineKeyboardButton("Cm9", callback_data="Cm9")
            chord22 = types.InlineKeyboardButton("Cm11", callback_data="Cm11")
            chord23 = types.InlineKeyboardButton("Cm13", callback_data="Cm13")
            chord24 = types.InlineKeyboardButton("Cm maj7", callback_data="Cm_maj7")
            chord25 = types.InlineKeyboardButton("C add2", callback_data="C_add2")
            chord26 = types.InlineKeyboardButton("C add9", callback_data="C_add9")
            chord27 = types.InlineKeyboardButton("C sus2", callback_data="C_sus2")
            chord28 = types.InlineKeyboardButton("C sus4", callback_data="C_sus4")

            chordsmarkup.add(chord1, chord2, chord3, chord4, chord5, chord6, chord7, chord8, chord9, chord10, chord11,
                             chord12,
                             chord13, chord14, chord15, chord16, chord17, chord18, chord19, chord20, chord21, chord22,
                             chord23,
                             chord24, chord25, chord26, chord27, chord28)

            bot.send_message(call.message.chat.id, 'Выберите аккорд:', reply_markup=chordsmarkup)

    if call.message:
        if call.data == 'C_major':
            bot.send_message(call.message.chat.id, 'Вы выбрали C major (До мажор)')
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                                      text="Вы выбрали C major (До мажор)")

            C_majorp = open('bot_files/p_chords/C/c.png', 'rb')

            bot.send_photo(call.message.chat.id, C_majorp)
            C_majorp.close()

    if call.message:
        if call.data == 'C_minor':
            bot.send_message(call.message.chat.id, 'Вы выбрали C minor (До минор)')
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                                      text="Вы выбрали C minor (До минор)")

            C_minor = open('bot_files/p_chords/C/cm.png', 'rb')

            bot.send_photo(call.message.chat.id, C_minor)
            C_minor.close()

    if call.message:
        if call.data == 'C5':
            bot.send_message(call.message.chat.id, 'Вы выбрали C5')
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                                      text="Вы выбрали C5")

            C5p = open('bot_files/p_chords/C/c5.png', 'rb')

            bot.send_photo(call.message.chat.id, C5p)
            C5p.close()

    if call.message:
        if call.data == 'C6':
            bot.send_message(call.message.chat.id, 'Вы выбрали C6')
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                                      text="Вы выбрали C6")

            C6p = open('bot_files/p_chords/C/c6.png', 'rb')

            bot.send_photo(call.message.chat.id, C6p)
            C6p.close()

    if call.message:
        if call.data == 'C6_9':
            bot.send_message(call.message.chat.id, 'Вы выбрали C6 add9 ')
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                                      text="Вы выбрали C6 add9")

            C6add9p = open('bot_files/p_chords/C/c6_9.png', 'rb')

            bot.send_photo(call.message.chat.id, C6add9p)
            C6add9p.close()

    if call.message:
        if call.data == 'C7':
            bot.send_message(call.message.chat.id, 'Вы выбрали C7')
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                                      text="Вы выбрали C7")

            C7p = open('bot_files/p_chords/C/c7.png', 'rb')

            bot.send_photo(call.message.chat.id, C7p)
            C7p.close()

    if call.message:
        if call.data == 'C_maj7':
            bot.send_message(call.message.chat.id, 'Вы выбрали C maj7')
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                                      text="Вы выбрали C maj7")

            C_maj7p = open('bot_files/p_chords/C/cmaj7.png', 'rb')

            bot.send_photo(call.message.chat.id, C_maj7p)
            C_maj7p.close()

    if call.message:
        if call.data == 'C_maj9':
            bot.send_message(call.message.chat.id, 'Вы выбрали C maj9')
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                                      text="Вы выбрали C maj9")

            C_maj9p = open('bot_files/p_chords/C/cmaj9.png', 'rb')

            bot.send_photo(call.message.chat.id, C_maj9p)
            C_maj9p.close()

    if call.message:
        if call.data == 'C7-5':
            bot.send_message(call.message.chat.id, 'Вы выбрали C7-5')
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                                      text="Вы выбрали C7-5")

            C7min5p = open('bot_files/p_chords/C/c7minus5.png', 'rb')

            bot.send_photo(call.message.chat.id, C7min5p)
            C7min5p.close()

    if call.message:
        if call.data == 'C7+5':
            bot.send_message(call.message.chat.id, 'Вы выбрали C7+5')
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                                      text="Вы выбрали C7+5")

            C7plus5p = open('bot_files/p_chords/C/c7plus5.png', 'rb')

            bot.send_photo(call.message.chat.id, C7plus5p)
            C7plus5p.close()

    if call.message:
        if call.data == 'C9':
            bot.send_message(call.message.chat.id, 'Вы выбрали C9')
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                                      text="Вы выбрали C9")

            C9p = open('bot_files/p_chords/C/c9.png', 'rb')

            bot.send_photo(call.message.chat.id, C9p)
            C9p.close()

    if call.message:
        if call.data == 'C11':
            bot.send_message(call.message.chat.id, 'Вы выбрали C11')
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                                      text="Вы выбрали C11")

            C11p = open('bot_files/p_chords/C/c11.png', 'rb')

            bot.send_photo(call.message.chat.id, C11p)
            C11p.close()

    if call.message:
        if call.data == 'C13':
            bot.send_message(call.message.chat.id, 'Вы выбрали C13')
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                                      text="Вы выбрали C13")

            C13p = open('bot_files/p_chords/C/c13.png', 'rb')

            bot.send_photo(call.message.chat.id, C13p)
            C13p.close()

    if call.message:
        if call.data == 'C_aug':
            bot.send_message(call.message.chat.id, 'Вы выбрали C aug')
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                                      text="Вы выбрали C aug")

            C_augp = open('bot_files/p_chords/C/caug.png', 'rb')

            bot.send_photo(call.message.chat.id, C_augp)
            C_augp.close()

    if call.message:
        if call.data == 'C_aug7':
            bot.send_message(call.message.chat.id, 'Вы выбрали C_aug7')
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                                      text="Вы выбрали C_aug7")

            C_aug7p = open('bot_files/p_chords/C/caug7.png', 'rb')

            bot.send_photo(call.message.chat.id, C_aug7p)
            C_aug7p.close()

    if call.message:
        if call.data == 'C_dim':
            bot.send_message(call.message.chat.id, 'Вы выбрали C dim')
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                                      text="Вы выбрали C dim")

            C_dimp = open('bot_files/p_chords/C/cdim.png', 'rb')

            bot.send_photo(call.message.chat.id, C_dimp)
            C_dimp.close()

    if call.message:
        if call.data == 'C_dim7':
            bot.send_message(call.message.chat.id, 'Вы выбрали C dim7')
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                                      text="Вы выбрали C dim7")

            C_dim7p = open('bot_files/p_chords/C/cdim7.png', 'rb')

            bot.send_photo(call.message.chat.id, C_dim7p)
            C_dim7p.close()

    if call.message:
        if call.data == 'Cm6':
            bot.send_message(call.message.chat.id, 'Вы выбрали Cm6')
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                                      text="Вы выбрали Cm6")

            Cm6p = open('bot_files/p_chords/C/cm6.png', 'rb')

            bot.send_photo(call.message.chat.id, Cm6p)
            Cm6p.close()

    if call.message:
        if call.data == 'Cm7':
            bot.send_message(call.message.chat.id, 'Вы выбрали Cm7')
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                                      text="Вы выбрали Cm7")

            Cm7p = open('bot_files/p_chords/C/cm7.png', 'rb')

            bot.send_photo(call.message.chat.id, Cm7p)
            Cm7p.close()

    if call.message:
        if call.data == 'Cm7b5':
            bot.send_message(call.message.chat.id, 'Вы выбрали Cm7(b5)')
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                                      text="Вы выбрали Cm7(b5)")

            Cm7b5p = open('bot_files/p_chords/C/cm7b5.png', 'rb')

            bot.send_photo(call.message.chat.id, Cm7b5p)
            Cm7b5p.close()

    if call.message:
        if call.data == 'Cm9':
            bot.send_message(call.message.chat.id, 'Вы выбрали Cm9')
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                                      text="Вы выбрали Cm9")

            Cm9p = open('bot_files/p_chords/C/cm9.png', 'rb')

            bot.send_photo(call.message.chat.id, Cm9p)
            Cm9p.close()

    if call.message:
        if call.data == 'Cm11':
            bot.send_message(call.message.chat.id, 'Вы выбрали Cm11')
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                                      text="Вы выбрали Cm11")

            Cm11p = open('bot_files/p_chords/C/cm11.png', 'rb')

            bot.send_photo(call.message.chat.id, Cm11p)
            Cm11p.close()

    if call.message:
        if call.data == 'Cm13':
            bot.send_message(call.message.chat.id, 'Вы выбрали Cm13')
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                                      text="Вы выбрали Cm13")

            Cm13p = open('bot_files/p_chords/C/cm13.png', 'rb')

            bot.send_photo(call.message.chat.id, Cm13p)
            Cm13p.close()

    if call.message:
        if call.data == 'Cm_maj7':
            bot.send_message(call.message.chat.id, 'Вы выбрали Cm maj7')
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                                      text="Вы выбрали Cm maj7")

            Cm_maj7p = open('bot_files/p_chords/C/cminmaj7.png', 'rb')

            bot.send_photo(call.message.chat.id, Cm_maj7p)
            Cm_maj7p.close()

    if call.message:
        if call.data == 'C_add2':
            bot.send_message(call.message.chat.id, 'Вы выбрали C add2')
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                                      text="Вы выбрали C add2")

            C_add2p = open('bot_files/p_chords/C/cadd2.png', 'rb')

            bot.send_photo(call.message.chat.id, C_add2p)
            C_add2p.close()

    if call.message:
        if call.data == 'C_add4':
            bot.send_message(call.message.chat.id, 'Вы выбрали C add4')
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                                      text="Вы выбрали C add4")

            C_add4p = open('bot_files/p_chords/C/cadd4.png', 'rb')

            bot.send_photo(call.message.chat.id, C_add4p)
            C_add4p.close()

    if call.message:
        if call.data == 'C_sus2':
            bot.send_message(call.message.chat.id, 'Вы выбрали C sus2')
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                                      text="Вы выбрали C sus2")

            C_sus2p = open('bot_files/p_chords/C/csus2.png', 'rb')

            bot.send_photo(call.message.chat.id, C_sus2p)
            C_sus2p.close()

    if call.message:
        if call.data == 'C_sus4':
            bot.send_message(call.message.chat.id, 'Вы выбрали C sus4')
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                                      text="Вы выбрали C sus4")

            C_sus4p = open('bot_files/p_chords/C/csus4.png', 'rb')

            bot.send_photo(call.message.chat.id, C_sus4p)
            C_sus4p.close()

#C#chords
    if call.message:
        if call.data == 'C#p':
            bot.send_message(call.message.chat.id, 'Вы выбрали C# (До диез)')

            bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                                      text="Вы выбрали C# (До диез)")

            chordsmarkup = types.InlineKeyboardMarkup(row_width=3)

            chord1 = types.InlineKeyboardButton("C#", callback_data="C#_major")
            chord2 = types.InlineKeyboardButton("C#m", callback_data="C#_minor")
            chord3 = types.InlineKeyboardButton("C#5", callback_data="C#5")
            chord4 = types.InlineKeyboardButton("C#6", callback_data="C#6")
            chord5 = types.InlineKeyboardButton("C#6 add9", callback_data="C#6_9")
            chord6 = types.InlineKeyboardButton("C#7", callback_data="C#7")
            chord7 = types.InlineKeyboardButton("C# maj7", callback_data="C#_maj7")
            chord8 = types.InlineKeyboardButton("C# maj9", callback_data="C#_maj9")
            chord9 = types.InlineKeyboardButton("C#7-5", callback_data="C#7-5")
            chord10 = types.InlineKeyboardButton("C#7+5", callback_data="C#7+5")
            chord11 = types.InlineKeyboardButton("C#9", callback_data="C#9")
            chord12 = types.InlineKeyboardButton("C#11", callback_data="C#11")
            chord13 = types.InlineKeyboardButton("C#13", callback_data="C#13")
            chord14 = types.InlineKeyboardButton("C# aug", callback_data="C#_aug")
            chord15 = types.InlineKeyboardButton("C# aug7", callback_data="C#_aug7")
            chord16 = types.InlineKeyboardButton("C# dim", callback_data="C#_dim")
            chord17 = types.InlineKeyboardButton("C# dim7", callback_data="C#_dim7")
            chord18 = types.InlineKeyboardButton("C#m6", callback_data="C#m6")
            chord19 = types.InlineKeyboardButton("C#m7", callback_data="C#m7")
            chord20 = types.InlineKeyboardButton("C#m7(b5)", callback_data="C#m7b5")
            chord21 = types.InlineKeyboardButton("C#m9", callback_data="C#m9")
            chord22 = types.InlineKeyboardButton("C#m11", callback_data="C#m11")
            chord23 = types.InlineKeyboardButton("C#m13", callback_data="C#m13")
            chord24 = types.InlineKeyboardButton("C#m maj7", callback_data="C#m_maj7")
            chord25 = types.InlineKeyboardButton("C# add2", callback_data="C#_add2")
            chord26 = types.InlineKeyboardButton("C# add9", callback_data="C#_add9")
            chord27 = types.InlineKeyboardButton("C# sus2", callback_data="C#_sus2")
            chord28 = types.InlineKeyboardButton("C# sus4", callback_data="C#_sus4")

            chordsmarkup.add(chord1, chord2, chord3, chord4, chord5, chord6, chord7, chord8, chord9, chord10, chord11,
                             chord12,
                             chord13, chord14, chord15, chord16, chord17, chord18, chord19, chord20, chord21, chord22,
                             chord23,
                             chord24, chord25, chord26, chord27, chord28)

            bot.send_message(call.message.chat.id, 'Выберите аккорд:', reply_markup=chordsmarkup)

    if call.message:
        if call.data == 'C#_major':
            bot.send_message(call.message.chat.id, 'Вы выбрали C# major (До диез мажор)')
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                                      text="Вы выбрали C# major (До диез мажор)")

            Dd_majorp = open('bot_files/p_chords/C#/c#.png', 'rb')

            bot.send_photo(call.message.chat.id, Dd_majorp)
            Dd_majorp.close()

    if call.message:
        if call.data == 'C#_minor':
            bot.send_message(call.message.chat.id, 'Вы выбрали C# minor (До диез минор)')
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                                      text="Вы выбрали C# minor (До диез минор)")

            C_minor = open('bot_files/p_chords/C#/c#m.png', 'rb')

            bot.send_photo(call.message.chat.id, C_minor)
            C_minor.close()

    if call.message:
        if call.data == 'C#5':
            bot.send_message(call.message.chat.id, 'Вы выбрали C#5')
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                                      text="Вы выбрали C#5")

            Dd5p = open('bot_files/p_chords/C#/d_flat_5.png', 'rb')

            bot.send_photo(call.message.chat.id, Dd5p)
            Dd5p.close()

    if call.message:
        if call.data == 'C#6':
            bot.send_message(call.message.chat.id, 'Вы выбрали C#6')
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                                      text="Вы выбрали C#6")

            Dd6p = open('bot_files/p_chords/C#/d_flat_6.png', 'rb')

            bot.send_photo(call.message.chat.id, Dd6p)
            Dd6p.close()

    if call.message:
        if call.data == 'C#6_9':
            bot.send_message(call.message.chat.id, 'Вы выбрали C#6 add9 ')
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                                      text="Вы выбрали C#6 add9")

            Dd6add9p = open('bot_files/p_chords/C#/d_flat_6_9.png', 'rb')

            bot.send_photo(call.message.chat.id, Dd6add9p)
            Dd6add9p.close()

    if call.message:
        if call.data == 'C#7':
            bot.send_message(call.message.chat.id, 'Вы выбрали C#7')
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                                      text="Вы выбрали C#7")

            Dd7p = open('bot_files/p_chords/C#/d_flat_7.png', 'rb')

            bot.send_photo(call.message.chat.id, Dd7p)
            Dd7p.close()

    if call.message:
        if call.data == 'C#_maj7':
            bot.send_message(call.message.chat.id, 'Вы выбрали C# maj7')
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                                      text="Вы выбрали C# maj7")

            Dd_maj7p = open('bot_files/p_chords/C#/d_flat_maj7.png', 'rb')

            bot.send_photo(call.message.chat.id, Dd_maj7p)
            Dd_maj7p.close()

    if call.message:
        if call.data == 'C#_maj9':
            bot.send_message(call.message.chat.id, 'Вы выбрали C# maj9')
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                                      text="Вы выбрали C# maj9")

            Dd_maj9p = open('bot_files/p_chords/C#/d_flat_maj9.png', 'rb')

            bot.send_photo(call.message.chat.id, Dd_maj9p)
            Dd_maj9p.close()

    if call.message:
        if call.data == 'C#7-5':
            bot.send_message(call.message.chat.id, 'Вы выбрали C#7-5')
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                                      text="Вы выбрали C#7-5")

            Dd7min5p = open('bot_files/p_chords/C#/d_flat_7minus5.png', 'rb')

            bot.send_photo(call.message.chat.id, Dd7min5p)
            Dd7min5p.close()

    if call.message:
        if call.data == 'C#7+5':
            bot.send_message(call.message.chat.id, 'Вы выбрали C#7+5')
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                                      text="Вы выбрали C#7+5")

            Dd7plus5p = open('bot_files/p_chords/C/d_flat_7plus5.png', 'rb')

            bot.send_photo(call.message.chat.id, Dd7plus5p)
            Dd7plus5p.close()

    if call.message:
        if call.data == 'C#9':
            bot.send_message(call.message.chat.id, 'Вы выбрали C#9')
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                                      text="Вы выбрали C#9")

            Dd9p = open('bot_files/p_chords/C#/d_flat_9.png', 'rb')

            bot.send_photo(call.message.chat.id, Dd9p)
            Dd9p.close()

    if call.message:
        if call.data == 'C#11':
            bot.send_message(call.message.chat.id, 'Вы выбрали C#11')
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                                      text="Вы выбрали C#11")

            Dd11p = open('bot_files/p_chords/C#/d_flat_11.png', 'rb')

            bot.send_photo(call.message.chat.id, Dd11p)
            Dd11p.close()

    if call.message:
        if call.data == 'C#13':
            bot.send_message(call.message.chat.id, 'Вы выбрали C#13')
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                                      text="Вы выбрали C#13")

            Dd13p = open('bot_files/p_chords/C#/d_flat_13.png', 'rb')

            bot.send_photo(call.message.chat.id, Dd13p)
            Dd13p.close()

    if call.message:
        if call.data == 'C#_aug':
            bot.send_message(call.message.chat.id, 'Вы выбрали C# aug')
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                                      text="Вы выбрали C# aug")

            Dd_augp = open('bot_files/p_chords/C#/d_flat_aug.png', 'rb')

            bot.send_photo(call.message.chat.id, Dd_augp)
            Dd_augp.close()

    if call.message:
        if call.data == 'C#_aug7':
            bot.send_message(call.message.chat.id, 'Вы выбрали C#_aug7')
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                                      text="Вы выбрали C#_aug7")

            Dd_aug7p = open('bot_files/p_chords/C#/d_flat_aug7.png', 'rb')

            bot.send_photo(call.message.chat.id, Dd_aug7p)
            Dd_aug7p.close()

    if call.message:
        if call.data == 'C#_dim':
            bot.send_message(call.message.chat.id, 'Вы выбрали C# dim')
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                                      text="Вы выбрали C# dim")

            Dd_dimp = open('bot_files/p_chords/C#/d_flat_dim.png', 'rb')

            bot.send_photo(call.message.chat.id, Dd_dimp)
            Dd_dimp.close()

    if call.message:
        if call.data == 'C#_dim7':
            bot.send_message(call.message.chat.id, 'Вы выбрали C# dim7')
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                                      text="Вы выбрали C# dim7")

            Dd_dim7p = open('bot_files/p_chords/C#/d_flat_dim7.png', 'rb')

            bot.send_photo(call.message.chat.id, Dd_dim7p)
            Dd_dim7p.close()

    if call.message:
        if call.data == 'C#m6':
            bot.send_message(call.message.chat.id, 'Вы выбрали C#m6')
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                                      text="Вы выбрали C#m6")

            Ddm6p = open('bot_files/p_chords/C#/d_flat_m6.png', 'rb')

            bot.send_photo(call.message.chat.id, Ddm6p)
            Ddm6p.close()

    if call.message:
        if call.data == 'C#m7':
            bot.send_message(call.message.chat.id, 'Вы выбрали C#m7')
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                                      text="Вы выбрали C#m7")

            Ddm7p = open('bot_files/p_chords/C#/d_flat_m7.png', 'rb')

            bot.send_photo(call.message.chat.id, Ddm7p)
            Ddm7p.close()

    if call.message:
        if call.data == 'C#m7b5':
            bot.send_message(call.message.chat.id, 'Вы выбрали C#m7(b5)')
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                                      text="Вы выбрали C#m7(b5)")

            Ddm7b5p = open('bot_files/p_chords/C#/d_flat_m7b5.png', 'rb')

            bot.send_photo(call.message.chat.id, Ddm7b5p)
            Ddm7b5p.close()

    if call.message:
        if call.data == 'C#m9':
            bot.send_message(call.message.chat.id, 'Вы выбрали C#m9')
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                                      text="Вы выбрали C#m9")

            Ddm9p = open('bot_files/p_chords/C#/d_flat_m9.png', 'rb')

            bot.send_photo(call.message.chat.id, Ddm9p)
            Ddm9p.close()

    if call.message:
        if call.data == 'C#m11':
            bot.send_message(call.message.chat.id, 'Вы выбрали C#m11')
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                                      text="Вы выбрали C#m11")

            Ddm11p = open('bot_files/p_chords/C#/d_flat_m11.png', 'rb')

            bot.send_photo(call.message.chat.id, Ddm11p)
            Ddm11p.close()

    if call.message:
        if call.data == 'C#m13':
            bot.send_message(call.message.chat.id, 'Вы выбрали C#m13')
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                                      text="Вы выбрали C#m13")

            Ddm13p = open('bot_files/p_chords/C#/d_flat_m13.png', 'rb')

            bot.send_photo(call.message.chat.id, Ddm13p)
            Ddm13p.close()

    if call.message:
        if call.data == 'C#m_maj7':
            bot.send_message(call.message.chat.id, 'Вы выбрали C#m maj7')
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                                      text="Вы выбрали C#m maj7")

            Ddm_maj7p = open('bot_files/p_chords/C#/d_flat_minmaj7.png', 'rb')

            bot.send_photo(call.message.chat.id, Ddm_maj7p)
            Ddm_maj7p.close()

    if call.message:
        if call.data == 'C#_add2':
            bot.send_message(call.message.chat.id, 'Вы выбрали C# add2')
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                                      text="Вы выбрали C# add2")

            Dd_add2p = open('bot_files/p_chords/C#/d_flat_add2.png', 'rb')

            bot.send_photo(call.message.chat.id, Dd_add2p)
            Dd_add2p.close()

    if call.message:
        if call.data == 'C#_add4':
            bot.send_message(call.message.chat.id, 'Вы выбрали C# add4')
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                                      text="Вы выбрали C# add4")

            Dd_add4p = open('bot_files/p_chords/C#/d_flat_add9.png', 'rb')

            bot.send_photo(call.message.chat.id, Dd_add4p)
            Dd_add4p.close()

    if call.message:
        if call.data == 'C#_sus2':
            bot.send_message(call.message.chat.id, 'Вы выбрали C# sus2')
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                                      text="Вы выбрали C# sus2")

            Dd_sus2p = open('bot_files/p_chords/C#/d_flat_sus2.png', 'rb')

            bot.send_photo(call.message.chat.id, Dd_sus2p)
            Dd_sus2p.close()

    if call.message:
        if call.data == 'C#_sus4':
            bot.send_message(call.message.chat.id, 'Вы выбрали C# sus4')
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                                      text="Вы выбрали C# sus4")

            Dd_sus4p = open('bot_files/p_chords/C#/d_flat_sus4.png', 'rb')

            bot.send_photo(call.message.chat.id, Dd_sus4p)
            Dd_sus4p.close()


#Cchords
    if call.message:
        if call.data == 'Dp':
            bot.send_message(call.message.chat.id, 'Вы выбрали D (Ре)')

            bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                                      text="Вы выбрали D (Ре)")

            chordsmarkup = types.InlineKeyboardMarkup(row_width=3)

            chord1 = types.InlineKeyboardButton("D", callback_data="D_major")
            chord2 = types.InlineKeyboardButton("Dm", callback_data="D_minor")
            chord3 = types.InlineKeyboardButton("D5", callback_data="D5")
            chord4 = types.InlineKeyboardButton("D6", callback_data="D6")
            chord5 = types.InlineKeyboardButton("D6 add9", callback_data="D6_9")
            chord6 = types.InlineKeyboardButton("D7", callback_data="D7")
            chord7 = types.InlineKeyboardButton("D maj7", callback_data="D_maj7")
            chord8 = types.InlineKeyboardButton("D maj9", callback_data="D_maj9")
            chord9 = types.InlineKeyboardButton("D7-5", callback_data="D7-5")
            chord10 = types.InlineKeyboardButton("D7+5", callback_data="D7+5")
            chord11 = types.InlineKeyboardButton("D9", callback_data="9")
            chord12 = types.InlineKeyboardButton("D11", callback_data="D11")
            chord13 = types.InlineKeyboardButton("D13", callback_data="13")
            chord14 = types.InlineKeyboardButton("D aug", callback_data="D_aug")
            chord15 = types.InlineKeyboardButton("D aug7", callback_data="D_aug7")
            chord16 = types.InlineKeyboardButton("D dim", callback_data="D_dim")
            chord17 = types.InlineKeyboardButton("D dim7", callback_data="D_dim7")
            chord18 = types.InlineKeyboardButton("Dm6", callback_data="Dm6")
            chord19 = types.InlineKeyboardButton("Dm7", callback_data="Dm7")
            chord20 = types.InlineKeyboardButton("Dm7(b5)", callback_data="Dm7b5")
            chord21 = types.InlineKeyboardButton("Dm9", callback_data="Dm9")
            chord22 = types.InlineKeyboardButton("Dm11", callback_data="Dm11")
            chord23 = types.InlineKeyboardButton("Dm13", callback_data="Dm13")
            chord24 = types.InlineKeyboardButton("Dm maj7", callback_data="Dm_maj7")
            chord25 = types.InlineKeyboardButton("D add2", callback_data="D_add2")
            chord26 = types.InlineKeyboardButton("D add9", callback_data="D_add9")
            chord27 = types.InlineKeyboardButton("D sus2", callback_data="D_sus2")
            chord28 = types.InlineKeyboardButton("D sus4", callback_data="D_sus4")

            chordsmarkup.add(chord1, chord2, chord3, chord4, chord5, chord6, chord7, chord8, chord9, chord10, chord11,
                             chord12,
                             chord13, chord14, chord15, chord16, chord17, chord18, chord19, chord20, chord21, chord22,
                             chord23,
                             chord24, chord25, chord26, chord27, chord28)

            bot.send_message(call.message.chat.id, 'Выберите аккорд:', reply_markup=chordsmarkup)

    if call.message:
        if call.data == 'D_major':
            bot.send_message(call.message.chat.id, 'Вы выбрали D major (Ре мажор)')
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                                      text="Вы выбрали D major (Ре мажор)")

            D_majorp = open('bot_files/p_chords/D/d.png', 'rb')

            bot.send_photo(call.message.chat.id, D_majorp)
            D_majorp.close()

    if call.message:
        if call.data == 'D_minor':
            bot.send_message(call.message.chat.id, 'Вы выбрали D minor (Ре минор)')
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                                      text="Вы выбрали D minor (Ре минор)")

            D_minor = open('bot_files/p_chords/D/dm.png', 'rb')

            bot.send_photo(call.message.chat.id, D_minor)
            D_minor.close()

    if call.message:
        if call.data == 'D5':
            bot.send_message(call.message.chat.id, 'Вы выбрали D5')
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                                      text="Вы выбрали D5")

            D5p = open('bot_files/p_chords/D/d5.png', 'rb')

            bot.send_photo(call.message.chat.id, D5p)
            D5p.close()

    if call.message:
        if call.data == 'D6':
            bot.send_message(call.message.chat.id, 'Вы выбрали D6')
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                                      text="Вы выбрали D6")

            D6p = open('bot_files/p_chords/D/d6.png', 'rb')

            bot.send_photo(call.message.chat.id, D6p)
            D6p.close()

    if call.message:
        if call.data == 'D6_9':
            bot.send_message(call.message.chat.id, 'Вы выбрали D6 add9 ')
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                                      text="Вы выбрали D6 add9")

            D6add9p = open('bot_files/p_chords/D/d6_9.png', 'rb')

            bot.send_photo(call.message.chat.id, D6add9p)
            D6add9p.close()

    if call.message:
        if call.data == 'C7':
            bot.send_message(call.message.chat.id, 'Вы выбрали C7')
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                                      text="Вы выбрали C7")

            D7p = open('bot_files/p_chords/D/d7.png', 'rb')

            bot.send_photo(call.message.chat.id, D7p)
            D7p.close()

    if call.message:
        if call.data == 'D_maj7':
            bot.send_message(call.message.chat.id, 'Вы выбрали D maj7')
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                                      text="Вы выбрали D maj7")

            D_maj7p = open('bot_files/p_chords/D/dmaj7.png', 'rb')

            bot.send_photo(call.message.chat.id, D_maj7p)
            D_maj7p.close()

    if call.message:
        if call.data == 'D_maj9':
            bot.send_message(call.message.chat.id, 'Вы выбрали D maj9')
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                                      text="Вы выбрали D maj9")

            D_maj9p = open('bot_files/p_chords/D/dmaj9.png', 'rb')

            bot.send_photo(call.message.chat.id, D_maj9p)
            D_maj9p.close()

    if call.message:
        if call.data == 'D7-5':
            bot.send_message(call.message.chat.id, 'Вы выбрали D7-5')
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                                      text="Вы выбрали D7-5")

            D7min5p = open('bot_files/p_chords/D/d7minus5.png', 'rb')

            bot.send_photo(call.message.chat.id, D7min5p)
            D7min5p.close()

    if call.message:
        if call.data == 'D7+5':
            bot.send_message(call.message.chat.id, 'Вы выбрали D7+5')
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                                      text="Вы выбрали D7+5")

            D7plus5p = open('bot_files/p_chords/D/d7plus5.png', 'rb')

            bot.send_photo(call.message.chat.id, D7plus5p)
            D7plus5p.close()

    if call.message:
        if call.data == 'D9':
            bot.send_message(call.message.chat.id, 'Вы выбрали D9')
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                                      text="Вы выбрали D9")

            D9p = open('bot_files/p_chords/D/d9.png', 'rb')

            bot.send_photo(call.message.chat.id, D9p)
            D9p.close()

    if call.message:
        if call.data == 'D11':
            bot.send_message(call.message.chat.id, 'Вы выбрали D11')
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                                      text="Вы выбрали D11")

            D11p = open('bot_files/p_chords/D/d11.png', 'rb')

            bot.send_photo(call.message.chat.id, D11p)
            D11p.close()

    if call.message:
        if call.data == 'D13':
            bot.send_message(call.message.chat.id, 'Вы выбрали D13')
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                                      text="Вы выбрали D13")

            D13p = open('bot_files/p_chords/D/d13.png', 'rb')

            bot.send_photo(call.message.chat.id, D13p)
            D13p.close()

    if call.message:
        if call.data == 'D_aug':
            bot.send_message(call.message.chat.id, 'Вы выбрали D aug')
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                                      text="Вы выбрали D aug")

            D_augp = open('bot_files/p_chords/D/daug.png', 'rb')

            bot.send_photo(call.message.chat.id, D_augp)
            D_augp.close()

    if call.message:
        if call.data == 'D_aug7':
            bot.send_message(call.message.chat.id, 'Вы выбрали D_aug7')
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                                      text="Вы выбрали D_aug7")

            D_aug7p = open('bot_files/p_chords/D/daug7.png', 'rb')

            bot.send_photo(call.message.chat.id, D_aug7p)
            D_aug7p.close()

    if call.message:
        if call.data == 'D_dim':
            bot.send_message(call.message.chat.id, 'Вы выбрали D dim')
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                                      text="Вы выбрали D dim")

            D_dimp = open('bot_files/p_chords/D/ddim.png', 'rb')

            bot.send_photo(call.message.chat.id, D_dimp)
            D_dimp.close()

    if call.message:
        if call.data == 'D_dim7':
            bot.send_message(call.message.chat.id, 'Вы выбрали D dim7')
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                                      text="Вы выбрали D dim7")

            D_dim7p = open('bot_files/p_chords/D/ddim7.png', 'rb')

            bot.send_photo(call.message.chat.id, D_dim7p)
            D_dim7p.close()

    if call.message:
        if call.data == 'Dm6':
            bot.send_message(call.message.chat.id, 'Вы выбрали Dm6')
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                                      text="Вы выбрали Dm6")

            Dm6p = open('bot_files/p_chords/D/dm6.png', 'rb')

            bot.send_photo(call.message.chat.id, Dm6p)
            Dm6p.close()

    if call.message:
        if call.data == 'Dm7':
            bot.send_message(call.message.chat.id, 'Вы выбрали Dm7')
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                                      text="Вы выбрали Dm7")

            Dm7p = open('bot_files/p_chords/D/dm7.png', 'rb')

            bot.send_photo(call.message.chat.id, Dm7p)
            Dm7p.close()

    if call.message:
        if call.data == 'Dm7b5':
            bot.send_message(call.message.chat.id, 'Вы выбрали Dm7(b5)')
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                                      text="Вы выбрали Dm7(b5)")

            Dm7b5p = open('bot_files/p_chords/D/dm7b5.png', 'rb')

            bot.send_photo(call.message.chat.id, Dm7b5p)
            Dm7b5p.close()

    if call.message:
        if call.data == 'Dm9':
            bot.send_message(call.message.chat.id, 'Вы выбрали Dm9')
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                                      text="Вы выбрали Dm9")

            Dm9p = open('bot_files/p_chords/D/dm9.png', 'rb')

            bot.send_photo(call.message.chat.id, Dm9p)
            Dm9p.close()

    if call.message:
        if call.data == 'Dm11':
            bot.send_message(call.message.chat.id, 'Вы выбрали Dm11')
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                                      text="Вы выбрали Dm11")

            Dm11p = open('bot_files/p_chords/D/dm11.png', 'rb')

            bot.send_photo(call.message.chat.id, Dm11p)
            Dm11p.close()

    if call.message:
        if call.data == 'Dm13':
            bot.send_message(call.message.chat.id, 'Вы выбрали Dm13')
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                                      text="Вы выбрали Dm13")

            Dm13p = open('bot_files/p_chords/D/dm13.png', 'rb')

            bot.send_photo(call.message.chat.id, Dm13p)
            Dm13p.close()

    if call.message:
        if call.data == 'Dm_maj7':
            bot.send_message(call.message.chat.id, 'Вы выбрали Dm maj7')
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                                      text="Вы выбрали Dm maj7")

            Dm_maj7p = open('bot_files/p_chords/D/dminmaj7.png', 'rb')

            bot.send_photo(call.message.chat.id, Dm_maj7p)
            Dm_maj7p.close()

    if call.message:
        if call.data == 'D_add2':
            bot.send_message(call.message.chat.id, 'Вы выбрали D add2')
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                                      text="Вы выбрали D add2")

            D_add2p = open('bot_files/p_chords/D/dadd2.png', 'rb')

            bot.send_photo(call.message.chat.id, D_add2p)
            D_add2p.close()

    if call.message:
        if call.data == 'D_add4':
            bot.send_message(call.message.chat.id, 'Вы выбрали D add4')
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                                      text="Вы выбрали D add4")

            D_add4p = open('bot_files/p_chords/D/dadd4.png', 'rb')

            bot.send_photo(call.message.chat.id, D_add4p)
            D_add4p.close()

    if call.message:
        if call.data == 'D_sus2':
            bot.send_message(call.message.chat.id, 'Вы выбрали D sus2')
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                                      text="Вы выбрали D sus2")

            D_sus2p = open('bot_files/p_chords/D/dsus2.png', 'rb')

            bot.send_photo(call.message.chat.id, D_sus2p)
            D_sus2p.close()

    if call.message:
        if call.data == 'D_sus4':
            bot.send_message(call.message.chat.id, 'Вы выбрали D sus4')
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                                      text="Вы выбрали D sus4")

            D_sus4p = open('bot_files/p_chords/D/dsus4.png', 'rb')

            bot.send_photo(call.message.chat.id, D_sus4p)
            D_sus4p.close()












































































@bot.message_handler(commands=['g_chords'])
def g_chord_rus(message):
    bot.send_message(message.chat.id, 'Функция находится в разработке')


bot.polling(none_stop=True)
