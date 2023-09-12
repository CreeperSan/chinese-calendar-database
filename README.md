# chinese-calendar-database

[中文版请查看这里](README_zh_CN.md)

All Chinese Calendar Days In One SQLite Database ( 1901 ~ 2100 )

All data from HongKong Observatory, this repository is just collect and convert to SQLite database.

[Source](https://www.hko.gov.hk/tc/gts/time/conversion1_text.htm)

## How to use

You can import the database file `chinese-calendar.db` to your project and do whatever you want.

[Download Database](https://github.com/CreeperSan/chinese-calendar-database/releases)

The database table name is `days`, all Chinese text in database is Traditional Chinese,the table structure is below:

| Field            | Type    | Description                                |
|------------------|---------|--------------------------------------------|
| id               | INTEGER | Primary Key                                |
| year             | INTEGER | Year in Gregorian calendar                 |
| month            | INTEGER | Month in Gregorian calendar, starts from 1 |
| day              | INTEGER | Day in Gregorian calendar                  |
| weekday          | INTEGER | Weekday, 1 means Sunday, 2 means Monday    |
| lunar_year       | INTEGER | Lunar Year                                 |
| lunar_month      | INTEGER | Lunar Month, starts from 1                 |
| lunar_day        | INTEGER | Lunar Day                                  |
| is_leap_month    | INTEGER | Is Lunar Leap Month                        |
| lunar_year_name  | TEXT    | Lunar year name in Traditional Chinese     |
| lunar_month_name | TEXT    | Lunar month name in Traditional Chinese    |
| lunar_day_name   | TEXT    | Lunar day name in Traditional Chinese      |
| solar_term       | INTEGER | Solar Term                                 |
| solar_term_name  | TEXT    | Solar Term name in Traditional Chinese     |
| zodiac           | INTEGER | Zodiac                                     |
| zodiac_name      | TEXT    | Zodiac name in Traditional Chinese         |
| raw              | TEXT    | Original content in text file              |


| Solar Term | Name in Traditional Chinese |
|------------|-----------------------------|
| 0          | Not a solar term            |
| 1          | 立春                          |
| 2          | 雨水                          |
| 3          | 驚蟄                          |
| 4          | 春分                          |
| 5          | 清明                          |
| 6          | 穀雨                          |
| 7          | 立夏                          |
| 8          | 小滿                          |
| 9          | 芒種                          |
| 10         | 夏至                          |
| 11         | 小暑                          |
| 12         | 大暑                          |
| 13         | 立秋                          |
| 14         | 處暑                          |
| 15         | 白露                          |
| 16         | 秋分                          |
| 17         | 寒露                          |
| 18         | 霜降                          |
| 19         | 立冬                          |
| 20         | 小雪                          |
| 21         | 大雪                          |
| 22         | 冬至                          |
| 23         | 小寒                          |
| 24         | 大寒                          |

| Zodiac | Name in Traditional Chinese |
|--------|-----------------------------|
| 1      | 鼠                           |
| 2      | 牛                           |
| 3      | 虎                           |
| 4      | 兔                           |
| 5      | 龍                           |
| 6      | 蛇                           |
| 7      | 馬                           |
| 8      | 羊                           |
| 9      | 猴                           |
| 10     | 雞                           |
| 11     | 狗                           |
| 12     | 豬                           |

## How to generate database by yourself

If you want to generate the database file by yourself, you can follow the steps below.

1. Clone this repository
2. Run `pip install -r requirements.txt` in command line
3. Execute `src/01_download_chinese_calendar_text.py` to download the data from HongKong Observatory
4. You will find some text files in `data/txt` folder
5. Execute `src/02_generate_database_from_chinese_calendar_text.py` to convert the text file to SQLite database
6. You will find the database file `chinese_calendar.db` in `data/db` folder, enjoy it!
