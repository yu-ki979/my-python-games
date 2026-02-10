import streamlit as st
import random

st.title("スマホで遊べるハイ＆ロー")

# セッション状態を保持する仕組み
if "current" not in st.session_state:
    st.session_state.current = random.randint(1, 10)

st.write(f"今のカードは **{st.session_state.current}** です。")

# ボタンを作る
col1, col2 = st.columns(2)
with col1:
    high_btn = st.button("High（次の方が大きい）")
with col2:
    low_btn = st.button("Low（次の方が小さい）")

if high_btn or low_btn:
    next_card = random.randint(1, 10)
    st.write(f"次のカードは **{next_card}** でした！")

    # ここから判定
    if high_btn:
        if next_card > st.session_state.current:
            st.success("当たり！🎯")
        else:
            st.error("はずれ...😢")
    
    elif low_btn:
        if next_card < st.session_state.current:
            st.success("当たり！🎯")
        else:
            st.error("はずれ...😢")

    #次のゲームのためにカードを更新
    st.session_state.current = next_card
    st.button("もう一度遊ぶ")