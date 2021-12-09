# 데이터베이스구주와운용 - PROJECT SQL문





### 엔티티생성 MYSQL



```mysql
CREATE TABLE 스팀계정(
  계정ID VARCHAR(20) NOT NULL,
  계정PW INT NOT NULL,
  게정닉네임 VARCHAR(10) NOT NULL,
  계정생성일 DATE NOT NULL,
  국가 VARCHAR(20),
  게임머니잔액 INT NOT NULL,
  PRIMARY KEY(계정ID)
  );
  
  CREATE TABLE 게임머니(
    게임머니일련번호 INT NOT NULL,
    게임머니종류 INT NOT NULL,
    PRIMARY KEY(게임머니일련번호),
    CHECK (게임머니종류 = 5000 or 게임머니종류 = 10000 or 게임머니종류= 20000)
    );
    
    
CREATE TABLE 게임머니충전(
  결제일련번호 INT NOT NULL,
  계정ID VARCHAR(20) NOT NULL,
  게임머니일련번호 INT NOT NULL,
  결제방식 VARCHAR(10) NOT NULL,
  결제일자 DATE NOT NULL,
  FOREIGN KEY(계정ID) REFERENCES 스팀계정(계정ID), 
  FOREIGN KEY(게임머니일련번호) REFERENCES 게임머니(게임머니일련번호)
  );
   
  CREATE TABLE 게임유저(
    계정ID VARCHAR(20) NOT NULL,
    유저일련번호 INT NOT NULL,
    유저닉네임 VARCHAR(10) NOT NULL,
    유료아이템장착여부 CHAR(1),
    PRIMARY KEY(유저일련번호),
    FOREIGN KEY(계정ID) REFERENCES 스팀계정(계정ID),
    CHECK (유료아이템장착여부 = 'Y' or 유료아이템장착여부 = 'N')
    );


CREATE TABLE 유료아이템(
  유료아이템일련번호 INT NOT NULL,
  아이템종류 VARCHAR(10) NOT NULL,
  아이템이름 VARCHAR(10) NOT NULL,
  아이템가격 INT NOT NULL,
  PRIMARY KEY(유료아이템일련번호)
  );
  
  CREATE TABLE 유료아이템결제(
    유료아이템일련번호 INT NOT NULL,
    유저일련번호 INT NOT NULL,
    구매일련번호 INT NOT NULL,
    PRIMARY KEY(구매일련번호),
    FOREIGN KEY(유저일련번호) REFERENCES 게임유저(유저일련번호),
    FOREIGN KEY(유료아이템일련번호) REFERENCES 유료아이템(유료아이템일련번호)
    );
    
    
CREATE TABLE 맵(
  맵이름 VARCHAR(10) NOT NULL,
  맵크기 VARCHAR(20) NOT NULL,
  맵날씨상태 CHAR(2) NOT NULL,
  맵랜드마크 VARCHAR(20) NOT NULL,
  PRIMARY KEY(맵이름)
  );
  
CREATE TABLE 낙하산(
  낙하산번호 INT NOT NULL,
  낙하산위치 FLOAT(24) NOT NULL,
  착륙지점 FLOAT(24) NOT NULL,
  PRIMARY KEY(낙하산번호)
  );
  
  CREATE TABLE 아이템(
    아이템일련번호 INT NOT NULL,
    아이템명 VARCHAR(10) NOT NULL,
    아이템유형 VARCHAR(10) NOT NULL,
    PRIMARY KEY(아이템일련번호)
    );

CREATE TABLE 탈것(
  탈것일련번호 INT NOT NULL,
  탈것명 VARCHAR(10) NOT NULL,
  탈것유형 VARCHAR(10) NOT NULL,
  PRIMARY KEY(탈것일련번호)
  );
  
  CREATE TABLE 총기(
    총기일련번호 INT NOT NULL,
    총기명 VARCHAR(10),
    총기유형 VARCHAR(10),
    PRIMARY KEY(총기일련번호)
    );
    
    CREATE TABLE 보상(
      보상일련번호 INT NOT NULL,
      보상내용 VARCHAR(20),
      보상일자 DATE,
      PRIMARY KEY(보상일련번호)
      );
      
      CREATE TABLE 업적(
        업적일련번호 INT NOT NULL,
        랭크명 VARCHAR(10),
        PRIMARY KEY(업적일련번호)
        );
        
        
       CREATE TABLE 시즌(
         시즌이름 VARCHAR(10) NOT NULL,
         보상일련번호 INT NOT NULL,
         업적일련번호 INT NOT NULL,
         PRIMARY KEY(시즌이름),
         FOREIGN KEY(보상일련번호) REFERENCES 보상(보상일련번호),
         FOREIGN KEY(업적일련번호) REFERENCES 업적(업적일련번호)
         );
         
                    CREATE TABLE 게임플레이(
                        플레이일련번호 INT NOT NULL,
                        유저일련번호 INT NOT NULL,
                        시즌이름 VARCHAR(10) NOT NULL,
                        맵이름 VARCHAR(10) NOT NULL,
                        플레이날짜 DATE,
                        플레이우승여부 BOOLEAN,
                        PRIMARY KEY(플레이일련번호),
                        FOREIGN KEY(유저일련번호) REFERENCES 게임유저(유저일련번호),
                      FOREIGN KEY(시즌이름) REFERENCES 시즌(시즌이름),
                      FOREIGN KEY(맵이름) REFERENCES 맵(맵이름)
                      );
                      
                      
                      
                   

         
         
         
         CREATE TABLE 총기사용상세내역(
           총기사용일련번호 INT NOT NULL,
           플레이일련번호 INT NOT NULL,
           총기일련번호 INT NOT NULL,
           총기사용횟수 INT NOT NULL,
           총기유효데미지 INT NOT NULL,
           총기사용KILL수 INT NOT NULL,
           총기사용기절횟수 INT NOT NULL,
          
           FOREIGN KEY(플레이일련번호) REFERENCES 게임플레이(플레이일련번호),
           FOREIGN KEY(총기일련번호) REFERENCES 총기(총기일련번호),           
           PRIMARY KEY(총기사용일련번호)
           );
           
           CREATE TABLE 아이템사용상세내역(
             아이템사용일련번호 INT NOT NULL,
             플레이일련번호 INT NOT NULL,
             아이템일련번호 INT NOT NULL,
             아이템사용시간 DATE,
             아이템사용횟수 INT NOT NULL,
             PRIMARY KEY(아이템사용일련번호),
             FOREIGN KEY(플레이일련번호) REFERENCES 게임플레이(플레이일련번호),
             FOREIGN KEY(아이템일련번호) REFERENCES 아이템(아이템일련번호)
             );
             
             
             CREATE TABLE 탈것사용상세내용(
               탈것사용일련번호 INT NOT NULL,
               플레이일련번호 INT NOT NULL,
               탈것일련번호 INT NOT NULL,
               운행경로 FLOAT(24),
               운행시간 DATE,
               플레이어승차시간 DATE,
               PRIMARY KEY(탈것사용일련번호),
               FOREIGN KEY(플레이일련번호) REFERENCES 게임플레이(플레이일련번호),
               FOREIGN KEY(탈것일련번호) REFERENCES 탈것(탈것일련번호)
               );
               
               
               
               
               
               
               
               
               
               
             
           
          
           

             
             
             
             
        
      
    
```

