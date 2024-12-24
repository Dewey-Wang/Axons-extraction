#Define parameters for our model.

encoder_weights = 'imagenet'
BACKBONE = 'vgg16'  #Try vgg16, efficientnetb7, inceptionv3, resnet50
activation = 'softmax'
n_classes = 3
channels=3

LR = 0.0001
optim = tf.keras.optimizers.Adam(LR)

# Segmentation models losses can be combined together by '+' and scaled by integer or float factor
# set class weights for dice_loss (car: 1.; pedestrian: 2.; background: 0.5;)
dice_loss = sm.losses.DiceLoss(class_weights=np.array([0.333, 0.333, 0.333])) #优点：对于不平衡的数据集和像素级别的分割任务效果较好，能够更好地处理类别间的不平衡。缺点：对噪声敏感，容易受到边缘效应的影响。
focal_loss = sm.losses.CategoricalFocalLoss()#优点：能够解决类别不平衡问题，通过调节alpha和gamma参数可以进一步调整损失函数的重点。缺点：需要调节额外的参数，可能需要进行一定的调参工作。
jaccard_loss = sm.losses.JaccardLoss() #优点：度量了预测和标签之间的相似度，对于不平衡的数据集效果较好。缺点：对于像素级别的分割任务可能存在不连续性，需要额外处理。

total_loss = dice_loss + (1 * focal_loss) + jaccard_loss


# actulally total_loss can be imported directly from library, above example just show you how to manipulate with losses
# total_loss = sm.losses.binary_focal_dice_loss # or sm.losses.categorical_focal_dice_loss 

metrics = [sm.metrics.IOUScore(threshold=0.5)]


preprocess_input = sm.get_preprocessing(BACKBONE)


#Preprocess input data - otherwise you end up with garbage resutls 
# and potentially model that does not converge.
X_train_prep = preprocess_input(X_train)
X_test_prep = preprocess_input(X_test)


#Define the model. Here we use Unet but we can also use other model architectures from the library.
model = sm.Unet(BACKBONE, classes=n_classes, 
                input_shape=(32, 64, 64, channels), 
                encoder_weights=encoder_weights,
                activation='softmax')

model.compile(optimizer = optim, loss=total_loss, metrics=metrics)

from tensorflow.keras.callbacks import ModelCheckpoint, ReduceLROnPlateau, CSVLogger, EarlyStopping
#early_stopping = EarlyStopping(monitor='val_loss', patience=20, restore_best_weights = False)
model_checkpoint = ModelCheckpoint('./best_model.h5', monitor='val_loss', save_best_only=True)

callbacks=[#early_stopping,
           model_checkpoint,
                  CSVLogger('./history_au.csv'),
            ReduceLROnPlateau(monitor='val_loss', factor=0.1, patience=10)
          ]

#Fit the model
history=model.fit(X_train_prep, 
                  y_train,
                  batch_size=2, 
                  epochs=500,
                  validation_data=(X_test_prep,y_test),
                  callbacks=callbacks)