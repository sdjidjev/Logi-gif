Logi-gif
========

Logi-gif loads and displays gifs in Logisim. Uses Logisim and Python, as well as the OpenCV and Convert library.

## For 64x64 gifs:
<p><code>convert [image-name].gif -coalesce [image-name].gif</code></p>
<p><code>convert [image-name].gif -colorspace Gray -resize 64x64\! [image-name]_resized.gif</code></p>
<p><code>convert [image-name]_resized.gif [image-name]_resized_%d.png</code></p>
<p>Go into images6464.py and change new_filename to [image-name]</p>
<p>run <code>python images6464.py</code></p>
<p>take [image-name]_1.txt [image-name]_2.txt [image-name]_3.txt [image-name]_4.txt and load it into logisim-img-64x64vfinal.circ into the data 1, data 2, data 3, and data 4 RAMs (respectively).</p>
<p>Do Command+K to run the gif.</p>

## For 32x32 gifs:
<p><code>convert [image-name].gif -coalesce [image-name].gif</code></p>
<p><code>convert [image-name].gif -colorspace Gray -resize 32x32\! [image-name]_resized.gif</code></p>
<p><code>convert [image-name]_resized.gif [image-name]_resized_%d.png</code></p>
<p>Go into images6464.py and change new_filename to [image-name]</p>
<p>run <code>python images6464.py</code></p>
<p>take [image-name].txt load it into logisim-img-64x64vfinal.circ into the data RAM.</p>
<p>Do Command+K to run the gif.</p>

