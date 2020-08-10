import lesson_16.aval_parser as aval_parser
import lesson_16.private_bank_parser as private_parser
import lesson_16.ukrsib_parser as ukrsib_parse

lst = [
    aval_parser.RaiffeisenBankAval(),
    private_parser.PrivateBank(),
    ukrsib_parse.UkrSibBank()
]


for bank in lst:
    rates = bank.get_currency_rate()

    for rate in rates['rate']:
        print('currency: {currency_name}\tpurchase: {p_rate}\tsale: {s_rate}'.format(
            currency_name=rate['currency'],
            p_rate=rate['purchase_rate'],
            s_rate=rate['sale_rate']
        ))
        # print()
    print('-' * 50)
