## 구글 드라이브 파일 별 분석



> 구글드라이브 폴더 안에 어떤 파일이 있는지 정리
>
> => 폴더는 <폴더명> 으로 표시
>
> 



1. #### <제안서 작업>

   - 프로젝트 초반에 보면 좋을 논문들 (브랜드 감성 분석 관련)

     - <기타 참고 자료>

   - LG 프로젝트가 하려고 하는 목적에 관한 PPT

     - <최종 제안서> -> [LG RFP]H_A 소셜리스닝 정교화 산학협력.pdf

   - < sample data > = 분석에 사용된 Sample Data

     - 웹소스 데이터를 모아둔 폴더 (Reddit과 Reviews, 블로그 웹사이트, forums) 에서 가져온 웹소스 데이터들.

     - > 폴더명 : 1016_Web Sources(Reddit, Reviews, Blog-Websites, Forums)_data_sample

     - 삼성 제품 2016 ~ 2021년 리뷰 데이터 (트위터로부터 온걸로 추정) => **전처리 작업 후의 버전과 전처리 작업 전의 버전이 있는 거 같다.**

     - > 전처리 전 파일 파일명 : 2016-2021_삼성리뷰데이터.zip
       >
       > 전처리 후 파일 파일명 : 2016~2021_삼성 냉장고_트위터_정제.zip

     - LG 제품 2016 ~ 2021년 리뷰 데이터 (트위터로부터 온걸로 추정) = > **전처리 작업 후의 버전과 전처리 작업 전의 버전이 있는 거 같다.**

     - > 전처리 전 파일 파일명 : 2016-2021_LG리뷰데이터.zip
       >
       > 전처리 후 파일 파일명 : 2016~2021_LG냉장고_트위터_정제.zip

   - 프로젝트 시작 당시 직접 크롤링해서 뽑아온 7일간의 데이터들

     - Instagram 통해서 뽑아온 데이터(7일간)

       - > 파일명 : Instargram_7days.xlsx

     - twitter 통해서 뽑아온 데이터 (7일간)

       - > 파일명 : twitter_7days.xlsx

   - 페이스북, 유튜브, 트위터, 인스타그램에서 노이즈(?) 를 정리한 파일 같음. (이건 무슨 파일인지 성민이형에게 물어봐야 할 듯!)

     - > 파일명 : noize sampling.xlsx
       >
       > 노이즈 제거 방법에 대한 ppt => 파일명 : 노이즈 예시 + 키워드 추출방안.pptx

   - < Volume >

     - sprinklr 에서 뽑아온 데이터들에 대한 설명 ppt 가 들어 있음 (twitter, youtube, facebook, instagram)

2. #### <데이터 전처리>

   - ##### <최종 전처리>

     - <1. Sentence 기준> => sentence 기준으로 전처리된 최종 pkl 파일들이 저장되어 있다.

       - Sentence 기준으로 데이터를 전처리한 것.  (POS 가 형태소를 성민형에게 의미하는지 물어봐야할 듯, 아닌거 같아..
         - <Sentence기준> => < ver4 > => <pos 후> => 2Sentence_POS

       - Mention 기준으로 데이터를 전처리한 것
         - 파일명 : 2Mention_POS => 감성 레이블이 전부 붙어있지 않고 일부 붙어 있음

       - > 이 두 가지의 의미를 모르겠음.

     - <2. Mention 기준> => mention 기준으로 전처리된 최종 pkl 파일들이 저장되어 있다.

       - Mention 기준으로 전처리한 최종 pkl들이 pos전, pos 후로 나뉘어 저장되어 있다.

     - <브랜드_제품군 정리_ 최종 전 데이터에서 제거>

       - ㅇ
       - ㅇ
       - ㅇ

     - < WEB > => RBF 란 웹소스를 의미한다. (REVIEW, BLOG, FORUM,)

       - < ver x >

         - 웹소스에 대한 최종전처리 파일들이 버전별로 존재한다.

       - < RBF(reddit, blog, forums) - sent >

         - sent 단위로 전처리된 최종 파일

       - < RBF(reddit, blog, forums) - mention >

         - mention 단위로 전처리된 최종 파일

       - <RBF 관련 코드 파일>

         - ##### web 소스에 대한 최종 전처리 파이썬 파일이 담겨 있음 => 이걸 따라하면 될 듯. .(전처리 전 파이리가 어딨는지 모르겠엄)

     - < SOCIAL >

       - <social media 관련>
         - social media 관련 전처리한 최종 pkl 파일 존재
         - social media 관련 전처리한 최종 코드 파일 존재

       - sentence 기준 mention 기준 별 전처리한 최종 pkl 파일들이 존재

       - 관련 코드 **(코드 where, 전처리 전 csv)**

         

   - ##### <코드>

     - 여러 전처리를 진행했던 파일들이 있음

       - <공통>

         - <공통 Preprocessing>

           - <외국어, 게임, 뭔지 모르겠는 단어들>

             - 모르는 단어들 모음을 csv 파일로 저장.

           - <성민>

             - 스프링클러의 reddit 으로부터 전처리 진행한 코드.

           - <박운찬>

             - > 파일명 : [0 원본]Document_labeling.ipynb => 제품군 라벨링 관련 코드임

         - <스프링클러 쿼리에 OR 붙이는 코드>

           - 이게 무슨 작업을 하는건지 모르겠음

         - <Label Source 붙이는 코드>

           - 각 sample의 데이터가 어떤 곳으로부터 가져왔는지 label 하는 코드
             - web source 부분과 소셜 네트워크 부분으로 나뉘는 거 같음
               - Web source 부분 label  : *Forums, Reviews Type, Blog post*
               - Social Media : Youtube, Instagram, Twitter, Facebook

           

           

     - .

       - <social media_blacks lists>

         - reddit, forums, blog 의 black list 관련 파일이 있음 (이게 뭔지 성민이 형에게 물어봐야 할 듯)

       - ##### < Web >

         - 웹소스에 데이터들에 대한 전처리 파일들이 있음
         - input type 의 종류(word, sentence, mention, aspect) 에 따른 전처리 코드가 있음
         - <웹소스 전처리 최종 코드>
           - Web source 데이터에 대한 최종 전치러 코드가 담겨 있다. (이 파일이 무슨 파일인지 성민이형한테 꼭 물어봐야 한다.)

         

   - ##### <Sprinklr_Message type>

     - web source 데이터 말고 소셜 미디어 데이터의 유형에 대해서 설명하는 파일이 있음

       

3. #### <쿼리 작업>

   - 쿼리 작업 폴더가 뭐하는 파일인지 성민이형에게 물어봐죵

     





> ##### 성민이형 (우리가 눈대중으로 봐서라도 전처리 과정을 알면 프로젝트 따라가는데 도움이됨)
>
> 1. 전처리 된 데이터가 아니라 전처리 전 파일
>
> 2. 전처리 전체 과정을 나타내는 파이썬 코드 파일