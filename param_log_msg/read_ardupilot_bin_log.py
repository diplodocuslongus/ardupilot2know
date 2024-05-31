# from:
# Very usefull: list of all possible log messages:
# https://ardupilot.org/copter/docs/logmessages.html#logmessages
# the code has some issues such as
# return an error if types is not specified (so it's not an option)
'''
>>> parser = Ardupilot.parse('2024-05-30_10-42-49_noIMU.bin')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/home/ludofw/.virtualenvs/Ardupilot/lib/python3.10/site-packages/ardupilot_log_reader/reader.py", line 77, in parse
    list(set(types + ['PARM'])), 
TypeError: unsupported operand type(s) for +: 'NoneType' and 'list'
'''
# when parsing with some types that are not present, there's no complain:
'''
>>> parser = Ardupilot.parse('2024-05-30_10-42-49_noIMU.bin',types=['XKF1','XKF2','GPS','VISP', 'VISV','BARO'])
But then when trying to print the corresponding key:
>>> print(parser.dfs['BARO'])
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'BARO'
'''

# not sure if possible to get the list of all the messages


from ardupilot_log_reader.reader import Ardupilot
parser = Ardupilot.parse('2024-05-30_10-42-49_noIMU.bin',types=['XKF1'])
type(parser.dfs)
# <class 'dict'>
print(parser.dfs)
{'PARM':          timestamp     TimeUS              Name     Value
0     1.631723e+09     693552    FORMAT_VERSION      13.0
1     1.631723e+09     693564     SYSID_THISMAV       1.0
2     1.631723e+09     693575       SYSID_MYGCS     255.0
3     1.631723e+09     693588      SERIAL0_BAUD     115.0
4     1.631723e+09     693602  SERIAL0_PROTOCOL       2.0
...            ...        ...               ...       ...
1158  1.631724e+09  525461816      STAT_RUNTIME  176933.0
1159  1.631724e+09  556461512      STAT_FLTTIME  133036.0
1160  1.631724e+09  556461804      STAT_RUNTIME  176964.0
1161  1.631724e+09  587461514      STAT_FLTTIME  133067.0
1162  1.631724e+09  587461825      STAT_RUNTIME  176995.0

[1163 rows x 4 columns], 'XKF1':           timestamp     TimeUS  Roll  Pitch     Yaw        VN        VE        VD       dPD        PN        PE        PD    GX    GY    GZ    OH
0      1.631723e+09    9501130 -0.07  -3.46    0.00  0.000000  0.000000  0.000000  0.000000  0.000000  0.000000  0.000000  0.00  0.00  0.00  0.00
1      1.631723e+09    9539669 -0.07  -3.46    0.00  0.000000  0.000000  0.000000  0.000000  0.000000  0.000000  0.000000  0.00  0.00  0.00  0.00
2      1.631723e+09    9579579 -0.07  -3.46    0.00  0.000000  0.000000  0.000000  0.000000  0.000000  0.000000  0.000000  0.00  0.00  0.00  0.00
3      1.631723e+09    9619606 -0.07  -3.46    0.00  0.000000  0.000000  0.000000  0.000000  0.000000  0.000000  0.000000  0.00  0.00  0.00  0.00
4      1.631723e+09    9659786 -0.07  -3.46    0.00  0.000000  0.000000  0.000000  0.000000  0.000000  0.000000  0.000000  0.00  0.00  0.00  0.00
...             ...        ...   ...    ...     ...       ...       ...       ...       ...       ...       ...       ...   ...   ...   ...   ...
15133  1.631724e+09  614821085  0.85   1.03  121.59  0.008308 -0.001549  0.092977 -0.038441  1.322874  0.354270 -0.535253  0.06 -0.09 -0.09  7.52
15134  1.631724e+09  614860282  0.95   0.99  121.59  0.000695 -0.004114  0.091411 -0.051954  1.323318  0.352860 -0.536961  0.06 -0.09 -0.09  7.52
15135  1.631724e+09  614900072  1.02   0.99  121.60  0.006779 -0.005545  0.088268 -0.050460  1.323673  0.351529 -0.538010  0.06 -0.09 -0.09  7.52
15136  1.631724e+09  614940187  1.00   1.00  121.62  0.012943  0.003316  0.091803 -0.033831  1.324265  0.350536 -0.538379  0.06 -0.09 -0.09  7.52
15137  1.631724e+09  614981108  0.94   1.00  121.63  0.017225  0.006682  0.091526 -0.017012  1.325427  0.349559 -0.539921  0.06 -0.09 -0.09  7.52

[15138 rows x 16 columns]}
print(parser.dfs.keys())
# dict_keys(['PARM', 'XKF1'])
print(parser.dfs['PARM'])
         timestamp     TimeUS              Name     Value
0     1.631723e+09     693552    FORMAT_VERSION      13.0
1     1.631723e+09     693564     SYSID_THISMAV       1.0
2     1.631723e+09     693575       SYSID_MYGCS     255.0
3     1.631723e+09     693588      SERIAL0_BAUD     115.0
4     1.631723e+09     693602  SERIAL0_PROTOCOL       2.0
...            ...        ...               ...       ...
1158  1.631724e+09  525461816      STAT_RUNTIME  176933.0
1159  1.631724e+09  556461512      STAT_FLTTIME  133036.0
1160  1.631724e+09  556461804      STAT_RUNTIME  176964.0
1161  1.631724e+09  587461514      STAT_FLTTIME  133067.0
1162  1.631724e+09  587461825      STAT_RUNTIME  176995.0

[1163 rows x 4 columns]
>>> print(parser.dfs['PARM'][:20])
       timestamp  TimeUS              Name     Value
0   1.631723e+09  693552    FORMAT_VERSION      13.0
1   1.631723e+09  693564     SYSID_THISMAV       1.0
2   1.631723e+09  693575       SYSID_MYGCS     255.0
3   1.631723e+09  693588      SERIAL0_BAUD     115.0
4   1.631723e+09  693602  SERIAL0_PROTOCOL       2.0
5   1.631723e+09  693616  SERIAL1_PROTOCOL       1.0
6   1.631723e+09  693630      SERIAL1_BAUD      57.0
7   1.631723e+09  693645  SERIAL2_PROTOCOL       1.0
8   1.631723e+09  693658      SERIAL2_BAUD      57.0
9   1.631723e+09  693673  SERIAL3_PROTOCOL       5.0
10  1.631723e+09  693687      SERIAL3_BAUD      38.0
11  1.631723e+09  693703  SERIAL4_PROTOCOL      23.0
12  1.631723e+09  693717      SERIAL4_BAUD      38.0
13  1.631723e+09  693733  SERIAL5_PROTOCOL      -1.0
14  1.631723e+09  693748      SERIAL5_BAUD      57.0
15  1.631723e+09  693765  SERIAL6_PROTOCOL       2.0
16  1.631723e+09  693780      SERIAL6_BAUD  115200.0
17  1.631723e+09  693795   SERIAL1_OPTIONS       0.0
18  1.631723e+09  693811   SERIAL2_OPTIONS       0.0
19  1.631723e+09  693835   SERIAL3_OPTIONS       0.0


parser = Ardupilot.parse('2024-05-30_10-42-49_noIMU.bin',types=[])
print(parser.dfs)
{'PARM':          timestamp     TimeUS             Name     Value  Default
0     1.717037e+09  264862224   FORMAT_VERSION     120.0    120.0
1     1.717037e+09  264862239    SYSID_THISMAV       1.0      1.0
2     1.717037e+09  264862255      SYSID_MYGCS     255.0    255.0
3     1.717037e+09  264862322   PILOT_THR_FILT       0.0      0.0
4     1.717037e+09  264862340  PILOT_TKOFF_ALT       0.0      0.0
...            ...        ...              ...       ...      ...
1025  1.717037e+09  457770048     STAT_RUNTIME  112282.0      NaN
1026  1.717037e+09  487770337     STAT_FLTTIME    4600.0      NaN
1027  1.717037e+09  487773100     STAT_RUNTIME  112312.0      NaN
1028  1.717037e+09  518768851     STAT_RUNTIME  112343.0      NaN
1029  1.717037e+09  548772670     STAT_RUNTIME  112373.0      NaN

parser = Ardupilot.parse('2024-05-30_10-42-49_noIMU.bin',types=['XKF1','XKF2','GPS','VISP', 'VISV'])
print(parser.dfs['VISV'])
         timestamp     TimeUS           RTimeUS  CTimeMS        VX        VY        VZ  VErr  Rst  Ign  Q
0     1.717037e+09  264912093  1716964424716522   264908 -0.000827  0.001344 -0.000732   0.5    0    0  0
1     1.717037e+09  264960339  1716964424765798   264958 -0.001090  0.001138 -0.001017   0.5    0    0  0
2     1.717037e+09  265012825  1716964424817237   265009 -0.001015  0.001159 -0.001171   0.5    0    0  0
3     1.717037e+09  265060932  1716964424866623   265058 -0.001059  0.000744 -0.000922   0.5    0    0  0
4     1.717037e+09  265110899  1716964424915711   265108 -0.000898  0.000380 -0.000188   0.5    0    0  0
...            ...        ...               ...      ...       ...       ...       ...   ...  ...  ... ..
4499  1.717037e+09  489842824  1716964649647048   489838  1.540815  4.547993  0.347845   0.5    0    0  0
4500  1.717037e+09  489889745  1716964649696191   489887  1.524032  4.421861  0.309490   0.5    0    0  0
4501  1.717037e+09  489942727  1716964649746912   489938  1.505512  4.362039  0.304738   0.5    0    0  0
4502  1.717037e+09  489992737  1716964649797679   489989  1.479072  4.268604  0.296279   0.5    0    0  0
4503  1.717037e+09  490042990  1716964649849802   490041  1.491498  4.424110  0.337405   0.5    0    0  0

[4504 rows x 11 columns]


p
