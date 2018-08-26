# BFSUjwc
## 北京外国语大学教务系统API抽象模块  
本模块仅作为学习用途，采用GPLv3 开源协议，谢绝任何商业用途。  
Under GPLv3 license. No commercial usage is allowed.  

&emsp;&emsp;倘若你来自*魏公村语言技校*，恭喜你发现了什么！  
&emsp;&emsp;本模块提供北京外国语大学教务系统登录、简要个人信息查询( 姓名及UserId( *该信息目前只发现选课时需要* ) )、成绩查询、快速选课功能。  
&emsp;&emsp;经试验表明选课高峰期选课系统瓶颈在于显示选课页面及查询可选课程中，选课本身并不是瓶颈，本模块在选课网页无法打开的高峰期也可以顺利流畅完成选课。

## 特性
- 可使用交互式界面便捷执行；
- 便于作为模块导入其他程序，会话、连接可复用；
- 流程鲁棒，允许登录尝试失败，可多次尝试；
- 对象可序列化，易于缓存；
- 易于修改配置、提供自定义OCR接口；
- 成绩返回方式多样，提供纯列表、字典等方式。

## 使用方式
- 交互式/简单调用
```python
from bfsujwc import Query

q = Query('14020033', 'password')
q.login()
# 弹出验证码请求人工识别并输入
# 登录成功返回 True

q.get_score('2017a')  # 此处查询日期格式为“年份学期”
# s: spring春季学期；a: autumn秋季学期
# 2017a：2017年秋季学期；2014s：2014年春季学期

q.quick_select('课程号') # 快速选课，需要知道课程的课程号，可在教务网站查询到
```
- 作为模块引入
```python
from bfsujwc import Query


# 假设拥有一个验证码识别函数
def ocr(imgBytesIO):
    # some magic ...
    result = '识别结果'
    return result

Query.captcha_rec = ocr

# 或者你可以继承复写
class MyQuery(Query):
    @staticmethod
    def captcha_rec(img):
        return ocr(img)
```
- 缓存、复用对象  
每一Query内部全部使用各自的requests.Session对象请求，保存状态、cookies，不包含任何其他副作用，对象的缓存、持久化极为便捷。你可以直接pickle Query对象也可以尝试只保存其session属性。与Redis配合可方便实现一个高速访问池，免去每次使用都需验证码识别登录的耗费。  
Python Redis需要一个string输入输出，utils.py提供了简单的工具以便实现你的缓存。
```python
import pickle


bytes_ = pickle.dumps(query)  # 序列化

q = pickle.loads(bytes_)  # 逆序列化
```

## 注意事项
- 本模块仅作为学习实现，不得用于商业用途；
- 请正确合理合法使用本模块或进行其它开发，**使用不当带来的一切后果自负**；
- **开发时请考虑公众利益、服务器性能**；
- 本模块选课只实现了依据课程号“快速选课”，课程号的有效预提取方法因时间问题尚未实现，目前只尝试了人工网站查询获取；
- 本模块最后测试于2018年6月运行正常，不保证未来运行效果，可能随着教务系统升级接口出现变化；
- 因毕业后不再更新，Issues可能无法处理；欢迎提Pull Requests。

## Requirements
Python3.5运行测试通过  

第三方包：
- BeautifulSoup4
- Requests
- Pillow

## 附
任何问题请开Issue  
Under GPLv3 License  
2018/8