
import numpy as np
import pandas as pd

import Network as In

# 프로그램 개요
#  
# =====================================================================================

# Python 변수, 함수, 클래스의 선언 룰
# 매우 중요함 (아래 룰을 안따라도 되지만 프로그램 작성 후 오류 발생가능성을 줄이기 위해)
# Local Value은 접두어 m를 붙이고 외부에서 절대 호출하지 말것 
# Local Function은 함수의 첫글자를 소문자로 하고 외부에서 절대 호출하지 말것 
# Class의 이름은 대문자로 시작할것 
# Class Local Value는 Local Value의 기준을 따르고 외부에서 클래스 외부에서 호출하지 말것
# Class Local Value는 Class External Function으로 변환하여 사용할것 
# Class Local Function은 Local Function의 기준을 따르고 클래스 외부에서 호출하지 말것 
# Class External Function은 함수의 첫글자를 대문자로 하여사용하고 외부에서 호출 하여 사용할것 

# =====================================================================================
# Label

# User: 구매자
# Object: 구매품
# Weight: 가중치
# Estimate: 추정치
# Recommend: 추천

# =====================================================================================
# 프로그램에서 사용하게 될 변수

# 1) User List: a, b, c, d 
# 2) Object List: X, Y, Z
# 3) User - Object Node Array
# 4) Weight Array
# 5) Estimation Array:  Node Array * Weight Array and Mask 
# 6) Recommend: 

# =====================================================================================
# 프로그램에서 사용하게 될 Class 정의
# RunNetwork
# Network

# =====================================================================================
# 프로그램 실행

# 초기값 선언 Class
InHandler = In.Network()

# -------------------------------------------------------------------------
# 프로그램 실행 


# User List 
InHandler.DisplayInputUserList()
mUserList = input("사용자 입력 내용이 정확합니까 ?  (정확할 경우 Y or y) ")
while(mUserList.upper() != "Y"):
    InHandler.DisplayInputUserList()
    mUserList = input("사용자 입력 내용이 정확합니까 ? (정확할 경우 Y or y) ")


# Object List 
InHandler.DisplayInputObjectList()
mObjectList = input("구매 입력 내용이 정확합니까 ? (정확할 경우 Y or y) ")
while(mObjectList.upper() != "Y"):
    InHandler.DisplayInputObjectList()
    mObjectList = input("구매 입력 내용이 정확합니까 ? (정확할 경우 Y or y) ")

# Node List 
InHandler.DisplayInputNodeList()
InHandler.calWeightArray()

# Weight Array
InHandler.calWeightArray()
InHandler.DisplayWeightArray()

# Estimate Array 
InHandler.calEstimateArray()
InHandler.DisplayEstimateArray()

# Recommend
InHandler.DisplayRecommend()
