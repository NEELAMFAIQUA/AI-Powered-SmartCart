import unittest

from cart import add_to_cart, recommend, remove_from_cart, subtotal


class CartTests(unittest.TestCase):
    def test_add_and_subtotal(self):
        cart = add_to_cart({}, "beans", 2)
        self.assertEqual(cart["beans"], 2)
        self.assertEqual(subtotal(cart), 19.0)

    def test_stock_limit(self):
        with self.assertRaises(ValueError):
            add_to_cart({}, "beans", 9)

    def test_remove_decrements_then_drops_item(self):
        cart = {"beans": 2}
        self.assertEqual(remove_from_cart(cart, "beans"), {"beans": 1})
        self.assertEqual(remove_from_cart({"beans": 1}, "beans"), {})

    def test_unknown_product(self):
        with self.assertRaises(KeyError):
            add_to_cart({}, "unknown")

    def test_recommendation_excludes_cart_products(self):
        picks = recommend({"beans": 1})
        self.assertNotIn("beans", [item["id"] for item in picks])
        self.assertTrue(picks)


if __name__ == "__main__":
    unittest.main()
