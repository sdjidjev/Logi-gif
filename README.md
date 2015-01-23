Logi-gif
========

Logi-gif loads and displays gifs in Logisim. Uses Logisim and Python, as well as the OpenCV and ImageMagick library (installed with brew on Mac OS X). <b>DISCLAIMER: </b> Some gifs work better than others.

Before loading a new gif, do Command+R, and make sure the gif is in the same directory as the python scripts.
## To make 64x64 gifs:
<p><code>convert [gif-name].gif -coalesce [gif-name].gif</code></p>
<p><code>convert [gif-name].gif -colorspace Gray -resize 64x64\! [gif-name]_resized.gif</code></p>
<p><code>convert [gif-name]_resized.gif [gif-name]_resized_%d.png</code></p>
<p>Run <code>python images64x64.py</code></p>
<p>Enter the gif name when it prompts you to do so. Make sure the gif is in the same directory as the code!</p>
<p>Take [gif-name]_1.txt [gif-name]_2.txt [gif-name]_3.txt [gif-name]_4.txt and load it into logisim-img-64x64.circ into the data 1, data 2, data 3, and data 4 RAMs (respectively).</p>
<p>Do Command+K to run the gif.</p>

## To make 32x32 gifs:
<p><code>convert [gif-name].gif -coalesce [gif-name].gif</code></p>
<p><code>convert [gif-name].gif -colorspace Gray -resize 32x32\! [gif-name]_resized.gif</code></p>
<p><code>convert [gif-name]_resized.gif [gif-name]_resized_%d.png</code></p>
<p>Run <code>python images32x32.py</code></p>
<p>Enter the gif name when it prompts you to do so. Make sure the gif is in the same directory as the code!</p>
<p>Take [gif-name].txt load it into logisim-img-32x32.circ into the data RAM.</p>
<p>Do Command+K to run the gif.</p>

## Demo
[![Logi-gif Demo](http://img.youtube.com/vi/5OTRVfKFdp4/0.jpg)](http://www.youtube.com/watch?v=5OTRVfKFdp4)

