import streamlit as st
import random

st.title("✊✌️🖐️ ジャンケンバトル")

# 1. 記憶の棚（スコアなど）を準備
if "win_count" not in st.session_state:
    st.session_state.win_count = 0

# 2. 自分の手を選ぶボタンを横に並べる
col1, col2, col3 = st.columns(3)

my_hand = None
if col1.button("✊"):
    my_hand = "グー"
if col2.button("✌"):
    my_hand = "チョキ"
if col3.button("✋"):
    my_hand = "パー"

# 勝敗判定
if my_hand:
    hands = ["グー", "チョキ", "パー"]
    com_hand = random.choice(hands)

    st.write(f"あなたの手： {my_hand}")
    st.write(f"相手の手： {com_hand}")

    if my_hand == com_hand:
        st.info("引き分けです！")
    
    elif (my_hand == "グー" and com_hand == "チョキ") or \
        (my_hand == "チョキ" and com_hand == "パー") or \
        (my_hand == "パー" and com_hand == "グー"):
        st.success("あなたの勝ち！")
        st.session_state.win_count += 1 # 勝ったらスコアを増やす

    else:
        st.error("あなたの負け...")

st.write(f"現在の勝ち数：{st.session_state.win_count}")

st.divider()

# 横に並べる
col_retry, col_reset = st.columns(2)

# もう１回勝負（スコアはそのまま）
if col_retry.button("もう１回勝負！"):
    st.rerun() # 画面を再読み込みするだけで、session_stateは維持される

# スコアをリセット
if col_reset.button("スコアをリセット"): 
    st.session_state.win_count = 0
    st.rerun() # 0に戻した後に画面をリフレッシュS
