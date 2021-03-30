#importing packages needed
import pandas as pd


# get persister data from excel sheet as dataframe
df_persister = pd.read_excel (r'/Users/mirna/Documents/BE20-440/pset4/data/persister_TableS4.xls', sheet_name='fold_change_data')

#  set protein as index for dataframe
df_persister.set_index('Protein', inplace=True)


# get one biofilm repplicate data from excel sheet as dataframe
df_biofilm = pd.read_excel (r'/Users/mirna/Documents/BE20-440/pset4/data/iTRAQ_data_of_MG1655_Biofilm_Vs_Planktonic.xls', sheet_name='WT_BIO1')

# set protein as index for dataframe
df_biofilm.set_index('Protein', inplace=True)

#getting proteins that appear in both datasets

#initializing common protein list with fold changes 
# in persister and biofilm cells from both datasets
common_proteins = {'Protein':[],
        'Biofilm':[], 
        'Persister':[]}

for index in df_biofilm.index:
    if index in df_persister.index:
        #getting fold changes of common proteins
        common_proteins['Protein'].append(index)
        common_proteins['Biofilm'].append(df_biofilm.at[index, 'Biofilm'])
        common_proteins['Persister'].append(df_persister.at[index, 'Persister'])

#generating a dataframe for commob proteins
df_common = pd.DataFrame(common_proteins)
df_common.set_index('Protein', inplace=True)
df_common.columns=['Biofilm','Persister']

# removing a duplicate dattapoint
# explicitily specified in code for future reference
updated_df = df_common.drop('P02925') 


# export common proteins list to excel for Matlab plotting
updated_df.to_excel(r'/Users/mirna/Documents/BE20-440/pset4/data/persister_biofilm_common.xls')