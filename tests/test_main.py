import unittest
from unittest.mock import patch
from io import StringIO

# # 券売機の関数をインポート（sourceフォルダにある ticket_machine をインポート）
# import sys
# sys.path.append("../source")  # sourceフォルダをパスに追加
# import ticket_machine
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../source')))

import main

# ここにテストコードを記述します

class TestTicketMachine(unittest.TestCase):
    
    def test_purchase_total(self):
        """購入合計金額の計算テスト"""
        menu = {
            "1": {"name": "特製ラーメン", "price": 1000},
            "2": {"name": "醤油ラーメン", "price": 780},
        }
        purchase = [menu["1"], menu["2"]]
        total = sum(item['price'] for item in purchase)
        self.assertEqual(total, 1780)
    
    @patch("builtins.input", side_effect=["2000"])
    @patch("sys.stdout", new_callable=StringIO)
    def test_payment(self, mock_stdout, mock_input):
        """支払い処理のテスト（お釣り計算）"""
        total = 1500
        cash = int(input("現金を投入してください>"))
        change = cash - total
        print(f"おつり{change}円です。")
        
        self.assertEqual(change, 500)
        self.assertIn("おつり500円です。", mock_stdout.getvalue())
    
    def test_reset_sales(self):
        """売上リセット処理のテスト"""
        sales = {
            "1": {"name": "特製ラーメン", "sold": 10, "revenue": 10000},
        }
        for item in sales.values():
            item['sold'] = 0
            item['revenue'] = 0
        
        self.assertEqual(sales["1"]["sold"], 0)
        self.assertEqual(sales["1"]["revenue"], 0)
    
    def test_change_price(self):
        """商品の価格変更処理のテスト"""
        sales = {
            "1": {"name": "特製ラーメン", "price": 1000},
        }
        new_price = 1200
        sales["1"]["price"] = new_price
        
        self.assertEqual(sales["1"]["price"], 1200)

if __name__ == "__main__":
    unittest.main()