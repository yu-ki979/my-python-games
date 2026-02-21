from pyscript import Element
import random
import asyncio # setTimeoutの代わりにPythonの非同期処理を使います
import js
import time

# 1. データの準備
images = ["img0.png", "img1.png", "img2.png", "img3.png", "img4.png", "img5.png"]
card_values = images * 2
random.shuffle(card_values)

# 2. 状態管理
flipped_indices = [] 
lock_board = False   
matched_count = 0
miss_count = 0
start_time = None
is_playing = False

def setup_game():
    global start_time, is_playing
    start_time = None
    is_playing = False

    board_el = js.document.getElementById("game-board")
    board_el.innerHTML = ""
    
    for i in range(12):
        card = js.document.createElement("div")
        card.id = f"card-{i}"
        card.className = "card"
        card.innerText = "?"
        
        # 非同期クリックイベントの設定
        def on_click_handler(e, idx=i):
            asyncio.ensure_future(py_click(idx))
            
        card.onclick = on_click_handler
        board_el.appendChild(card)
# タイムを更新し続ける関数
async def update_timer():
    global start_time, is_playing
    while is_playing:
        if start_time is not None:
            elapsed = int(time.time() - start_time)
            js.document.getElementById("timer").innerText = str(elapsed)
        await asyncio.sleep(1) # 1秒ごとに更新

async def py_click(index):
    global lock_board, flipped_indices,\
    matched_count, miss_count,\
    start_time, is_playing
    
    card = js.document.getElementById(f"card-{index}")
    
    # 論理ガードを強化
    # 1. ロック中 2. すでにめくられている 3. すでにそろっている
    if lock_board or index in flipped_indices or card.classList.contains("matched"):
        return

    # 最初の1枚をめくった瞬間にタイマースタート
    if start_time is None:
        start_time = time.time()
        is_playing = True
        asyncio.ensure_future(update_timer())

    card.innerText = "" # 一旦 "?" を消す
    img = js.document.createElement("img")
    img.src = f"./images/{card_values[index]}"
    img.style.width = "auto"   # 幅を自動に（枠に合わせるのではなく画像比率を優先）
    img.style.height = "auto"  # 高さを自動に
    img.style.maxWidth = "80%"  # 枠からはみ出さない
    img.style.maxHeight = "80%" # 枠からはみ出さない
    img.style.display = "block" # 隙間をなくす規律
    card.appendChild(img)
    
    flipped_indices.append(index)

    if len(flipped_indices) == 2:
        lock_board = True 
        idx1, idx2 = flipped_indices

        if card_values[idx1] == card_values[idx2]:
            # --- 一致した時の演出 ---
            js.document.getElementById(f"card-{idx1}").classList.add("matched")
            js.document.getElementById(f"card-{idx2}").classList.add("matched")
            matched_count += 1
            flipped_indices = []
            lock_board = False

            # --- 全部そろったかの判定 ---
            if matched_count == 6:
                is_playing = False # タイマー停止
                await asyncio.sleep(0.3)
                final_time = js.document.getElementById("timer").innerText
                msg_el = js.document.getElementById("message")
                msg_el.innerText = f"CLEAR!! 🎉)"
        else:
            # --- 不一致 ---
            # お手つきカウントアップ
            miss_count += 1
            js.document.getElementById("miss-count").innerText = str(miss_count)

            # Pythonの標準機能で0.7秒待機
            await asyncio.sleep(0.7)
            js.document.getElementById(f"card-{idx1}").innerText = "?"
            js.document.getElementById(f"card-{idx2}").innerText = "?"
            flipped_indices = []
            lock_board = False
setup_game()