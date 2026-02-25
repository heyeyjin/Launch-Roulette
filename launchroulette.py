import customtkinter as ctk
import random
import time

# 기본 창
root = ctk.CTk()
root.configure(fg_color="#9DE8D7")
root.title("오늘의 점심 메뉴 추천")
root.geometry("600x400")

# 메뉴 리스트
menus = ["국밥", "제육볶음", "돈까스", "샌드위치", "햄버거", "초밥", "치킨", "피자", "쌀국수", "파스타", "김밥", "라면"]

# 메뉴 레이블
label = ctk.CTkLabel(root, text="무엇을 먹을까?", font=("배달의민족 도현", 28, "bold"))
label.configure(text_color="black")
label.pack(pady=(60, 40))

def animation():
    start_button.configure(state="disabled")
    label.configure(text_color="black")

    for i in range(15):
        temp_pick = random.choice(menus)
        label.configure(text=temp_pick)
        root.update() # 실시간으로 화면 갱신
        time.sleep(0.05 + (i * 0.01))

    # 최종 선택
    final_pick = random.choice(menus)
    label.configure(text=f"🍽️ 오늘의 점심 메뉴는 {final_pick} 당첨! 🍽️", text_color="black")

    start_button.configure(state="normal", text="한 번 더 돌리기!")

# 룰렛 시작 버튼
def on_over(event):
    start_button.configure(text_color="#9DE8D7")
def on_leave(event):
    start_button.configure(text_color="white")

start_button = ctk.CTkButton(
    root,
    text="룰렛을 돌려보자!",
    width=100,
    height=50,
    corner_radius=25,
    command=animation, # animation 함수 실행
    fg_color="black",
    hover_color="white",
    text_color="white",
    font=("배달의민족 도현", 24, "bold"),
)
start_button.pack(pady=25, ipadx=5, ipady=5)

start_button.bind("<Enter>", on_over)
start_button.bind("<Leave>", on_leave)

root.mainloop()