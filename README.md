Logi-gif
========

It loads and displays gifs in Logisim. Uses Logisim and Python, as well as the OpenCV and Convert library.

<p>Use for 64x64 gif:</p>
<p><code>convert image-name.gif -colorspace Gray -trim +repage -resize 64x64\! image-name_resized.gif</code></p>
<p><code>convert image-name_resized.gif image-name_resized_%d.png</code></p>
<p>Go into images6464.py and change new_filename to image-name</p>
<p>run <code>python images6464.py</code></p>
<p>take image-name_1.txt image-name_2.txt image-name_3.txt image-name_4.txt and load it into logisim-img-64x64vfinal.circ into data 1, data 2, data 3, and data 4 respectively.</p>
<p>Do Command+K to run the gif.</p>

