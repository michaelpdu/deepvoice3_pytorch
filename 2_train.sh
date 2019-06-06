CUDA_VISIBLE_DEVICES=1 nohup python train.py --preset=presets/deepvoice3_pinyin.json --data-root=b31_pinyin --checkpoint-dir=checkpoint_b31 > train_b31.log 2>&1 &
