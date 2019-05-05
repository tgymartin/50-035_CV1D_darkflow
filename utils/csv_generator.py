import pathlib as p
import csv
import pandas as pd

# Settings
raw_file = r'raw_2.txt'
out_file = r'out_2.csv'

def read_to_df(filepath):
    filepath = p.Path(filepath)
    with open(filepath) as f:
        df = pd.read_csv(f,
                            sep = ' - ',
                            header = None,
                            names = ['step', 'loss', 'moving ave loss'])
        df = df[~df.step.str.contains('Checkpoint')] #filter out the checkpoint lines
        df = df[~df.step.str.contains('epoch')] #filter out epoches line

        df['step'] = df['step'].apply(lambda x: int(x.split(' ')[-1]))

        for col_name in ['loss', 'moving ave loss']:
            df[col_name] = df[col_name].apply(lambda x: float(x.split(' ')[-1]))

    return df

def write_to_csv(filepath, df):
    filepath = p.Path(filepath)
    df.to_csv(filepath)

if __name__ == "__main__":
    df = read_to_df(raw_file)
    write_to_csv(out_file, df)

