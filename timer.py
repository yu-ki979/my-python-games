import streamlit as st
import time

st.title("⏳ 集中タイマー")

# 1. 何分測るか選ぶ
minutes = st.number_input("タイマーをセット（分）", min_value=1, value=25)
seconds = minutes * 60

# スタートボタン
if st.button("スタート！"):
    # プログラム用の表示場所を確保
    display = st.empty()

    # カウントダウンのループ
    while seconds > 0:
        # 分と秒に計算し直す
        m, s = divmod(seconds, 60)
        # 画面を書き換える(02dは「2桁で表示」という意味)
        display.header(f"残り {m:02d}：{s:02d}")

        # １秒待機
        time.sleep(1)
        # 秒数を１減らす
        seconds -= 1

    # 4. 終了の合図
    display.header("⏰ 終了！お疲れさまでした！")
    st.balloons()