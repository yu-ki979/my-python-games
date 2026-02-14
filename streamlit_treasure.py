import streamlit as st
import random

#【論理の定義】
# ページをリロードしてもデータが消えないように、session_stateを使う
if "player_pos" not in st.session_state:
    st.session_state.player_pos = [2,2]
    st.session_state.treasure_pos = \
    [random.randint(0, 4), random.randint(0, 4)]
    st.session_state.message = "宝を探せ！ (5x5のどこかに眠っているぞ)"

st.title("💎 宝探し")

#【移動の型】
# ボタンによる座標の更新
st.write(st.session_state.message)

col1, col2, col3 = st.columns(3)
with col2:
    if st.button("↑ Up"):
        st.session_state.player_pos[1] \
        = max(0, st.session_state.player_pos[1] - 1)
col1, col2, col3 = st.columns(3)
with col1:
    if st.button("← Left"):
        st.session_state.player_pos[0] \
        = max(0, st.session_state.player_pos[0] - 1)
with col3:
    if st.button("→ Right"):
        st.session_state.player_pos[0] \
        = min(4, st.session_state.player_pos[0] + 1)
with col2:
    if st.button("↓ Down"):
        st.session_state.player_pos[1] \
        = min(4, st.session_state.player_pos[1] + 1)

#【判定の型】
# 現在地と宝の座標が一致するか？
if st.session_state.player_pos == st.session_state.treasure_pos:
    st.success("🎉 おめでとう！宝を見つけた！")
    if st.button("もう１度遊ぶ"):
        st.session_state.player_pos = [0, 0]
        st.session_state.treasure_pos \
        = [random.randint(0, 4), random.randint(0, 4)]
        st.rerun()

#【可視化】
# 5x5のグリッドを表示
st.write("---")
for y in range(5):
    cols = st.columns(5)
    for x in range(5):
        if [x, y] == st.session_state.player_pos:
            cols[x].markdown("## 👤") # プレイヤー
        else:
            cols[x].markdown("## ⬜") # 空きマス