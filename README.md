# Arteye
![alt text](https://github.com/husninazer/arteye/blob/master/ARTEYE%20LOGO.gif "Logo Title Text 1")

Capture tracks from eye movement and then convert it to an art work by using neural network model - style transfer.


## Using the gaze tracking.
<em>Credits: antoinelame</em>

 Install dependancies 
 
 Start python example.py

![alt text]( https://github.com/husninazer/arteye/blob/master/ezgif.com-crop.gif "gif 1")


## Using the style transfer application
<em>Credits:DavidCai1993</em>
### Download The [VGG-19 Model](https://github.com/DavidCai1993/vgg19-tensorflowjs-model)

```sh
npm run model
```

### Install Dependences

```sh
npm install
```
### Start the process

```js
node ./transfer.js transfer -c <contentImagePath> -s <styleImagePath> -o <outputImagePath> [--gpu]
```

## Samples

### Gaze tracked image
![alt text](https://github.com/husninazer/arteye/blob/master/style-transfer/images/input1.png "gif 1")

### Art Output
![alt text]( https://github.com/husninazer/arteye/blob/master/style-transfer/output.jpg "gif 1")
