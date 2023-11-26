import numpy as np


GL_CNN_PM25_indir = '/my-projects/Projects/MLCNN_PM25_2021/code/Prediction/Predict_Plot_Map_GPU_version/Map_Prediction_Results/GL/Monthly/'
version = 'vManuscript-2023May'
special_name = '_ResNet1111_SigmoidMSELoss_alpha0d005_beta8d0_gamma3d0_lambda1-0d2_ForceSlopeFalse'
number_of_channel = 28
cropped_mapdata_outdir = '/my-projects/Projects/PM25_Speices_DL_2023/data/input_variables_map/'


def padding_GLCNNPM25(init_map):
    '''
    The initial Global CNN PM2.5 estimation is
    '''
    padding_map = np.zeros((13000,36000),dtype = np.float64)
    padding_map[5:12995,10:35990] = init_map
    return padding_map