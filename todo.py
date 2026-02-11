import streamlit as st

st.title("📝 シンプルTODOリスト")

# 1. 記憶の棚（リスト）を準備する
if "todo_list" not in st.session_state:
    st.session_state.todo_list = []

# 2. 入力欄を作る
new_task = st.text_input("新しいタスクを入力してください")

# 3. 追加ボタン
if st.button("追加"):
    if new_task: # 文字が入っている時だけ実行
        st.session_state.todo_list.append(new_task)
        st.success(f"「{new_task}を追加しました！")
    else:
        st.warning("何か文字を入力してください。")

st.divider()

# 4. 保存されたリストを表示する
st.subheader("現在のリスト")

for i, task in enumerate(st.session_state.todo_list):
    col_t, col_b = st.columns([4, 1]) # 4:1の比率で横に分ける

    col_t.write(f"・{task}")

    # 削除ボタン。keyに番号を入れないと、全部同じボタンだと勘違いされる
    if col_b.button("削除", key=f"delete_{i}"):
        st.session_state.todo_list.pop(i) # リストの１番目を消す
        st.rerun() # 画面を更新して消えたことを反映


# 5. リセットボタン
if st.button("リストを空にする"):
    st.session_state.todo_list = []
    st.rerun() # 画面を強制的にリフレッシュ
        