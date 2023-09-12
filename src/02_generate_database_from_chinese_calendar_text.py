import sqlite3
import os


SOLAR_TERMS_NONE = ''
SOLAR_TERMS_LICHUN = '立春'
SOLAR_TERMS_YUSHUI = '雨水'
SOLAR_TERMS_JINGZHE = '驚蟄'
SOLAR_TERMS_CHUNFEN = '春分'
SOLAR_TERMS_QINGMING = '清明'
SOLAR_TERMS_GUYU = '穀雨'
SOLAR_TERMS_LIXIA = '立夏'
SOLAR_TERMS_XIAOMAN = '小滿'
SOLAR_TERMS_MANGZHONG = '芒種'
SOLAR_TERMS_XIAZHI = '夏至'
SOLAR_TERMS_XIAOSHU = '小暑'
SOLAR_TERMS_DASHU = '大暑'
SOLAR_TERMS_LIQIU = '立秋'
SOLAR_TERMS_CHUSHU = '處暑'
SOLAR_TERMS_BAILU = '白露'
SOLAR_TERMS_QIUFEN = '秋分'
SOLAR_TERMS_HANLU = '寒露'
SOLAR_TERMS_SHUANGJIANG = '霜降'
SOLAR_TERMS_LIDONG = '立冬'
SOLAR_TERMS_XIAOXUE = '小雪'
SOLAR_TERMS_DAXUE = '大雪'
SOLAR_TERMS_DONGZHI = '冬至'
SOLAR_TERMS_XIAOHAN = '小寒'
SOLAR_TERMS_DAHAN = '大寒'

SOLAR_TERMS_MAPPING = {
    SOLAR_TERMS_NONE: 0,
    SOLAR_TERMS_LICHUN: 1,
    SOLAR_TERMS_YUSHUI: 2,
    SOLAR_TERMS_JINGZHE: 3,
    SOLAR_TERMS_CHUNFEN: 4,
    SOLAR_TERMS_QINGMING: 5,
    SOLAR_TERMS_GUYU: 6,
    SOLAR_TERMS_LIXIA: 7,
    SOLAR_TERMS_XIAOMAN: 8,
    SOLAR_TERMS_MANGZHONG: 9,
    SOLAR_TERMS_XIAZHI: 10,
    SOLAR_TERMS_XIAOSHU: 11,
    SOLAR_TERMS_DASHU: 12,
    SOLAR_TERMS_LIQIU: 13,
    SOLAR_TERMS_CHUSHU: 14,
    SOLAR_TERMS_BAILU: 15,
    SOLAR_TERMS_QIUFEN: 16,
    SOLAR_TERMS_HANLU: 17,
    SOLAR_TERMS_SHUANGJIANG: 18,
    SOLAR_TERMS_LIDONG: 19,
    SOLAR_TERMS_XIAOXUE: 20,
    SOLAR_TERMS_DAXUE: 21,
    SOLAR_TERMS_DONGZHI: 22,
    SOLAR_TERMS_XIAOHAN: 23,
    SOLAR_TERMS_DAHAN: 24
}

ZODIAC_SHU = '鼠'
ZODIAC_NIU = '牛'
ZODIAC_HU = '虎'
ZODIAC_TU = '兔'
ZODIAC_LONG = '龍'
ZODIAC_SHE = '蛇'
ZODIAC_MA = '馬'
ZODIAC_YANG = '羊'
ZODIAC_HOU = '猴'
ZODIAC_JI = '雞'
ZODIAC_GOU = '狗'
ZODIAC_ZHU = '豬'

ZODIAC_MAPPING = {
    ZODIAC_SHU: 1,
    ZODIAC_NIU: 2,
    ZODIAC_HU: 3,
    ZODIAC_TU: 4,
    ZODIAC_LONG: 5,
    ZODIAC_SHE: 6,
    ZODIAC_MA: 7,
    ZODIAC_YANG: 8,
    ZODIAC_HOU: 9,
    ZODIAC_JI: 10,
    ZODIAC_GOU: 11,
    ZODIAC_ZHU: 12
}

MONTH_JANUARY = '正月'
MONTH_FEBRUARY = '二月'
MONTH_MARCH = '三月'
MONTH_APRIL = '四月'
MONTH_MAY = '五月'
MONTH_JUNE = '六月'
MONTH_JULY = '七月'
MONTH_AUGUST = '八月'
MONTH_SEPTEMBER = '九月'
MONTH_OCTOBER = '十月'
MONTH_NOVEMBER = '十一月'
MONTH_DECEMBER = '十二月'

MONTH_MAPPING = {
    MONTH_JANUARY: 1,
    MONTH_FEBRUARY: 2,
    MONTH_MARCH: 3,
    MONTH_APRIL: 4,
    MONTH_MAY: 5,
    MONTH_JUNE: 6,
    MONTH_JULY: 7,
    MONTH_AUGUST: 8,
    MONTH_SEPTEMBER: 9,
    MONTH_OCTOBER: 10,
    MONTH_NOVEMBER: 11,
    MONTH_DECEMBER: 12,
}


DAY_ONE = '初一'
DAY_TWO = '初二'
DAY_THREE = '初三'
DAY_FOUR = '初四'
DAY_FIVE = '初五'
DAY_SIX = '初六'
DAY_SEVEN = '初七'
DAY_EIGHT = '初八'
DAY_NINE = '初九'
DAY_TEN = '初十'
DAY_ELEVEN = '十一'
DAY_TWELVE = '十二'
DAY_THIRTEEN = '十三'
DAY_FOURTEEN = '十四'
DAY_FIFTEEN = '十五'
DAY_SIXTEEN = '十六'
DAY_SEVENTEEN = '十七'
DAY_EIGHTEEN = '十八'
DAY_NINETEEN = '十九'
DAY_TWENTY = '二十'
DAY_TWENTY_ONE = '廿一'
DAY_TWENTY_TWO = '廿二'
DAY_TWENTY_THREE = '廿三'
DAY_TWENTY_FOUR = '廿四'
DAY_TWENTY_FIVE = '廿五'
DAY_TWENTY_SIX = '廿六'
DAY_TWENTY_SEVEN = '廿七'
DAY_TWENTY_EIGHT = '廿八'
DAY_TWENTY_NINE = '廿九'
DAY_THIRTY = '三十'

DAY_MAPPING = {
    DAY_ONE: 1,
    DAY_TWO: 2,
    DAY_THREE: 3,
    DAY_FOUR: 4,
    DAY_FIVE: 5,
    DAY_SIX: 6,
    DAY_SEVEN: 7,
    DAY_EIGHT: 8,
    DAY_NINE: 9,
    DAY_TEN: 10,
    DAY_ELEVEN: 11,
    DAY_TWELVE: 12,
    DAY_THIRTEEN: 13,
    DAY_FOURTEEN: 14,
    DAY_FIFTEEN: 15,
    DAY_SIXTEEN: 16,
    DAY_SEVENTEEN: 17,
    DAY_EIGHTEEN: 18,
    DAY_NINETEEN: 19,
    DAY_TWENTY: 20,
    DAY_TWENTY_ONE: 21,
    DAY_TWENTY_TWO: 22,
    DAY_TWENTY_THREE: 23,
    DAY_TWENTY_FOUR: 24,
    DAY_TWENTY_FIVE: 25,
    DAY_TWENTY_SIX: 26,
    DAY_TWENTY_SEVEN: 27,
    DAY_TWENTY_EIGHT: 28,
    DAY_TWENTY_NINE: 29,
    DAY_THIRTY: 30
}


WEEKDAY_MONDAY = '星期一'
WEEKDAY_TUESDAY = '星期二'
WEEKDAY_WEDNESDAY = '星期三'
WEEKDAY_THURSDAY = '星期四'
WEEKDAY_FRIDAY = '星期五'
WEEKDAY_SATURDAY = '星期六'
WEEKDAY_SUNDAY = '星期日'

WEEKDAY_MAPPING = {
    WEEKDAY_SUNDAY: 1,
    WEEKDAY_MONDAY: 2,
    WEEKDAY_TUESDAY: 3,
    WEEKDAY_WEDNESDAY: 4,
    WEEKDAY_THURSDAY: 5,
    WEEKDAY_FRIDAY: 6,
    WEEKDAY_SATURDAY: 7
}


if __name__ == '__main__':
    # Initialize database
    path_db = 'data/db/chinese_calendar.db'
    if os.path.exists(path_db):
        os.remove(path_db)
    conn = sqlite3.connect(path_db)
    c = conn.cursor()
    c.execute('CREATE TABLE IF NOT EXISTS days('
              '_id INTEGER PRIMARY KEY AUTOINCREMENT,'
              'year INTEGER,'
              'month INTEGER,'
              'day INTEGER,'
              'weekday INTEGER,'
              'lunar_year INTEGER,'
              'lunar_month INTEGER,'
              'lunar_day INTEGER,'
              'is_leap_month INTEGER,'
              'lunar_year_name TEXT,'
              'lunar_month_name TEXT,'
              'lunar_day_name TEXT,'
              'solar_term INTEGER,'
              'solar_term_name TEXT,'
              'zodiac INTEGER,'
              'zodiac_name TEXT,'
              'raw TEXT'
              ')')
    # Generate database
    data_year = 1901
    data_month = 1
    data_day = 1
    data_weekday = 2
    data_lunar_year = 1900
    data_lunar_month = 11
    data_lunar_day = 11
    data_is_leap_month = 0
    data_lunar_year_name = '庚子'
    data_lunar_month_name = '十一'
    data_lunar_day_name = '十一'
    data_solar_term = SOLAR_TERMS_MAPPING[SOLAR_TERMS_NONE]
    data_solar_term_name = SOLAR_TERMS_NONE
    data_zodiac = ZODIAC_MAPPING[ZODIAC_SHU]
    data_zodiac_name = ZODIAC_SHU
    data_raw = ''

    loop_year_name = ''
    loop_zodiac = ''
    loop_is_leap_month = 0

    index_txt_file = 1901
    while index_txt_file <= 2100:
        path_file = 'data/txt/{}.txt'.format(index_txt_file)
        with open(path_file, 'r', encoding='utf-8') as f:
            txt_line_array = f.readlines()
            for (index_line, txt_line) in enumerate(txt_line_array):
                txt_line: str = txt_line.strip()  # Remove \n and space
                if len(txt_line) == 0:  # Skip empty line
                    continue
                if txt_line.startswith('公曆日期'):  # Skip title line
                    continue
                if '香港' in txt_line:  # Skip description line
                    continue
                if index_line == 0:
                    # Line 1 is the year information
                    zodiac_index = txt_line.find(')') - 1
                    lunar_year_name_index = txt_line.find('(') + 1
                    loop_zodiac: str = txt_line[zodiac_index:zodiac_index + 1].replace('犬', '狗')  # Replace 犬 with 狗, currently I don't know why some use 犬 and some use 狗
                    loop_year_name = txt_line[lunar_year_name_index:lunar_year_name_index + 2]
                    print('zodiac: {}, lunar_year_name: {}'.format(loop_zodiac, loop_year_name))
                else:
                    # Other lines are the day information
                    txt_line_split = txt_line.split(' ')
                    txt_line_split = list(filter(lambda x: len(x) > 0, txt_line_split))
                    # Original text
                    data_raw = txt_line
                    # Convert solar term
                    if len(txt_line_split) == 4:
                        data_solar_term_name = txt_line_split[3]
                        data_solar_term = SOLAR_TERMS_MAPPING[data_solar_term_name]
                    else:
                        data_solar_term_name = SOLAR_TERMS_NONE
                        data_solar_term = SOLAR_TERMS_MAPPING[SOLAR_TERMS_NONE]
                    # Convert year, month, day to number
                    text_line_split_date: str = txt_line_split[0]
                    data_year = text_line_split_date[0:4]
                    data_month = text_line_split_date[text_line_split_date.find('年') + 1:text_line_split_date.find('月')]
                    data_day = text_line_split_date[text_line_split_date.find('月') + 1:text_line_split_date.find('日')]
                    # Convert weekday to number
                    text_line_split_weekday = txt_line_split[2]
                    text_line_split_weekday_mapping = WEEKDAY_MAPPING[text_line_split_weekday]
                    data_weekday = text_line_split_weekday_mapping if text_line_split_weekday_mapping else 0
                    # Calculating lunar year, month, day, zodiac
                    text_line_split_lunar_name:str = txt_line_split[1]
                    if text_line_split_lunar_name == '正月':
                        # which means it's a new year
                        data_is_leap_month = 0
                        data_lunar_year += 1
                        data_lunar_year_name = loop_year_name
                        data_lunar_month = MONTH_MAPPING[MONTH_JANUARY]
                        data_lunar_month_name = MONTH_JANUARY
                        data_lunar_day = DAY_MAPPING[DAY_ONE]
                        data_lunar_day_name = DAY_ONE
                        data_zodiac_name = loop_zodiac
                        data_zodiac = ZODIAC_MAPPING[data_zodiac_name]
                    elif text_line_split_lunar_name.endswith('月'):
                        # which means it's a normal month
                        if text_line_split_lunar_name.startswith('閏'):
                            data_is_leap_month = 1
                            text_line_split_lunar_name = text_line_split_lunar_name[1:]  # Remove 閏
                        else:
                            data_is_leap_month = 0
                        data_lunar_month = MONTH_MAPPING[text_line_split_lunar_name]
                        data_lunar_month_name = text_line_split_lunar_name
                        data_lunar_day = DAY_MAPPING[DAY_ONE]
                        data_lunar_day_name = DAY_ONE
                    else:
                        # which means it's a normal day
                        data_lunar_day = DAY_MAPPING[text_line_split_lunar_name]
                        data_lunar_day_name = text_line_split_lunar_name
                    print('{}. {}'.format(index_line, txt_line.strip()))
                    c.execute('INSERT INTO days('
                                'year,'
                                'month,'
                                'day,'
                                'weekday,'
                                'lunar_year,'
                                'lunar_month,'
                                'lunar_day,'
                                'is_leap_month,'
                                'lunar_year_name,'
                                'lunar_month_name,'
                                'lunar_day_name,'
                                'solar_term,'
                                'solar_term_name,'
                                'zodiac,'
                                'zodiac_name,'
                                'raw'
                                ') VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)',
                                (
                                    data_year,
                                    data_month,
                                    data_day,
                                    data_weekday,
                                    data_lunar_year,
                                    data_lunar_month,
                                    data_lunar_day,
                                    data_is_leap_month,
                                    data_lunar_year_name,
                                    data_lunar_month_name,
                                    data_lunar_day_name,
                                    data_solar_term,
                                    data_solar_term_name,
                                    data_zodiac,
                                    data_zodiac_name,
                                    data_raw
                                ))
                    # conn.commit()
        index_txt_file += 1
        conn.commit()

    conn.close()
