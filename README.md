# real_estate_in_seoul

실거래가 조회하기 위한 파이썬 유틸리티 모아둠

# Quick Start

- Install package

  ```
  % git clone https://github.com/byung-u/real_estate_in_seoul
  % python3 setup.py build
  % python3 setup.py install
  ```

- Run

  - 3달치 아파트 매매가 확인 (def: 마포구 대흥동 자이)

    `% real_estate_in_seoul -m 3`

  - 원하는 '구' 정보로 아파트 정보 확인

    `% real_estate_in_seoul -g 서초구`

- Options

  - g : xx구(서초구, 마포구, 강북구, ... )
  - d : xx동(서초동, 공덕동, 우이동, ... )
  - t : 아파트(자이, SK리더스뷰, 레미안, ... )
  - m : 조회 주기 (월 단위)

    ```
      만약 오늘이 201702 이고 -m 3 옵션을 주면
      201702 201701 201612 3달치를 조회하게 됨
      max: 36 month 제한 (일단은 limit을 둠)
    ```
