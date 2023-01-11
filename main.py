from work_prices import measurement_deduction, measurement_cost, cost_of_delivery, first_floor_price
from margin import installation_factor, work_factor, markup_factor, hardware_coefficient
usd_to_byn = 2.57
eur_to_byn = 2.89


dvp_price = 3.00  # $


def toFixed(numObj, digits=0):
    return f"{numObj:.{digits}f}"


def count_product_price_clear(amount_of_product, product_price):
    price = amount_of_product * product_price
    return price


def count_product_price_with_work(amount_of_product, product_price):
    price = amount_of_product * product_price * work_factor
    return price




if __name__ == '__main__':
    dvp_amount = input('Кол-во двп: ')
    product_price_clear = count_product_price_clear(int(dvp_amount), dvp_price)
    product_price_with_work = count_product_price_with_work(int(dvp_amount), dvp_price)
    print("Сумма изделия: ", toFixed(product_price_clear), "$,",
          toFixed((product_price_clear * usd_to_byn), 2), "BYN")
    print("Сумма изделия с работой: ", toFixed(product_price_with_work), "$,",
          toFixed((product_price_with_work * usd_to_byn), 2), "BYN")
    print("Стоимость работы: ", toFixed(product_price_with_work - product_price_clear, 2), "$,",
          toFixed(((product_price_with_work - product_price_clear) * usd_to_byn), 2), "BYN")

    # print("Сумма изделия: ", product_price_clear, "$,",
    #       product_price_clear * usd_to_byn, "BYN")
    # print("Сумма изделия с работой: ", product_price_with_work, "$,",
    #       product_price_with_work * usd_to_byn, "BYN")
    # print("Стоимость работы: ", product_price_with_work - product_price_clear, "$,",
    #       ((product_price_with_work - product_price_clear) * usd_to_byn), "BYN")

#### pyuic5 -x kitchen.ui -o kitchen.py

