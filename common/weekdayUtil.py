import datetime

'''
    根据日期得出星期几
'''

def get_week_day(date):
  week_day_dict = {
    0 : '星期一',
    1 : '星期二',
    2 : '星期三',
    3 : '星期四',
    4 : '星期五',
    5 : '星期六',
    6 : '星期日',
  }
  day = date.weekday()
  return week_day_dict[day]

if __name__ == '__main__':

    # curr_time = [
    # '2020-09-26_12:50:43',
    # '2020-09-26_17:46:40',
    # '2020-09-26_19:38:30',
    # '2020-09-27_07:33:32',
    # '2020-09-27_13:31:23',
    # '2020-09-27_14:49:11',
    # '2020-09-27_17:45:10',
    # '2020-09-28_07:55:21',
    # '2020-09-28_08:59:33',
    # '2020-09-28_16:31:54',
    # '2020-09-28_17:37:06',
    # '2020-09-29_10:04:28',
    # '2020-09-29_12:18:21',
    # '2020-09-29_18:33:44',
    # '2020-09-29_19:53:03',
    # '2020-09-30_15:23:51',
    # '2020-09-30_16:47:38',
    # '2020-09-30_18:30:57',
    # '2020-09-30_19:54:26',
    # '2020-10-01_12:26:45',
    # '2020-10-01_15:31:29',
    # '2020-10-01_16:02:02',
    # '2020-10-01_17:13:57',
    # '2020-10-01_19:26:54',
    # '2020-10-01_19:28:33',
    # '2020-10-02_10:12:50',
    # '2020-10-02_19:27:12',
    # '2020-10-02_20:27:42',
    # '2020-10-03_11:52:14',
    # '2020-10-03_16:13:28',
    # '2020-10-03_17:00:08',
    # '2020-10-04_10:30:42',
    # '2020-10-04_10:43:16',
    # '2020-10-04_16:09:20',
    # '2020-10-04_21:01:52',
    # '2020-10-05_11:43:46',
    # '2020-10-05_11:43:50',
    # '2020-10-05_15:54:18',
    # '2020-10-05_22:13:27',
    # '2020-10-06_12:01:54',
    # '2020-10-06_12:08:17',
    # '2020-10-06_16:32:08',
    # '2020-10-07_08:52:54',
    # '2020-10-07_14:53:50',
    # '2020-10-07_16:31:58']

    curr_time = ['2020.06.25',
                 '2020.06.26',
                 '2020.06.27',
                 '2020.06.28',
                 '2020.06.29',
                 '2020.06.30',
                 '2020.07.01',
                 '2020.07.02',
                 '2020.07.03',
                 '2020.07.04',
                 '2020.07.05',
                 '2020.07.06',
                 '2020.07.07',
                 '2020.07.08',
                 '2020.07.09',
                 '2020.07.10',
                 '2020.07.11',
                 '2020.07.12',
                 '2020.07.13',
                 '2020.07.14',
                 '2020.07.15',
                 '2020.07.16',
                 '2020.07.17',
                 '2020.07.18',
                 '2020.07.19',
                 '2020.07.20',
                 '2020.07.21',
                 '2020.07.22',
                 '2020.07.23',
                 '2020.07.24',
                 '2020.07.25',
                 '2020.07.26',
                 '2020.07.27',
                 '2020.07.28',
                 '2020.07.29',
                 '2020.07.30',
                 '2020.07.31',
                 '2020.08.01',
                 '2020.08.02',
                 '2020.08.03',
                 '2020.08.04',
                 '2020.08.05',
                 '2020.08.06',
                 '2020.08.07',
                 '2020.08.08',
                 '2020.08.09',
                 '2020.08.10',
                 '2020.08.11',
                 '2020.08.12',
                 '2020.08.13',
                 '2020.08.14',
                 '2020.08.15',
                 '2020.08.16',
                 '2020.08.17',
                 '2020.08.18',
                 '2020.08.19',
                 '2020.08.20',
                 '2020.08.21',
                 '2020.08.22',
                 '2020.08.23',
                 '2020.08.24',
                 '2020.08.25',
                 '2020.08.26',
                 '2020.08.27',
                 '2020.08.28',
                 '2020.08.29',
                 '2020.08.30',
                 '2020.08.31',
                 '2020.09.01',
                 '2020.09.02',
                 '2020.09.03',
                 '2020.09.04',
                 '2020.09.05',
                 '2020.09.06',
                 '2020.09.07',
                 '2020.09.08',
                 '2020.09.09',
                 '2020.09.10',
                 '2020.09.11',
                 '2020.09.12',
                 '2020.09.13',
                 '2020.09.14',
                 '2020.09.15',
                 '2020.09.16',
                 '2020.09.17',
                 '2020.09.18',
                 '2020.09.19',
                 '2020.09.20',
                 '2020.09.21',
                 '2020.09.22',
                 '2020.09.23',
                 '2020.09.24',
                 '2020.09.25',
                 '2020.09.26',
                 '2020.09.27',
                 '2020.09.28',
                 '2020.09.29',
                 '2020.09.30',
                 '2020.10.01',
                 '2020.10.02',
                 '2020.10.03',
                 '2020.10.04',
                 '2020.10.05',
                 '2020.10.06',
                 '2020.10.07',
                 '2020.10.30',
                 '2020.10.31',
                 '2020.11.01',
                 '2020.11.02'
                 ]

    for ctime in curr_time:
        # 1.先转成datetime
        dtime = datetime.datetime.strptime(ctime, "%Y.%m.%d")
        # reformat = ctime.split("_")[0].replace("-", "/") + " " + get_week_day(dtime) + " " + ctime.split("_")[1]
        # arr =
        reformat = ctime + "（" + get_week_day(dtime) + ")"
        # print(ctime, get_week_day(dtime))
        print(reformat)