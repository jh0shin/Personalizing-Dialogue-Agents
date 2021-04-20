import sys
from parlai.scripts.display_model import DisplayModel

f = open("seq2seq_self_1000.txt", 'w')
sys.stdout = f

DisplayModel.main(
    task='personachat',
    model_file='model/seq2seq/self_persona_2',
    num_examples=1000,
)

f.close()