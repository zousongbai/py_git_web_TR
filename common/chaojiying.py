from hashlib import md5
import requests

class Chaojiying(object):
    """验证码：超级鹰第三方平台"""

    def __init__(self, username, password, soft_id):
        self.username = username
        self.password = md5(password.encode('utf-8')).hexdigest()
        self.soft_id = soft_id
        self.base_params = {
            'user': self.username,
            'pass2': self.password,
            'softid': self.soft_id,
        }
        self.headers = {
            'Connection': 'Keep-Alive',
            'User-Agent': 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0)',
        }

    def post_pic(self, im, codetype):
        """
        im: 图片字节
        codetype: 题目类型 参考 http://www.chaojiying.com/price.html
        """
        params = {
            'codetype': codetype,
        }
        params.update(self.base_params)
        files = {'userfile': ('ccc.jpg', im)}
        r = requests.post('http://upload.chaojiying.net/Upload/Processing.php', data=params, files=files,
                          headers=self.headers)
        return r.json()

    def report_error(self, im_id):
        """
        im_id:报错题目的图片ID
        """
        params = {
            'id': im_id,
        }
        params.update(self.base_params)
        r = requests.post('http://upload.chaojiying.net/Upload/ReportError.php', data=params, headers=self.headers)
        return r.json()


if __name__ == '__main__':
    # 创建一个对象，传入账号，密码，和软件id
    yz = Chaojiying(username='zousongbai', password='880320aa', soft_id='903275')
    # 读取验证码图片
    pic = open('a.png', 'rb').read()
    # 通过对象调用post_pic方法，进行图片识别，返回的结果是一个地点类型数据，其中的pic_str就是识别的结果
    result = yz.post_pic(pic, codetype='1004') # codetype：验证码类型
    print('识别的结果:', result.get('pic_str'))
