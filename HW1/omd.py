def get_check_option(options: dict):
    option = ''

    while option not in options:
        print('Выберите: {}/{}'.format(*options))
        option = input().lower()

    return option


def step2_umbrella():
    print('ну, он же не поможет от дождя из уток...\n'
          'Утка-массажист сделала маникюр и решила заглянуть в бар,\n'
          'чтобы узнать, не нужны ли кому-нибудь клиенты для массажа. Ну, или хотя бы один клиент для вечернего\n'
          'массажа '
          'после работы. И тогда утка с улыбкой на лице взяла коктейль. Так как у утки-бармена не было зонта,\n'
          'то она решила '
          'использовать свои крылья, чтобы купить один коктейль вместо зонтика. Она пошла в бар и спросила: «У вас\n'
          'нет '
          'зонтика?». «Нет!» - сказали все, кто сидел в баре.')

    print('Возразить утке на их совместный ответ?')
    options = {'да': True, 'нет': False}

    option = get_check_option(options)
    if options[option]:
        print('Что вы все кричите? Я же просто хотела намокнуть... - сказала утка и улетела. '
              'На улице стояла ясная морозная погода января.')
    else:
        print('Утка ушла без зонта, не сказав ни слова, хотя он ей и не был нужен.')
    print('To be continued')


def step2_no_umbrella():
    print('Отставить зонтик!\n'
          'В бар пришёл моряк с большим чемоданом.\n'
          'Он хотел сказать, что он купил свой дом, но было уже поздно.\n'
          'Моряка пригласили сесть, и тут он вспомнил: у него нет с собой паспорта.\n')

    print('Узнать откуда взялся моряк?')
    options = {'да': True, 'нет': False}

    option = get_check_option(options)
    if options[option]:
        print('Он приплыл.')
    else:
        print('Ладно.')
    print('To be continued')


def step1():
    print(
        'Утка-маляр 🦆 решила выпить зайти в бар. '
        'Взять ей зонтик? ☂️'
    )
    options = {'да': True, 'нет': False}

    option = get_check_option(options)

    if options[option]:
        return step2_umbrella()
    return step2_no_umbrella()


if __name__ == '__main__':
    """
    Balaboba generated text
    """
    step1()
