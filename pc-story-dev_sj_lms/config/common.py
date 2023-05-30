# coding = utf-8
"""
@Author: sujie
@Create on:
@Modify on:
@File:
"""
import platform


# WinAppDriver driver 存放位置
# DRIVER_URL = "D:\\Program Files(x86)\\Windows Application Driver\\WinAppDriver"





# setting_list = {'zh': '设置', 'en': 'Settings', 'zh-tw': '設置', 'es': 'Ajustes', 'ja': 'セット',
#                 'ko': '설정', 'vi': 'Cài đặt', 'ar': 'الإعدادات', 'id': 'Pengaturan'
#                 # , 'zh': '设置', 'zh': '设置', 'zh': '设置'
#                 }

lang_setting = {
    'zh': ['登  录', '设置', '简体中文'],  'en': ['Log In', 'Settings', 'English'], 'zh-tw': ['登  錄', '設置', '繁體中文'],
    'es': ['Iniciar sesión', 'Ajustes', 'Español'], 'ja': ['日本', 'セット', '日本語'], 'ko': ['로그인', '설정', '한국어'],
    'vi': ['Đăng nhập', 'Cài đặt', 'Tiếng Việt'], 'ar': ['تسجيل الدخول', 'الإعدادات', 'العربية'], 'id': ['Login', 'Pengaturan', 'Bahasa Indonesia'],
    'fr': ['Se connecter', 'Set', 'Français'], 'ru': ['Вход', 'Настройка', 'Pусский'], 'pt': ['Entrar', 'configurações', 'Português']
}

# 获取当前操作系统版本
current_sys = platform.platform()[0: 10]