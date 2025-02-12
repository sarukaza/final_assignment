import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def display_menu():
    clear_screen()
    print("\n***********************")
    print("       券売機シミュレータ")
    print("***********************\n")
    print("Enterキー押下で画面がクリアされて処理が進む")
    print("（ESCキー押下で管理画面に処理が進む）")
    print("（qキー押下でシミュレータ終了）\n")
    print("商品      金額")
    print("=======================")
    print("1.特製ラーメン 1000円")
    print("2.醤油ラーメン 780円")
    print("3.しおラーメン 880円")
    print("4.ごはん 150円")
    print("———")

def process_purchase():
    menu = {
        "1": {"name": "特製ラーメン", "price": 1000},
        "2": {"name": "醤油ラーメン", "price": 780},
        "3": {"name": "しおラーメン", "price": 880},
        "4": {"name": "ごはん", "price": 150},
    }
    purchase = []
    while True:
        item = input("購入する商品番号(支払いに進む場合はc)>")
        if item == 'c':
            break
        elif item in menu:
            purchase.append(menu[item])
        else:
            print("無効な入力です。もう一度試してください。")
    
    total = sum(item['price'] for item in purchase)

    # 商品ごとの数量をカウント
    item_counts = {}
    for item in purchase:
        name = item['name']
        if name in item_counts:
            item_counts[name] += 1
        else:
            item_counts[name] = 1

    print("\n商品       数量")
    for name, count in item_counts.items():
        print(f"{name}   {count}")
    print(f"===\n合計{total}円\n———")
    
    cash = int(input("現金を投入してください>"))
    if cash >= total:
        print(f"\nご購入ありがとうございます。おつり{cash - total}円です。")
    else:
        print("\n現金が不足しています。もう一度やり直してください。")
    
    input("\n（Enterキー押下でタイトル画面に戻ります）")

def management_mode():
    sales = {
        "1": {"name": "特製ラーメン", "price": 1000, "sold": 50, "revenue": 50000},
        "2": {"name": "醤油ラーメン", "price": 780, "sold": 10, "revenue": 7800},
        "3": {"name": "しおラーメン", "price": 880, "sold": 25, "revenue": 22000},
        "4": {"name": "ごはん", "price": 150, "sold": 6, "revenue": 900},
    }
    
    while True:
        clear_screen()
        print("\n***********************")
        print("       管理画面")
        print("***********************\n")
        print("======= 商品一覧 =======")
        print("商品      単価  販売数  売上金額")
        print("=======================")
        for key, value in sales.items():
            print(f"{key}.{value['name']} {value['price']}円  {value['sold']}   {value['revenue']}円")
        total_revenue = sum(item['revenue'] for item in sales.values())
        print(f"———\n総売上金額 {total_revenue}円\n")
        print("=== 管理メニュー ====")
        print("1. 売上をリセットする")
        print("2. 商品の価格を変更する")
        print("※売上がリセットされていないと利用できません。")
        print("3. 管理画面を終了する")
        print("———")
        
        option = input("管理コード入力: ")
        if option == '1':
            for value in sales.values():
                value['sold'] = 0
                value['revenue'] = 0
            print("\n売上をリセットしました。")
            input("\n（Enterキー押下でメニューに戻ります）")
        elif option == '2':
            item_num = input("\n価格を変更する商品の番号を入力してください。> ")
            if item_num in sales:
                new_price = int(input("変更金額を入力してください。> "))
                print(f"\n【{sales[item_num]['name']} {new_price}円】に変更します。")
                confirm = input("よろしいですか(Y/N）>").strip().lower()
                if confirm == 'y':
                    sales[item_num]['price'] = new_price
                    print("\n変更しました。")
                else:
                    print("\n変更をキャンセルしました。")
            else:
                print("\n無効な商品番号です。")
            input("\n（Enterキー押下でメニューに戻ります）")
        elif option == '3':
            print("\n管理画面を終了します。")
            input("\n（Enterキー押下でタイトル画面に戻ります）")
            break
        else:
            print("\n無効な入力です。")
            input("\n（Enterキー押下でメニューに戻ります）")

if __name__ == "__main__":
    while True:
        display_menu()
        # ※実際のESCキーはinput()で取得できないため、ここでは "esc" と入力することで管理画面に移行
        command = input("Enter your command: ").strip().lower()
        if command == 'q':
            break
        elif command == 'esc':
            management_mode()
        else:
            process_purchase()