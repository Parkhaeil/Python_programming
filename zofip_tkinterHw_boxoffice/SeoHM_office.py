import os
import tkinter as tk
from tkinter import messagebox, simpledialog
import datetime

class MenuOrderApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Zeze's Restaurant")


        # 메뉴 및 가격 정보
        self.menu_items = {
            "알리오올리오": 8.9,
            "새우토마토파스타": 9.9,
            "샐러드파스타": 7.9,
            "목살스테이크": 16.9,
            "목살필라프": 9.9
        }

        # 상단 제목
        self.title_label = tk.Label(root, text="Menu", font=("Arial", 20, "bold"))
        self.title_label.grid(row=0, column=0, columnspan=2, pady=10)

        # 메뉴판 가격 표시
        price_label = tk.Label(root, text="(1.0 = 1000원)", font=("Arial", 10), fg="purple")
        price_label.grid(row=0, column=2, padx=10, pady=10, sticky="e")

        # 메뉴 목록 및 가격 표시
        menu_frame = tk.Frame(root, bg="light blue", padx=10, pady=10)
        menu_frame.grid(row=1, column=0, columnspan=2)

        for i, (menu, price) in enumerate(self.menu_items.items(), start=1):
            menu_label = tk.Label(menu_frame, text=menu, font=("Arial", 12))
            menu_label.grid(row=i, column=0, padx=10, pady=5, sticky="e")

            price_label = tk.Label(menu_frame, text=f"{price}", font=("Arial", 12))
            price_label.grid(row=i, column=1, padx=10, pady=5, sticky="w")

        # 구매자 정보 입력
        self.name_label = tk.Label(root, text="이름:")
        self.name_label.grid(row=2, column=0, sticky="e")
        self.name_entry = tk.Entry(root)
        self.name_entry.grid(row=2, column=1, pady=5)

        self.phone_label = tk.Label(root, text="휴대폰 번호:")
        self.phone_label.grid(row=3, column=0, sticky="e")
        self.phone_entry = tk.Entry(root)
        self.phone_entry.grid(row=3, column=1, pady=5)
        self.phone_placeholder = "010-xxxx-xxxx"
        self.phone_entry.insert(0, self.phone_placeholder)
        self.phone_entry.config(fg="gray")

        self.phone_entry.bind("<FocusIn>", self.on_phone_entry_focus_in)
        self.phone_entry.bind("<FocusOut>", self.on_phone_entry_focus_out)

        # 메뉴 선택
        self.menu_label = tk.Label(root, text="주문 수량:", bg="dark grey", fg="white")
        self.menu_label.grid(row=4, column=0, columnspan=2, pady=10, sticky="w")

        self.menu_frame = tk.Frame(root, bg="yellow", padx=10, pady=10)
        self.menu_frame.grid(row=5, column=0, columnspan=2)

        self.menu_vars = {}
        self.menu_entries = {}
        for i, (menu, price) in enumerate(self.menu_items.items(), start=1):
            var = tk.IntVar()

            entry = tk.Spinbox(self.menu_frame, from_=0, to=5, width=3, textvariable=var)
            entry.grid(row=i, column=1, padx=5, pady=2, sticky="w")

            self.menu_vars[menu] = var
            self.menu_entries[menu] = entry

            label = tk.Label(self.menu_frame, text=menu)
            label.grid(row=i, column=0, sticky="e")

        # 버튼
        self.order_button = tk.Button(root, text="구매완료", command=self.place_order)
        self.order_button.grid(row=6, column=0, pady=10)

        self.birthday_discount_button = tk.Button(root, text="생일할인", command=self.apply_birthday_discount)
        self.birthday_discount_button.grid(row=6, column=1, pady=10)

        self.cancel_button = tk.Button(root, text="취소", command=self.cancel_order)
        self.cancel_button.grid(row=6, column=2, pady=10)

        # 주문 번호 초기화
        self.order_number = 1

        # 생일할인 적용 여부
        self.birthday_discount_applied = False

        #광고
        # 회색 배경 프레임 생성
        ad_frame = tk.Frame(root, bg="lightgray")
        ad_frame.grid(row=len(self.menu_items)+10, column=0, padx=10, pady=5, sticky="w", columnspan=2)

        # 광고 표시
        ad = tk.Label(ad_frame, text="<zeze_Restuarant>", font=("Arial", 10), bg="lightgray", anchor="w")
        ad.pack(side="top", anchor="w")

        ad1 = tk.Label(ad_frame, text="T.051-111-1111", font=("Arial", 10), bg="lightgray", anchor="w")
        ad1.pack(side="top", anchor="w")

        ad2 = tk.Label(ad_frame, text="E:zeze@pusan.ac.kr", font=("Arial", 10), bg="lightgray", anchor="w")
        ad2.pack(side="top", anchor="w")

        ad3 = tk.Label(ad_frame, text="51051", font=("Arial", 10), bg="lightgray", anchor="w")
        ad3.pack(side="top", anchor="w")


    def on_phone_entry_focus_in(self, event):
        if self.phone_entry.get() == self.phone_placeholder:
            self.phone_entry.delete(0, tk.END)
            self.phone_entry.config(fg="black")

    def on_phone_entry_focus_out(self, event):
        if not self.phone_entry.get():
            self.phone_entry.insert(0, self.phone_placeholder)
            self.phone_entry.config(fg="gray")

    def place_order(self):

        # 이름 입력 확인
        name = self.name_entry.get().strip()
        if not name:
            messagebox.showerror("오류", "이름을 입력하세요.")
            return

        # 휴대폰 번호 입력 확인
        phone = self.phone_entry.get().strip()
        if phone == self.phone_placeholder:
            phone = ""
        if not phone:
            messagebox.showerror("오류", "휴대폰 번호를 입력하세요.")
            return

        # 주문 내용 확인
        order_items = []
        total_price = 0
        for menu, var in self.menu_vars.items():
            quantity = var.get()
            if quantity > 0:
                price = self.menu_items[menu]
                order_items.append(f"{menu} (수량: {quantity})")
                total_price += price * quantity

        if not order_items:
            messagebox.showerror("오류", "주문할 메뉴를 선택하세요.")
            return

        #전화번호 010 오류
        if not phone.startswith("010"):
            messagebox.showerror("오류", "전화번호는 010으로 시작해야 합니다.")
            return

        if not phone[3] == "-":
            messagebox.showerror("오류", "010-xxxx-xxxx으로 해야합니다.")
            return




        # 주문 내용 저장
        order_details = f"주문번호: 주문{self.order_number}\n이름: {name}\n휴대폰 번호: {phone}\n메뉴: {', '.join(order_items)}\n"

        if self.birthday_discount_applied:
            discount_price = total_price * 0.1
            total_price -= discount_price
            order_details += f"할인 가격: {discount_price:.2f}\n"
            order_details += f"총 가격: {total_price:.2f} (생일할인 10% 적용됨)\n"
            self.birthday_discount_applied = False
        else:
            order_details += f"총 가격: {total_price:.2f}\n"

        # 파일 경로 설정
        with open("SeoHM_order.txt", "a", encoding="utf-8") as file:
            file.write(order_details)
            file.write("\n")

        # 주문 완료 메시지 및 초기화
        messagebox.showinfo("주문 완료", "주문이 완료되었습니다.")
        self.name_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)
        self.phone_entry.insert(0, self.phone_placeholder)
        self.phone_entry.config(fg="gray")
        self.order_number += 1
        for menu_entry in self.menu_entries.values():
            menu_entry.delete(0, tk.END)
            menu_entry.insert(0, 0)

    def apply_birthday_discount(self):
        # 생일 정보 입력 확인
        birth_month = simpledialog.askinteger("생일 정보", "생일 달을 입력하세요 (숫자로 입력)")
        if not birth_month:
            return

        today = datetime.date.today()
        if birth_month == today.month:
            self.birthday_discount_applied = True
            messagebox.showinfo("할인 적용", "생일 할인이 적용되었습니다. 구매완료 버튼을 눌러주십시오.")
        else:
            messagebox.showinfo("할인 적용 불가", "생일 달이 아닙니다.")

    def cancel_order(self):
        self.name_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)
        self.phone_entry.insert(0, self.phone_placeholder)
        self.phone_entry.config(fg="gray")
        for menu_entry in self.menu_entries.values():
            menu_entry.delete(0, tk.END)
            menu_entry.insert(0, 0)


# 메인 윈도우 생성
root = tk.Tk()
root.configure(bg="sky blue")
app = MenuOrderApp(root)
root.mainloop()
