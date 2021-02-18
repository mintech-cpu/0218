import random

d = {'apple':"リンゴ", 'banana':"バナナ", 'peach':"モモ"}

while True:
    # 英単語を表示
    word = random.choice(list(d.keys()))
    print(word)
    # 自分が日本語を入力
    answer = input()
    # 自分が入力した日本語と、答えが合っているか確認
    if answer == "0":
        print("終了します。")
        break
    elif answer == d[word]:
        print("正解！")
    else:
        print("不正解")

