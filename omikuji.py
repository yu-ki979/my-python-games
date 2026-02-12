import streamlit as st
import random

st.title("🔮 今日の運勢占い")

# おみくじのリスト
fortunes = [
    "超ラッキー！🌟",
    "なかなかの強運✨",
    "普通が一番😊",
    "のんびり過ごそう🍵",
    "逆にチャンス！💪"
            ]

if st.button("おみくじを引く"):
    # リストからランダムに１つ選ぶ
    result = random.choice(fortunes)

    # 演出
    st.balloons()
    st.success(f"結果は... **{result}** です！")
