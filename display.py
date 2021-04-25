import sys
from parlai.scripts.display_model import DisplayModel

f = open("kv_self_short_0.4679.txt", 'w')
sys.stdout = f

DisplayModel.main(
    task='personachat',
    # model_file='model/seq2seq/self_persona_2',
    model_file='model/kvmemnn/self_persona_short',
    num_examples=1000,
)

f.close()