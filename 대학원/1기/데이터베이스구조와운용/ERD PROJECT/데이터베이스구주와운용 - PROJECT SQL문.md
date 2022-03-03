# 데이터베이스구주와운용 - PROJECT SQL문





### 엔티티생성 MYSQL





```mysql
CREATE TABLE 스팀계정(
  계정ID VARCHAR(20) NOT NULL,
  계정PW VARCHAR(20) NOT NULL,
  계정닉네임 VARCHAR(20) NOT NULL,
  계정생성일 DATE,국가 VARCHAR(20),
  게임머니잔액 INT NOT NULL,PRIMARY KEY(계정ID)
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
  운행시간 INT,
  플레이어승차시간 DATE,
  차량훼손여부 BOOLEAN,
  PRIMARY KEY(탈것사용일련번호),
  FOREIGN KEY(플레이일련번호) REFERENCES 게임플레이(플레이일련번호),
  FOREIGN KEY(탈것일련번호) REFERENCES 탈것(탈것일련번호)
);


INSERT INTO 스팀계정 VALUES ('steam_account1','1234','DAY','2021-12-10', 'KOREA', 0);
INSERT INTO 스팀계정 VALUES ('steam_account2','1234','LONDON','2021-01-05', 'JAPAN', 0);
INSERT INTO 스팀계정 VALUES ('steam_account3','1234','GODKOONG','2021-07-25', 'CHINA', 0);
INSERT INTO 스팀계정 VALUES ('steam_account4','wkddmswns1!','MAN LOVES BTG','2021-06-11', 'KOREA', 50000);
INSERT INTO 스팀계정 VALUES ('steam_account5','1234','HOLYMOLY','2021-06-12', 'KOREA', 50000);

INSERT INTO 업적 VALUES(6660, 'UNTITLE');
INSERT INTO 업적 VALUES(6666, 'BRONZE');
INSERT INTO 업적 VALUES(6665, 'SILVER');
INSERT INTO 업적 VALUES(6664, 'GOLD');
INSERT INTO 업적 VALUES(6663, 'PLETINUM');
INSERT INTO 업적 VALUES(6662, 'DIAMOND');
INSERT INTO 업적 VALUES(6661, 'MASTER');

INSERT INTO 게임유저 VALUES ('steam_account1',3323,'GOGO','N','SEASON15',6664);
INSERT INTO 게임유저 VALUES ('steam_account2',3221,'GOGOPECADO','N','SEASON15',6664);

INSERT INTO 게임유저 VALUES ('steam_account3',3222,'GEN_MOM','N','SEASON15',6664);

INSERT INTO 게임유저 VALUES ('steam_account4',3552,'NEWHAPPY','N','SEASON15',6664);

INSERT INTO 게임유저 VALUES ('steam_account5',3434,'VIRTUS PRO','N','SEASON15',6664);

INSERT INTO 게임머니 VALUES(1234,5000);
INSERT INTO 게임머니 VALUES(1235,10000);
INSERT INTO 게임머니 VALUES(1236,50000);
INSERT INTO 게임머니 VALUES(1237,100000);

INSERT INTO 게임머니충전 VALUES(1111,'steam_account4', 1236, 'card','2021-12-10');
INSERT INTO 게임머니충전 VALUES(1112,'steam_account5', 1236, 'card','2021-12-05');

INSERT INTO 유료아이템유형 VALUES('CLOTHES');
INSERT INTO 유료아이템유형 VALUES('DANCE');
INSERT INTO 유료아이템유형 VALUES('FACE');
INSERT INTO 유료아이템유형 VALUES('ACC');
INSERT INTO 유료아이템유형 VALUES('VEHICLE');
INSERT INTO 유료아이템유형 VALUES('GUN');

INSERT INTO 유료아이템 VALUES (123000, 'GUN','BERYL_CONTRABAND',100000);
INSERT INTO 유료아이템 VALUES(123456, 'CLOTHES','KAKAO_LION',15000);
INSERT INTO 유료아이템 VALUES(123440, 'CLOTHES','PGC_CLOTHES',50000);
INSERT INTO 유료아이템 VALUES(123434, 'FACE','PGC_MASK',3000);
INSERT INTO 유료아이템 VALUES(123435, 'FACE','SUMMER_SUNGLASS',3000);
INSERT INTO 유료아이템 VALUES(123436, 'ACC','NECK_TATOO',5000);
INSERT INTO 유료아이템 VALUES(123123, 'GUN','SLR_CONTRABAND',100000);
INSERT INTO 유료아이템 VALUES(122222, 'GUN','M4A1_CONTRABAND',100000);
INSERT INTO 유료아이템 VALUES(122200, 'VEHICLE','PGC_RETONA',5000);
INSERT INTO 유료아이템 VALUES(122201, 'VEHICLE','PGC_DACIA',5000);

INSERT INTO 유료아이템결제 VALUES(122200, 3552, 55555,5000);
INSERT INTO 유료아이템결제 VALUES(123456, 3434, 55556,15000); 
INSERT INTO 유료아이템결제 VALUES(122222, 3552, 55550,100000);
INSERT INTO 유료아이템결제 VALUES(122222, 3221, 55557,100000); 
INSERT INTO 유료아이템결제 VALUES(123440, 3552, 55558,50000); 
INSERT INTO 유료아이템결제 VALUES(123440, 3434, 55559,50000); 
INSERT INTO 유료아이템결제 VALUES(123434, 3434, 55560,3000); 
INSERT INTO 유료아이템결제 VALUES(123436, 3222, 55561,5000); 
INSERT INTO 유료아이템결제 VALUES(123436, 3434, 55562,5000); 


INSERT INTO 맵 VALUES('SANHOK','4 X 4 KM');
INSERT INTO 맵 VALUES('Erangel','8 X 8 KM');
INSERT INTO 맵 VALUES('Miramar','8 X 8 KM');
INSERT INTO 맵 VALUES('Karakin','4 X 4 KM');
INSERT INTO 맵 VALUES('Vikendi','8 X 8 KM');

INSERT INTO 아이템 VALUES(9999, 'painkiller', 'RECOVERY');
INSERT INTO 아이템 VALUES(9998,'energy_drink', 'RECOVERY');
INSERT INTO 아이템 VALUES(9997, 'first_aid_kid', 'RECOVERY');
INSERT INTO 아이템 VALUES(9899, 'grenade', 'THROW_TYPE');
INSERT INTO 아이템 VALUES(9898, 'smoke_shell', 'THROW_TYPE');
INSERT INTO 아이템 VALUES(9897, 'flash_bomb', 'THROW_TYPE');
INSERT INTO 아이템 VALUES(9896, 'Molotov', 'THROW_TYPE'); 
INSERT INTO 아이템 VALUES(9799, '5.56mm', 'Bullet_type');
INSERT INTO 아이템 VALUES(9798,'7.62mm','Bullet_type');
INSERT INTO 아이템 VALUES(9797, '9mm', 'Bullet_type');
INSERT INTO 아이템 VALUES(9796, '45acp', 'Bullet_type');
INSERT INTO 아이템 VALUES(9795, '45acp', 'Bullet_type');
INSERT INTO 아이템 VALUES(9699, 'POLICE_VEST', 'armor_type');
INSERT INTO 아이템 VALUES(9698, 'ARMY_VEST', 'armor_type');
INSERT INTO 아이템 VALUES(9697, 'NORMAL_VEST', 'armor_type');
INSERT INTO 아이템 VALUES(9696, 'BICYCLE_HEAD', 'armor_type');
INSERT INTO 아이템 VALUES(9695, 'ARMY_HEAD', 'armor_type');
INSERT INTO 아이템 VALUES(9694, '3LV_HEAD', 'armor_type');

INSERT INTO 탈것 VALUES(7777,'RETONA','CAR');
INSERT INTO 탈것 VALUES(7776, 'DACIA', 'CAR');
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
          
                  INSERT INTO 게임플레이 VALUES(
          1234569,
          3221,
          'Miramar',
          '2021-12-13',
          0);       
                            INSERT INTO 게임플레이 VALUES(
          1234570,
          3221,
          'Karakin',
          '2021-12-13',
          1);     
                            INSERT INTO 게임플레이 VALUES(
          1234571,
          3221,
          'Vikendi',
          '2021-12-13',
          1);      
          
          
          INSERT INTO 아이템사용상세내역 VALUES(
            4321,
            1234567,
            9899,
            '2021-12-13',
            5                        
            );
            
            INSERT INTO 아이템사용상세내역 VALUES(
            4322,
            1234567,
            9998,
            '2021-12-13',
            3                        
            );
            
            INSERT INTO 아이템사용상세내역 VALUES(
            4323,
            1234567,
            9897,
            '2021-12-13',
            10                        
            );
            
                       INSERT INTO 아이템사용상세내역 VALUES(
            4324,
            1234569,
            9897,
            '2021-12-13',
            10                        
            );
            
                                   INSERT INTO 아이템사용상세내역 VALUES(
            4325,
            1234569,
            9998,
            '2021-12-13',
            7                        
            );
            
            
            INSERT INTO 탈것사용상세내용 VALUES(
              5432,
              1234567,
              7676,
              0.5,
              40,
              '2021-12-13',
              1
              );
              
                          INSERT INTO 탈것사용상세내용 VALUES(
              5433,
              1234567,
              7676,
              0.5,
              30,
              '2021-12-11',
              0
              );
              
           
                
                
                
              
              INSERT INTO 총기사용상세내역 VALUES(
                8765,
                1234567,
                8886,
                3,
                550,
                6,
                6
                );
                
                
                              INSERT INTO 총기사용상세내역 VALUES(
                8766,
                1234567,
                8887,
                1,
                0,
                0,
                0
                );
                
                   INSERT INTO 게임플레이 VALUES(
                1234572,
                3222,
                'Vikendi',
                '2021-12-14',
                1);
                
                                   INSERT INTO 게임플레이 VALUES(
                1234573,
                3222,
                'Miramar',
                '2021-11-05',
                0);
                
                                                   INSERT INTO 게임플레이 VALUES(
                1234574,
                3552,
                'ERANGEL',
                '2021-12-13',
                1);
                
                                                                   INSERT INTO 게임플레이 VALUES(
                1234575,
                3552,
                'ERANGEL',
                '2021-12-13',
                1);
                
                
                INSERT INTO 게임플레이 VALUES(
                  1234500,
                  3323,
                  'SANHOK',
                  '2020-12-25',
                  0);
                  
                                  INSERT INTO 게임플레이 VALUES(
                  1234501,
                  3323,
                  'Vikendi',
                  '2020-12-25',
                  1);
                  
                                                    INSERT INTO 게임플레이 VALUES(
                  1234531,
                  3434,
                  'ERANGEL',
                  '2021-07-31',
                  1);
                  
                  INSERT INTO 게임플레이 VALUES(
                  1234532,
                  3434,
                  'Miramar',
                  '2021-08-05',
                  1);
                  
                  INSERT INTO 게임머니충전 VALUES(
                    1113,
                    'steam_account4',
                    1235,
                    'card',
                    '2021-11-10'
                    );
                    
                                       

  
                                      INSERT INTO 게임머니충전 VALUES(
                    1100,
                    'steam_account2',
                    1235,
                    'card',
                    '2020-05-10'
                    );
                    
                                                        INSERT INTO 게임머니충전 VALUES(
                    1105,
                    'steam_account1',
                    1237,
                    'card',
                    '2020-07-22'
                    );
                    
                    INSERT INTO 게임플레이 VALUES(
                      1234222,
                      3323,
                      'Vikendi',
                      '2021-03-22',
                      0);
                                          INSERT INTO 게임플레이 VALUES(
                      1234212,
                      3323,
                      'Miramar',
                      '2021-02-22',
                      0);
                      
                                                                INSERT INTO 게임플레이 VALUES(
                      1234211,
                      3323,
                      'ERANGEL',
                      '2021-02-22',
                      0);
                      
                      
                                                                                      INSERT INTO 게임플레이 VALUES(
                      1234011,
                      3323,
                      'ERANGEL',
                      '2021-02-02',
                      0);
                      
                      
                       INSERT INTO 게임플레이 VALUES(
                  1233531,
                  3434,
                  'ERANGEL',
                  '2020-07-31',
                  0);
                  
                  INSERT INTO 게임플레이 VALUES(
                  1233530,
                  3434,
                  'ERANGEL',
                  '2020-06-05',
                  0);
                  
                                   INSERT INTO 게임플레이 VALUES(
                  1233520,
                  3434,
                  'ERANGEL',
                  '2020-08-11',
                  0);
                  
                  
                  
INSERT INTO 총기사용상세내역 VALUES(
  8764,
  1234011,
  8787,
  1,
  10,
  0,
  0);
  
  INSERT INTO 총기사용상세내역 VALUES(
  8763,
  1234211,
  8787,
  0,
  0,
  0,
  0);
  
  
    INSERT INTO 총기사용상세내역 VALUES(
  8762,
  1234212,
  8886,
  1,
  100,
  1,
  1);
  
      INSERT INTO 총기사용상세내역 VALUES(
  8761,
  1234222,
  8788,
  2,
  110,
  1,
  1);
  
        INSERT INTO 총기사용상세내역 VALUES(
  8760,
  1234500,
  8887,
  3,
  220,
  2,
  2);
  
  
         INSERT INTO 총기사용상세내역 VALUES(
  8759,
  1234501,
  8888,
  1,
  30,
  0,
  0);
  
         INSERT INTO 총기사용상세내역 VALUES(
  8758,
  1233520,
  8886,         
  0,
  0,
  0,
  0);
  
           INSERT INTO 총기사용상세내역 VALUES(
  8757,
  1233530,
  8887,         
  0,
  0,
  0,
  0);
  
  
             INSERT INTO 총기사용상세내역 VALUES(
  8756,
  1233531,
  8887,         
  3,
  44,
  0,
  0);
  
              INSERT INTO 총기사용상세내역 VALUES(
  8755,
  1234531,
  8787,         
  0,
  0,
  0,
  0);
  
                INSERT INTO 총기사용상세내역 VALUES(
  8754,
  1234532,
  8788,         
  5,
  450,
  6,
  4);
  
  
                    
                    
                    
                    
                    
                    
                    
                  
                  
```





# 비즈니스 SELECT  쿼리문



```mysql
-- 1. 유료 아이템 결제 부분 SELECT 쿼리문
-- 스팀계정별 결제 횟수 및 최근결제일 그리고 총 결제액

SELECT CHARGE.계정ID, COUNT(*) AS 결제수, MAX(결제일자) AS 최근결제일,
SUM(MONEY.게임머니종류) AS 총결제액
FROM 게임머니충전 CHARGE, 게임머니 MONEY
WHERE CHARGE.게임머니일련번호 = MONEY.게임머니일련번호
GROUP BY CHARGE.계정ID;

-- 최근 한달간 결제한 스팀 계정과 마지막 결제일자.

SELECT 계정ID, MAX(결제일자) AS 최근결제일자
FROM 게임머니충전
WHERE 결제일자 >= '2021-11-14'
GROUP  BY 계정ID;

-- 과거에 결제를 했지만 최근 한달간 결제를 하지 않은 스팀 계정

SELECT 계정ID
FROM 게임머니충전
WHERE 결제일자 < '2021-11-14'
AND 계정ID NOT IN (SELECT 계정ID 
                  FROM 게임머니충전 
                  WHERE 결제일자 >= '2021-11-14');



-- 2. 게임 플레이 부분 SELECT 쿼리문
-- 유저별 플레이 수 및 우승 횟수 및 우승 확률

SELECT 유저일련번호,COUNT(*) AS 플레이수 ,SUM(플레이우승여부) AS 우승수,
SUM(플레이우승여부)/COUNT(*) * 100 AS 평균플레이우승확률
FROM 게임플레이
GROUP BY 유저일련번호;

-- 맵 별 플레이 횟수 및 우승 횟수 그리고 게임유저들의 평균 우승 확률


SELECT 맵이름, COUNT(*) AS 플레이수, SUM(플레이우승여부) AS 우승수,
SUM(플레이우승여부) / COUNT(*) * 100 AS 평균플레이우승확률
FROM 게임플레이
GROUP BY 맵이름;

-- 최근 한달간 플레이 유저
# 3323,3434
SELECT 유저일련번호, COUNT(*) AS 플레이수, MAX(플레이날짜) AS 마지막플레이
FROM 게임플레이
WHERE 플레이날짜 > '2021-11-14'
GROUP BY 유저일련번호;


-- 한달 이상 휴면 유저의 마지막 플레이 날짜 및 지금까지 휴먼일
SELECT 유저일련번호, MAX(플레이날짜) AS 마지막플레이날짜, DATEDIFF(NOW(),MAX(플레이날짜)) AS 휴먼일
FROM 게임플레이
WHERE 플레이날짜 < '2021-11-14'
AND 유저일련번호 NOT IN (SELECT 유저일련번호 
                   FROM 게임플레이 WHERE 플레이날짜 >= '2021-11-14' )
                   GROUP BY 유저일련번호;
                   
                   

-- 3. 본격 조인 데이터 베이스
-- 최근 한달간 플레이 하지 않은 유저들의 게임 플레이 및 우승횟수
-- 승률이 낮게끔 설정
-- 게임플레이, 게임유저

SELECT GP.유저일련번호, GU.유저닉네임,COUNT(*) AS 플레이수, SUM(플레이우승여부) AS 게임우승횟수, SUM(플레이우승여부) /COUNT(*) * 100 AS 승률
FROM 게임플레이 GP, 게임유저 GU
WHERE GP.플레이날짜 < '2021-11-14'
AND GP.유저일련번호 NOT IN (SELECT 유저일련번호 
                   FROM 게임플레이 WHERE 플레이날짜 >= '2021-11-14' )
                   AND GP.유저일련번호 = GU.유저일련번호
                   GROUP BY GP.유저일련번호;
                   
                   
-- 휴먼 유저의 과거 상세 게임플레이
-- 1. 휴먼 유저의 총기 사용 상세내역                  
-- 휴면유저 총기사용상세내역 GROUP BY 
                                     
SELECT GP.유저일련번호, AVG(GUN.총기사용횟수) AS 평균총기사용횟수 ,AVG(GUN.총기유효데미지) AS 평균총기유효데미지,AVG(GUN.총기사용KILL수) AS 평균KILL수, AVG(GUN.총기사용기절횟수) AS 평균총기기절횟수
FROM 게임플레이 GP, 총기사용상세내역 GUN
WHERE GP.플레이일련번호 = GUN.플레이일련번호
AND GP.플레이날짜 < '2021-11-14'
AND GP.유저일련번호 NOT IN (SELECT 유저일련번호
                      FROM 게임플레이 WHERE 플레이날짜 >= '2021-11-14')
                      GROUP BY GP.유저일련번호;
                   
                   
-- 4. 본격 조인 데이터베이스
-- 유료아이템결제 부분

-- SELECT * FROM 게임유저;
-- 어떤 유저가 몇 건을 구매했고, 얼마를 구매했는지
SELECT 유저닉네임, COUNT(*) AS 구매건수, SUM(결제금액) AS 총구매금액
FROM 게임유저 GU, 유료아이템결제 CASH, 유료아이템 ITEM
WHERE GU.유저일련번호 = CASH.유저일련번호
AND CASH.유료아이템일련번호 = ITEM.유료아이템일련번호
GROUP BY 유저닉네임;


#가장 인기 있는 유료 아이템 항목은?

# SELECT ITEM.유료아이템타입, COUNT(*) AS 구매건수, SUM(결제금액) AS 총구매액
# FROM 유료아이템결제 CASH, 유료아이템 ITEM
# WHERE CASH.유료아이템일련번호 = ITEM.유료아이템일련번호
# GROUP BY 유료아이템타입;

SELECT ITEM.유료아이템타입,ITEM.아이템이름 ,COUNT(*) AS 구매건수, SUM(결제금액) AS 총구매액
FROM 유료아이템결제 CASH, 유료아이템 ITEM
WHERE CASH.유료아이템일련번호 = ITEM.유료아이템일련번호
GROUP BY 유료아이템타입, 아이템이름;
                   

```



# 최종 결정 쿼리문



```mysql
-- 1. 한달 이상 휴면 유저의 마지막 플레이 날짜 및 지금까지 휴먼일

SELECT 유저일련번호, MAX(플레이날짜) AS 마지막플레이날짜, DATEDIFF(NOW(),MAX(플레이날짜)) AS 휴먼일
FROM 게임플레이
WHERE 플레이날짜 < '2021-11-14'
AND 유저일련번호 NOT IN (SELECT 유저일련번호 
                   FROM 게임플레이 WHERE 플레이날짜 >= '2021-11-14' )
                   GROUP BY 유저일련번호;
                   
                  
-- 2. 최근 한달간 플레이 하지 않은 유저들의 게임 플레이 및 우승횟수


SELECT GP.유저일련번호, GU.유저닉네임,COUNT(*) AS 플레이수, SUM(플레이우승여부) AS 게임우승횟수, SUM(플레이우승여부) /COUNT(*) * 100 AS 승률
FROM 게임플레이 GP, 게임유저 GU
WHERE GP.플레이날짜 < '2021-11-14'
AND GP.유저일련번호 NOT IN (SELECT 유저일련번호 
                   FROM 게임플레이 WHERE 플레이날짜 >= '2021-11-14' )
                   AND GP.유저일련번호 = GU.유저일련번호
                   GROUP BY GP.유저일련번호;
                   

-- 3. 가장 인기 있는 유료 아이템 항목은?


SELECT ITEM.유료아이템타입,ITEM.아이템이름 ,COUNT(*) AS 구매건수, SUM(결제금액) AS 총구매액
FROM 유료아이템결제 CASH, 유료아이템 ITEM
WHERE CASH.유료아이템일련번호 = ITEM.유료아이템일련번호
GROUP BY 유료아이템타입, 아이템이름;
                   
                   


```



# 번외



```mysql
SELECT GP.유저일련번호, AVG(GUN.총기사용횟수) AS 평균총기사용횟수 ,AVG(GUN.총기유효데미지) AS 평균총기유효데미지,AVG(GUN.총기사용KILL수) AS 평균KILL수, AVG(GUN.총기사용기절횟수) AS 평균총기기절횟수
FROM 게임플레이 GP, 총기사용상세내역 GUN
WHERE GP.플레이일련번호 = GUN.플레이일련번호
AND GP.플레이날짜 < '2021-11-14'
AND GP.유저일련번호 NOT IN (SELECT 유저일련번호
                      FROM 게임플레이 WHERE 플레이날짜 >= '2021-11-14')
                      GROUP BY GP.유저일련번호;
```

