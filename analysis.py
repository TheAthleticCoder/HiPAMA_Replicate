import pandas as pd
import os

def combine_csv_files(input_folder, output_file, eval_file):
    # Get all files with the name 'result.csv' in the input folder and its subdirectories
    result_files = [os.path.join(root, file) for root, dirs, files in os.walk(input_folder) for file in files if file == 'result.csv']

    # Check if there are any result files
    if not result_files:
        print("No result.csv files found in the specified folder.")
        return

    # Read the header from the first result.csv file
    first_file = pd.read_csv(result_files[0])
    header = list(first_file.columns)
    last_row_data = pd.DataFrame(columns=header)

    for result_file in result_files:
        last_row = pd.read_csv(result_file).tail(1)
        last_row_data = pd.concat([last_row_data, last_row], ignore_index=True)

    last_row_data.to_csv(output_file, index=False)
    print(f"Combined data written to {output_file}")

    # Read the combined CSV file
    df = pd.read_csv(output_file)
    
    # Drop the 'epoch' column
    df = df.drop(columns=['epoch'])
    df = df.drop(columns=['learning rate'])
    
    # Calculate mean and std for each column
    df_mean = df.mean()
    df_std = df.std()
    
    # Create a new DataFrame with mean and std information
    eval_measure_df = pd.DataFrame({
        'eval_measure': ['mean', 'std'],
        **{col: [mean, std] for col, mean, std in zip(df_mean.index, df_mean.values, df_std.values)}
    })
    
    # Save the new DataFrame to a CSV file
    eval_measure_file = eval_file
    eval_measure_df.to_csv(eval_measure_file, index=False)
    
    print(f"Eval measure data written to {eval_measure_file}")

input_folder = "exp"
output_file = "summ_hipama_kernel10.csv"
eval_file = "eval_hipama_kernel10.csv"
combine_csv_files(input_folder, output_file, eval_file)
