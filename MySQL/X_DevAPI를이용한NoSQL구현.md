# Why MySQL X-DevAPI??
- 클라우드와 빅데이터의 시대 -> 비정형 데이터를 이용
- RDBMS와 NoSQL을 동시에 사용하는 경우
  - 개발의 어려움
  - 백업과 복구를 각각 관리
  - Maintenance Burden이 두배
  - 데이터가 나누어져 있어 서버 어플리케이션 Source가 복잡, Join이 불가능하여 Data Mapping 및 동시성 처리가 어려움

- 데이터 sharding의 목적이아닌 Document 저장의 목적이라면 Document Store Database(예를 들면 MongoDB, CouchDB)를 따로 운영하지 않아도 된다는 큰 장점이있다.
  - 내부적으로 저장소는 InnoDB를 사용함으로, ACID를 포함한 Transaction을 모두 지원한다.
  - 백업/복귀의 경우 기존의 방법을 통해 진행될 수 있다.
  - 전통적 방식의 Mysql client tool 혹은 JDBC방식으로 데이터 조회 및 조작이 가능하다.
- SQL보다는 제공되는 API호출에 익숙하며, JSON형태의 데이터를 잘 다루는 개발자들에게 더욱 쉬운 개발환경을 제공한다.