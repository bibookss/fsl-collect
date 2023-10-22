# fsl-collect
A web app to aid in collecting Filipino Sign Language data for an FSL-to-text app. It follows the format of this [Youtube video](https://www.youtube.com/watch?v=doDUihpj6ro). It saves the keypoint in a npy file.

### To do
- [/] Allow a predefined set of actions to be acted out for a certain amount of frames
- [/] Save each keypoint to a file grouped per action
- [ ] Allow video upload
- [ ] Configure for mobile

## Installation 
```
pip install -r requirements.txt
```

## Usage
Update the signs.json file to cater your needed part of speech and words/phrases.
```
cd src
streamlit run main.py
```