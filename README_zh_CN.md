# 农历数据库

整合了 1901年 至 2100 年每一天农历信息的数据库

所有的数据均来源于香港天文台的公开数据，这里只是做个整合

[数据来源](https://www.hko.gov.hk/tc/gts/time/conversion1_text.htm)

## 如何使用

你可以直接导入 `chinese-calendar.db` 数据库文件到你的项目中，然后做任何你想做的事情

[下载数据库](https://github.com/CreeperSan/chinese-calendar-database/releases)

数据库表名为 `days`，其中的中文均为繁体中文，表结构如下：

| 字段               | 类型      | 描述                 |
|------------------|---------|--------------------|
| id               | INTEGER | 主键                 |
| year             | INTEGER | 对应公历的年             |
| month            | INTEGER | 对应公历的月, 从 0 开始     |
| day              | INTEGER | 对应公历的日             |
| weekday          | INTEGER | 对应星期, 1 为周日, 2 为周一 |
| lunar_year       | INTEGER | 对应农历的年             |
| lunar_month      | INTEGER | 对应农历的月, 从 0 开始     |
| lunar_day        | INTEGER | 对应农历的日             |
| is_leap_month    | INTEGER | 是否为闰月              |
| lunar_year_name  | TEXT    | 农历年份的名称            |
| lunar_month_name | TEXT    | 农历月份的名称            |
| lunar_day_name   | TEXT    | 农历日的名称             |
| solar_term       | INTEGER | 节气                 |
| solar_term_name  | TEXT    | 节气的名称              |
| zodiac           | INTEGER | 生肖                 |
| zodiac_name      | TEXT    | 生肖的名称              |
| raw              | TEXT    | 香港天文台的原始数据         |


| 节气取值 | 节气名称   |
|------|--------|
| 0    | 当天不是节气 |
| 1    | 立春     |
| 2    | 雨水     |
| 3    | 驚蟄     |
| 4    | 春分     |
| 5    | 清明     |
| 6    | 穀雨     |
| 7    | 立夏     |
| 8    | 小滿     |
| 9    | 芒種     |
| 10   | 夏至     |
| 11   | 小暑     |
| 12   | 大暑     |
| 13   | 立秋     |
| 14   | 處暑     |
| 15   | 白露     |
| 16   | 秋分     |
| 17   | 寒露     |
| 18   | 霜降     |
| 19   | 立冬     |
| 20   | 小雪     |
| 21   | 大雪     |
| 22   | 冬至     |
| 23   | 小寒     |
| 24   | 大寒     |

| 生肖取值 | 生肖名称 |
|------|------|
| 1    | 鼠    |
| 2    | 牛    |
| 3    | 虎    |
| 4    | 兔    |
| 5    | 龍    |
| 6    | 蛇    |
| 7    | 馬    |
| 8    | 羊    |
| 9    | 猴    |
| 10   | 雞    |
| 11   | 狗    |
| 12   | 豬    |

## 如何自行生成数据库

如果你想自行生成数据库文件，可以按照以下步骤进行

1. 克隆本仓库
2. 在命令行中执行 `pip install -r requirements.txt` 安装依赖
3. 运行 `src/01_download_chinese_calendar_text.py` 从香港天文台网站中下载数据
4. 确保数据正确下载到了 `data/txt` 文件夹中
5. 运行 `src/02_generate_database_from_chinese_calendar_text.py` 将文本文件转换为 SQLite 数据库
6. 你将在 `data/db` 文件夹中找到生成的数据库文件 `chinese_calendar.db`，尽情享用吧！
