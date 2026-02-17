# type: ignore

from pyodide.ffi import create_proxy
from js import document
import random

count = 0

# 画像のリストを作る
Dogus = ["Dogu0.png", "Dogu1.png", "Dogu2.png", "Dogu3.png"]

def hakkutsu(event):
    global count # 外にあるcountを使う宣言
    count += 1

    # 画面の文字を書き換える
    document.getElementById("counter").innerText = f"発掘された遺物：{count} 個"

    # 1. 画面に表示する要素を作る
    selected_item = random.choice(Dogus)
    el = document.createElement("img")
    el.src = selected_item
    el.style.position = "absolute"
    el.style.width = "100px"

    # 2. 座標を計算
    ground = document.getElementById("ground")
    rect = ground.getBoundingClientRect()
    pos_x = event.clientX - rect.left
    pos_y = event.clientY - rect.top

    el.style.left = f"{pos_x -50}px"
    el.style.top = f"{pos_y -50}px"

    # ランダムな値を決める
    kakudo = random.randint(0,360)
    tomeido = random.uniform(0.3, 1.0)

    # 4. 演出：回転と拡大を適用
    el.style.transform = f"rotate({kakudo}deg) scale(0.1)"
    el.style.transition = "transform 0.2s cubic-bezier(0.17, 0.67, 0.83, 0.67)"
    el.style.opacity = str(tomeido)

    # 6. 地面(ground)の中に追加
    document.getElementById("ground").appendChild(el)

    #7. 追加した直後に、サイズを1.0倍（本来の大きさ）に上書きする
    # ※一瞬遅らせるために、Pythonの「魔法の呪文」を使うよ
    from js import setTimeout
    from pyodide.ffi import create_proxy

    def resize():
        el.style.transform = f"rotate({kakudo}deg) scale(1.0)"
    
    setTimeout(create_proxy(resize), 10) # 0.01秒後に大きくする
# 関数を登録
proxy = create_proxy(hakkutsu)
document.getElementById("ground").addEventListener("click", proxy)