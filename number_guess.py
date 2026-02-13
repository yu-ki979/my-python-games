import streamlit as st
import random

# タイトルを表示
st.title("🔢 1/1000のキセキ")

# 答えの数字を準備（まだなければ作成）
if "target" not in st.session_state:
    st.session_state.target = random.randint(1, 1000)
    st.session_state.count = 0

st.write("１から１０００の間で数字を当ててね！")

# 入力ホームを作る
guess = st.number_input("予想した数字", min_value=1, max_value=1000)

# ボタンが押された時の処理
if st.button("予想する"):
    st.session_state.count += 1

    # 差を計算する
    diff = abs(guess - st.session_state.target)
    if guess < st.session_state.target:
        if diff <= 5:
            st.warning("うわ～！あとちょっと！あと少しだけ上！ 🤏")
        else:
            st.warning("全然足りないよ！もっと上 ⬆️")
    elif guess > st.session_state.target:
        if diff <= 5:
            st.warning("惜しい！あとちょっとだけ下！ 🤏")
        else:
            st.warning("行き過ぎ！戻ってきて ⬇️")
    else:
        st.success(f"大正解！天才かよ！ 🎉 {st.session_state.count}回目で正解しました！")
        st.balloons()

# リプレイボタン
if st.button("もう１度遊ぶ"):
    # セッションの中身を消して、最初の状態に戻す
    st.session_state.clear()
    # 画面を再読読み込みする
    st.rerun()
