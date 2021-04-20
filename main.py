# https://github.com/facebookresearch/ParlAI/issues/2225
# options from here

# https://parl.ai/docs/cli_usage.html
# CLI-command to code option

from parlai.scripts.train_model import TrainModel
TrainModel.main(
    # model_file='model/kvmemnn/self_persona',
    # task='personachat:self',
    # 5트
    
    # model_file='model/kvmemnn/self_persona_rv',
    # task='personachat:self_revised',

    # model_file='model/kvmemnn/no_persona',
    # task='personachat:none',
    
    # model_file='model/kvmemnn/no_persona_rv',
    # task='personachat:none_revised', 

    # model_file='model/kvmemnn/other_persona',
    # task='personachat:other',
    
    # model_file='model/kvmemnn/other_persona_rv',
    # task='personachat:other_revised',

    # model_file='model/kvmemnn/both_persona',
    # task='personachat:both',

    # model_file='model/kvmemnn/both_persona_rv',
    # task='personachat:both_revised',

    # model='projects.personachat.kvmemnn.kvmemnn:KvmemnnAgent',

    # log_every_n_secs=60,
    # validation_max_exs=10000,
    # validation_every_n_secs=900,
    # hops=1,
    # lins=0,
    # validation_patience=-1,
    # validation_metric='accuracy',
    # max_train_time=12 * 3600,
    # share_embeddings=True,
    # batchsize=1,
    # learningrate=0.1,
    # embeddingsize=500,
    # margin=0.1,
    # tfidf=False,
    # numthreads=10,

    ###################### GENERATIVE #################

    # model_file='model/seq2seq/self_persona',
    # task='personachat:self',

    # model='seq2seq',

    # log_every_n_secs=60,
    # validation_max_exs=10000,
    # validation_every_n_secs=900,
    # # hops=1,
    # # lins=0,
    # validation_patience=-1,
    # validation_metric='ppl',
    # max_train_time=10 * 3600,
    # # share_embeddings=True,
    # batchsize=1,
    # learningrate=0.1,
    # embeddingsize=500,
    # # margin=0.1,
    # # tfidf=False,
    # numthreads=12,

    #### FROM : https://github.com/facebookresearch/ParlAI/pull/662#issuecomment-475629794

    model_file='model/seq2seq/self_persona_2',
    task='personachat:self',

    model='seq2seq',

    log_every_n_secs=300,
    # validation_every_n_secs=1800,
    # validation_patience=-1,
    # validation_metric='ppl',
    max_train_time=9 * 3600,
    batchsize=128,
    learningrate=0.001,
    embeddingsize=300,
    numlayers=2,
    hiddensize=512,
    dropout=0.5,
    optimizer='adam',
    lookuptable='enc_dec',
    # margin=0.1,
    # tfidf=False,
    # numthreads=8,

    ## GPU : https://dailylime.kr/2020/06/wsl2%EC%97%90%EC%84%9C-ubuntu%EC%99%80-cuda-%EC%82%AC%EC%9A%A9%ED%95%98%EA%B8%B0/
    fp16=True, fp16_impl='mem_efficient',
)

# from parlai.scripts.display_model import DisplayModel
# DisplayModel.main(
#     task='personachat:none',
#     model_file='model/none_kv',
#     num_examples=15,
# )

