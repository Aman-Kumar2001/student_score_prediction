
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OrdinalEncoder, OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer

# processing columns

def processing_data(num_col, ordinal_col, nominal_col):
    num_pipeline = Pipeline(steps=[("imputing_num",SimpleImputer(strategy='median')),
                               ("Scaling_values",StandardScaler())])

    ordinal_pipeline = Pipeline(steps=[("impute_ordinal", SimpleImputer(strategy='most_frequent')),
                                    ("encoding_ordinal", OrdinalEncoder(categories=[['no','yes'],['low','medium','high'],['easy','moderate','hard']]))])

    nominal_pipeline = Pipeline(steps=[("impute_nominal", SimpleImputer(strategy='most_frequent')),
                                    ("encoding_nominal", OneHotEncoder(handle_unknown='ignore', drop='first'))])

    preprocess_trf = ColumnTransformer(transformers=[("numerical_process", num_pipeline, num_col),
                                                    ("ordinal_process", ordinal_pipeline, ordinal_col),
                                                    ("nominal_process",nominal_pipeline, nominal_col)])
    
    return preprocess_trf

