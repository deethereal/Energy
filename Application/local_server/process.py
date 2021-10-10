import joblib
import pandas as pd
import numpy as np
import json

def main(args):
    scaler = joblib.load('scaler.pkl')
    model = joblib.load('ridge_reg.pkl')
    if args[1] == "0":
        df = pd.read_csv(args[0],sep=";")
        predictions = model.predict(scaler.transform(df.values))[0]
        ver_preds = []
        for i in range(len(predictions)):
            if predictions[i]>1:
                ver_preds.append(1)
            elif predictions[i]<0:
                 ver_preds.append(0.1)
            else:
                ver_preds.append(predictions[i])

        result = pd.DataFrame(np.array(ver_preds).reshape(1,-1),columns=['valve_'+str(i) for i in range(1,13)])
    else :
        with open(args[0],'r') as f:
            data = json.load(f)
        print(args[0])
        df = pd.DataFrame({'count': data})
        print(df)
        df = df.astype(float)
        result = pd.DataFrame(model.predict(scaler.transform(df.values)),columns=['valve_'+str(i) for i in range(1,13)])
    result.to_json('./WebApp/result.json')

if __name__ == '__main__':
    import sys
    main(sys.argv[1:])