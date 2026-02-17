# type: ignore

import random
from pyscript import Element

# 1. 土偶（カード）の準備
card_values = ["A", "B", "C", "D", "E"] * 2
random.shuffle(card_values)

# 2. ゲーム画面にカードを並べる
def setup_game():
    board = Element("game-board")

    # 10回繰り返してカードを作る
    for i in range(10):
        # HTMLの型を作成
        card_html= f'<div id="card"-{i}" class="card" onclick="py_click({i})">?</div>'
        # 画面（game-board)に追加
        board.element.innerHTML += card_html

# 3. クリックしたときの「型」
def py_click(index):
    # クリックされたカードの文字を表示する
    card = Element(f"card-{index}")
    card.element.innerText = card_values[index]
    print(f"{index}番目のカード「{card_values[index]}」が選ばれました！")

# ゲーム開始
setup_game()
