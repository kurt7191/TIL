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



DAY2 SQL 문 CREATE TABLE 및 INSERT



```mysql
CREATE TABLE 스팀계정(
  계정ID VARCHAR(20) NOT NULL,
  계정PW VARCHAR(20) NOT NULL,
  계정닉네임 VARCHAR(20) NOT NULL,
  계정생성일 DATE,
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
  게임머니일련번호 INT,
  결제방식 VARCHAR(10) NOT NULL,
  결제일자 DATE,
  FOREIGN KEY(계정ID) REFERENCES 스팀계정(계정ID), 
  FOREIGN KEY(게임머니일련번호) REFERENCES 게임머니(게임머니일련번호)
  );
  
        CREATE TABLE 업적(
        업적일련번호 INT NOT NULL,
        랭크명 VARCHAR(10),
        PRIMARY KEY(업적일련번호)
        );
        

   
  CREATE TABLE 게임유저(
    계정ID VARCHAR(20) NOT NULL,
    유저일련번호 INT NOT NULL,
    유저닉네임 VARCHAR(10) NOT NULL,
    유료아이템장착여부 CHAR(1),
    시즌이름 VARCHAR(10) NOT NULL,
    업적일련번호 INT NOT NULL,
    
    PRIMARY KEY(유저일련번호),
    FOREIGN KEY(계정ID) REFERENCES 스팀계정(계정ID),
    FOREIGN KEY(업적일련번호) REFERENCES 업적(업적일련번호), 
    CHECK (유료아이템장착여부 = 'Y' or 유료아이템장착여부 = 'N'),
    UNIQUE KEY uk_name (계정ID)
    );
    
      
      
      CREATE TABLE 유료아이템유형(
        유료아이템타입 VARCHAR(20) NOT NULL,
        PRIMARY KEY(유료아이템타입)
    );


CREATE TABLE 유료아이템(
  유료아이템일련번호 INT NOT NULL,
  유료아이템타입 VARCHAR(20) NOT NULL,
  아이템이름 VARCHAR(20) NOT NULL,
  아이템가격 INT NOT NULL,
  PRIMARY KEY(유료아이템일련번호),
  FOREIGN KEY(유료아이템타입) REFERENCES 유료아이템유형(유료아이템타입)
  );
  

  
  CREATE TABLE 유료아이템결제(
    유료아이템일련번호 INT NOT NULL,
    유저일련번호 INT NOT NULL,
    구매일련번호 INT NOT NULL,
    결제금액 INT NOT NULL,
    PRIMARY KEY(구매일련번호),
    FOREIGN KEY(유저일련번호) REFERENCES 게임유저(유저일련번호),
    FOREIGN KEY(유료아이템일련번호) REFERENCES 유료아이템(유료아이템일련번호)
    );
    
    
CREATE TABLE 맵(
  맵이름 VARCHAR(10) NOT NULL,
  맵크기 VARCHAR(20) NOT NULL,
  PRIMARY KEY(맵이름)
  );
  
  
  CREATE TABLE 아이템(
    아이템일련번호 INT NOT NULL,
    아이템명 VARCHAR(20) NOT NULL,
    아이템유형 VARCHAR(20) NOT NULL,
    PRIMARY KEY(아이템일련번호)
    );

CREATE TABLE 탈것(
  탈것일련번호 INT NOT NULL,
  탈것명 VARCHAR(30) NOT NULL,
  탈것유형 VARCHAR(10) NOT NULL,
  PRIMARY KEY(탈것일련번호)
  );
  
  CREATE TABLE 총기(
    총기일련번호 INT NOT NULL,
    총기명 VARCHAR(10),
    총기유형 VARCHAR(10),
    PRIMARY KEY(총기일련번호)
    );

      

         


         
                    CREATE TABLE 게임플레이(
                        플레이일련번호 INT NOT NULL,
                        유저일련번호 INT NOT NULL,
                        맵이름 VARCHAR(10) NOT NULL,
                        플레이날짜 DATE,
                        플레이우승여부 BOOLEAN,
                        PRIMARY KEY(플레이일련번호),
                        FOREIGN KEY(유저일련번호) REFERENCES 게임유저(유저일련번호),
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
               
               
               INSERT INTO 스팀계정 VALUES ('steam_account1','1234','DAY','2021-12-10', 'KOREA', 0);

INSERT INTO 스팀계정 VALUES ('steam_account2','1234','LONDON','2021-01-05', 'JAPAN', 0);

INSERT INTO 스팀계정 VALUES ('steam_account3','1234','GODKOONG','2021-07-25', 'CHINA', 0);

INSERT INTO 스팀계정 VALUES ('steam_account4','wkddmswns1!','MAN LOVES BTG','2021-06-11', 'KOREA', 50000);


INSERT INTO 스팀계정 VALUES ('steam_account5','1234','HOLYMOLY','2021-06-12', 'KOREA', 50000);

INSERT INTO 업적 VALUES
(6660, 'UNTITLE');
INSERT INTO 업적 VALUES
(6666, 'BRONZE');
INSERT INTO 업적 VALUES
(6665, 'SILVER');
INSERT INTO 업적 VALUES
(6664, 'GOLD');
INSERT INTO 업적 VALUES
(6663, 'PLETINUM');
INSERT INTO 업적 VALUES
(6662, 'DIAMOND');
INSERT INTO 업적 VALUES
(6661, 'MASTER');



INSERT INTO 게임유저 VALUES ('steam_account1',3323,'GOGO','N','SEASON15',6664);
INSERT INTO 게임유저 VALUES ('steam_account2',3221,'GOGOPECADO','N','SEASON15',6664);
INSERT INTO 게임유저 VALUES ('steam_account3',3222,'GEN_MOM','N','SEASON15',6664);
INSERT INTO 게임유저 VALUES ('steam_account4',3552,'NEWHAPPY','N','SEASON15',6664);
INSERT INTO 게임유저 VALUES ('steam_account5',3434,'VIRTUS PRO','N','SEASON15',6664);


INSERT INTO 게임머니 VALUES
(1234,5000);
INSERT INTO 게임머니 VALUES
(1235,10000);
INSERT INTO 게임머니 VALUES
(1236,50000);
INSERT INTO 게임머니 VALUES
(1237,100000);

INSERT INTO 게임머니충전 VALUES
(1111,'steam_account4', 1236, 'card','2021-12-10');

INSERT INTO 게임머니충전 VALUES
(1112,'steam_account5', 1236, 'card','2021-12-05');

INSERT INTO 유료아이템유형 VALUES
('CLOTHES');

INSERT INTO 유료아이템유형 VALUES
('DANCE');

INSERT INTO 유료아이템유형 VALUES
('VEHICLE');

INSERT INTO 유료아이템유형 VALUES
('ACC');

INSERT INTO 유료아이템유형 VALUES
('FACE');

INSERT INTO 유료아이템유형 VALUES
('GUN');

INSERT INTO 유료아이템 VALUES
(123456, 'CLOTHES','KAKAO_LION',15000);


INSERT INTO 유료아이템 VALUES
(123440, 'CLOTHES','PGC_CLOTHES',50000);

INSERT INTO 유료아이템 VALUES
(123434, 'FACE','PGC_MASK',3000);

INSERT INTO 유료아이템 VALUES
(123435, 'FACE','SUMMER_SUNGLASS',3000);

INSERT INTO 유료아이템 VALUES
(123436, 'ACC','NECK_TATOO',5000);


INSERT INTO 유료아이템 VALUES
(123000, 'GUN','BERYL_CONTRABAND',100000);

INSERT INTO 유료아이템 VALUES
(123123, 'GUN','SLR_CONTRABAND',100000);

INSERT INTO 유료아이템 VALUES
(122222, 'GUN','M4A1_CONTRABAND',100000);

INSERT INTO 유료아이템 VALUES
(122200, 'VEHICLE','PGC_RETONA',5000);

INSERT INTO 유료아이템 VALUES
(122201, 'VEHICLE','PGC_DACIA',5000);


INSERT INTO 유료아이템결제 VALUES
(122200, 3552, 55555,5000); 

INSERT INTO 유료아이템결제 VALUES
(123456, 3434, 55556,15000); 

INSERT INTO 맵 VALUES
('SANHOK','4 X 4 KM');

INSERT INTO 맵 VALUES
('Erangel','8 X 8 KM');

INSERT INTO 맵 VALUES
('Miramar','8 X 8 KM');


INSERT INTO 맵 VALUES
('Karakin','4 X 4 KM');

INSERT INTO 맵 VALUES
('Vikendi','8 X 8 KM');

INSERT INTO 아이템 VALUES(
  9999, 'painkiller', 'RECOVERY');
INSERT INTO 아이템 VALUES(
  9998, 'energy_drink', 'RECOVERY');
INSERT INTO 아이템 VALUES(
  9997, 'first_aid_kid', 'RECOVERY');
  
  INSERT INTO 아이템 VALUES(
  9899, 'grenade', 'THROW_TYPE');

  INSERT INTO 아이템 VALUES(
  9898, 'smoke_shell', 'THROW_TYPE');
  
    INSERT INTO 아이템 VALUES(
  9897, 'flash_bomb', 'THROW_TYPE');
  
      INSERT INTO 아이템 VALUES(
  9896, 'Molotov', 'THROW_TYPE');
  
        INSERT INTO 아이템 VALUES(
  9799, '5.56mm', 'Bullet_type');

        INSERT INTO 아이템 VALUES(
  9798, '7.62mm', 'Bullet_type');
  
          INSERT INTO 아이템 VALUES(
  9797, '9mm', 'Bullet_type');
  
            INSERT INTO 아이템 VALUES(
  9796, '45acp', 'Bullet_type');

            INSERT INTO 아이템 VALUES(
  9795, '45acp', 'Bullet_type');
  
  INSERT INTO 아이템 VALUES(
  9699, 'POLICE_VEST', 'armor_type');

  INSERT INTO 아이템 VALUES(
  9698, 'ARMY_VEST', 'armor_type');
  
  
    INSERT INTO 아이템 VALUES(
  9697, 'NORMAL_VEST', 'armor_type');


    INSERT INTO 아이템 VALUES(
  9696, 'BICYCLE_HEAD', 'armor_type');

    INSERT INTO 아이템 VALUES(
  9695, 'ARMY_HEAD', 'armor_type');

    INSERT INTO 아이템 VALUES(
  9694, '3LV_HEAD', 'armor_type');
  
  INSERT INTO 탈것 VALUES(
    7777,'RETONA','CAR');
    
  INSERT INTO 탈것 VALUES(
    7776, 'DACIA', 'CAR');
    
  INSERT INTO 탈것 VALUES(
    7677, 'TWO_WHEELED_MOTOCYCLE', 'MOTO');
    
    INSERT INTO 탈것 VALUES(
      7676, 'THREE_WHEELED_MOTOCYCLE', 'MOTO');

    INSERT INTO 탈것 VALUES(
      7577, 'AIR_PLANE_1', 'AIR_PLANE');
      
      
      INSERT INTO 총기 VALUES(
        8888, 'M4A1','AR');
      INSERT INTO 총기 VALUES(
        8887, 'AK','AR');        
      INSERT INTO 총기 VALUES(
        8886, 'BERYL','AR');        
      INSERT INTO 총기 VALUES(
        8788, 'MINI','DMR');        
      INSERT INTO 총기 VALUES(
        8787, 'SLR','DMR');
        
        
        INSERT INTO 게임플레이 VALUES(
          1234567,
          3221,
          'SANHOK',
          '2021-12-10',
          0);
          
        INSERT INTO 게임플레이 VALUES(
          1234568,
          3221,
          'ERANGEL',
          '2021-12-10',
          0);          
          
      SELECT * FROM 스팀계정;
SELECT * FROM 게임유저;
SELECT * FROM 게임머니;
SELECT * FROM 게임머니충전;
SELECT * FROM 유료아이템;
SELECT * FROM 유료아이템결제;
SELECT * FROM 업적;
SELECT * FROM 맵;
SELECT * FROM 아이템;
SELECT * FROM 탈것;
SELECT * FROM 총기;    
          
          
          
        

    
    
  
  







  
  
  










               
               
               
               
               
             
           
          
           

             
             
             
             
        
      
      
  
  
```

