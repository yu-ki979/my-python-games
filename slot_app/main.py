import js
import random
import asyncio

# 1. 画像リスト
images = ["img0.png", "img1.png", "img2.png", "img3.png", "img4.png"]
is_spinning = [False, False, False]
results = [None, None, None]

async def spin_logic(i):
    # 各リールを個別に回し続ける関数
    global is_spinning, results
    while is_spinning[i]:
        selected = random.choice(images)
        reel = js.document.getElementById(f"reel-{i}")
        reel.innerHTML = f'<img src="./images/{selected}">'
        results[i] = selected
        await asyncio.sleep(0.1) # 高速回転
    
async def spin():
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

    # 3つとも止まったかチェック
    if not any(is_spinning):
        check_result()

def check_result():
    msg_el = js.document.getElementById("result-message")
    js.document.getElementById("spin-btn").disabled = False

    if results[0] == results[1] == results[2]:
        msg_el.innerText = "JNOMON WIN!!! 🎉"
        msg_el.style.color = "#ff4500"
    else:
        msg_el.innerText = "残念！！"
        msg_el.style.color = "#8b4513"
