
from webullsdkmdata.quotes.subscribe.basic_quote_decoder import BasicQuoteDecoder
from webullsdkmdata.quotes.subscribe.message_pb2 import QuoteData
import unittest


class TestSnapshotDecoder(unittest.TestCase):
    def test_serial_deserial(self):
        quote = QuoteData()
        quote.ask_price = "0.01"
        quote.bid_price = "0.02"
        quote.ask_size = "100"
        quote.bid_size = "99"
        quote.basic.symbol = "AAPL"
        quote.basic.instrument_id = "1000001"
        quote.basic.timestamp = "1645100239111"
        serialized_value = quote.SerializeToString()
        print("serialized value:", serialized_value, ", type:", type(serialized_value))
        decoder = BasicQuoteDecoder()
        deserialized_value = decoder.parse(serialized_value)
        print("deserialized value:", deserialized_value, ", type:", type(deserialized_value))
        self.assertFalse(isinstance(deserialized_value, QuoteData))
        self.assertEqual(quote.ask_price, str(deserialized_value.get_ask_price()))
        self.assertEqual(quote.basic.timestamp, str(deserialized_value.basic.get_timestmap()))
