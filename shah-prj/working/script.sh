#pip3 install tensor2tensor --user
#pip3 install tensor2tensor[tensorflow_gpu] --user
#pip3 install tensor2tensor[tensorflow] --user

# See what problems, models, and hyperparameter sets are available.
# You can easily swap between them (and add new ones).
t2t-trainer --registry_help

HERE="~/git/MSCS/shah-prj/working/"

PROBLEM=translate_enfr_wmt32k
MODEL=transformer
HPARAMS=transformer_base_single_gpu

DATA_DIR=data/
TMP_DIR=temp/
TRAIN_DIR=train/$PROBLEM/$MODEL-$HPARAMS/

mkdir -p $DATA_DIR $TMP_DIR $TRAIN_DIR

# Generate data
t2t-datagen \
  --data_dir=$DATA_DIR \
  --tmp_dir=$TMP_DIR \
  --problem=$PROBLEM

# Train
# *  If you run out of memory, add --hparams='batch_size=1024'.
t2t-trainer \
  --data_dir=$DATA_DIR \
  --problems=$PROBLEM \
  --model=$MODEL \
  --hparams_set=$HPARAMS \
  --output_dir=$TRAIN_DIR \
  
# Decode

DECODE_FILE=$DATA_DIR/decode_this.txt
echo "Hello world" >> $DECODE_FILE
echo "Goodbye world" >> $DECODE_FILE

BEAM_SIZE=4
ALPHA=0.6

t2t-decoder \
  --data_dir=$DATA_DIR \
  --problems=$PROBLEM \
  --model=$MODEL \
  --hparams_set=$HPARAMS \
  --output_dir=$TRAIN_DIR \
  --decode_hparams="beam_size=$BEAM_SIZE,alpha=$ALPHA" \
  --decode_from_file=$DECODE_FILE

cat $DECODE_FILE.$MODEL.$HPARAMS.beam$BEAM_SIZE.alpha$ALPHA.decodes
