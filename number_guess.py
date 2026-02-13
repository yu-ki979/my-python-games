import streamlit as st
import random

# タイトルを表示
st.title("🔢 数当てゲーム")

# 答えの数字を準備（まだなければ作成）
if "target" not in st.session_state:
    st.session_state.target = random.randint(1, 100)
    st.session_state.count = 0

st.write("１から１００の間で数字を当ててね！")

# 入力ホームを作る
guess = st.number_input("予想した数字", min_value=1, max_value=100)

# ボタンが押された時の処理
if st.button("予想する"):
    st.session_state.count += 1

    if guess < st.session_state.target:
        st.warning("もっと大きいよ！ ⬆️")
    elif guess > st.session_state.target:
        st.warning("もっと小さいよ！ ⬇️")
    else:
        st.success(f"正解！ 🎉 {st.session_state.count}回目で正解しました！")
        st.balloons()
