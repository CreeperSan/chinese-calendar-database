# chinese-calendar-database

All Chinese Calendar Days In One SQLite Database ( 1901 ~ 2100 )

All data from HongKong Observatory, this repository is just collect and convert to SQLite database.

Source: https://www.hko.gov.hk/tc/gts/time/conversion1_text.htm

## How to use

You can import the database file `chinese-calendar.db` to your project and do whatever you want.

## How to generate

If you want to generate the database file by yourself, you can follow the steps below.

1. Clone this repository
2. Run `pip install -r requirements.txt` in command line
3. Execute `01_download_chinese_calendar_text.py` to download the data from HongKong Observatory
4. You will find some text files in `data/txt` folder
5. Execute `02_generate_database_from_chinese_calendar_text.py` to convert the text file to SQLite database
6. You will find the database file `chinese-calendar.db` in `data/db` folder, enjoy it!
