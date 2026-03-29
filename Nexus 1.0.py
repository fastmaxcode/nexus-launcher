import tkinter as tk
import customtkinter as ctk
import requests
import threading
import os
import subprocess
import zipfile
import webbrowser
from datetime import datetime

# --- visual configuration ---
ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue") 

BG_COLOR = "#0A0A0B"        
SIDEBAR_COLOR = "#0D0E12"   
ACCENT_COLOR = "#3498DB"    
GLOW_COLOR = "#5DADE2"      

class NexusLauncher(ctk.CTk):
    def __init__(self):
        super().__init__()

        # --- window setup ---
        self.title("N E X U S | launcher")
        self.geometry("1100x750")
        self.configure(fg_color=BG_COLOR)
        
        self.attributes("-alpha", 0.0)
        
        # pathing
        self.mc_path = os.path.expandvars(r"%localappdata%\Packages\Microsoft.MinecraftUWP_8wekyb3d8bbwe\LocalState\games\com.mojang\minecraftWorlds")
        
        # version data
        self.all_versions = [
            {"v": "1.26.11", "full": "1.26.1101.0", "url": "https://github.com/OnixClient/onix_compatible_appx/releases/download/1.26.11/1.26.11.msixvc"},
            {"v": "1.26.10", "full": "1.26.1004.0", "url": "https://github.com/OnixClient/onix_compatible_appx/releases/download/1.26.10/1.26.10.msixvc"},
            {"v": "1.26.3", "full": "1.26.301.0", "url": "https://github.com/OnixClient/onix_compatible_appx/releases/download/1.26.3/1.26.3.msixvc"},
            {"v": "1.26.2", "full": "1.26.201.0", "url": "https://github.com/OnixClient/onix_compatible_appx/releases/download/1.26.2/1.26.2.msixvc"},
            {"v": "1.26.1", "full": "1.26.101.0", "url": "https://github.com/OnixClient/onix_compatible_appx/releases/download/1.26.1/1.26.1.msixvc"},
            {"v": "1.26.0", "full": "1.26.2.0", "url": "https://github.com/OnixClient/onix_compatible_appx/releases/download/1.26.0/1.26.0.msixvc"},
            {"v": "1.21.132", "full": "1.21.13201.0", "url": "https://github.com/OnixClient/onix_compatible_appx/releases/download/1.21.132/1.21.132.msixvc"},
            {"v": "1.21.131", "full": "1.21.13101.0", "url": "https://github.com/OnixClient/onix_compatible_appx/releases/download/1.21.131/1.21.131.msixvc"},
            {"v": "1.21.130", "full": "1.21.13004.0", "url": "https://github.com/OnixClient/onix_compatible_appx/releases/download/1.21.130/1.21.130.msixvc"},
            {"v": "1.21.124", "full": "1.21.12402.0", "url": "https://github.com/OnixClient/onix_compatible_appx/releases/download/1.21.124/1.21.124.msixvc"},
            {"v": "1.21.123", "full": "1.21.12302.0", "url": "https://github.com/OnixClient/onix_compatible_appx/releases/download/1.21.123/1.21.123.msixvc"},
            {"v": "1.21.122", "full": "1.21.12201.0", "url": "https://github.com/OnixClient/onix_compatible_appx/releases/download/1.21.122/1.21.122.msixvc"},
            {"v": "1.21.121", "full": "1.21.12101.0", "url": "https://github.com/OnixClient/onix_compatible_appx/releases/download/1.21.121/1.21.121.msixvc"},
            {"v": "1.21.120", "full": "1.21.12004.0", "url": "https://github.com/OnixClient/onix_compatible_appx/releases/download/1.21.120/1.21.120.msixvc"},
            {"v": "1.21.114", "full": "1.21.11401.0", "url": "https://github.com/OnixClient/onix_compatible_appx/releases/download/1.21.114/1.21.114.Appx"},
            {"v": "1.21.113", "full": "1.21.11301.0", "url": "https://github.com/OnixClient/onix_compatible_appx/releases/download/1.21.113/1.21.113.Appx"},
            {"v": "1.21.111", "full": "1.21.11101.0", "url": "https://github.com/OnixClient/onix_compatible_appx/releases/download/1.21.111/1.21.111.Appx"},
            {"v": "1.21.101", "full": "1.21.10101.0", "url": "https://github.com/OnixClient/onix_compatible_appx/releases/download/1.21.101/1.21.101.Appx"},
            {"v": "1.21.100", "full": "1.21.10006.0", "url": "https://github.com/OnixClient/onix_compatible_appx/releases/download/1.21.100/1.21.100.Appx"},
            {"v": "1.21.94", "full": "1.21.9401.0", "url": "https://github.com/OnixClient/onix_compatible_appx/releases/download/1.21.94/1.21.94.Appx"},
            {"v": "1.21.93", "full": "1.21.9301.0", "url": "https://github.com/OnixClient/onix_compatible_appx/releases/download/1.21.93/1.21.93.Appx"},
            {"v": "1.21.92", "full": "1.21.9201.0", "url": "https://github.com/OnixClient/onix_compatible_appx/releases/download/1.21.92/1.21.92.Appx"},
            {"v": "1.21.90", "full": "1.21.9003.0", "url": "https://github.com/OnixClient/onix_compatible_appx/releases/download/1.21.90/1.21.90.Appx"},
            {"v": "1.21.82", "full": "1.21.8201.0", "url": "https://github.com/OnixClient/onix_compatible_appx/releases/download/1.21.82/1.21.82.Appx"},
            {"v": "1.21.81", "full": "1.21.8102.0", "url": "https://github.com/OnixClient/onix_compatible_appx/releases/download/1.21.81/1.21.81.Appx"},
            {"v": "1.21.80", "full": "1.21.8003.0", "url": "https://github.com/OnixClient/onix_compatible_appx/releases/download/1.21.80/1.21.80.Appx"},
            {"v": "1.21.73", "full": "1.21.7301.0", "url": "https://github.com/OnixClient/onix_compatible_appx/releases/download/1.21.73/1.21.73.Appx"},
            {"v": "1.21.72", "full": "1.21.7201.0", "url": "https://github.com/OnixClient/onix_compatible_appx/releases/download/1.21.72/1.21.72.Appx"},
            {"v": "1.21.71", "full": "1.21.7101.0", "url": "https://github.com/OnixClient/onix_compatible_appx/releases/download/1.21.71/1.21.71.Appx"},
            {"v": "1.21.70", "full": "1.21.7003.0", "url": "https://github.com/OnixClient/onix_compatible_appx/releases/download/1.21.70/1.21.70.Appx"},
            {"v": "1.21.62", "full": "1.21.6201.0", "url": "https://github.com/OnixClient/onix_compatible_appx/releases/download/1.21.62/1.21.62.Appx"},
            {"v": "1.21.61", "full": "1.21.6101.0", "url": "https://github.com/OnixClient/onix_compatible_appx/releases/download/1.21.61/1.21.61.Appx"},
            {"v": "1.21.60", "full": "1.21.6010.0", "url": "https://github.com/OnixClient/onix_compatible_appx/releases/download/1.21.60/1.21.60.Appx"},
            {"v": "1.21.51", "full": "1.21.5101.0", "url": "https://github.com/OnixClient/onix_compatible_appx/releases/download/1.21.51/1.21.51.Appx"},
            {"v": "1.21.50", "full": "1.21.5007.0", "url": "https://github.com/OnixClient/onix_compatible_appx/releases/download/1.21.50/1.21.50.Appx"},
            {"v": "1.21.44", "full": "1.21.4401.0", "url": "https://github.com/OnixClient/onix_compatible_appx/releases/download/1.21.44/1.21.44.Appx"},
            {"v": "1.21.43", "full": "1.21.4301.0", "url": "https://github.com/OnixClient/onix_compatible_appx/releases/download/1.21.43/1.21.43.Appx"},
            {"v": "1.21.41", "full": "1.21.4101.0", "url": "https://github.com/OnixClient/onix_compatible_appx/releases/download/1.21.41/1.21.41.Appx"},
            {"v": "1.21.40", "full": "1.21.4003.0", "url": "https://github.com/OnixClient/onix_compatible_appx/releases/download/1.21.40/1.21.40.Appx"},
            {"v": "1.21.31", "full": "1.21.3104.0", "url": "https://github.com/OnixClient/onix_compatible_appx/releases/download/1.21.31/1.21.31.Appx"},
            {"v": "1.21.30", "full": "1.21.3003.0", "url": "https://github.com/OnixClient/onix_compatible_appx/releases/download/1.21.30/1.21.30.Appx"},
            {"v": "1.21.23", "full": "1.21.2301.0", "url": "https://github.com/OnixClient/onix_compatible_appx/releases/download/1.21.23/1.21.23.Appx"},
            {"v": "1.21.22", "full": "1.21.2201.0", "url": "https://github.com/OnixClient/onix_compatible_appx/releases/download/1.21.22/1.21.22.Appx"},
            {"v": "1.21.21", "full": "1.21.2101.0", "url": "https://github.com/OnixClient/onix_compatible_appx/releases/download/1.21.21/1.21.21.Appx4"},
            {"v": "1.21.20", "full": "1.21.2003.0", "url": "https://github.com/OnixClient/onix_compatible_appx/releases/download/1.21.20/1.21.20.Appx"},
            {"v": "1.21.2", "full": "1.21.202.0", "url": "https://github.com/OnixClient/onix_compatible_appx/releases/download/1.21.2/1.21.2.Appx"},
            {"v": "1.21.1", "full": "1.21.103.0", "url": "https://github.com/OnixClient/onix_compatible_appx/releases/download/1.21.1/1.21.1.Appx"},
            {"v": "1.21.0", "full": "1.21.3.0", "url": "https://github.com/OnixClient/onix_compatible_appx/releases/download/1.21.0/1.21.0.Appx"},
            {"v": "1.20.81", "full": "1.20.8101.0", "url": "https://github.com/OnixClient/onix_compatible_appx/releases/download/1.20.81/1.20.81.Appx"},
            {"v": "1.20.80", "full": "1.20.8005.0", "url": "https://github.com/OnixClient/onix_compatible_appx/releases/download/1.20.80/1.20.80.Appx"},
            {"v": "1.20.73", "full": "1.20.7301.0", "url": "https://github.com/OnixClient/onix_compatible_appx/releases/download/1.20.73/1.20.73.Appx"},
            {"v": "1.20.72", "full": "1.20.7201.0", "url": "https://github.com/OnixClient/onix_compatible_appx/releases/download/1.20.72/1.20.72.Appx"},
            {"v": "1.20.71", "full": "1.20.7101.0", "url": "https://github.com/OnixClient/onix_compatible_appx/releases/download/1.20.71/1.20.71.Appx"},
            {"v": "1.20.70", "full": "1.20.7005.0", "url": "https://github.com/OnixClient/onix_compatible_appx/releases/download/1.20.70/1.20.70.Appx"},
            {"v": "1.20.62", "full": "1.20.6201.0", "url": "https://github.com/OnixClient/onix_compatible_appx/releases/download/1.20.62/1.20.62.Appx"},
            {"v": "1.20.60", "full": "1.20.6004.0", "url": "https://github.com/OnixClient/onix_compatible_appx/releases/download/1.20.60/1.20.60.Appx"},
            {"v": "1.20.51", "full": "1.20.5101.0", "url": "https://github.com/OnixClient/onix_compatible_appx/releases/download/1.20.51/1.20.51.Appx"},
            {"v": "1.20.50", "full": "1.20.5003.0", "url": "https://github.com/OnixClient/onix_compatible_appx/releases/download/1.20.50/1.20.50.Appx"},
            {"v": "1.20.41", "full": "1.20.4102.0", "url": "https://github.com/OnixClient/onix_compatible_appx/releases/download/1.20.41/1.20.41.Appx"},
            {"v": "1.20.40", "full": "1.20.4001.0", "url": "https://github.com/OnixClient/onix_compatible_appx/releases/download/1.20.40/1.20.40.Appx"},
            {"v": "1.20.32", "full": "1.20.3203.0", "url": "https://github.com/OnixClient/onix_compatible_appx/releases/download/1.20.32/1.20.32.Appx"},
            {"v": "1.20.31", "full": "1.20.3101.0", "url": "https://github.com/OnixClient/onix_compatible_appx/releases/download/1.20.31/1.20.31.Appx"},
            {"v": "1.20.30", "full": "1.20.3002.0", "url": "https://github.com/OnixClient/onix_compatible_appx/releases/download/1.20.30/1.20.30.Appx"},
            {"v": "1.20.15", "full": "1.20.1501.0", "url": "https://github.com/OnixClient/onix_compatible_appx/releases/download/1.20.15/1.20.15.Appx"},
            {"v": "1.20.12", "full": "1.20.1201.0", "url": "https://github.com/OnixClient/onix_compatible_appx/releases/download/1.20.12/1.20.12.Appx"},
            {"v": "1.20.10", "full": "1.20.1001.0", "url": "https://github.com/OnixClient/onix_compatible_appx/releases/download/1.20.10/1.20.10.Appx"},
            {"v": "1.20.1", "full": "1.20.102.0", "url": "https://github.com/OnixClient/onix_compatible_appx/releases/download/1.20.1/1.20.1.Appx"},
            {"v": "1.20.0", "full": "1.20.1.0", "url": "https://github.com/OnixClient/onix_compatible_appx/releases/download/1.20.0/1.20.0.Appx"},
            {"v": "1.19.83", "full": "1.19.8301.0", "url": "https://github.com/OnixClient/onix_compatible_appx/releases/download/1.19.83/1.19.83.Appx"},
            {"v": "1.19.81", "full": "1.19.8101.0", "url": "https://github.com/OnixClient/onix_compatible_appx/releases/download/1.19.81/1.19.81.Appx"},
            {"v": "1.19.80", "full": "1.19.8002.0", "url": "https://github.com/OnixClient/onix_compatible_appx/releases/download/1.19.80/1.19.80.Appx"},
            {"v": "1.19.73", "full": "1.19.7302.0", "url": "https://github.com/OnixClient/onix_compatible_appx/releases/download/1.19.73/1.19.73.Appx"},
            {"v": "1.19.71", "full": "1.19.7102.0", "url": "https://github.com/OnixClient/onix_compatible_appx/releases/download/1.19.71/1.19.71.Appx"},
            {"v": "1.19.70", "full": "1.19.7002.0", "url": "https://github.com/OnixClient/onix_compatible_appx/releases/download/1.19.70/1.19.70.Appx"},
            {"v": "1.19.63", "full": "1.19.6301.0", "url": "https://github.com/OnixClient/onix_compatible_appx/releases/download/1.19.63/1.19.63.Appx"},
            {"v": "1.19.62", "full": "1.19.6201.0", "url": "https://github.com/OnixClient/onix_compatible_appx/releases/download/1.19.62/1.19.62.Appx"},
            {"v": "1.19.60", "full": "1.19.6003.0", "url": "https://github.com/OnixClient/onix_compatible_appx/releases/download/1.19.60/1.19.60.Appx"},
            {"v": "1.19.51", "full": "1.19.5101.0", "url": "https://github.com/OnixClient/onix_compatible_appx/releases/download/1.19.51/1.19.51.Appx"},
            {"v": "1.19.50", "full": "1.19.5002.0", "url": "https://github.com/OnixClient/onix_compatible_appx/releases/download/1.19.50/1.19.50.Appx"},
            {"v": "1.19.41", "full": "1.19.4101.0", "url": "https://github.com/OnixClient/onix_compatible_appx/releases/download/1.19.41/1.19.41.Appx"},
            {"v": "1.19.40", "full": "1.19.4002.0", "url": "https://github.com/OnixClient/onix_compatible_appx/releases/download/1.19.40/1.19.40.Appx"},
            {"v": "1.19.31", "full": "1.19.3101.0", "url": "https://github.com/OnixClient/onix_compatible_appx/releases/download/1.19.31/1.19.31.Appx"},
            {"v": "1.19.30", "full": "1.19.3004.0", "url": "https://github.com/OnixClient/onix_compatible_appx/releases/download/1.19.30/1.19.30.Appx"},
            {"v": "1.19.22", "full": "1.19.2201.0", "url": "https://github.com/OnixClient/onix_compatible_appx/releases/download/1.19.22/1.19.22.Appx"},
            {"v": "1.19.21", "full": "1.19.2101.0", "url": "https://github.com/OnixClient/onix_compatible_appx/releases/download/1.19.21/1.19.21.Appx"},
            {"v": "1.19.20", "full": "1.19.2002.0", "url": "https://github.com/OnixClient/onix_compatible_appx/releases/download/1.19.20/1.19.20.Appx"},
            {"v": "1.19.11", "full": "1.19.1101.0", "url": "https://github.com/OnixClient/onix_compatible_appx/releases/download/1.19.11/1.19.11.Appx"},
            {"v": "1.19.10", "full": "1.19.1003.0", "url": "https://github.com/OnixClient/onix_compatible_appx/releases/download/1.19.10/1.19.10.Appx"},
            {"v": "1.19.2", "full": "1.19.202.0", "url": "https://github.com/OnixClient/onix_compatible_appx/releases/download/1.19.2/1.19.2.Appx"},
            {"v": "1.19.0", "full": "1.19.5.0", "url": "https://github.com/OnixClient/onix_compatible_appx/releases/download/1.19.0/1.19.0.Appx"},
            {"v": "1.18.31", "full": "1.18.3104.0", "url": "https://github.com/OnixClient/onix_compatible_appx/releases/download/1.18.31/1.18.31.Appx"},
            {"v": "1.18.30", "full": "1.18.3004.0", "url": "https://github.com/OnixClient/onix_compatible_appx/releases/download/1.18.30/1.18.30.Appx"},
            {"v": "1.18.12", "full": "1.18.1201.0", "url": "https://github.com/OnixClient/onix_compatible_appx/releases/download/1.18.12/1.18.12.Appx"},
            {"v": "1.18.10", "full": "1.18.1004.0", "url": "https://github.com/OnixClient/onix_compatible_appx/releases/download/1.18.10/1.18.10.Appx"},
            {"v": "1.18.2", "full": "1.18.203.0", "url": "https://github.com/OnixClient/onix_compatible_appx/releases/download/1.18.2/1.18.2.Appx"},
            {"v": "1.18.1", "full": "1.18.102.0", "url": "https://github.com/OnixClient/onix_compatible_appx/releases/download/1.18.1/1.18.1.Appx"},
            {"v": "1.18.0", "full": "1.18.2.0", "url": "https://github.com/OnixClient/onix_compatible_appx/releases/download/1.18.0/1.18.0.Appx"},
            {"v": "1.17.41", "full": "1.17.4101.0", "url": "https://github.com/OnixClient/onix_compatible_appx/releases/download/1.17.41/1.17.41.Appx"},
            {"v": "1.17.40", "full": "1.17.4006.0", "url": "https://github.com/OnixClient/onix_compatible_appx/releases/download/1.17.40/1.17.40.Appx"},
            {"v": "1.17.34", "full": "1.17.3402.0", "url": "https://github.com/OnixClient/onix_compatible_appx/releases/download/1.17.34/1.17.34.Appx"},
            {"v": "1.17.32", "full": "1.17.3202.0", "url": "https://github.com/OnixClient/onix_compatible_appx/releases/download/1.17.32/1.17.32.Appx"},
            {"v": "1.17.30", "full": "1.17.3004.0", "url": "https://github.com/OnixClient/onix_compatible_appx/releases/download/1.17.30/1.17.30.Appx"},
            {"v": "1.17.11", "full": "1.17.1101.0", "url": "https://github.com/OnixClient/onix_compatible_appx/releases/download/1.17.11/1.17.11.Appx"},
            {"v": "1.17.10", "full": "1.17.1004.0", "url": "https://github.com/OnixClient/onix_compatible_appx/releases/download/1.17.10/1.17.10.Appx"},
            {"v": "1.17.2", "full": "1.17.201.0", "url": "https://github.com/OnixClient/onix_compatible_appx/releases/download/1.17.2/1.17.2.Appx"},
            {"v": "1.17.0", "full": "1.17.2.0", "url": "https://github.com/OnixClient/onix_compatible_appx/releases/download/1.17.0/1.17.0.Appx"},
            {"v": "1.16.221", "full": "1.16.22101.0", "url": "https://github.com/OnixClient/onix_compatible_appx/releases/download/1.16.221/1.16.221.Appx"},
            {"v": "1.16.220", "full": "1.16.22002.0", "url": "https://github.com/OnixClient/onix_compatible_appx/releases/download/1.16.220/1.16.220.Appx"},
            {"v": "1.16.210", "full": "1.16.21005.0", "url": "https://github.com/OnixClient/onix_compatible_appx/releases/download/1.16.210/1.16.210.Appx"},
            {"v": "1.16.201", "full": "1.16.20102.0", "url": "https://github.com/OnixClient/onix_compatible_appx/releases/download/1.16.201/1.16.201.Appx"},
            {"v": "1.16.200", "full": "1.16.20002.0", "url": "https://github.com/OnixClient/onix_compatible_appx/releases/download/1.16.200/1.16.200.Appx"},
            {"v": "1.16.100", "full": "1.16.10004.0", "url": "https://github.com/OnixClient/onix_compatible_appx/releases/download/1.16.100/1.16.100.Appx"},
            {"v": "1.16.40", "full": "1.16.4002.0", "url": "https://github.com/OnixClient/onix_compatible_appx/releases/download/1.16.40/1.16.40.Appx"},
            {"v": "1.12.1", "full": "1.12.101.0", "url": "https://github.com/OnixClient/onix_compatible_appx/releases/download/1.12.1/1.12.1.Appx"},
            {"v": "1.12.0", "full": "1.12.28.0", "url": "https://github.com/OnixClient/onix_compatible_appx/releases/download/1.12.0/1.12.0.Appx"} 
        ]

        # --- layout ---
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # --- sidebar (left) ---
        self.sidebar = ctk.CTkFrame(self, width=240, corner_radius=0, fg_color=SIDEBAR_COLOR, border_width=1, border_color="#1F1F1F")
        self.sidebar.grid(row=0, column=0, sticky="nsew", rowspan=2)
        self.sidebar.grid_rowconfigure(5, weight=1)

        self.brand_label = ctk.CTkLabel(
            self.sidebar, 
            text="N E X U S", 
            font=ctk.CTkFont(size=28, weight="bold") 
        )
        self.brand_label.pack(pady=(40, 20))

        # nav buttons
        self.nav_switcher = self.create_nav_button("version switcher", self.show_switcher)
        self.nav_archive = self.create_nav_button("client downloads", self.show_archive)
        self.nav_backup = self.create_nav_button("backup worlds", self.run_backup, color="#2C3E50")
        
        self.search_entry = ctk.CTkEntry(
            self.sidebar, 
            placeholder_text="search version...", 
            fg_color="#16161D", 
            border_color="#2A2A35",
            height=35
        )
        self.search_entry.pack(padx=20, pady=20, fill="x")
        self.search_entry.bind("<KeyRelease>", self.filter_versions)

        self.status_indicator = ctk.CTkLabel(self.sidebar, text="ready", text_color="#2ECC71", font=ctk.CTkFont(size=11, weight="bold"))
        self.status_indicator.pack(side="bottom", pady=20)

        # --- content screens ---
        self.switcher_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.scroll_container = ctk.CTkScrollableFrame(
            self.switcher_frame, 
            label_text="version list", 
            label_fg_color=SIDEBAR_COLOR,
            fg_color="transparent"
        )
        self.scroll_container.pack(fill="both", expand=True, padx=20, pady=20)

        self.archive_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.setup_archive_ui()

        # --- bottom control bar ---
        self.bottom_bar = ctk.CTkFrame(self, height=80, fg_color=SIDEBAR_COLOR, corner_radius=0)
        self.bottom_bar.grid(row=1, column=1, sticky="ew")
        
        self.progress = ctk.CTkProgressBar(self.bottom_bar, progress_color=ACCENT_COLOR, height=8)
        self.progress.pack(fill="x", padx=40, pady=(20, 0))
        self.progress.set(0)

        self.version_info = ctk.CTkLabel(self.bottom_bar, text="N E X U S v1.2 | waiting for selection...", font=ctk.CTkFont(size=12))
        self.version_info.pack(pady=10)

        self.buttons = []
        self.populate_list(self.all_versions)
        self.show_switcher()
        self.fade_in()

    def create_nav_button(self, text, command, color=None):
        btn = ctk.CTkButton(
            self.sidebar, 
            text=text, 
            command=command, 
            height=40,
            fg_color=color if color else "transparent",
            hover_color=GLOW_COLOR,
            anchor="w",
            font=ctk.CTkFont(size=13)
        )
        btn.pack(padx=20, pady=5, fill="x")
        return btn

    def setup_archive_ui(self):
        title = ctk.CTkLabel(self.archive_frame, text="other clients", font=ctk.CTkFont(size=24, weight="bold"))
        title.pack(pady=30)
        
        clients = [
            ("horion", "https://horion.download/"),
            ("borion", "https://github.com/Borion-Updated/Releases/"),
            ("nature", "https://natureclient.com/Launcher.exe")
        ]
        
        for name, url in clients:
            b = ctk.CTkButton(
                self.archive_frame, text=name, height=60, width=400,
                corner_radius=12, border_width=1, border_color=ACCENT_COLOR,
                fg_color="#16161D", hover_color="#1F1F2E",
                command=lambda u=url: webbrowser.open(u)
            )
            b.pack(pady=10)

    def fade_in(self):
        alpha = self.attributes("-alpha")
        if alpha < 1.0:
            alpha += 0.05
            self.attributes("-alpha", alpha)
            self.after(20, self.fade_in)

    def populate_list(self, version_list):
        for btn in self.buttons: btn.destroy()
        self.buttons = []
        for data in version_list:
            btn = ctk.CTkButton(
                self.scroll_container, 
                text=f"minecraft version: v{data['v']}", 
                anchor="w", height=50, corner_radius=10,
                fg_color="#16161D", border_width=1, border_color="#2A2A35",
                hover_color=ACCENT_COLOR,
                command=lambda d=data: self.start_task(d)
            )
            btn.pack(fill="x", pady=6, padx=15)
            self.buttons.append(btn)

    def show_switcher(self):
        self.archive_frame.grid_forget()
        self.switcher_frame.grid(row=0, column=1, sticky="nsew")

    def show_archive(self):
        self.switcher_frame.grid_forget()
        self.archive_frame.grid(row=0, column=1, sticky="nsew")

    def filter_versions(self, event):
        query = self.search_entry.get().lower()
        filtered = [v for v in self.all_versions if query in v['v']]
        self.populate_list(filtered)

    def update_status(self, text, color="#3498DB"):
        self.version_info.configure(text=text, text_color=color)

    def run_backup(self):
        threading.Thread(target=self.backup_logic, daemon=True).start()

    def backup_logic(self):
        self.update_status("preparing backup...")
        if not os.path.exists(self.mc_path):
            self.update_status("error: minecraft folder not found", "red")
            return
        
        backup_folder = "nexus_backups"
        if not os.path.exists(backup_folder): os.makedirs(backup_folder)
        
        timestamp = datetime.now().strftime("%Y-%m-%d_%H%M")
        zip_name = f"{backup_folder}/backup_{timestamp}.zip"
        
        try:
            with zipfile.ZipFile(zip_name, 'w', zipfile.ZIP_DEFLATED) as zipf:
                for root, _, files in os.walk(self.mc_path):
                    for file in files:
                        zipf.write(os.path.join(root, file), os.path.relpath(os.path.join(root, file), self.mc_path))
            self.update_status("backup complete", "#2ECC71")
            os.startfile(backup_folder)
        except:
            self.update_status("backup failed", "red")

    def start_task(self, data):
        threading.Thread(target=self.download_and_run, args=(data,), daemon=True).start()

    def download_and_run(self, data):
        url = data['url']
        ext = ".msixvc" if ".msixvc" in url.lower() else ".appx"
        filename = f"nexus_setup_{data['v']}{ext}"
        
        if not os.path.exists(filename):
            self.update_status(f"downloading version {data['v']}...")
            r = requests.get(url, stream=True)
            total = int(r.headers.get('content-length', 0))
            dl = 0
            with open(filename, 'wb') as f:
                for chunk in r.iter_content(chunk_size=1024*1024):
                    if chunk:
                        f.write(chunk)
                        dl += len(chunk)
                        self.progress.set(dl/total)
        
        self.update_status("setup ready", "#2ECC71")
        os.startfile(os.path.abspath(filename))
        self.progress.set(0)

if __name__ == "__main__":
    app = NexusLauncher()
    app.mainloop()