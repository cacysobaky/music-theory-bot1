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


    if call.message:
        if call.data == 'Ap':
            bot.send_message(call.message.chat.id, 'Вы выбрали А (Ля)')

            bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                                      text="Вы выбрали А (Ля)")

            Achordsmarkup = types.InlineKeyboardMarkup(row_width=3)

            Achord1 = types.InlineKeyboardButton("A", callback_data="A_major")
            Achord2 = types.InlineKeyboardButton("Am", callback_data="A_minor")
            Achord3 = types.InlineKeyboardButton("A5", callback_data="A5")
            Achord4 = types.InlineKeyboardButton("A6", callback_data="A6")
            Achord5 = types.InlineKeyboardButton("A6 add9", callback_data="A6_9")
            Achord6 = types.InlineKeyboardButton("A7", callback_data="A7")
            Achord7 = types.InlineKeyboardButton("A maj7", callback_data="A_maj7")
            Achord8 = types.InlineKeyboardButton("A maj9", callback_data="A_maj9")
            Achord9 = types.InlineKeyboardButton("A7-5", callback_data="A7-5")
            Achord10 = types.InlineKeyboardButton("A7+5", callback_data="A7+5")
            Achord11 = types.InlineKeyboardButton("A9", callback_data="A9")
            Achord12 = types.InlineKeyboardButton("A11", callback_data="A11")
            Achord13 = types.InlineKeyboardButton("A13", callback_data="A13")
            Achord14 = types.InlineKeyboardButton("A aug", callback_data="A_aug")
            Achord15 = types.InlineKeyboardButton("A aug7", callback_data="A_aug7")
            Achord16 = types.InlineKeyboardButton("A dim", callback_data="A_dim")
            Achord17 = types.InlineKeyboardButton("A dim7", callback_data="A_dim7")
            Achord18 = types.InlineKeyboardButton("Am6", callback_data="Am6")
            Achord19 = types.InlineKeyboardButton("Am7", callback_data="Am7")
            Achord20 = types.InlineKeyboardButton("Am7(b5)", callback_data="Am7b5")
            Achord21 = types.InlineKeyboardButton("Am9", callback_data="Am9")
            Achord22 = types.InlineKeyboardButton("Am11", callback_data="Am11")
            Achord23 = types.InlineKeyboardButton("Am13", callback_data="Am13")
            Achord24 = types.InlineKeyboardButton("Am maj7", callback_data="Am_maj7")
            Achord25 = types.InlineKeyboardButton("A add2", callback_data="A_add2")
            Achord26 = types.InlineKeyboardButton("A add9", callback_data="A_add9")
            Achord27 = types.InlineKeyboardButton("A sus2", callback_data="A_sus2")
            Achord28 = types.InlineKeyboardButton("A sus4", callback_data="A_sus4")

            Achordsmarkup.add(Achord1, Achord2, Achord3, Achord4, Achord5, Achord6, Achord7, Achord8, Achord9, Achord10, Achord11,
                             Achord12,
                             Achord13, Achord14, Achord15, Achord16, Achord17, Achord18, Achord19, Achord20, Achord21, Achord22,
                             Achord23,
                             Achord24, Achord25, Achord26, Achord27, Achord28)

            bot.send_message(call.message.chat.id, 'Выберите аккорд:', reply_markup=Achordsmarkup)

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

            a_add9p = open('bot_files/p_chords/A/aadd9.png.png', 'rb')

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


    if call.message:
        if call.data == 'A#p':
            bot.send_message(call.message.chat.id, 'Вы выбрали А#/Bb (Ля диез / Си бемоль)')

            bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                                      text="Вы выбрали А#/Bb (Ля диез / Си бемоль)")

            Bbchordsmarkup = types.InlineKeyboardMarkup(row_width=3)

            Bbchord1 = types.InlineKeyboardButton("A#", callback_data="Bb_major")
            Bbchord2 = types.InlineKeyboardButton("A#m", callback_data="Bb_minor")
            Bbchord3 = types.InlineKeyboardButton("A#5", callback_data="Bb5")
            Bbchord4 = types.InlineKeyboardButton("A#6", callback_data="Bb6")
            Bbchord5 = types.InlineKeyboardButton("A#6 add9", callback_data="Bb6_9")
            Bbchord6 = types.InlineKeyboardButton("A#7", callback_data="Bb7")
            Bbchord7 = types.InlineKeyboardButton("A# maj7", callback_data="Bb_maj7")
            Bbchord8 = types.InlineKeyboardButton("A# maj9", callback_data="Bb_maj9")
            Bbchord9 = types.InlineKeyboardButton("A#7-5", callback_data="Bb7-5")
            Bbchord10 = types.InlineKeyboardButton("A#7+5", callback_data="Bb7+5")
            Bbchord11 = types.InlineKeyboardButton("A#9", callback_data="Bb9")
            Bbchord12 = types.InlineKeyboardButton("A#11", callback_data="Bb11")
            Bbchord13 = types.InlineKeyboardButton("A#13", callback_data="Bb13")
            Bbchord14 = types.InlineKeyboardButton("A# aug", callback_data="Bb_aug")
            Bbchord15 = types.InlineKeyboardButton("A# aug7", callback_data="Bb_aug7")
            Bbchord16 = types.InlineKeyboardButton("A# dim", callback_data="Bb_dim")
            Bbchord17 = types.InlineKeyboardButton("A# dim7", callback_data="Bb_dim7")
            Bbchord18 = types.InlineKeyboardButton("A#m6", callback_data="Bbm6")
            Bbchord19 = types.InlineKeyboardButton("A#m7", callback_data="Bbm7")
            Bbchord20 = types.InlineKeyboardButton("A#m7(b5)", callback_data="Bbm7b5")
            Bbchord21 = types.InlineKeyboardButton("A#m9", callback_data="Bbm9")
            Bbchord22 = types.InlineKeyboardButton("A#m11", callback_data="Bbm11")
            Bbchord23 = types.InlineKeyboardButton("A#m13", callback_data="Bbm13")
            Bbchord24 = types.InlineKeyboardButton("A#m maj7", callback_data="Bbm_maj7")
            Bbchord25 = types.InlineKeyboardButton("A# add2", callback_data="Bb_add2")
            Bbchord26 = types.InlineKeyboardButton("A# add9", callback_data="Bb_add9")
            Bbchord27 = types.InlineKeyboardButton("A# sus2", callback_data="Bb_sus2")
            Bbchord28 = types.InlineKeyboardButton("A# sus4", callback_data="Bb_sus4")

            Bbchordsmarkup.add(Bbchord1, Bbchord2, Bbchord3, Bbchord4, Bbchord5, Bbchord6, Bbchord7, Bbchord8, Bbchord9, Bbchord10, Bbchord11,
                             Bbchord12,
                             Bbchord13, Bbchord14, Bbchord15, Bbchord16, Bbchord17, Bbchord18, Bbchord19, Bbchord20, Bbchord21, Bbchord22,
                             Bbchord23,
                             Bbchord24, Bbchord25, Bbchord26, Bbchord27, Bbchord28)

            bot.send_message(call.message.chat.id, 'Выберите аккорд:', reply_markup=Bbchordsmarkup)


    if call.message:
        if call.data == 'Bb_major':
            bot.send_message(call.message.chat.id, 'Вы выбрали А# / Bb major(Ля диез / Си бемоль мажор)')

            bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                                      text="Вы выбрали А# / Bb major(Ля диез / Си бемоль мажор)")

            Bb_majorp = open('bot_files/p_chords/c/c.png')

            bot.send_photo(call.message.chat.id, Bb_majorp)
            Bb_majorp.close()





























@bot.message_handler(commands=['g_chords'])
def g_chord_rus(message):
    bot.send_message(message.chat.id, 'Функция находится в разработке')


bot.polling(none_stop=True)
