close all
% data imported manually
% plot figure
heatmap(persisterbiofilmcommonS1, 'type','protein', 'ColorVariable', 'fold_change', 'colormap', hot, 'GridVisible', 'off')
caxis([0 8])
title ({'Fold change in protein abundance for',  'Biofilm or persister vs planktonic E. Coli MG1655'})