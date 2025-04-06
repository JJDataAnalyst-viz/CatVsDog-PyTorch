from torch import  nn
from torchvision import models
import yaml

with open('params.yaml','r') as f:
    params = yaml.safe_load(f)['DATA']

def Model_Dense_Net(fine_tuned: bool = True,num_classes: int = params['NUM_CLASSESS'],out_features: int = 1024):
    '''Set Dense_Net as main model which is used for Cats vs Dogs image classification problem.

    Parameters
    ----------
        fine_tuned (bool,optional):
            - If `True`, all layers of the model are fine-tuned (default is `True`).
            - If `False`, all layers are frozen and no gradients are calculated for the model's parameters.
        num_classes (int) :
            - Number of classess put into our model (default is `2`)
        out_features (int) :
            - Number of output features (default is `1024`)
    
    '''

    model = models.densenet169()
    
    if fine_tuned is False:

        print("[INFO] Freezing all layers...")
        for parameters in model.parameters():
            parameters.requires_grad = False
    else:

        print('[INFO] Fine-tuning all layers...')
        for parameters in model.parameters():
            parameters.requires_grad = True

    model.classifier[1] = nn.Sequential([
        nn.Linear(in_features=1664, out_features=out_features), 
        nn.ReLU(),
        nn.Dropout(0.5), 
        nn.Linear(out_features, num_classes)  
    ])

    return model

