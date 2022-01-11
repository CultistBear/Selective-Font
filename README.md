# Selective-Font

## What is this?

Selective Font helps user to change an existing TrueType font file so that only specific characters and symbols that are needed from the original TrueType font file, are present in the new TrueType font file (ttf for short). This is done to reduce the size of the original ttf significantly by removing anything that is not needed in the font, and thus helps when you need to add your own font to your website or something similar.

## Requirements

This project requires [FontTools](https://github.com/fonttools/fonttools) and thus requires [Python](http://www.python.org/download/) 3.7 or later.

FontTools is listed in the Python Package Index (PyPI), so you can install it with [pip](https://pip.pypa.io):

```
pip install fonttools
```
## Syntax and an Example
We will be taking [Newsreader — Extra-light italic](https://fonts.google.com/share?selection.family=Newsreader:ital,wght@1,200) as an example for this test run.

The original file for __Newsreader — Extra-light italic__ is around __480 KB__

![image](https://user-images.githubusercontent.com/79724656/149006094-53f49ef9-7b61-4810-91f0-32e8c96fcb5d.png)

With all the proper fonts

![image](https://user-images.githubusercontent.com/79724656/149006795-4ace5827-f9f1-488b-83ee-c866f50223d6.png)

Using the Selective Font script, we convert our desired sentence or letters into this font to get the new ttf file.

```bash
Enter string or letters you want to convert:
$ I have a brown fox

Path to TTF File (path\to\file\file.ttf):
$ C:\Users\Public\Documents\Newsreader-Italic-VariableFont_opsz,wght.ttf

Completed!
```

Looking at the newly generated file, we find that the size for the new ttf file, __Newsreader-Italic-VariableFont_opsz,wght.subset.ttf__ is around __20 KB__.

![image](https://user-images.githubusercontent.com/79724656/149008028-95ad32f1-c2b5-4060-95d2-3d14c397ead6.png)

And it only has the fonts we desire.

![image](https://user-images.githubusercontent.com/79724656/149008231-abcfcd46-954d-4b35-8c74-9927bdd219e1.png)

And this is more or less how Selective Font is used.

Even if we take one step further, and convert all the letters in the alphabet, digits and commonly used symbols into the desired font,

```
Enter string or letters you want to convert:
ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz[\]^_`!"#$%&'()*+,-./0123456789:;<=>?@{}|~

Path to TTF File (path\to\file\file.ttf):
C:\Users\Public\Documents\Newsreader-Italic-VariableFont_opsz,wght.ttf

Completed!
```

We find that the size of the newly generated ttf font (__135 KB__) is still not as big as the original

![image](https://user-images.githubusercontent.com/79724656/149009899-8202b503-6e37-40cc-9b6d-c7808ce45fd1.png)

since we have kept only the things we need, the size of the ttf file has decreased by roughly 3.5 times.

![image](https://user-images.githubusercontent.com/79724656/149010231-73c1c03e-136d-4504-9625-726d2a966cdd.png)




