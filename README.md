# neucaptcha

NEUcaptcha 是一个识别东北大学教务处验证码的简单工具。

网址是 http://aao.neu.edu.cn/ 或 http://202.118.31.197/。

### 使用

```python
import neucaptcha
with open("captcha45.jpg", "rb") as img:
    r = neucaptcha.scan_captcha(img)
print(r)
```

可选参数 *threshold* 是阈值，用于二值化，建议在130~150；*tol* 是确定度，建议不要超过0.95。
