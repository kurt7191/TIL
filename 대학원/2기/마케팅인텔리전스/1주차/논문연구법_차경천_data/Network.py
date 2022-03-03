import os
import sys
import numpy as np
import pandas as pd
from itertools import product

class Network(object):
    def __init__(self):
        self.mUserListLabel = []
        self.mObjectListLabel = []
        self.mNodeListValue = []
        self.mNodeArrayValue = np.array(0)
        self.mUserProjection = np.array(0)
        self.mObjectProjection = np.array(0)
        self.mWeightArray = np.array(0)
        self.mEstmateArray = np.array(0)

    # -------------------------------------------------------------------------
    # User List
    def GetUserList(self):
        return self.mUserListLabel

    # User List를 설정하기위한 함수
    def SetUserList(self, pUserString):
        # 양 끝단의 White space 삭제
        self.mUserListLabel = pUserString.strip().split(',')
        # 중간에 공백인 자료 삭제 
        self.mUserListLabel = list(filter(str.strip, self.mUserListLabel))
        self.mUserListLabel = [item.strip() for item in self.mUserListLabel]

    # 구매자를 화면에서 입력받도록 하는 기능
    def DisplayInputUserList(self):
        self.screenClear()
        print('구매자 이름은 \',\'로 구분됩니다.')
        print('구매자 이름의 앞, 뒤 공백은 무시됩니다.')
        print('구매자 이름이 공백이면 무시됩니다.')
        print('')
        self.SetUserList(input('구매자 이름을 입력하세요: '))
        print(self.GetUserList())

    # -------------------------------------------------------------------------
    # Object List
    def GetObjectList(self):
        return self.mObjectListLabel

    def SetObjectList(self, pObjectList):
        # 양 끝단의 White space 삭제
        self.mObjectListLabel = pObjectList.strip().split(',');
        # 중간에 공백인 자료 삭제 
        self.mObjectListLabel = list(filter(str.strip, self.mObjectListLabel))
        self.mObjectListLabel = [item.strip() for item in self.mObjectListLabel]

    # Object List 입력용 화면
    def DisplayInputObjectList(self):
        self.screenClear()
        print('오브젝트 이름은 \',\'로 구분됩니다.')
        print('오브젝트 이름의 앞, 뒤 공백은 무시됩니다.')
        print('오브젝트 이름이 공백이면 무시됩니다.')
        print('')
        self.SetObjectList(input('오브젝트 이름을 입력하세요: '))
        print(self.GetObjectList())

    # -------------------------------------------------------------------------
    # Node List

    # Set/Get 함수
    # Node List에 할당된 값을 불러오는 기능
    def GetNodeListValue(self):
        return self.mNodeListValue

    # Node List Value을 할당하는 기능
    def SetNodeListValue(self, pNodeListValue):
        self.mNodeListValue = pNodeListValue

    # Node List Label에 할당된 값 불러오는 기능
    def GetNodeListLabel(self):
        return self.mNodeListLabel

    # Node List Label을 할당하는 기능
    def SetNodeListLabel(self, pNodeListLabel):
        self.mNodeListLabel = pNodeListLabel    

    # Object Projection을 할당하는 기능
    def SetObjectProjection(self, pObjectProjection):
        self.mObjectProjection = pObjectProjection

    # Object Projection을 불러오는 기능
    def GetObjectProjection(self):
        return self.mObjectProjection

    # User Projection을 할당하는 기능
    def SetUserProjection(self, pUserProjection):
        self.mUserProjection = pUserProjection

    # User Projection을 불러오는 기능
    def GetUserProjection(self):
        return self.mUserProjection

    # 화면 제어용 
    # Node List의 값을 입력받기위한 화면 
    def DisplayInputNodeList(self):
        self.screenClear()
        mNodeSource = [self.GetObjectList(), self.GetUserList()]
        self.mNodeListLabel = list(product(*mNodeSource))
        for item in self.GetNodeListLabel():
            result = self.nodeValue(item[0], item[1])
        self.calNodeArray()
        self.calObjectProjection()
        self.calUserProjection()

        print('')
        print('입력된 구매자의 보유량입니다. ')
        print(self.GetUserProjection())
        print('')
        print('입력된 Object의 판매량입니다. ')
        print(self.GetObjectProjection())
        print('')
        print('입력된 Node 배열입니다. ')
        print(self.GetNodeArrayValue())
        _ = input('Enter 를 누르세요')
        

    # Node Array Value 값을 읽어 오는 기능
    def GetNodeArrayValue(self):
        return self.mNodeArrayValue;
    
    # Node Label를 출력하여 Node Value을 입력받는 함수
    def nodeValue(self,pItem, pUser):
        TrueValue = ['0', '1']
        result = input('구매물품: ' + pItem + ' -> ' + '구매자: ' + pUser +' (구매 실적이 있으면 1, 없으면 0) ? ')
        if result in TrueValue:
            self.mNodeListValue.append(result)
        else:
            print('0 or 1을 입력해 주세요')
            self.nodeValue(pItem, pUser)
        
    # Node List Value를 Node Array Value로 하는 함수 
    def calNodeArray(self):
        mUserCount = len(self.mUserListLabel)
        mObjectCount = len(self.mObjectListLabel)
        self.mNodeArrayValue = np.array(self.mNodeListValue).reshape(mObjectCount, mUserCount).astype(np.int)


    # Node List Value의 Object Projection를 계산하는 함수
    def calObjectProjection(self):
        mObjectProjection = np.array(self.GetNodeArrayValue()).sum(axis=1)
        self.SetObjectProjection(mObjectProjection)
        
    # Node List Value의 User Projection를 계산하는 함수
    def calUserProjection(self):
        mUserProjection = np.array(self.GetNodeArrayValue()).sum(axis=0)
        self.SetUserProjection(mUserProjection)
    
    # -------------------------------------------------------------------------
    # Weight Array
    
    # 가중치 불러오는 기능
    def GetWeightArray(self):
        return self.mWeightArray

    # 가중치 설정하는 기능
    def SetWeightArray(self, pWeight):
        self.mWeightArray = pWeight
    
    # 가중치를 계산하는 함수
    def calWeightArray(self):
        mWeightArray = np.ones((self.GetObjectProjection().shape[0], self.GetObjectProjection().shape[0]), dtype=float)
        mWeightArray = mWeightArray / self.GetObjectProjection() * np.dot(self.GetNodeArrayValue(), (self.GetNodeArrayValue() / self.GetUserProjection()).T)
        self.SetWeightArray(mWeightArray)
    
    # 가중치를 화면에 뿌려주는 함수 
    def DisplayWeightArray(self):
        self.screenClear()
        print('계산된 가중치 입니다. ')
        print(self.GetWeightArray())
        _ = input('Enter 를 누르세요')

    # -------------------------------------------------------------------------
    # Estimate Array
    # 추정치를 불러오는 기능
    def GetEstimateArray(self):
        return self.mEstimateArray

    #추정치를 설정하는 기능
    def SetEstimateArray(self, pEstimate):
        self.mEstimateArray = pEstimate

    # 추정치를 계산하는 함수
    def calEstimateArray(self):
        mEstimateArray = np.dot(self.GetWeightArray(), self.GetNodeArrayValue())
        mEstimateArray = mEstimateArray * np.where(self.GetNodeArrayValue() <= 0, 1, 0)
        self.SetEstimateArray(mEstimateArray)

    # 추정치를 화면에 뿌려주는 함수 
    def DisplayEstimateArray(self):
        print('')
        print('계산된 추정치 입니다. ')
        print(self.GetEstimateArray())
        _ = input('Enter 를 누르세요')

    # -------------------------------------------------------------------------
    # Recommend 
    
    def DisplayRecommend(self):
        mUserName = np.array(self.GetUserList())
        mUserNameIndex = np.arange(len(self.GetUserList()))
        self.screenClear()
        self.printUserLabel(mUserNameIndex, mUserName)
        self.recommendValue(mUserNameIndex ,mUserName)

    def recommendValue(self, pUserNameIndex, pUserName):
        print('')
        print('종료하고 싶으면 \'x\'를 누르세요')
        print('')
        mUserIndex = input('구매자 번호를 입력하세요 ')
        if(mUserIndex != 'x'.upper()):
            mUserIndexs = np.arange(len(self.GetUserList()))
            if mUserIndex in mUserIndexs.astype(str):
                mUserIndexNum = int(mUserIndex)
                mRecommend = self.GetEstimateArray()
                mRecommendMax = mRecommend[:, mUserIndexNum:mUserIndexNum+1].max()
                mRecommendIndex = mRecommend[:, mUserIndexNum:mUserIndexNum+1].argmax()
                mRecommendObject = self.GetObjectList()[mRecommendIndex]
                if mRecommendMax <= 0 :
                    self.screenClear()
                    print("모두구매하여 추천항목이 없습니다. ")
                    print("다른 구매자를 입력해 주세요 ")
                    print('')
                    self.printUserLabel(pUserNameIndex, pUserName)
                    self.recommendValue(pUserNameIndex, pUserName)
                else:
                    mUserName = pUserName[mUserIndexNum:mUserIndexNum+1]
                    self.screenClear()
                    print('구매자 ' + mUserName[0] +' 의 추천 항목은 ' + mRecommendObject + ' 입니다')
                    print('')
                    self.printUserLabel(pUserNameIndex, pUserName)
                    self.recommendValue(pUserNameIndex, pUserName)
            else:
                self.screenClear()
                print('존재하지 않는 구매자 번호입니다. 다시 입력해 주세요')
                print('')
                self.printUserLabel(pUserNameIndex, pUserName)
                self.recommendValue(pUserNameIndex, pUserName)
        else:
            exit()

    # 사용자 레이블 출력 
    def printUserLabel(self, pUserNameIndex, pUserName):
        for item in pUserNameIndex:
            print('Index: ' + str(item) + ',  Name: ' +  pUserName[item])


    # -------------------------------------------------------------------------
    # Private Function 
    # 화면을 클리어 하기 위한 기능
    def screenClear(self):
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')