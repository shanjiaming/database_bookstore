**You:**

我现在在写一个书店数据管理系统的大作业。以下是作业要求。 # bookstore \[!\[Build Status\](https://travis-ci.com/DaSE-DBMS/bookstore.svg?branch=master)\](https://travis-ci.com/DaSE-DBMS/bookstore) \[!\[codecov\](https://codecov.io/gh/DaSE-DBMS/bookstore/branch/master/graph/badge.svg)\](https://codecov.io/gh/DaSE-DBMS/bookstore) ## 功能 实现一个提供网上购书功能的网站后端。<br> 网站支持书商在上面开商店，购买者可以通过网站购买。<br> 买家和卖家都可以注册自己的账号。<br> 一个卖家可以开一个或多个网上商店， 买家可以为自已的账户充值，在任意商店购买图书。<br> 支持 下单->付款->发货->收货 流程。<br> 1.实现对应接口的功能，见项目的doc文件夹下面的.md文件描述 （60%）<br> 其中包括： 1)用户权限接口，如注册、登录、登出、注销<br> 2)买家用户接口，如充值、下单、付款<br> 3)卖家用户接口，如创建店铺、填加书籍信息及描述、增加库存<br> 通过对应的功能测试，所有test case都pass <br> 2.为项目添加其它功能 ：（40%）<br> 1)实现后续的流程 <br> 发货 -> 收货 2)搜索图书 <br> 用户可以通过关键字搜索，参数化的搜索方式； 如搜索范围包括，题目，标签，目录，内容；全站搜索或是当前店铺搜索。 如果显示结果较大，需要分页 (使用全文索引优化查找) 3)订单状态，订单查询和取消定单<br> 用户可以查自已的历史订单，用户也可以取消订单。<br> 取消定单可由买家主动地取消定单，或者买家下单后，经过一段时间超时仍未付款，定单也会自动取消。 <br> ## bookstore目录结构 \`\`\` bookstore |-- be 后端 |-- model 后端逻辑代码 |-- view 访问后端接口 |-- .... |-- doc JSON API规范说明 |-- fe 前端访问与测试代码 |-- access |-- bench 效率测试 |-- data |-- book.db sqlite 数据库(book.db，较少量的测试数据) |-- book\_lx.db sqlite 数据库(book\_lx.db， 较大量的测试数据，要从网盘下载) |-- scraper.py 从豆瓣爬取的图书信息数据的代码 |-- test 功能性测试（包含对前60%功能的测试，不要修改已有的文件，可以提pull request或bug） |-- conf.py 测试参数，修改这个文件以适应自己的需要 |-- conftest.py pytest初始化配置，修改这个文件以适应自己的需要 |-- .... |-- .... \`\`\` ## 安装配置 安装python (需要python3.6以上) 进入bookstore文件夹下： 安装依赖 pip install -r requirements.txt 执行测试 bash script/test.sh （注意：如果提示"RuntimeError: Not running with the Werkzeug Server"，请输入下述命令，将flask和Werkzeug的版本均降低为2.0.0。 pip install flask==2.0.0 pip install Werkzeug==2.0.0） ## 要求 2～3人一组，做好分工，完成下述内容： 1.bookstore文件夹是该项目的demo，采用flask后端框架与sqlite数据库，实现了前60%功能以及对应的测试用例代码。 要求大家创建本地MongoDB数据库，将bookstore/fe/data/book.db中的内容以合适的形式存入本地数据库 书本的内容可自行构造一批，也可参从网盘下载，下载地址为： https://pan.baidu.com/s/1bjCOW8Z5N\_ClcqU54Pdt8g 提取码： hj6q 2.在完成前60%功能的基础上，继续实现后40%功能，要有接口、后端逻辑实现、数据库操作、代码测试。对所有接口都要写test case，通过测试并计算测试覆盖率（尽量提高测试覆盖率）。 3.尽量使用索引，对程序与数据库执行的性能有考量 4.尽量使用git等版本管理工具 5.不需要实现界面，只需通过代码测试体现功能与正确性 ## 报告内容 1.每位组员的学号、姓名，以及分工 2.文档数据库设计：文档schema 3.对60%基础功能和40%附加功能的接口、后端逻辑、数据库操作、测试用例进行介绍，展示测试结果与测试覆盖率。 4.如果完成，可以展示本次大作业的亮点，比如要求中的“3 4”两点。 注：验收依据为报告，本次大作业所作的工作要完整展示在报告中。 ## 验收与考核准测 - 提交 \*\*代码+报告\*\* 压缩包到 \*\*作业提交入口\*\* - 命名规则：2023\_SJTU\_PJ1\_第几组(.zip) - 提交截止日期：\*\*2023.4.22 23:59\*\* 考核标准： 1. 没有提交或没有实质的工作，得D 2. 完成"要求"中的第点，可得C 3. 完成前3点，通过全部测试用例且有较高的测试覆盖率，可得B 4. 完成前2点的基础上，体现出第3 4点，可得A 5. 以上均为参考，最后等级会根据最终的工作质量有所调整

* * *

**ChatGPT:**

您好！需要我为您做些什么？

* * *

**You:**

我需要你帮我写一份后40%工作量的对应的接口文档。为了参照，我会给你看看前60%工作量的那部分的接口文档是怎么写的。下面是接口文档。 auth.md ## 注册用户 #### URL： POST http://$address$/auth/register #### Request Body: \`\`\` { "user\_id":"$user name$", "password":"$user password$" } \`\`\` 变量名 | 类型 | 描述 | 是否可为空 ---|---|---|--- user\_id | string | 用户名 | N password | string | 登陆密码 | N #### Response Status Code: 码 | 描述 --- | --- 200 | 注册成功 5XX | 注册失败，用户名重复 Body: \`\`\` { "message":"$error message$" } \`\`\` 变量名 | 类型 | 描述 | 是否可为空 ---|---|---|--- message | string | 返回错误消息，成功时为"ok" | N ## 注销用户 #### URL： POST http://$address$/auth/unregister #### Request Body: \`\`\` { "user\_id":"$user name$", "password":"$user password$" } \`\`\` 变量名 | 类型 | 描述 | 是否可为空 ---|---|---|--- user\_id | string | 用户名 | N password | string | 登陆密码 | N #### Response Status Code: 码 | 描述 --- | --- 200 | 注销成功 401 | 注销失败，用户名不存在或密码不正确 Body: \`\`\` { "message":"$error message$" } \`\`\` 变量名 | 类型 | 描述 | 是否可为空 ---|---|---|--- message | string | 返回错误消息，成功时为"ok" | N ## 用户登录 #### URL： POST http://$address$/auth/login #### Request Body: \`\`\` { "user\_id":"$user name$", "password":"$user password$", "terminal":"$terminal code$" } \`\`\` 变量名 | 类型 | 描述 | 是否可为空 ---|---|---|--- user\_id | string | 用户名 | N password | string | 登陆密码 | N terminal | string | 终端代码 | N #### Response Status Code: 码 | 描述 --- | --- 200 | 登录成功 401 | 登录失败，用户名或密码错误 Body: \`\`\` { "message":"$error message$", "token":"$access token$" } \`\`\` 变量名 | 类型 | 描述 | 是否可为空 ---|---|---|--- message | string | 返回错误消息，成功时为"ok" | N token | string | 访问token，用户登录后每个需要授权的请求应在headers中传入这个token | 成功时不为空 #### 说明 1.terminal标识是哪个设备登录的，不同的设备拥有不同的ID，测试时可以随机生成。 2.token是登录后，在客户端中缓存的令牌，在用户登录时由服务端生成，用户在接下来的访问请求时不需要密码。token会定期地失效，对于不同的设备，token是不同的。token只对特定的时期特定的设备是有效的。 ## 用户更改密码 #### URL： POST http://$address$/auth/password #### Request Body: \`\`\` { "user\_id":"$user name$", "oldPassword":"$old password$", "newPassword":"$new password$" } \`\`\` 变量名 | 类型 | 描述 | 是否可为空 ---|---|---|--- user\_id | string | 用户名 | N oldPassword | string | 旧的登陆密码 | N newPassword | string | 新的登陆密码 | N #### Response Status Code: 码 | 描述 --- | --- 200 | 更改密码成功 401 | 更改密码失败 Body: \`\`\` { "message":"$error message$", } \`\`\` 变量名 | 类型 | 描述 | 是否可为空 ---|---|---|--- message | string | 返回错误消息，成功时为"ok" | N ## 用户登出 #### URL： POST http://$address$/auth/logout #### Request Headers: key | 类型 | 描述 ---|---|--- token | string | 访问token Body: \`\`\` { "user\_id":"$user name$" } \`\`\` 变量名 | 类型 | 描述 | 是否可为空 ---|---|---|--- user\_id | string | 用户名 | N #### Response Status Code: 码 | 描述 --- | --- 200 | 登出成功 401 | 登出失败，用户名或token错误 Body: \`\`\` { "message":"$error message$" } \`\`\` 变量名 | 类型 | 描述 | 是否可为空 ---|---|---|--- message | string | 返回错误消息，成功时为"ok" | N buyer.md ## 买家下单 #### URL： POST http://\[address\]/buyer/new\_order #### Request ##### Header: key | 类型 | 描述 | 是否可为空 ---|---|---|--- token | string | 登录产生的会话标识 | N ##### Body: \`\`\`json { "user\_id": "buyer\_id", "store\_id": "store\_id", "books": \[ { "id": "1000067", "count": 1 }, { "id": "1000134", "count": 4 } \] } \`\`\` ##### 属性说明： 变量名 | 类型 | 描述 | 是否可为空 ---|---|---|--- user\_id | string | 买家用户ID | N store\_id | string | 商铺ID | N books | class | 书籍购买列表 | N books数组： 变量名 | 类型 | 描述 | 是否可为空 ---|---|---|--- id | string | 书籍的ID | N count | string | 购买数量 | N #### Response Status Code: 码 | 描述 --- | --- 200 | 下单成功 5XX | 买家用户ID不存在 5XX | 商铺ID不存在 5XX | 购买的图书不存在 5XX | 商品库存不足 ##### Body: \`\`\`json { "order\_id": "uuid" } \`\`\` ##### 属性说明： 变量名 | 类型 | 描述 | 是否可为空 ---|---|---|--- order\_id | string | 订单号，只有返回200时才有效 | N ## 买家付款 #### URL： POST http://\[address\]/buyer/payment #### Request ##### Body: \`\`\`json { "user\_id": "buyer\_id", "order\_id": "order\_id", "password": "password" } \`\`\` ##### 属性说明： 变量名 | 类型 | 描述 | 是否可为空 ---|---|---|--- user\_id | string | 买家用户ID | N order\_id | string | 订单ID | N password | string | 买家用户密码 | N #### Response Status Code: 码 | 描述 --- | --- 200 | 付款成功 5XX | 账户余额不足 5XX | 无效参数 401 | 授权失败 ## 买家充值 #### URL： POST http://\[address\]/buyer/add\_funds #### Request ##### Body: \`\`\`json { "user\_id": "user\_id", "password": "password", "add\_value": 10 } \`\`\` ##### 属性说明： key | 类型 | 描述 | 是否可为空 ---|---|---|--- user\_id | string | 买家用户ID | N password | string | 用户密码 | N add\_value | int | 充值金额，以分为单位 | N Status Code: 码 | 描述 --- | --- 200 | 充值成功 401 | 授权失败 5XX | 无效参数

* * *

**ChatGPT:**

好的，请问需要写多少接口呢？需要补充哪些接口文档呢？

* * *

**You:**

补充40%工作量的那部分的接口文档

* * *

**ChatGPT:**

对于补充40%工作量的部分，以下是可能需要包含在接口文档中的内容：

1.  API名称和版本号：确保每个API都有一个独特的名称和版本号，并且这些信息在文档中得到清楚的说明。
    
2.  接口描述：说明该API的主要功能、输入参数和输出结果等信息。此外，也应该包括响应状态码的说明，例如200表示成功，400表示请求错误等。
    
3.  调用方式：说明如何调用API，包括HTTP方法、URL和请求体的格式等信息。
    
4.  输入参数和数据格式：说明需要传递给API的所有输入参数，以及这些参数的数据格式和限制条件等信息。
    
5.  输出结果和数据格式：说明API的输出结果，以及这些结果的数据格式和限制条件等信息。
    
6.  授权和认证：说明如何进行授权和认证，以便只有授权用户可以使用API。
    
7.  错误处理：说明API返回的错误信息，以及如何处理这些错误。
    
8.  示例代码：提供示例代码以帮助开发人员更好地理解如何调用API。
    
9.  限制和限制条件：说明API的使用限制和限制条件，例如请求速率限制、最大请求大小等。
    
10.  安全：说明如何保证API的安全性，包括如何

* * *

**You:**

请你帮我写这份接口文档。

* * *

**ChatGPT:**

当然，我可以帮您写接口文档。请提供以下信息：

1.  接口的名称和功能
2.  请求参数和请求体
3.  返回数据和返回状态码
4.  接口的调用示例

提供这些信息后，我将为您编写一个完整的接口文档。

* * *

**You:**

接口的大概功能在最开始的作业要求中已经给出了。我再说一遍，然后你估计着写写。 1)实现后续的流程 <br> 发货 -> 收货 2)搜索图书 <br> 用户可以通过关键字搜索，参数化的搜索方式； 如搜索范围包括，题目，标签，目录，内容；全站搜索或是当前店铺搜索。 如果显示结果较大，需要分页 (使用全文索引优化查找) 3)订单状态，订单查询和取消定单<br> 用户可以查自已的历史订单，用户也可以取消订单。<br> 取消定单可由买家主动地取消定单，或者买家下单后，经过一段时间超时仍未付款，定单也会自动取消。 <br>

* * *

**ChatGPT:**

好的，以下是接口文档的初步版本，请参考：

1.  发货接口

**接口地址：** /api/deliver

**请求方式：** POST

**请求参数：**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| order\_id | string | 是 | 要发货的订单号 |
| address | string | 是 | 收货地址 |
| items | array | 是 | 要发货的图书信息，每个元素包含图书的ID（book\_id）和数量（quantity） |

**返回参数：**

| 参数名 | 类型 | 描述 |
| --- | --- | --- |
| success | bool | 请求是否成功 |
| message | string | 返回的信息提示 |
| order\_id | string | 发货成功后的订单号 |
| items | array | 发货成功的图书信息，每个元素包含图书的ID（book\_id）和数量（quantity） |

**返回示例：**

```json
{
    "success": true,
    "message": "发货成功",
    "order_id": "123456789",
    "items": [
        {
            "book_id": "123",
            "quantity": 2
        },
        {
            "book_id": "456",
            "quantity": 1
        }
    ]
}
```

2.  搜索图书接口

**接口地址：** /api/search-books

**请求方式：** GET

**请求参数：**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| keyword | string | 是 | 搜索关键字，可以是图书标题、标签、目录、内容等 |
| store | int | 否 | 搜索范围，如果为空则搜索全站，否则搜索指定店铺（店铺ID） |
| page | int | 否 | 搜索结果分页的页码，从1开始，默认值为1 |
| size | int | 否 | 每页显示的搜索结果数量，默认值为10 |

**返回参数：**

| 参数名 | 类型 | 描述 |
| --- | --- | --- |
| success | bool | 请求是否成功 |
| message | string | 返回的信息提示 |
| total | int | 符合搜索条件的图书总数量 |
| books | array | 符合搜索条件的图书列表，每个元素包含图书的ID、标题、作者、出版社、标签等信息 |

**返回示例：**

```json
{
    "success": true,
    "message": "搜索成功",
    "total": 50,
    "books": [
        {
            "book_id": "123",
            "title": "Python编程入门",
            "author": "张三",
            "publisher": "人民邮电出版社",
            "tags": ["Python", "编程", "入门"],
            "price": 29.99,
            "stock": 100
        },
        {
            "book_id": "456",
            "title": "Java编程实践",
            "author": "李四",
            "publisher":
```

* * *

**You:**

继续

* * *

**ChatGPT:**

4.  购物车<br> 用户可以将想要购买的商品加入购物车中，然后再去结算下单。购物车可以支持添加、删除商品，修改商品数量等操作。用户也可以将购物车中的商品移入收藏夹中。
    
5.  支付<br> 用户可以使用不同的支付方式来完成订单支付，如微信支付、支付宝、银行卡等。支付流程应该简单明了，用户应该能够清楚地看到订单总金额、运费、税费等信息，并且可以选择使用哪种

* * *

**You:**

继续 搜索图书接口

* * *

**ChatGPT:**

搜索图书接口

URL: /api/book/search

请求方法: GET

请求参数:

| 参数名 | 类型 | 是否必填 | 说明 |
| --- | --- | --- | --- |
| query | string | 是 | 搜索关键字，支持参数化的搜索方式，包括题目、标签、目录、内容 |
| scope | string | 否 | 搜索范围，包括全站搜索或是当前店铺搜索，默认为全站搜索 |
| page | int | 否 | 分页页码，默认为1 |
| limit | int | 否 | 每页结果数，默认为20 |

请求示例:

```sql
GET /api/book/search?query=python&scope=all&page=1&limit=20 HTTP/1.1
Host: example.com
Authorization: Bearer xxxxxxxx
```

响应参数:

| 参数名 | 类型 | 是否必填 | 说明 |
| --- | --- | --- | --- |
| id | int | 是 | 图书 ID |
| title | string | 是 | 图书标题 |
| author | string | 是 | 图书作者 |
| publisher | string | 是 | 出版社名称 |
| price | float | 是 | 图书价格 |
| cover\_url | string | 是 | 图书封面 URL |
| created\_at | string | 是 | 图书创建时间戳 |
| updated\_at | string | 是 | 图书更新时间戳 |

响应示例:

```css
HTTP/1.1 200 OK
Content-Type: application/json

{
  "count": 10,
  "page": 1,
  "limit": 20,
  "books": [
    {
      "id": 1,
      "title": "Python编程从入门到实践",
      "author": "Eric Matthes",
      "publisher": "人民邮电出版社",
      "price": 59.9,
      "cover_url": "https://example.com/book1.jpg",
      "created_at": "2022-01-01 00:00:00",
      "updated_at": "2022-01-01 00:00:00"
    },
    {
      "id": 2,
      "title": "Fluent Python",
      "author": "Luciano Ramalho",
      "publisher": "O'Reilly Media",
      "price": 69.99,
      "cover_url": "https://example.com/book2.jpg",
      "created_at": "2022-01-01 00:00:00",
      "updated_at": "2022-01-01 00:00:00"
    },
    ...
  ]
}
```

错误码:

| 错误码 | 说明 |
| --- | --- |
| 400 | 请求参数不合法 |
| 401 | 用户未登录 |
| 403 | 用户无权访问该店铺 |
| 500 | 服务器内部错误 |

* * *

**You:**

继续生成 订单状态，订单查询和取消定单 接口

* * *

**ChatGPT:**

接口名称：获取订单状态

请求方法：GET

请求URL：/api/orders/status

请求参数：

| 参数名 | 必选 | 类型 | 说明 |
| --- | --- | --- | --- |
| order\_id | 是 | string | 订单ID |
| user\_id | 是 | string | 用户ID |
| timestamp | 是 | int | 请求时间戳 |
| sign | 是 | string | 请求签名 |

请求示例：

```sql
GET /api/orders/status?order_id=123456&user_id=1001&timestamp=1647465363&sign=xxxxxxxx
```

响应参数：

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| status | string | 订单状态 |
| order\_id | string | 订单ID |
| user\_id | string | 用户ID |
| message | string | 响应信息说明 |

响应示例：

```json
{
    "status": "已发货",
    "order_id": "123456",
    "user_id": "1001",
    "message": "获取订单状态成功"
}
```

接口名称：查询订单

请求方法：GET

请求URL：/api/orders/query

请求参数：

| 参数名 | 必选 | 类型 | 说明 |
| --- | --- | --- | --- |
| order\_id | 否 | string | 订单ID |
| user\_id | 是 | string | 用户ID |
| start\_time | 否 | int | 查询起始时间 |
| end\_time | 否 | int | 查询结束时间 |
| page | 否 | int | 查询页数 |
| limit | 否 | int | 每页显示数量 |
| timestamp | 是 | int | 请求时间戳 |
| sign | 是 | string | 请求签名 |

请求示例：

```bash
GET /api/orders/query?user_id=1001&start_time=1647465363&end_time=1647565363&page=1&limit=10&timestamp=1647465363&sign=xxxxxxxx
```

响应参数：

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| order\_id | string | 订单ID |
| user\_id | string | 用户ID |
| book\_name | string | 书名 |
| book\_author | string | 作者 |
| book\_price | float | 单价 |
| book\_num | int | 数量 |
| order\_time | int | 下单时间 |
| status | string | 订单状态 |
| total\_price | float | 订单总价 |
| message | string | 响应信息说明 |
| total\_count | int | 总订单数量 |
| total\_pages | int | 总页数 |
| current\_page | int | 当前页数 |

响应示例：

```json
{
    "orders": [
        {
            "order_id": "123456",
            "user_id": "1001",
            "book_name": "《时间简史》",
            "book_author": "霍金",
            "book_price": 20.5,
            "book_num": 2,
            "order_time": 1647465363
```

* * *

**You:**

继续 接口名称：查询订单

* * *

**ChatGPT:**

接口名称：查询订单

接口描述：用户查询自己的历史订单信息

请求方法：GET

请求URL：/api/order

请求参数：

| 参数名 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | --- | --- |
| user\_id | int | 是 | 用户ID |
| order\_id | int | 否 | 订单ID，若不填则返回该用户所有订单信息 |
| page | int | 否 | 页码，若不填则默认为第一页 |
| page\_size | int | 否 | 每页显示的订单数，若不填则默认为10 |

请求示例：

```json
{
    "user_id": 12345,
    "order_id": 1001,
    "page": 2,
    "page_size": 20
}
```

返回参数：

| 参数名 | 参数类型 | 参数描述 |
| --- | --- | --- |
| order\_list | list | 包含订单信息的列表 |
| total\_page | int | 总页数 |
| total\_num | int | 总订单数 |
| page | int | 当前页码 |
| page\_size | int | 每页显示的订单数 |

返回示例：

```json
{
    "order_list": [
        {
            "order_id": 1001,
            "book_id": 123,
            "book_title": "Python编程从入门到实践",
            "book_price": 59.9,
            "order_time": "2023-03-14 14:30:00",
            "status": "已完成"
        },
        {
            "order_id": 1002,
            "book_id": 456,
            "book_title": "算法导论",
            "book_price": 99.9,
            "order_time": "2023-03-13 10:20:00",
            "status": "已取消"
        }
    ],
    "total_page": 5,
    "total_num": 10,
    "page": 2,
    "page_size": 2
}
```

错误码：

| 错误码 | 错误信息 | 备注 |
| --- | --- | --- |
| 400 | Bad Request | 请求参数错误 |
| 401 | Unauthorized | 未授权 |
| 404 | Not Found | 订单不存在 |
| 500 | Internal Server Error | 服务器内部错误 |
| 503 | Service Unavailable | 服务不可用 |

备注：当返回码为200时，表示请求成功，可以从返回参数中获取订单信息。

* * *

**You:**

继续 取消订单 接口

* * *

**ChatGPT:**

接口名称：取消订单

接口描述：用户可以取消未支付或待发货的订单。

请求方法：POST

请求参数：

| 参数名 | 必选 | 类型 | 描述 |
| --- | --- | --- | --- |
| order\_id | 是 | string | 待取消订单的ID |

请求示例：

```bash
POST /api/cancel_order HTTP/1.1
Content-Type: application/json;charset=utf-8

{
  "order_id": "123456789"
}
```

响应参数：

| 参数名 | 类型 | 描述 |
| --- | --- | --- |
| code | int | 状态码，200表示成功 |
| msg | string | 响应信息 |

响应示例：

```css
HTTP/1.1 200 OK
Content-Type: application/json;charset=utf-8

{
  "code": 200,
  "msg": "取消订单成功"
}
```

错误码：

| 错误码 | 错误信息 |
| --- | --- |
| 400 | 参数错误 |
| 401 | 用户未登录 |
| 404 | 订单不存在或已支付/发货 |
| 500 | 服务器错误 |