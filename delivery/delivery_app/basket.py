def basket_add(request, dish):
    b = request.session.get('basket')
    if b is None:
        # print('нет корзины')
        b = {str(dish.pk): {'count': 1, 'price': dish.price, 'name': dish.name}}
    else:
        # print('есть корзина')
        # print('Корзина до измеения= ', b)
        if b.get(str(dish.pk)) is None:
            b[str(dish.pk)] = {'count': 1, 'price': dish.price, 'name': dish.name}
        else:
            b[str(dish.pk)]['count'] += 1
    request.session['basket'] = b
    request.session.save()
    # print('Корзина после изменения = ', request.session['basket'])
    # print('Полная сумма = ', basket_total(request))


def basket_sub(request, dish_pk):
    b = request.session.get('basket')
    print(b)
    for key, value in b.items():
        if key == str(dish_pk):
            print('Отнимаем от блюда', value['name'])
            if value['count'] > 1:
                b[key]['count'] -= 1
            else:
                del b[key]
            request.session['basket'] = b
            request.session.save()
            return


def basket_clear(request):
    request.session['basket'] = {}
    request.session.save()
    return


def basket_total(request):
    b = request.session.get('basket')
    count = 0
    if b is not None:
        for key in b:
            count = count + b[key]['count'] * b[key]['price']
    return count


def get_basket_as_dict(request):
    b = request.session.get('basket')
    if b is not None:
        return  request.session.get('basket')
    return {}


def basket_present(request):
    b = request.session.get('basket')
    if b is None:
        return False
    else:
        return True
