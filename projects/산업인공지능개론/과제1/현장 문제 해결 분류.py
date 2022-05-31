# -*- coding: utf-8 -*-
"""Untitled3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1NhwOZByPFFd-h8VGIdcSRB7O6R9agBOs
"""

#!pip install durable_rules
from durable.lang import *

# 간이무기고 - 간이무기고 관리 시스템
# m.설치     - 설치 시 일어나는 증상
# m.함체     - 간이무기고 관리 시스템의 기기 본체
# m.LED1     - 함체의 LED1 색깔
# m.LED2     - 함체의 LED2 색깔
# m.순번     - 정상, 비정상의 순번 분류
# m.소리     - 비프음 여부
# m.지문     - 지문인식기 지문 등록 여부
# m.태그     - RFID 태그 등록 여부
# m.최종     - 최종 작동 함체
# m.매칭     - 매칭 여부
# m.작동여부 - 작동 결과
# m.결과 - 사용 가능 여부



with ruleset('간이무기고'):
    # 1. 함체는 LED가 초록불 + 초록불이면 정상이다. 
    @when_all((m.설치 == '함체') & (m.LED1 == '초록불') & (m.LED2 == '초록불'))
    def 결과1(c):
        c.assert_fact({'순번' : c.m.순번, '함체순번' : c.m.함체, '결과' : '정상'})
        print('작동 전 체크 메뉴얼 : {0}'.format(c.m.순번))

    # 2. 함체는 LED가 초록불 + 빨간불이면 비정상이다. 
    @when_all((m.설치 == '함체') & (m.LED1 == '빨간불') & (m.LED2 == '초록불'))
    def 결과2(c):
        c.assert_fact({'순번' : c.m.순번, '함체순번' : c.m.함체, '결과' : '비정상'})
        print('작동 전 체크 메뉴얼 : {0}'.format(c.m.순번))

    # 3. 함체는 LED가 빨간불 + 빨간불이면 비정상이다. 
    @when_all((m.설치 == '함체') & (m.LED1 == '빨간불') & (m.LED2 == '빨간불'))
    def 결과3(c):
        c.assert_fact({'순번' : c.m.순번, '함체순번' : c.m.함체, '결과' : '비정상'})
        print('작동 전 체크 메뉴얼 : {0}'.format(c.m.순번))

    # 4. 함체는 소리가 비프음이면 정상이다. 
    @when_all((m.설치 == '함체') & (m.소리 == '비프음'))
    def 결과4(c):
        c.assert_fact({'순번' : c.m.순번, '함체순번' : c.m.함체, '결과' : '정상'})
        print('작동 전 체크 메뉴얼 : {0}'.format(c.m.순번))

    # 5. 함체는 소리가 무음이면 비정상이다. 
    @when_all((m.설치 == '함체') & (m.소리 == '무음'))
    def 결과5(c):
        c.assert_fact({'순번' : c.m.순번, '함체순번' : c.m.함체, '결과' : '비정상'})
        print('작동 전 체크 메뉴얼 : {0}'.format(c.m.순번))

    # 6. PC프로그램은 LED가 초록불 + 초록불이면 정상이다. 
    @when_all((m.설치 == 'PC프로그램') & (m.LED1 == '초록불') & (m.LED2 == '초록불'))
    def 결과6(c):
        c.assert_fact({'순번' : c.m.순번, '함체순번' : c.m.함체, '결과' : '정상'})
        print('작동 전 체크 메뉴얼 : {0}'.format(c.m.순번))

    # 7. PC프로그램은 LED가 초록불 + 빨간불이면 비정상이다. 
    @when_all((m.설치 == 'PC프로그램') & (m.LED1 == '빨간불') & (m.LED2 == '초록불'))
    def 결과7(c):
        c.assert_fact({'순번' : c.m.순번, '함체순번' : c.m.함체, '결과' : '비정상'})
        print('작동 전 체크 메뉴얼 : {0}'.format(c.m.순번))

    # 8. PC프로그램은 LED가 빨간불 + 빨간불이면 비정상이다. 
    @when_all((m.설치 == 'PC프로그램') & (m.LED1 == '빨간불') & (m.LED2 == '빨간불'))
    def 결과8(c):
        c.assert_fact({'순번' : c.m.순번, '함체순번' : c.m.함체, '결과' : '비정상'})
        print('작동 전 체크 메뉴얼 : {0}'.format(c.m.순번))

    # 9. 지문인식기는 지문이 등록되어있으면 정상이다. 
    @when_all((m.설치 == '지문인식기') & (m.지문 == '등록'))
    def 결과9(c):
        c.assert_fact({'순번' : c.m.순번, '함체순번' : c.m.함체, '결과' : '정상'})
        print('작동 전 체크 메뉴얼 : {0}'.format(c.m.순번))

    # 10. 지문인식기는 지문이 미등록되어있으면 비정상이다. 
    @when_all((m.설치 == '지문인식기') & (m.지문 == '미등록'))
    def 결과10(c):
        c.assert_fact({'순번' : c.m.순번, '함체순번' : c.m.함체, '결과' : '비정상'})
        print('작동 전 체크 메뉴얼 : {0}'.format(c.m.순번))

    # 11. RFID는 태그가 등록되어있으면 정상이다. 
    @when_all((m.설치 == 'RFID') & (m.태그 == '등록'))
    def 결과11(c):
        c.assert_fact({'순번' : c.m.순번, '함체순번' : c.m.함체, '결과' : '정상'})
        print('작동 전 체크 메뉴얼 : {0}'.format(c.m.순번))

    # 12. RFID는 태그이 미등록되어있으면 비정상이다. 
    @when_all((m.설치 == 'RFID') & (m.태그 == '미등록'))
    def 결과12(c):
        c.assert_fact({'순번' : c.m.순번, '함체순번' : c.m.함체, '결과' : '비정상'})
        print('작동 전 체크 메뉴얼 : {0}'.format(c.m.순번))

    # 13. 최종은 지문과 RFID가 둘 다 등록되어 있으면 정상이다. 
    @when_all((m.설치 == '최종') & (m.지문 == '등록') & (m.태그 == '등록'))
    def 결과13(c):
        c.assert_fact({'순번' : c.m.순번, '함체순번' : c.m.함체, '결과' : '정상'})
        print('작동 전 체크 메뉴얼 : {0}'.format(c.m.순번))

    # 14. 최종은 지문과 RFID가 둘 다 등록되어 있는데 매칭이 가능하면 정상이다.
    @when_all((m.설치 == '최종') & (m.지문 == '등록') & (m.태그 == '등록') & (m.매칭 == '가능'))
    def 결과14(c):
        c.assert_fact({'순번' : c.m.순번, '함체순번' : c.m.함체, '결과' : '정상'})
        print('작동 전 체크 메뉴얼 : {0}'.format(c.m.순번))

    # 15. 최종은 지문과 RFID가 둘 다 등록되어 있는데 매칭이 안되면 비정상이다.
    @when_all((m.설치 == '최종') & (m.지문 == '등록') & (m.태그 == '등록') & (m.매칭 == '불가능'))
    def 결과15(c):
        c.assert_fact({'순번' : c.m.순번, '함체순번' : c.m.함체, '결과' : '비정상'})
        print('작동 전 체크 메뉴얼 : {0}'.format(c.m.순번))


    # 결과 출력
    @when_all(m.작동여부 == '정상')
    def 결과출력1(c):
        print('순번 : {0} , 설치 : {1} , 작동여부 : 정상\n'.format(c.m.순번, c.m.함체순번))

    @when_all(m.작동여부 == '비정상')
    def 결과출력2(c):
        print('순번 : {0} , 설치 : {1} , 작동여부 : 비정상\n'.format(c.m.순번, c.m.함체순번))




#FACT

#함체
assert_fact('간이무기고', {'순번' : '1', '설치' : '함체', 'LED1' : '초록불', 'LED2' : '초록불'})
assert_fact('간이무기고', {'순번' : '2', '설치' : '함체', 'LED1' : '빨간불', 'LED2' : '초록불'})
assert_fact('간이무기고', {'순번' : '3', '설치' : '함체', 'LED1' : '빨간불', 'LED2' : '빨간불'})
assert_fact('간이무기고', {'순번' : '4', '설치' : '함체', '소리' : '비프음'})
assert_fact('간이무기고', {'순번' : '5', '설치' : '함체', '소리' : '무음'})

#PC프로그램
assert_fact('간이무기고', {'순번' : '6', '설치' : 'PC프로그램', 'LED1' : '초록불', 'LED2' : '초록불'})
assert_fact('간이무기고', {'순번' : '7', '설치' : 'PC프로그램', 'LED1' : '빨간불', 'LED2' : '초록불'})
assert_fact('간이무기고', {'순번' : '8', '설치' : 'PC프로그램', 'LED1' : '빨간불', 'LED2' : '초록불'})

#지문인식기
assert_fact('간이무기고', {'순번' : '9', '설치' : '지문인식기', '지문' : '등록'})
assert_fact('간이무기고', {'순번' : '10', '설치' : '지문인식기', '지문' : '미등록'})

#RFID
assert_fact('간이무기고', {'순번' : '11', '설치' : 'RFID', '태그' : '등록'})
assert_fact('간이무기고', {'순번' : '12', '설치' : 'RFID', '태그' : '미등록'})

#최종
assert_fact('간이무기고', {'순번' : '13', '설치' : '최종', '지문' : '등록', '태그' : '등록'})
assert_fact('간이무기고', {'순번' : '14', '설치' : '최종', '지문' : '등록', '태그' : '등록', '매칭' : '가능'})
assert_fact('간이무기고', {'순번' : '15', '설치' : '최종', '지문' : '등록', '태그' : '등록', '매칭' : '불가능'})