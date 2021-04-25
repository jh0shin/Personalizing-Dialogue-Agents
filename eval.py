from parlai.scripts.eval_model import EvalModel

# evaluate generative model with hits@1 method

EvalModel.main(
    task='personachat',

    ##### generative model - seq2seq #####
    # model_file='model/seq2seq/self_persona_2',
    # batchsize=512,
    # # metrics='hits@1',
    # datatype='test',
    # rank_candidates=True, 

    ##### ranking model - kv memory network #####
    model_file='model/kvmemnn/self_persona_short',
    # batchsize=512,
    metrics='hits@1',
    datatype='test',    
)