import pandas as pd

def read_and_sort_csv(file_path, column_to_sort):

    try:
        
        data = pd.read_csv(file_path)
        
       
        sorted_data = data.sort_values(by=column_to_sort)
        
        
        return sorted_data
    
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def save_sorted_csv(data, output_file_path):
   
    try:
       
        data.to_csv(output_file_path, index=False)
        print(f"Sorted CSV saved successfully to {output_file_path}")
    except Exception as e:
        print(f"Failed to save CSV: {e}")


if __name__ == "__main__":
   
    input_file ="C:\\Users\\Garv\\Desktop\\DAA project\\customers-1000.csv"
    
    
    column ="City" # First name , Last name , City , Index
    
    
    sorted_data = read_and_sort_csv(input_file, column)
    
    if sorted_data is not None:
        output_file = "C:\\Users\\Garv\\Desktop\\DAA project\\sorted_large_data.csv"
        save_sorted_csv(sorted_data, output_file)
