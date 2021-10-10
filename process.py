import joblib
import pandas as pd
def main(file_name):
    scaler = joblib.load('scaler.pkl')
    model = joblib.load('ridge_reg.pkl')
    df = pd.read_csv(file_name[0])
    result = pd.DataFrame(model.predict(scaler.transform(df.values)),columns=['valve_'+str(i) for i in range(1,13)])
    result.to_csv('result.csv')

if __name__ == '__main__':
    import sys
    main(sys.argv[1:])