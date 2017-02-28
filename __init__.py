"""NEU captcha

NEU captcha Is a simple tool to identify NEU (China) verification
code, whose website is http://aao.neu.edu.cn/ or http://202.118.31.197/.

"""

__author__ = "eleflea"
__version__ = "0.1"

__all__ = ['identify', 'scan_captcha', 'BOX_1', 'BOX_O', 'BOX_2']

from .captcha import identify, scan_captcha, BOX_1, BOX_2, BOX_O
