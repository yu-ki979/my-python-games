<<<<<<< HEAD
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
=======
import streamlit as st
import random

# 1. ページの設定
st.set_page_config(page_title="最強ハイ＆ロー", page_icon="🃏")

# 2. 記憶の箱（セッション状態）の初期化
if "current" not in st.session_state:
    st.session_state.current = random.randint(1, 13)
if "score" not in st.session_state:
    st.session_state.score = 0
if "max_score" not in st.session_state:
    st.session_state.max_score = 0

# 3. 画面の表示
st.title("🃏 超・ハイ＆ロー")
st.markdown("""
次に出てくる数字が今の数字より、**大きい(High)** か **小さい(Low)** かを当ててください。
連勝してハイスコアを目指しましょう！
""")

st.divider()

# スコア表示
col_s1, col_s2 = st.columns(2)
col_s1.metric("現在の連勝数：", f"{st.session_state.score}回")
col_s2.metric("これまでの最高記録：", f"{st.session_state.max_score}回")

st.write("今のカードは...")
st.header(f"✨ {st.session_state.current}")

# 4. 操作ボタン
col1, col2 = st.columns(2)
with col1:
    high_btn = st.button("⬆️ High（次の方が大きい）", use_container_width=True)
with col2:
    low_btn = st.button("⬇️ Low（次の方が小さい）", use_container_width=True)

# 5. ゲームの判定ロジック（ここから下が全部セット！）
if high_btn or low_btn:
    next_card = random.randint(1, 13)
    st.write(f"次のカードは... **{next_card}** でした！")

    # --- ここから下の判定も、全部「ボタンが押された時」の部屋に入れる ---
    win = False
    if high_btn and next_card > st.session_state.current:
        win = True
    elif low_btn and next_card < st.session_state.current:
        win = True

    if next_card == st.session_state.current:
        st.warning("引き分け！数字が同じでした。")
    elif win:
        st.success("🎉 正解！おめでとう！")
        st.session_state.score += 1
        if st.session_state.score > st.session_state.max_score:
            st.session_state.max_score = st.session_state.score
            st.balloons()
    else:
        st.error("残念... はずれです😢")
        st.session_state.score = 0 # .score を忘れずに！

    # 次の勝負のためにカードを更新
    st.session_state.current = next_card
    
    # 画面を再読み込みしてスコアを更新反映させるためのボタン
    st.button("次のカードへ")
>>>>>>> 9c3b2e7e14b752914c849225a6be5faa6987c9ab
