import js
import random
import asyncio

images = ["img0.png", "img1.png", "img2.png", "img3.png", "img4.png"]
won_images = set()
is_spinning = [False, False, False]
results = [None, None, None]

def play_sound(sound_id):
    el = js.document.getElementById(f"snd-{sound_id}")
    if el:
        el.currentTime = 0
        el.play()

def control_reach(action):
    el = js.document.getElementById("snd-reach")
    if el:
        if action == "play":
            el.play()
        else:
            el.pause()
            el.currentTime = 0

async def spin_logic(i):
    global is_spinning, results
    while is_spinning[i]:
        selected = random.choice(images)
        js.document.getElementById(f"reel-{i}").innerHTML = f'<img src="./images/{selected}">'
        results[i] = selected
        await asyncio.sleep(0.08)

async def spin():
    # スマホの音出し制限を解除
    for s in ["stop", "reach", "win", "miss", "complete"]:
        el = js.document.getElementById(f"snd-{s}")
        if el:
            el.play()
            el.pause()
    
    global is_spinning
    js.document.getElementById("result-message").innerText = ""
    js.document.getElementById("spin-btn").disabled = True
    for i in range(3):
        is_spinning[i] = True
        js.document.getElementById(f"stop-{i}").disabled = False
        asyncio.ensure_future(spin_logic(i))

def stop_reel(i):
    global is_spinning
    if not is_spinning[i]: return
    is_spinning[i] = False
    js.document.getElementById(f"stop-{i}").disabled = True
    play_sound("stop") 

    stopped_count = is_spinning.count(False)
    if stopped_count == 2:
        stopped_indices = [idx for idx, s in enumerate(is_spinning) if not s]
        if results[stopped_indices[0]] == results[stopped_indices[1]]:
            control_reach("play")

    if not any(is_spinning):
        control_reach("stop")
        check_result()

def check_result():
    js.document.getElementById("spin-btn").disabled = False
    msg_el = js.document.getElementById("result-message")
    
    if results[0] == results[1] == results[2]:
        winning_img = results[0]
        won_images.add(winning_img)
        msg_el.innerText = "🎉 JOMON WIN!!! 🎉"
        
        idx = images.index(winning_img)
        col_box = js.document.getElementById(f"col-{idx}")
        col_box.style.opacity = "1"
        col_box.innerHTML = f'<img src="./images/{winning_img}">'
        
        if len(won_images) >= 5:
            play_sound("complete")
            js.document.getElementById("complete-msg").style.display = "block"
            js.document.getElementById("reset-btn").style.display = "inline-block"
        else:
            play_sound("win")
    else:
        play_sound("miss")
        msg_el.innerText = "残念！"

def reset_game():
    js.window.location.reload()