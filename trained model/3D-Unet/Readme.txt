I use the my own 3D unet model. The dataset that I used to train is only contain unqiue label 1,2,3. The data is without any normalize and standardize.


LR = 0.0001
optim = tf.keras.optimizers.Adam(LR)

# Segmentation models losses can be combined together by '+' and scaled by integer or float factor
# set class weights for dice_loss (car: 1.; pedestrian: 2.; background: 0.5;)
dice_loss = sm.losses.DiceLoss(class_weights=np.array([0.333, 0.333, 0.333])) #优点：对于不平衡的数据集和像素级别的分割任务效果较好，能够更好地处理类别间的不平衡。缺点：对噪声敏感，容易受到边缘效应的影响。
focal_loss = sm.losses.CategoricalFocalLoss()#优点：能够解决类别不平衡问题，通过调节alpha和gamma参数可以进一步调整损失函数的重点。缺点：需要调节额外的参数，可能需要进行一定的调参工作。
#jaccard_loss = sm.losses.JaccardLoss() #优点：度量了预测和标签之间的相似度，对于不平衡的数据集效果较好。缺点：对于像素级别的分割任务可能存在不连续性，需要额外处理。

total_loss = dice_loss + (1 * focal_loss)


# actulally total_loss can be imported directly from library, above example just show you how to manipulate with losses
# total_loss = sm.losses.binary_focal_dice_loss # or sm.losses.categorical_focal_dice_loss 

metrics = [sm.metrics.IOUScore(threshold=0.5)]

model = Unet3D(( 32, 64, 64, 3), n_classes=3)

model.compile(optimizer = optim, loss=total_loss, metrics=metrics)
print(model.summary())

from tensorflow.keras.callbacks import ModelCheckpoint, ReduceLROnPlateau, CSVLogger, EarlyStopping
#early_stopping = EarlyStopping(monitor='val_loss', patience=20, restore_best_weights = False)
model_checkpoint = ModelCheckpoint('./best_model.h5', monitor='val_loss', save_best_only=True)

callbacks=[#early_stopping,
           model_checkpoint,
                  CSVLogger('./history_au.csv'),
            ReduceLROnPlateau(monitor='val_loss', factor=0.1, patience=10)
          ]


#Fit the model
history=model.fit(X_train, 
                  y_train,
                  batch_size=2, 
                  epochs=150,
                  validation_data=(X_test,y_test),
                  callbacks=callbacks)