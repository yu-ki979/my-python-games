import streamlit as st
import random

# タイトルを表示
st.title("🔢 1/1000のキセキ")
if st.session_state.best_score != float("inf"):
    st.sidebar.metric("🏆 自己ベスト", f"{st.session_state.best_score}回")
# 答えの数字を準備（まだなければ作成）
if "target" not in st.session_state:
    st.session_state.target = random.randint(1, 1000)
    st.session_state.count = 0
    # 履歴を入れる「空のリスト」を作る
    st.session_state.history = []

if "best_score" not in st.session_state:
    st.session_state.best_score = float("inf") # 最初は無限大にしておく

st.write("１から１０００の間で数字を当ててね！")

# 入力ホームを作る
guess = st.number_input("予想した数字", min_value=1, max_value=1000)

# ボタンが押された時の処理
if st.button("予想する"):
    st.session_state.count += 1
    # 入力した数字を履歴リストに追加
    st.session_state.history.append(guess)

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

        # 今回のスコアがベストスコアより小さければ更新
        if st.session_state.count < st.session_state.best_score:
            st.session_state.best_score = st.session_state.count
            st.write(f"🌟 自己ベスト更新！現在の記録：{st.session_state.best_score}回")
        else:
            st.write(f"現在の自己ベスト：{st.session_state.best_score}回")    
# 履歴を画面に表示する
if st.session_state.history:
    st.write("---")
    st.subheader("📝 あなたがこれまでに予想した数字")
    # 履歴を横並びに
    st.info(",".join(map(str, st.session_state.history)))
# リプレイボタン
if st.button("もう１度遊ぶ"):
    # 全消しせず特定のデータだけ上書き
    st.session_state.target = random.randint(1, 1000) # 新しい正解
    st.session_state.count = 0 # 回数を0に
    st.session_state.history = [] # 履歴を空に    
    # 画面を再読読み込みする
    st.rerun()
