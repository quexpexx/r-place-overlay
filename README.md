# Thanks everyone for the great time on r/place.


# Original README --------------------

# What is this?
It's a userscript that, following a specific template, puts an overlay over your r/place canvas for what a pixel *should* be.
# How do I install it?
1. Get a userscript manager (like Tampermonkey on Chrome or Violentmonkey on Firefox, Tampermonkey on Firefox didn't work for me with this script for some reason).
2. Click on `userscript.user.js` in the files
3. Click on Raw.
4. Your userscript manager should prompt you to install the script. Install it.
5. Refresh r/place.
# Why do I need this?
So you don't have to keep wondering where to place a pixel, what color it should be, or refer to some template constantly. Just fork this and make your own overlay.
# How do I make my own overlay?
1. Fork this repo.
2. Modify the link in `userscript.user.js` to the correct direct link (your fork's link) to `template.png`
2. Edit `canvas.png`, it's an image of the entire canvas. Place your pixels on the correct positions.
3. Run `expandpixels.py` (pillow is a dependency). It should convert your `canvas.png` file to a `template.png`
4. Add all the modified files, commit your changes, and push them.
# For contributors
If you've changed `canvas.png`, make sure you run `expandpixels.py` to get a proper `template.png`. Add both `canvas.png` and `template.png` into your pull request.  
If you've changed `template.png`, make sure you run `reducepixels.py` to get back a `canvas.png`. Add both `canvas.png` and `template.png` to your pull request.