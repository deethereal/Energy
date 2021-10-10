import joblib
import pandas as pd
def main(file_name):
    scaler = joblib.load('scaler.pkl')
    model = joblib.load('ridge_reg.pkl')
    df = pd.read_csv(file_name[0],sep=";")
    result = pd.DataFrame(model.predict(scaler.transform(df.values)),columns=['valve_'+str(i) for i in range(1,13)])
    result.to_json('result.json', orient = 'records')

if __name__ == '__main__':
    import sys
    main(sys.argv[1:])