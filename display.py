import sys
from parlai.scripts.display_model import DisplayModel

f = open("kv_self_1000.txt", 'w')
sys.stdout = f

DisplayModel.main(
    task='personachat',
    model_file='model/kvmemnn/self_persona',
    num_examples=1000,
)

f.close()