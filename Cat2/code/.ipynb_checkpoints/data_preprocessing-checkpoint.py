import pandas as pd


def fill_null_0(series):
    return series.fillna(0)

def fill_null_n1(series):
    return series.fillna(-1)

def fill_null_mode(series):
    mode = series.mode()
    return series.fillna(mode)

def fill_null_mean(series):
    mean = series.mean()
    return series.fillna(mean)


# class TrainingSetPreprocessingInfo:
#     # 나중에 이 정보를 기반으로 valid, test set을 똑같이 encoding하기 위함.
#     # 1. 각 컬럼별 인코딩 정보
#     ### 1) 각각의 unique값들 (여기 없으면 NaN처리)
#     # 2. 아이디 컬럼 정의
#     # 3. X, y 컬럼 정의
#     def __init__(self, raw_df):
#         self.raw_columns = raw_df.columns
    
#     def
    

missing_value_handling = [fill_null_0, fill_null_n1, fill_null_mode, fill_null_mean]

