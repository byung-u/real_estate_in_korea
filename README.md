# real_estate_in_korea

실거래 매매/전세 가격 조회하기 위한 파이썬 유틸리티

# Quick Start

- Requirements

  - [아파트 실거래자료 openapi 키 신청](https://www.data.go.kr/subMain.jsp?param=T1BFTkFQSUAzMDUwOTg4#/L3B1YnIvdXNlL3ByaS9Jcm9zT3BlbkFwaURldGFpbC9vcGVuQXBpTGlzdFBhZ2UkQF4wMTJtMSRAXnB1YmxpY0RhdGFQaz0zMDUwOTg4JEBeYnJtQ2Q9T0MwMDAzJEBecmVxdWVzdENvdW50PTI0MDYkQF5vcmdJbmRleD1PUEVOQVBJ)

- Install package

  ```
  % git clone https://github.com/byung-u/real_estate_in_korea
  % python3 setup.py build
  % python3 setup.py install
  ```

- Run

  - 3달치 아파트 매매가 확인 (def: 마포구 대흥동 자이)

    ```
    % real_estate_in_korea -m 3

    전세가 조회인 경우 뒤에 --rent 추가 이하 동일
    % real_estate_in_korea -m 3 --rent
    ```

  - 원하는 '구' 정보로 아파트 정보 확인

    ```
    % real_estate_in_korea -g 서초구
    ```

  - 알고자하는 그 아파트를 검색

    ```
    % real_estate_in_korea -g 중구 -d 황학동 -t 황학 -m 6
    % real_estate_in_korea -g 서대문구 -d 북가좌동 -t 한양 -m 60
    ```

- Options

  - g : xx구(서초구, 마포구, 강북구, ... )
  - d : xx동(서초동, 공덕동, 우이동, ... )
  - t : 아파트(자이, SK리더스뷰, 레미안, ... )
  - m : 조회 주기 (월 단위)
  - --rent : 전세가 조회 (명령어에 없으면 default로 매매가 조회)

    ```
      만약 오늘이 201702 이고 -m 3 옵션을 주면
      201702 201701 201612 3달치를 조회하게 됨
      max: 36 month 제한 (일단은 limit을 둠)
    ```
