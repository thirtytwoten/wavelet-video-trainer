# Wavelet Video Trainer

embedded youtube video web app that dims sound and video brightness based on values sent from flask server for use in neurofeedback training

## To run this app locally:

`% git clone https://github.com/thirtytwoten/wavelet-video-trainer.git`
`% cd wavelet-video-trainer`
`% python3 -m pip install -r requirements.txt`
`% python3 app.py`

Open web app running on localhost:5000 on web browser passing in video id of some youtube video as the 'video' url param, e.g. http://localhost:5000/?video=SOCrBa8peCg

If you just open http://localhost:5000/ it will prompt you for a video id.

The video ID can be found by looking at the url of the youtube video. Look at the value after v=
example: https://www.youtube.com/watch?v=SOCrBa8peCg >> SOCrBa8peCg