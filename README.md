Logi-gif
========

It loads and displays gifs in Logisim. Uses Logisim and Python, as well as the OpenCV and Convert library.

<p>Use for 64x64 gif:</p>
<p>convert <image-name>.gif -colorspace Gray -trim +repage -resize 64x64\! <image-name>_resized.gif</p>
<p>convert <image-name>_resized.gif <image-name>_resized_%d.png</p>
<p>Go into images6464.py and change new_filename to <image-name></p>
<p>run python images6464.py</p>
<p>take <image-name>_1.txt <image-name>_2.txt <image-name>_3.txt <image-name>_4.txt and load it into logisim-img-64x64vfinal.circ into data 1, data 2, data 3, and data 4 respectively.</p>
<p>Do Command+K to run the gif.</p>

