Overview
This repo contains all the code and data needed to reproduce a heatmap figure outlining fold change in abundance of commonly detected proteins in the biofilm and persister E. coli MG 1655 datasets (obtained from two different publications- see below).
See project background here: https://docs.google.com/document/d/1bJdGNSJAJV1m0InJ_x3p9zJ1leSg1cY7cd4h84mI_M0/edit?usp=sharing


Folder structure

Code folder: contains python and matlab code to generate figure
proteomics_common_Ecoli.py python code used to generate a table of proteins common between the two datasets and saves common protein list along with fold changes in persistor and biofilm populations as an excel sheet in the data folder.
common_protein_heatmap.mat matlab code used to generate heatmap based on data obtained from proteomics_common_Ecoli.py python code.

Data folder: contains published data needed to produce figure, see data section in this README.md.
persister_biofilm_common.xls is obtained from python code described above and contains common protein list along with fold changes in persistor and biofilm populations
common_protein_heatmap_MATLABdata.m in this folder that can be used directly with the MATLAB code in the code folder to produce figure.

Figures folder: contains MATLAB figure that is to be reproduced for reference.


Data
The data used are stored in the data folder of this repository.

We will be using processed proteomics datasets from two different papers that both worked with the same strain of E. coli K-12 (MG1655). The first paper enriched for persister cells through rifampin pretreatment followed by ampicillin exposure. Then, spectral counting proteomics was used to compare different abundances of proteins between persister-enriched and normal populations.  The second paper used quantitative proteomics (iTRAQ) to identify proteins differentially expressed in biofilm versus planktonic cultures. 

Persister data was included in table S4 of the supplementary material PDF of the following publication:

Specific Enrichment and Proteomics Analysis of Escherichia coli Persisters from Rifampin Pretreatment 
https://pubs.acs.org/doi/abs/10.1021/acs.jproteome.8b00625?casa_token=vsL9GqC__d4AAAAA:DUfGwSPD9KtqG9TCss5VKkSihurtYCVsBK1SrPoWY54Zh2keJMdSMPCH0K5C6mUyTFSXjzNsjDl4mIy9

Data was copied into an excel sheet (persister_TableS4.xls) for analysis.
Fold change in protein abundance data was copied in a separate sheet in the same excel file for further processing, sheet was named "fold_change_data".

Biofilm data was included as an excel sheet (iTRAQ_data_of_MG1655_Biofilm_Vs_Planktonic.xls) in the supplementary material of the following publication:
Quantitative protein expression and cell surface characteristics of Escherichia coli MG1655 biofilms
https://analyticalsciencejournals.onlinelibrary.wiley.com/doi/full/10.1002/pmic.201000386?casa_token=_YDS83Fbm-QAAAAA%3AQEAXau3pENSFdISUAM7rD59O_mcEfP0VuqYSyZu5WehFhwQu5UCjePo_H0u2ll5HZdY2BX6YtjjSCrfF

Fold change in protein abundance for one of two Biofilm replicates (replicate 1) was copied in a separate sheet in the same excel file for further processing, sheet was named "WT_BIO1".


Installation
To run the code you need: 
Python 3.x
python package: pandas
MATLAB_R2020b

Steps to reproduce figure:
Method 1:
1) Download this repository
2) Run python code proteomics_common_Ecoli.py, this will generate a table of proteins common between the two datasets and saves common protein list along with fold changes in persistor and biofilm populations as an excel sheet in the data folder.
3) Open excel file generated from python code and create a new sheet where data is such that each fold_change value is associated with a protein and a population type (This is the format needed for the matlab code to work- see persister_biofilm_common.xls file for example ):

4) open matlab code common_protein_heatmap.mat
5) In Matlab, import data from the sheet in #3
6) run matlab code, figure will be generated and can be saved through the matlab figure IDE.

Note: In the following Matlab line variable names will vary based on what you name your folder, columns in excel sheet...etc., see matlab heatmap documentation for further help https://www.mathworks.com/help/matlab/ref/heatmap.html: 
heatmap(persisterbiofilmcommonS1, 'type','Protein', 'ColorVariable', 'fold_change', 'colormap', hot, 'GridVisible', 'off')




Method 2:
1) Download this repository
2) open matlab code common_protein_heatmap.mat
3) open common_protein_heatmap_MATLABdata.m
4) Run matlab code, figure will be generated and can be saved through the matlab figure IDE.
Note: In the following Matlab line variable names will vary based on what you name your folder, columns in excel sheet...etc., see matlab heatmap documentation for further help https://www.mathworks.com/help/matlab/ref/heatmap.html: 
heatmap(persisterbiofilmcommonS1, 'type','Protein', 'ColorVariable', 'fold_change', 'colormap', hot, 'GridVisible', 'off')











