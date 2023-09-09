import wget

if __name__ == '__main__':
    print('Running 01_download_chinese_calendar_text.py')
    print('This script downloads the Chinese calendar text from the HongKong Observatory Website and saves it to a text file.')
    year = 1901
    while year <= 2100:
        print('Downloading Chinese calendar text for year {}...'.format(year))
        download_url = 'https://www.hko.gov.hk/tc/gts/time/calendar/text/files/T{}c.txt'.format(year)
        download_path = 'data/txt/{}.txt'.format(year)
        wget.download(download_url, download_path)
        print('Convert text file format from big5 to utf-8 for year {}.'.format(year))
        with open(download_path, 'r', encoding='big5') as f:
            text = f.read()
            with open(download_path, 'w', encoding='utf-8') as f:
                f.write(text)
        year += 1
    print('Finished 01_download_chinese_calendar_text.py')
