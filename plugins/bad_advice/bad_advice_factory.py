# coding=utf-8
import random

__author__ = 'Andrew Kuchev (kuchevad@gmail.com)'

__all__ = ['BadAdviceFactory']


class BadAdviceFactory(object):
    advices = ["""Потерявшийся ребенок
 Должен помнить, что его
 Отведут домой, как только
 Назовет он адрес свой.
 Надо действовать умнее,
 Говорите: "Я живу
 Возле пальмы с обезьяной
 На далеких островах".
 Потерявшийся ребенок,
 Если он не дурачок,
 Не упустит верный случай
 В разных странах побывать.
""", """
Руками никогда нигде
Не трогай ничего.
Не впутывайся ни во что
И никуда не лезь.
В сторонку молча отойди,
Стань скромно в уголке
И тихо стой, не шевелясь,
До старости своей.
""", """
Кто не прыгал из окошка
Вместе с маминым зонтом,
Тот лихим парашютистом
Не считается пока.
Не лететь ему, как птице,
Над взволнованной толпой,
Не лежать ему в больнице
С забинтованной ногой.
""", """
Если всей семьей купаться
Вы отправились к реке,
Не мешайте папе с мамой
Загорать на берегу.
Не устраивайте крика,
Дайте взрослым отдохнуть.
Ни к кому не приставая,
Постарайтесь утонуть.
""", """
Нет приятнее занятья,
Чем в носу поковыряться.
Всем ужасно интересно,
Что там спрятано внутри.
А кому смотреть противно,
Тот пускай и не глядит.
Мы же в нос к нему не лезем,
Пусть и он не пристает.Если вас поймала мама
За любимым делом вашим,
Например, за рисованьем
В коридоре на обоях,
Объясните ей, что это -
Ваш сюрприз к Восьмому марта.
Называется картина:
"Милой мамочки портрет".
""", """
Не бери чужое, если
На тебя глядят чужие.
Пусть они глаза закроют
Или выйдут на часок.
А своих чего бояться!
Про своих свои не скажут.
Пусть глядят.
Хватай чужое
И тащи его к своим.
""", """
Никогда вопросов глупых
Сам себе не задавай,
А не то еще глупее
Ты найдешь на них ответ.
Если глупые вопросы
Появились в голове,
Задавай их сразу взрослым.
Пусть у них трещат мозги.
""", """
Посещайте почаще
Театральный буфет.
Там пирожные с кремом,
С пузырьками вода.
Как дрова на тарелках
Шоколадки лежат,
И сквозь трубочку можно
Пить молочный коктейль.
Не просите билеты
На балкон и в партер,
Пусть дадут вам билеты
В театральный буфет.
Уходя из театра,
Унесете с собой
Под трепещущим сердцем,
В животе бутерброд.
""", """
Родился девочкой - терпи
Подножки и толчки.
И подставляй косички всем,
Кто дернуть их не прочь.
Зато когда-нибудь потом
Покажешь кукиш им
И скажешь: "Фигушки, за вас
Я замуж не пойду!" Если вы с друзьями вместе
Веселитесь во дворе,
А с утра на вас надели
Ваше новое пальто,
То не стоит ползать в лужах
И кататься по земле,
И взбираться на заборы,
Повисая на гвоздях.
Чтоб не портить и не пачкать
Ваше новое пальто,
Нужно сделать его старым.
Это делается так:
Залезайте прямо в лужу,
Покатайтесь по земле,
И немножко на заборе
Повисите на гвоздях.
Очень скоро станет старым
Ваше новое пальто,
Вот теперь спокойно можно
Веселиться во дворе.
Можно смело ползать в лужах
И кататься по земле,
И взбираться на заборы,
Повисая на гвоздях.
""", """
Если вы по коридору
Мчитесь на велосипеде,
А навстречу вам из ванной
Вышел папа погулять,
Не сворачивайте в кухню,
В кухне - твердый холодильник.
Тормозите лучше в папу.
Папа мягкий.
Он простит.
""", """
Если вас навек сплотили,
Озарили и ведут,
Не пытайтесь уклониться
От движенья к торжеству.
Все равно на труд поднимет
И на подвиг вдохновит
Вас великий и могучий,
И надежный наш оплот.
""", """
Главным делом жизни вашей
Может стать любой пустяк.
Надо только твердо верить,
Что важнее дела нет.
И тогда не помешает
Вам ни холод, ни жара,
Задыхаясь от восторга,
Заниматься чепухой.
""", """
Бейте палками лягушек.
Это очень интересно.
Отрывайте крылья мухам,
Пусть побегают пешком.
Тренируйтесь ежедневно,
И наступит день счастливый -
Вас в какое-нибудь царство
Примут главным палачом.
""", """
Девчонок надо никогда
Нигде не замечать.
И не давать прохода им
Нигде и никогда.
Им надо ножки подставлять,
Пугать из-за угла,
Чтоб сразу поняли они:
До них вам дела нет.
Девчонку встретил - быстро ей
Показывай язык.
Пускай не думает она,
Что ты в нее влюблен.
""", """
Начиная драку с папой,
Затевая с мамой бой,
Постарайся сдаться маме, -
Папа пленных не берет.
Кстати, выясни у мамы,
Не забыла ли она
Пленных бить ремнем по попе
Запрещает Красный Крест.
""", """
Если ты весь мир насилья
Собираешься разрушить,
И при этом стать мечтаешь
Всем, не будучи ничем,
Смело двигайся за нами
По проложенной дороге,
Мы тебе дорогу эту
Можем даже уступить.
""", """
Не соглашайся ни за что
Ни с кем и никогда,
А кто с тобой согласен, тех
Трусливыми зови.
За это все тебя начнут
Любить и уважать.
И всюду будет у тебя
Полным полно друзей.
""", """
Если в кухне тараканы
Маршируют по столу,
И устраивают мыши
На полу учебный бой,
Значит, вам пора на время
Прекратить борьбу за мир,
И все силы ваши бросить
На борьбу за чистоту.
""", """
Если вы собрались другу
Рассказать свою беду,
Брать за пуговицу друга
Бесполезно - убежит,
И на память вам оставит
Эту пуговицу друг.
Лучше дать ему подножку,
На пол бросить, сверху сесть
И тогда уже подробно
Рассказать свою беду.
""", """
Если ты пришел к знакомым,
Не здоровайся ни с кем.
Слов: "пожалуйста", "спасибо"
Никому не говори.
Отвернись и на вопросы
Ни на чьи не отвечай.
И тогда никто не скажет
Про тебя, что ты болтун.
""", """
Если что-нибудь случилось,
И никто не виноват,
Не ходи туда, иначе
Виноватым будешь ты.
Спрячься где-нибудь в сторонке.
А потом иди домой.
И про то, что видел это,
Никому не говори.
""", """
Если не купили вам пирожное
И в кино с собой не взяли вечером,
Нужно на родителей обидеться,
И уйти без шапки в ночь холодную.
Но не просто так
Бродить по улицам,
А в дремучий темный
Лес отправиться.
Там вам сразу волк
Голодный встретится,
И, конечно, быстро
Вас он скушает.
Вот тогда узнают папа с мамою,
Закричат, заплачут и забегают.
И помчатся покупать пирожное,
И в кино с собой
Возьмут вас вечером.
""", """
Посмотрите, что творится
В каждом доме по ночам.
Отвернувшись к стенке носом,
Молча взрослые лежат.
Шевелят они губами
В беспросветной темноте
И с закрытыми глазами
Пяткой дергают во сне.
Ни за что не соглашайтесь
По ночам идти в кровать.
Никому не позволяйте
Вас укладывать в постель.
Неужели вы хотите
Годы детские свои
Провести под одеялом,
На подушке, без штанов?
""", """
Есть верное средство
Понравиться взрослым:
С утра начинайте
 Орать и сорить,
 Подслушивать, хныкать,
 По дому носиться
 Лягаться и клянчить
 Подарки у всех.
 Хамите, хитрите,
  Дразните и врите,
  А к вечеру вдруг
  Перестаньте на час, -
  И сразу, с улыбкой
  Растроганной гладя,
  Все взрослые вас
  По головке погладят
  И скажут, что вы
  Замечательный мальчик
  И нету ребенка
  Приятнее вас.
""", """
Если ты пришел на елку,
Свой подарок требуй сразу,
Да гляди, чтоб ни конфеты
Не зажилил Дед Мороз.
И не вздумай беззаботно
Приносить домой остатки.
Как наскачут папа с мамой -
Половину отберут.
""", """
Если ждет вас наказанье
За плохое поведенье,
Например, за то, что в ванной
Вы свою купали кошку,
Не спросивши разрешенья
Ни у кошки, ни у мамы,
Предложить могу вам способ,
Как спастись от наказанья.
Головою в пол стучите,
Бейте в грудь себя руками
И рыдайте, и кричите:
 "Ах, зачем я мучил кошку!?
 Я достоин страшной кары!
 Мой позор лишь смерть искупит!"
 Не пройдет и полминуты,
 Как, рыдая вместе с вами,
 Вас простят и, чтоб утешить,
 Побегут за сладким тортом.
 И тогда спокойно кошку
Вы за хвост ведите в ванну,
Ведь наябедничать кошка
Не сумеет никогда.
""", """
Например, у вас в кармане
Оказалась горсть конфет,
А навстречу вам попались
Ваши верные друзья.
Не пугайтесь и не прячьтесь,
Не кидайтесь убегать,
Не пихайте все конфеты
Вместе с фантиками в рот.
Подойдите к ним спокойно,
Лишних слов не говоря,
Быстро вынув из кармана,
Протяните им... ладонь.
Крепко руки им пожмите,
Попрощайтесь не спеша
И, свернув за первый угол,
Мчитесь быстренько домой.
Чтобы дома съесть конфеты,
Залезайте под кровать,
Потому что там, конечно,
Вам не встретится никто.
""", """
Возьми густой вишневый сок
И белый мамин плащ.
Лей аккуратно сок на плащ -
Появится пятно.
Теперь, чтоб не было пятна
На мамином плаще,
Плащ надо сунуть целиком
В густой вишневый сок.
Возьми вишневый мамин плащ
И кружку молока.
Лей аккуратно молоко -
Появится пятно.
Теперь, чтоб не было пятна
На мамином плаще,
Плащ надо сунуть целиком
В кастрюлю с молоком.
Возьми густой вишневый сок
И белый мамин плащ.
Лей аккуратно...
""", """""", """Если вы окно разбили,
Не спешите признаваться.
Погодите, - не начнется ль
Вдруг гражданская война.
Артиллерия ударит,
Стекла вылетят повсюду,
И никто ругать не станет
За разбитое окно.
""", """
Бей друзей без передышки
Каждый день по полчаса,
И твоя мускулатура
Станет крепче кирпича.
А могучими руками,
Ты, когда придут враги,
Сможешь в трудную минуту
Защитить своих друзей.
""", """
Никогда не мойте руки,
Шею, уши и лицо.
Это глупое занятье
Не приводит ни к чему.
Вновь испачкаются руки,
Шея, уши и лицо,
Так зачем же тратить силы,
Время попусту терять.
Стричься тоже бесполезно,
Никакого смысла нет.
К старости сама собою
Облысеет голова.
""", """
Никогда не разрешайте
Ставить градусник себе,
И таблеток не глотайте,
И не ешьте порошков.
Пусть болят живот и зубы,
Горло, уши, голова,
Все равно лекарств не пейте,
И не слушайте врача.
Перестанет биться сердце,
Но зато наверняка
Не прилепят вам горчичник
И не сделают укол.
""", """
Если ты попал в больницу
И не хочешь там валяться,
Жди, когда к тебе в палату
Самый главный врач придет.
Укуси его - и сразу
Кончится твое леченье,
В тот же вечер из больницы
Заберут тебя домой.
""", """
Если мама в магазине
Вам купила только мячик
И не хочет остальное,
Все, что видит, покупать,
Станьте прямо, пятки вместе,
Руки в стороны расставьте,
Открывайте рот пошире
И кричите букву "А"!
И когда, роняя сумки,
С воплем: "Граждане! Тревога!"
Покупатели помчатся
С продавцами во главе,
К вам директор магазина
Подползет и скажет маме:
"Заберите все бесплатно,
Пусть он только замолчит".
""", """
Когда тебя родная мать
Ведет к зубным врачам,
Не жди пощады от нее,
Напрасных слез не лей.
Молчи, как пленный партизан,
И стисни зубы так,
Чтоб не сумела их разжать
Толпа зубных врачей.
""", """
Если ты остался дома
Без родителей один,
Предложить тебе могу я
Интересную игру
Под названьем "Смелый повар"
Или "Храбрый кулинар".
Суть игры в приготовленьи
Всевозможных вкусных блюд.
Предлагаю для начала
Вот такой простой рецепт:
Нужно в папины ботинки
Вылить мамины духи,
А потом ботинки эти
мазать кремом для бритья,
И, полив их рыбьим жиром
С черной тушью пополам,
Бросить в суп, который мама
Приготовила с утра.
И варить с закрытой крышкой
Ровно семьдесят минут
Что получится, узнаешь,
Когда взрослые придут.
""", """
Если друг твой самый лучший
Поскользнулся и упал,
Покажи на друга пальцем
И хватайся за живот.
Пусть он видит, лежа в луже, -
Ты ничуть не огорчен.
Настоящий друг не любит
Огорчать своих друзей.
""", """
Если вы еще не твердо
В жизни выбрали дорогу
И не знаете, с чего бы
Трудовой свой путь начать,
Бейте лампочки в подъездах -
Люди скажут вам "спасибо".
Вы поможете народу
Электричество беречь.
""", """
Чтобы выгнать из квартиры
Разных мух и комаров,
Надо сдернуть занавеску
И крутить над головой.
Полетят со стен картины,
С подоконника - цветы.
Кувыркнется телевизор,
Люстра врежется в паркет.
И, от грохота спасаясь,
Разлетятся комары,
А испуганные мухи
Стаей кинутся на юг.
""", """
Если вы с утра решили
Хорошо себя вести,
Смело в шкаф себя ведите
И ныряйте в темноту.
Там ни мамы нет, ни папы,
Только папины штаны.
Там никто не крикнет громко:
"Прекрати! Не смей! Не тронь!"
Там гораздо проще будет,
Не мешая никому,
Целый день себя прилично
И порядочно вести.
""", """
Решил подраться - выбирай
Того, кто послабей.
А сильный может сдачи дать,
Зачем тебе она?
Чем младше тот, кого ты бьешь,
Тем сердцу веселей
Глядеть, как плачет он, кричит,
И мамочку зовет.
Но если вдруг за малыша
Вступился кто-нибудь,
Беги, кричи и громко плачь,
И мамочку зови.
""", """
Есть надежный способ папу
Навсегда свести с ума.
Расскажите папе честно,
Что вы делали вчера.
Если он при этом сможет
Удержаться на ногах,
Объясните, чем заняться
Завтра думаете вы.
И когда с безумным видом
Папа песни запоет,
Вызывайте неотложку.
Телефон ее 03.
""", """
Если вы гуляли в шапке,
 А потом она пропала,
 Не волнуйтесь, маме дома
 Можно что-нибудь соврать.
 Но старайтесь врать красиво,
 Чтобы глядя восхищенно,
 Затаив дыханье, мама
 Долго слушала вранье.
 Но уж если вы наврали
 Про потерянную шапку,
 Что ее в бою неравном
 Отобрал у вас шпион,
 Постарайтесь, чтобы мама
 Не ходила возмущаться
 В иностранную разведку,
 Там ее не так поймут.
""", """
"Надо с младшими делиться!"
"Надо младшим помогать!"
Никогда не забывайте
Эти правила, друзья.
Очень тихо повторяйте
Их тому, кто старше вас,
Чтобы младшие про это
Не узнали ничего.
""", """
Если руки за обедом
Вы испачкали салатом
И стесняетесь о скатерть
Пальцы вытереть свои,
Опустите незаметно
Их под стол, и там спокойно
Вытирайте ваши руки
Об соседские штаны.
""", """
Если ты в своем кармане
Ни копейки не нашел,
Загляни в карман к соседу, -
Очевидно, деньги там.
""", """
Если твой сосед по парте
Стал источником заразы,
Обними его - и в школу
Две недели не придешь.
""", """
Чтобы самовозгоранья
В доме не произошло,
Выходя из помещенья
Уноси с собой утюг.
Пылесос, электроплитку,
Телевизор и торшер
Лучше, с лампочками вместе,
Вынести в соседний двор.
А еще надежней будет
Перерезать провода,
Чтоб во всем твоем районе
Сразу вырубился свет.
Тут уж можешь быть уверен
Ты почти наверняка,
Что от самовозгоранья
Дом надежно уберег.
""", """
Спички - лучшая игрушка
Для скучающих детей.
Папин галстук, мамин паспорт -
Вот и маленький костер.
Если тапочки подкинуть
Или веник подложить
Можно целый стул зажарить,
В тумбочке сварить уху.
Если взрослые куда-то
Спички спрятали от вас,
Объясните им, что спички
Для пожара вам нужны.
""", """
Если сына отмывая
Обнаружит мама вдруг,
Что она не сына моет,
А чужую чью-то дочь...
Пусть не нервничает мама,
Ну не все ли ей равно.
Никаких различий нету
Между грязными детьми.
""", """
Когда состаришься - ходи
По улице пешком.
Не лезь в автобус, все равно
Стоять придется там.
И нынче мало дураков,
Чтоб место уступать,
А к тем далеким временам
Не станет их совсем.
""", """
Если вы в футбол играли
На широкой мостовой
И, ударив по воротам,
Вдруг услышали свисток,
Не кричите: "Гол!", возможно,
Это милиционер
 Засвистел,  когда попали
 Не в ворота, а в него.
""", """
Убегая от трамвая,
Не спеши под самосвал.
Погоди у светофора
Не покажется пока
Скорой помощи машина -
В ней полным полно врачей
Пусть они тебя задавят.
Сами вылечат потом.
""", """
Если вы врагов хотите
Победить одним ударом,
Вам ракеты и снаряды,
И патроны ни к чему.
Сбросьте к ним на парашюте
(эту строчку сам заполни.)
Через час враги, рыдая,
Прибегут сдаваться в плен.
""", """
Если ты в совет последний
Сам не хочешь вставить строчку,
Выбери себе любую
Из предложенных тебе.
Сбросьте к ним на парашюте:
Вашу младшую сестренку,
Папу, бабушку и маму,
Два мешка рублей и трешек,
Директрису вашей школы,
Педсовет в составе полном,
Двигатель от "Запорожца",
Стоматологов десяток,
МАЛЬЧИКА ЧЕРНОВА САШУ,
МАЛЕНЬКУЮ МАШУ ОСТЕР,
Чай из школьного буфета,
Книжку "Вредные советы"...
Через час враги, рыдая,
Прибегут сдаваться в плен.
""", """
Если вас зовут обедать,
Гордо прячьтесь под диван
И лежите там тихонько,
Чтоб не сразу вас нашли.
А когда из-под дивана
Будут за ноги тащить,
Вырывайтесь и кусайтесь,
Не сдавайтесь без борьбы.
Если все-таки достанут
И за стол посадят вас,
Опрокидывайте чашку,
Выливайте на пол суп.
Зажимайте рот руками,
Падайте со стула вниз.
А котлеты вверх бросайте,
Пусть прилипнут к потолку.
Через месяц люди скажут
С уважением о вас:
 "С виду он худой и дохлый,
 Но зато характер тверд".
""", """
Если вы решили первым
Стать в рядах своих сограждан -
Никогда не догоняйте
Устремившихся вперед.
Через пять минут, ругаясь,
Побегут они обратно,
И тогда, толпу возглавив,
Вы помчитесь впереди.
""", """
Если к папе или к маме
Тетя взрослая пришла
И ведет какой-то важный
И серьезный разговор,
Нужно сзади незаметно
К ней подкрасться, а потом
Громко крикнуть прямо в ухо:
"Стой! Сдавайся! Руки вверх!"
И когда со стула тетя
С перепугу упадет
И прольет себе на платье
Чай, компот или кисель,
То, наверно, очень громко
Будет мама хохотать,
И, гордясь своим ребенком,
Папа руку вам пожмет.
За плечо возьмет вас папа
И куда-то поведет.
Там, наверно, очень долго
Папа будет вас хвалить.
""", """
Заведи себе тетрадку
И записывай подробно,
Кто кого на переменке
Сколько раз куда послал,
С кем учитель физкультуры
Пил кефир в спортивном зале,
И что папа ночью маме
Тихо на ухо шептал.
""", """
Если острые предметы
Вам попались на глаза,
Постарайтесь их поглубже
В самого себя воткнуть.
Это самый лучший способ
Убедиться самому,
Что опасные предметы
Надо прятать от детей.
""", """
Требуют тебя к ответу?
Что ж, умей держать ответ.
Не трясись, не хнычь, не мямли,
Никогда не прячь глаза.
Например, спросила мама:
"Кто игрушки разбросал?"
Отвечай, что это папа
Приводил своих друзей.
Ты подрался с младшим братом?
Говори, что первый он
Бил тебя ногой по шее
И ругался как бандит.
Если спросят, кто на кухне
Все котлеты искусал,
Отвечай, что кот соседский,
А, возможно, сам сосед.
В чем бы ты ни провинился,
Научись держать ответ.
За свои поступки каждый
Должен смело отвечать.
""", """
Если вы решили твердо
Самолет угнать на Запад,
Но не можете придумать,
Чем пилотов напугать,
Почитайте им отрывки
Из сегодняшней газеты, -
И они в страну любую
Вместе с вами улетят.
""", """
Дразниться лучше из окна,
С восьмого этажа.
Из танка тоже хорошо,
Когда крепка броня.
Но если хочешь довести
Людей до горьких слез,
Их безопаснее всего
По радио дразнить.
""", """
Когда роняет чашку гость,
Не бейте гостя в лоб.
Другую чашку дайте, пусть
Он пьет спокойно чай.
Когда и эту чашку гость
Уронит со стола,
В стакан налейте чай ему,
И пусть спокойно пьет.
Когда же всю посуду гость
В квартире перебьет,
Придется сладкий чай налить
За шиворот ему.
""", """
Если вас по телефону
Обозвали дураком
И не стали ждать ответа,
Бросив трубку на рычаг,
Наберите быстро номер
Из любых случайных цифр
И тому, кто снимет трубку,
Сообщите - сам дурак.
""", """
Адрес школы, той в которой
Посчастливилось учиться,
Как таблицу умноженья
Помни твердо, наизусть,
И когда тебе случится
Повстречаться с диверсантом,
Не теряя ни минуты,
Адрес школы сообщи.
""", """
Не расстраивайтесь, если
Вызывают в школу маму
Или папу. Не стесняйтесь,
Приводите всю семью.
Пусть приходят дяди, тети
И троюродные братья,
Если есть у вас собака,
Приводите и ее.
""", """
Если вы сестру решили
Только в шутку напугать,
А она от вас по стенке
Убегает босиком,
Значит, шуточки смешные
Не доходят до нее,
И не стоит класть сестренке
В тапочки живых мышей.
""", """
Если ты сестру застукал
С женихами во дворе,
Не спеши ее скорее
Папе с мамой выдавать.
Пусть родители сначала
Замуж выдадут ее,
Вот тогда расскажешь мужу
Все, что знаешь про сестру.
""", """
Если гонится за вами
Слишком много человек,
Расспросите их подробно
Чем они огорчены?
Постарайтесь всех утешить.
Дайте каждому совет,
Но снижать при этом скорость
Совершенно ни к чему.
""", """
Не обижайтесь на того,
Кто бьет руками вас,
И не ленитесь каждый раз
Его благодарить,
За то, что не жалея сил,
Он вас руками бьет,
А мог бы в эти руки взять
И палку, и кирпич.
""", """
Если друг на день рожденья
Пригласил тебя к себе,
Ты оставь подарок дома -
Пригодится самому.
Сесть старайся рядом с тортом.
В разговоры не вступай.
Ты во время разговора
Вдвое меньше съешь конфет.
Выбирай куски помельче,
Чтоб быстрее проглотить.
Не хватай салат руками -
Ложкой больше зачерпнешь.
Если вдруг дадут орехи,
Сыпь их бережно в карман,
Но не прячь туда варенье -
Трудно будет вынимать."""]

    @classmethod
    def get_bad_advice(cls):
        return random.choice(cls.advices)