from logging import currentframe
import unittest
from client3 import getDataPoint

class ClientTest(unittest.TestCase):
  def test_getDataPoint_calculatePrice(self):
    quotes = [
      {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    for quote in quotes:
      local_price = (quote["top_bid"]["price"] + quote["top_ask"]["price"]) / 2
      test_price = getDataPoint(quote)[-1]
      self.assertEqual(test_price, local_price)


  def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    # anidado
    for quote in quotes:
      # varible local
      local_isGreater = quote["top_bid"]["price"] > quote["top_ask"]["price"]
      # pasada por funcion
      _, test_bid_price, test_ask_price, _ = getDataPoint(quote)
      # comprobacion del test
      test_isGreater = test_bid_price > test_ask_price
      # check
      self.assertEqual(test_isGreater, local_isGreater)

  """ ------------ Add more unit tests ------------ """
  def test_getDataPoint_calculateRatio(self):
    quotes = [
      {'top_ask': {'price': 119.92, 'size': 107}, 'timestamp': '2020-11-17 00:11:13.274292', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 118.9, 'size': 33}, 'timestamp': '2020-11-18 07:41:41.259854', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    # variables
    test_list_prices = {}
    local_list_prices = {}

    # loop
    for quote in quotes:
      # local variable calculation
      local_price = (quote["top_bid"]["price"] + quote["top_ask"]["price"]) / 2
      local_list_prices[quote["stock"]] = local_price

      # test variable through function
      test_stock, _, _, test_price = getDataPoint(quote)
      test_list_prices[test_stock] = test_price

    # assert between two objects
    self.assertEqual(test_list_prices, local_list_prices)


if __name__ == '__main__':
    unittest.main()
