# Arteye

Capture tracks from eye movement and then convert it to an art work by using neural network model - style transfer.


## Using the gaze tracking.
Credits: antoinelame
Install dependancies 
Start python example.py

## Using the style transfer application
Credits:DavidCai1993
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

