Logi-gif
========

Logi-gif loads and displays gifs in Logisim. Uses Logisim and Python, as well as the OpenCV and Convert library.

## To make 64x64 gifs:
<p><code>convert [gif-name].gif -coalesce [gif-name].gif</code></p>
<p><code>convert [gif-name].gif -colorspace Gray -resize 64x64\! [gif-name]_resized.gif</code></p>
<p><code>convert [gif-name]_resized.gif [image-name]_resized_%d.png</code></p>
<p>Go into images6464.py and change new_filename to [gif-name]</p>
<p>run <code>python images6464.py</code></p>
<p>take [gif-name]_1.txt [gif-name]_2.txt [gif-name]_3.txt [gif-name]_4.txt and load it into logisim-img-64x64vfinal.circ into the data 1, data 2, data 3, and data 4 RAMs (respectively).</p>
<p>Do Command+K to run the gif.</p>

## To make 32x32 gifs:
<p><code>convert [gif-name].gif -coalesce [gif-name].gif</code></p>
<p><code>convert [gif-name].gif -colorspace Gray -resize 32x32\! [gif-name]_resized.gif</code></p>
<p><code>convert [gif-name]_resized.gif [gif-name]_resized_%d.png</code></p>
<p>Go into images6464.py and change new_filename to [gif-name]</p>
<p>run <code>python images6464.py</code></p>
<p>take [gif-name].txt load it into logisim-img-64x64vfinal.circ into the data RAM.</p>
<p>Do Command+K to run the gif.</p>

