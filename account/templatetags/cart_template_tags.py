from django import template
from django.contrib.auth.models import User

from account.models import Cart, Account
register = template.Library()


@register.filter
def cart_item_count(user):
    print ('get ttttttttttttttttttttttttttttttttttttttttttt')
    if user.is_authenticated:
        qty = Cart.objects.filter(news_station=user).count()
        return qty
    return 0


@register.filter
def total_price(user):
    print ('get total')
    if user.is_authenticated:
        cart = Cart.objects.filter(news_station=user)
        acc_price = 0
        for items in cart:
            acc_price = acc_price + items.price
            print(acc_price, items.title, items.news_station)
#        qs = Cart.objects.filter(user=user, ordered=False)
#        if qs.exists():
        return acc_price
    return 0


@register.filter
def total_account(user):
    print ('get total')
    if user.is_authenticated:
        acc = Account.objects.filter(user=user)
        acc_price = 0
        for items in acc:
            acc_price = acc_price + items.price
            print(acc_price, items.title, items.user)
#        qs = Cart.objects.filter(user=user, ordered=False)
#        if qs.exists():
        return acc_price
    return 0