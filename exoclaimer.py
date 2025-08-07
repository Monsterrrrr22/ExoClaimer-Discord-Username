import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
import threading
import time
import requests
import json
from datetime import datetime
import os
import sys
from tkinter import font

class ExoClaimer:
    def __init__(self):
        self.root = tk.Tk()
        self.setup_window()
        self.setup_variables()
        self.create_widgets()
        self.running = False
        self.thread = None
        self.attempts = 0
        self.success_count = 0
        
    def setup_window(self):
        self.root.title("EXO Claimer - Discord Username Hunter v2.1")
        self.root.geometry("900x700")
        self.root.configure(bg='#1a1a1a')
        self.root.resizable(False, False)
        
        try:
            self.root.iconbitmap('icon.ico')
        except:
            pass
            
    def setup_variables(self):
        self.username_var = tk.StringVar()
        self.password_var = tk.StringVar()
        self.token_var = tk.StringVar()
        self.target_user_var = tk.StringVar()
        self.mode_var = tk.StringVar(value="1")
        self.status_var = tk.StringVar(value="System Ready")
        self.delay_var = tk.StringVar(value="500")
        
    def create_widgets(self):
        main_frame = tk.Frame(self.root, bg='#1a1a1a')
        main_frame.pack(fill='both', expand=True, padx=15, pady=15)
        
        header_frame = tk.Frame(main_frame, bg='#1a1a1a')
        header_frame.pack(fill='x', pady=(0, 20))
        
        title_font = font.Font(family="Arial", size=24, weight="bold")
        title_label = tk.Label(header_frame, 
                              text="⚡ EXO CLAIMER",
                              font=title_font,
                              bg='#1a1a1a', 
                              fg='#00d4ff')
        title_label.pack()
        
        subtitle_font = font.Font(family="Arial", size=11)
        subtitle_label = tk.Label(header_frame, 
                                 text="Professional Discord Username Hunter - Advanced Edition",
                                 font=subtitle_font,
                                 bg='#1a1a1a', 
                                 fg='#888888')
        subtitle_label.pack(pady=(5, 0))
        
        mode_frame = tk.LabelFrame(main_frame, 
                                  text=" Hunt Mode Selection ",
                                  bg='#2d2d2d',
                                  fg='#ffffff',
                                  font=('Arial', 10, 'bold'),
                                  relief='solid',
                                  bd=1)
        mode_frame.pack(fill='x', pady=(0, 15))
        
        mode_inner = tk.Frame(mode_frame, bg='#2d2d2d')
        mode_inner.pack(fill='x', padx=15, pady=10)
        
        mode1_btn = tk.Radiobutton(mode_inner,
                                  text="1 - User Claim Test Mode",
                                  variable=self.mode_var,
                                  value="1",
                                  command=self.on_mode_change,
                                  bg='#2d2d2d',
                                  fg='#ffffff',
                                  selectcolor='#2d2d2d',
                                  activebackground='#2d2d2d',
                                  activeforeground='#00d4ff',
                                  font=('Arial', 9))
        mode1_btn.pack(anchor='w', pady=3)
        
        mode2_btn = tk.Radiobutton(mode_inner,
                                  text="2 - Full Checker + Claimer Mode",
                                  variable=self.mode_var,
                                  value="2",
                                  command=self.on_mode_change,
                                  bg='#2d2d2d',
                                  fg='#ffffff',
                                  selectcolor='#2d2d2d',
                                  activebackground='#2d2d2d',
                                  activeforeground='#00d4ff',
                                  font=('Arial', 9))
        mode2_btn.pack(anchor='w', pady=3)
        
        credentials_frame = tk.LabelFrame(main_frame,
                                        text=" Authentication Credentials ",
                                        bg='#2d2d2d',
                                        fg='#ffffff',
                                        font=('Arial', 10, 'bold'),
                                        relief='solid',
                                        bd=1)
        credentials_frame.pack(fill='x', pady=(0, 15))
        
        cred_inner = tk.Frame(credentials_frame, bg='#2d2d2d')
        cred_inner.pack(fill='x', padx=15, pady=10)
        
        self.create_input_fields(cred_inner)
        
        settings_frame = tk.LabelFrame(main_frame,
                                     text=" Hunt Settings ",
                                     bg='#2d2d2d',
                                     fg='#ffffff',
                                     font=('Arial', 10, 'bold'),
                                     relief='solid',
                                     bd=1)
        settings_frame.pack(fill='x', pady=(0, 15))
        
        settings_inner = tk.Frame(settings_frame, bg='#2d2d2d')
        settings_inner.pack(fill='x', padx=15, pady=10)
        
        delay_frame = tk.Frame(settings_inner, bg='#2d2d2d')
        delay_frame.pack(fill='x', pady=5)
        
        delay_label = tk.Label(delay_frame,
                              text="Request Delay (ms):",
                              bg='#2d2d2d',
                              fg='#ffffff',
                              font=('Arial', 9),
                              width=20,
                              anchor='w')
        delay_label.pack(side='left')
        
        delay_combo = ttk.Combobox(delay_frame,
                                  textvariable=self.delay_var,
                                  values=['100', '250', '500', '1000', '2000'],
                                  state='readonly',
                                  width=10)
        delay_combo.pack(side='left', padx=(10, 0))
        
        control_frame = tk.Frame(main_frame, bg='#1a1a1a')
        control_frame.pack(fill='x', pady=(0, 15))
        
        self.start_btn = tk.Button(control_frame,
                                  text="🚀 START HUNT",
                                  command=self.start_hunt,
                                  bg='#00d4ff',
                                  fg='#000000',
                                  font=('Arial', 11, 'bold'),
                                  relief='flat',
                                  padx=20,
                                  pady=8,
                                  cursor='hand2')
        self.start_btn.pack(side='left', padx=(0, 10))
        
        self.stop_btn = tk.Button(control_frame,
                                 text="⏹️ STOP HUNT",
                                 command=self.stop_hunt,
                                 bg='#ff4757',
                                 fg='#ffffff',
                                 font=('Arial', 11, 'bold'),
                                 relief='flat',
                                 padx=20,
                                 pady=8,
                                 cursor='hand2',
                                 state='disabled')
        self.stop_btn.pack(side='left', padx=(0, 10))
        
        clear_btn = tk.Button(control_frame,
                             text="🗑️ CLEAR LOG",
                             command=self.clear_log,
                             bg='#ffa502',
                             fg='#000000',
                             font=('Arial', 11, 'bold'),
                             relief='flat',
                             padx=20,
                             pady=8,
                             cursor='hand2')
        clear_btn.pack(side='left')
        
        status_frame = tk.Frame(main_frame, bg='#1a1a1a')
        status_frame.pack(fill='x', pady=(0, 10))
        
        status_left = tk.Frame(status_frame, bg='#1a1a1a')
        status_left.pack(side='left')
        
        status_indicator = tk.Label(status_left,
                                   text="●",
                                   bg='#1a1a1a',
                                   fg='#00ff00',
                                   font=('Arial', 12))
        status_indicator.pack(side='left')
        
        status_text = tk.Label(status_left,
                              text="Status:",
                              bg='#1a1a1a',
                              fg='#ffffff',
                              font=('Arial', 9))
        status_text.pack(side='left', padx=(5, 5))
        
        self.status_display = tk.Label(status_left,
                                      textvariable=self.status_var,
                                      bg='#1a1a1a',
                                      fg='#00d4ff',
                                      font=('Arial', 9, 'bold'))
        self.status_display.pack(side='left')
        
        stats_frame = tk.Frame(status_frame, bg='#1a1a1a')
        stats_frame.pack(side='right')
        
        self.attempts_label = tk.Label(stats_frame,
                                      text="Attempts: 0",
                                      bg='#1a1a1a',
                                      fg='#ffa502',
                                      font=('Arial', 9))
        self.attempts_label.pack(side='right', padx=(0, 20))
        
        self.success_label = tk.Label(stats_frame,
                                     text="Success: 0",
                                     bg='#1a1a1a',
                                     fg='#00ff00',
                                     font=('Arial', 9))
        self.success_label.pack(side='right', padx=(0, 20))
        
        log_frame = tk.LabelFrame(main_frame,
                                 text=" Hunt Activity Log ",
                                 bg='#2d2d2d',
                                 fg='#ffffff',
                                 font=('Arial', 10, 'bold'),
                                 relief='solid',
                                 bd=1)
        log_frame.pack(fill='both', expand=True)
        
        self.log_text = scrolledtext.ScrolledText(log_frame,
                                                 height=12,
                                                 bg='#0d1117',
                                                 fg='#00ff41',
                                                 font=('Consolas', 9),
                                                 insertbackground='#00ff41',
                                                 selectbackground='#264f78',
                                                 relief='flat',
                                                 bd=0)
        self.log_text.pack(fill='both', expand=True, padx=5, pady=5)
        
        self.log("[EXO-CLAIMER] System initialized successfully ✅")
        self.log("[INFO] Discord Username Hunter v2.1 - Ready for operation")
        self.log("[GUIDE] Select hunt mode and enter your credentials to begin")
        
    def create_input_fields(self, parent):
        fields = [
            ("Username:", self.username_var, False),
            ("Password:", self.password_var, True),
            ("Bot Token:", self.token_var, True)
        ]
        
        for i, (label_text, var, is_password) in enumerate(fields):
            field_frame = tk.Frame(parent, bg='#2d2d2d')
            field_frame.pack(fill='x', pady=5)
            
            label = tk.Label(field_frame,
                           text=label_text,
                           bg='#2d2d2d',
                           fg='#ffffff',
                           font=('Arial', 9),
                           width=15,
                           anchor='w')
            label.pack(side='left')
            
            entry = tk.Entry(field_frame,
                           textvariable=var,
                           bg='#1a1a1a',
                           fg='#ffffff',
                           font=('Arial', 9),
                           relief='solid',
                           bd=1,
                           insertbackground='#ffffff',
                           show='*' if is_password else '',
                           width=40)
            entry.pack(side='left', padx=(10, 0))
            
            if label_text == "Username:":
                self.username_entry = entry
            elif label_text == "Password:":
                self.password_entry = entry
            elif label_text == "Bot Token:":
                self.token_entry = entry
        
        self.target_frame = tk.Frame(parent, bg='#2d2d2d')
        
        target_label = tk.Label(self.target_frame,
                              text="Target Username:",
                              bg='#2d2d2d',
                              fg='#ffffff',
                              font=('Arial', 9),
                              width=15,
                              anchor='w')
        target_label.pack(side='left')
        
        self.target_entry = tk.Entry(self.target_frame,
                                   textvariable=self.target_user_var,
                                   bg='#1a1a1a',
                                   fg='#ffffff',
                                   font=('Arial', 9),
                                   relief='solid',
                                   bd=1,
                                   insertbackground='#ffffff',
                                   width=40)
        self.target_entry.pack(side='left', padx=(10, 0))
        
    def on_mode_change(self):
        if self.mode_var.get() == "2":
            self.target_frame.pack(fill='x', pady=5)
            self.log("[MODE] Switched to Full Checker + Claimer mode")
        else:
            self.target_frame.pack_forget()
            self.log("[MODE] Switched to User Claim Test mode")
            
    def log(self, message):
        timestamp = datetime.now().strftime("%H:%M:%S")
        log_message = f"[{timestamp}] {message}\n"
        
        self.log_text.insert(tk.END, log_message)
        self.log_text.see(tk.END)
        self.root.update_idletasks()
        
    def clear_log(self):
        self.log_text.delete(1.0, tk.END)
        self.log("[EXO-CLAIMER] Log cleared - System ready for new session")
        
    def validate_inputs(self):
        if not self.username_var.get().strip():
            messagebox.showerror("Input Error", "Username is required")
            return False
        if not self.password_var.get().strip():
            messagebox.showerror("Input Error", "Password is required")
            return False
        if not self.token_var.get().strip():
            messagebox.showerror("Input Error", "Bot token is required")
            return False
        if self.mode_var.get() == "2" and not self.target_user_var.get().strip():
            messagebox.showerror("Input Error", "Target username is required for mode 2")
            return False
        return True
        
    def update_stats(self):
        self.attempts_label.config(text=f"Attempts: {self.attempts}")
        self.success_label.config(text=f"Success: {self.success_count}")
        
    def start_hunt(self):
        if not self.validate_inputs():
            return
            
        self.running = True
        self.attempts = 0
        self.success_count = 0
        self.update_stats()
        
        self.start_btn.config(state='disabled')
        self.stop_btn.config(state='normal')
        
        self.status_var.set("Hunt Active")
        
        mode = self.mode_var.get()
        if mode == "1":
            self.log("[HUNT] Starting User Claim Test mode...")
            self.thread = threading.Thread(target=self.user_claim_test)
        else:
            self.log("[HUNT] Starting Full Checker + Claimer mode...")
            self.thread = threading.Thread(target=self.full_checker_claimer)
            
        self.thread.daemon = True
        self.thread.start()
        
    def stop_hunt(self):
        self.running = False
        self.status_var.set("Stopping Hunt...")
        self.log("[HUNT] Hunt stopped by user")
        
        self.start_btn.config(state='normal')
        self.stop_btn.config(state='disabled')
        self.status_var.set("Hunt Stopped")
        
    def user_claim_test(self):
        username = self.username_var.get().strip()
        password = self.password_var.get().strip()
        token = self.token_var.get().strip()
        delay = int(self.delay_var.get()) / 1000
        
        self.log(f"[TEST] Testing claim ability for user: {username}")
        self.log(f"[CONFIG] Request delay set to {self.delay_var.get()}ms")
        
        while self.running:
            try:
                self.attempts += 1
                self.update_stats()
                
                self.log(f"[ATTEMPT {self.attempts}] Testing username availability...")
                
                headers = {
                    'Authorization': f'Bot {token}',
                    'Content-Type': 'application/json',
                    'User-Agent': 'EXO-Claimer/2.1'
                }
                
                response = requests.get('https://discord.com/api/v9/users/@me', 
                                      headers=headers, 
                                      timeout=10)
                
                if response.status_code == 200:
                    self.log(f"[SUCCESS] Token validated successfully")
                    self.success_count += 1
                    self.update_stats()
                else:
                    self.log(f"[ERROR] Token validation failed - Status: {response.status_code}")
                
                time.sleep(delay)
                
            except requests.exceptions.RequestException as e:
                self.log(f"[ERROR] Request failed: {str(e)}")
            except Exception as e:
                self.log(f"[ERROR] Unexpected error: {str(e)}")
                
            time.sleep(delay)
            
    def full_checker_claimer(self):
        username = self.username_var.get().strip()
        password = self.password_var.get().strip()
        token = self.token_var.get().strip()
        target = self.target_user_var.get().strip()
        delay = int(self.delay_var.get()) / 1000
        
        self.log(f"[CLAIMER] Target username: {target}")
        self.log(f"[CLAIMER] Authentication user: {username}")
        self.log(f"[CONFIG] Request delay set to {self.delay_var.get()}ms")
        self.log(f"[CLAIMER] Starting continuous check for username availability...")
        
        while self.running:
            try:
                self.attempts += 1
                self.update_stats()
                
                self.log(f"[CHECK {self.attempts}] Checking availability of '{target}'...")
                
                headers = {
                    'Authorization': f'Bot {token}',
                    'Content-Type': 'application/json',
                    'User-Agent': 'EXO-Claimer/2.1'
                }
                
                search_url = f'https://discord.com/api/v9/users/{target}'
                response = requests.get(search_url, headers=headers, timeout=10)
                
                if response.status_code == 404:
                    self.log(f"[AVAILABLE] Username '{target}' is available! Attempting to claim...")
                    
                    claim_data = {
                        'username': target,
                        'password': password
                    }
                    
                    claim_response = requests.patch('https://discord.com/api/v9/users/@me',
                                                  headers=headers,
                                                  json=claim_data,
                                                  timeout=10)
                    
                    if claim_response.status_code == 200:
                        self.log(f"[SUCCESS] Username '{target}' claimed successfully! 🎉")
                        self.success_count += 1
                        self.update_stats()
                        self.running = False
                        self.status_var.set("Hunt Completed - Success!")
                        break
                    else:
                        self.log(f"[FAILED] Claim attempt failed - Status: {claim_response.status_code}")
                        
                elif response.status_code == 200:
                    self.log(f"[TAKEN] Username '{target}' is currently taken")
                else:
                    self.log(f"[ERROR] Check failed - Status: {response.status_code}")
                
                time.sleep(delay)
                
            except requests.exceptions.RequestException as e:
                self.log(f"[ERROR] Request failed: {str(e)}")
            except Exception as e:
                self.log(f"[ERROR] Unexpected error: {str(e)}")
                
            time.sleep(delay)
            
        if self.running:
            self.stop_hunt()
            
    def run(self):
        try:
            self.root.mainloop()
        except KeyboardInterrupt:
            self.stop_hunt()
            self.root.quit()

def main():
    print("EXO Claimer - Discord Username Hunter")
    print("=====================================")
    print("Please choose one of the following options:")
    print("1 -- User Claim Test")
    print("2 -- Full Checker + Claimer")
    
    choice = input("Enter your choice (1 or 2): ").strip()
    username = input("Enter your username: ").strip() 
    password = input("Enter your password: ").strip()
    token = input("Enter your token: ").strip()
    
    print("Token failed to load, please check your token and try again.")
    print("Application terminated")
    
   

if __name__ == "__main__":
    main()