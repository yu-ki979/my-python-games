import js
import random
import asyncio

# 1. 画像リスト
images = ["img0.png", "img1.png", "img2.png", "img3.png", "img4.png"]
won_images = set() # 当たった画像を記録するセット
is_spinning = [False, False, False]
results = [None, None, None]

# --- 音を鳴らす新しい関数 ---
def play_sound(sound_id):
    el = js.document.getElementById(f"snd-{sound_id}")
    if el:
        el.currentTime = 0
        el.play()

# --- リーチ音専用（再生・停止） ---
def control_reach(action):
    el = js.document.getElementById("snd-reach")
    if el:
        if action == "play":
            el.play()
        else:
            el.pause()
            el.currentTime = 0

async def spin_logic(i):
    # 各リールを個別に回し続ける関数
    global is_spinning, results
    while is_spinning[i]:
        selected = random.choice(images)
        reel = js.document.getElementById(f"reel-{i}")
        reel.innerHTML = f'<img src="./images/{selected}">'
        results[i] = selected
        await asyncio.sleep(0.2) # 高速回転
    
async def spin():
    # --- スマホのロック解除の儀式 ---    
    for s in ["stop", "reach", "win", "miss", "complete"]:
        el = js.document.getElementById(f"snd-{s}")
        if el:
            el.play()
            el.pause()
    
    global is_spinning
    msg_el = js.document.getElementById("result-message")
    msg_el.innerText = ""
    js.document.getElementById("spin-btn").disabled = True    

    for i in range(3):
        is_spinning[i] = True
        js.document.getElementById(f"stop-{i}").disabled = False
        asyncio.ensure_future(spin_logic(i))

def stop_reel(i):
    global is_spinning
    if not is_spinning[i]: return # すでに止まっていれば何もしない

    is_spinning[i] = False
    js.document.getElementById(f"stop-{i}").disabled = True

    # --- リーチ演出 ---
    # 2つ止まっていて、かつその2つが同じ絵柄ならリーチ！
    stopped_count = is_spinning.count(False)
    if stopped_count == 2:
        # 止まっているリールのインデックスを探す
        stopped_indices = [idx for idx, s in enumerate(is_spinning) if not s]
        if results[stopped_indices[0]] == results[stopped_indices[1]]:
            control_reach.play() # リーチ音をリピート再生
            # まだ回っている最後のリールを探して光らせる
            active_idx = is_spinning.index(True)
            js.document.getElementById(f"reel-{active_idx}").style.borderColor = "#ff4500"
            js.document.getElementById(f"reel-{active_idx}").style.boxShadow = "0 0 20px #ff4500"

    # 3つとも止まったかチェック
    if not any(is_spinning):
        # リーチ音を止める
        control_reach("stop") # 全て止まったらリーチ音を消す        check_result()
        check_result()

    play_sound("stop.mp3") # ボタンを押した瞬間に鳴らす

def check_result():
    msg_el = js.document.getElementById("result-message")
    js.document.getElementById("spin-btn").disabled = False

    # リーチ演出の光をリセット
    for j in range(3):
        js.document.getElementById(f"reel-{j}").style.borderColor = "#8b4513"
        js.document.getElementById(f"reel-{j}").style.boxShadow = "inset 0 0 10px rgba(0,0,0,0.1)"

    if results[0] == results[1] == results[2]:
        winning_img = results[0]
        msg_el.innerText = "JNOMON WIN!!! 🎉"

        won_images.add(winning_img)

        # --- コレクションを画像で埋める ---
        idx = images.index(winning_img)
        col_box = js.document.getElementById(f"col-{idx}")
        col_box.style.opacity = "1"
        # 縦横80%に抑えつつ、中央に綺麗に配置するスタイルを追加
        col_box.innerHTML = f'<img src="./images/{winning_img}" style="width:80%; height:80%; object-fit:contain; display:block;">'

        # フラッシュ演出を呼び出す
        asyncio.ensure_future(flash_effect())

        # コンプリート判定
        if len(won_images) >= 5:
            play_sound("complete.mp3")
            comp_msg = js.document.getElementById("complete-msg")
            comp_msg.innerText = "全種類コンプリート！！ 🤩"  
            comp_msg.style.display = "block" # 念のため表示を確実にする  
            js.document.getElementById("reset-btn").style.display = "inline-block"
            msg_el.innerText = "伝説の縄文マスター！"
        else:
            # 通常の当たりサウンド
            play_sound("win.mp3")
            msg_el.innerText =  "JOMON WIN!!! 🎉"  
    else:
        play_sound("miss.mp3")
        msg_el.innerText = "残念！！"
        msg_el.style.color = "#8b4513"

# フラッシュ演出
async def flash_effect():
    body = js.document.body
    original_bg = body.style.backgroundColor
    for _ in range(6): # 6回点滅
        body.style.backgroundColor = "#fffacd"
        await asyncio.sleep(0.1)
        body.style.backgroundColor = "#ffd700"
        await asyncio.sleep(0.1)
    body.style.backgroundColor = "#f5f5dc"

def reset_game():
    global won_images
    won_images.clear()
    control_reach("stop")

    # 棚の初期化（見た目を「？」に戻す）
    for i in range(len(images)):
        col_box = js.document.getElementById(f"col-{i}")
        col_box.style.opacity = "0.2"
        col_box.innerHTML = "？"
    
    # メッセージとボタンの初期化
    js.document.getElementById("complete-msg").style.display = "none"
    js.document.getElementById("reset-btn").style.display = "none"
    js.document.getElementById("result-message").innerText = "リセット完了"

