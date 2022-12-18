from work_prices import measurement_deduction, measurement_cost, cost_of_delivery, first_floor_price
from margin import installation_factor, work_factor, markup_factor, hardware_coefficient
usd_to_byn = 2.57
eur_to_byn = 2.89


dvp_price = 3.00  # $


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
    print("Сумма изделия: ", product_price_clear, "$")
    print("Сумма изделия с работой: ", product_price_with_work, "$")
    print("Стоимость работы: ", product_price_with_work - product_price_clear, "$")

