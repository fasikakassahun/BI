Name: Fasika kassahun ID: DBUR/4100/13

### 4. How to run and get the result  
Follow the steps below to download, clean, load, and visualize the data:  

1. **clone the repository**  
   - run this in your terminal 
   ```
   git clone https://github.com/fasikakassahun/BI.git
   ```
   - then change directory 
   ```
   cd BI
   ```
   - After that to open vscode editor 
   ```
   code .
   ```  

2. **Get all dependencies mentioned above and configure them**  
   - install python packages by running the following commands sequencially:  
     ```
     pip install kagglehub
     ``` 
     ```
     pip install pandas
     ```

3. **Run the files**  
   - step 1: Run
     `download_data_from_kaggle.py` 
     This python code downloads and saves the data
   - step 2: Run  
     `_clen_store_data.py` 
     This python code clean and transforms the data
   - step 3: Run 
     `load_dataset.py` 
     This python code loads the cleaned data
