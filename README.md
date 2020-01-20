# LaTeX Glossary Entry
This small [Python](https://www.python.org) program creates efficiently a **full LaTeX glossary entry** to your clipboard and command line.

Why doing it by hand when you can do it by code?

The benefit of using a [LaTeX](https://www.latex-project.org) [Glossary](http://tug.ctan.org/macros/latex/contrib/glossaries/glossariesbegin.pdf) is to get abbreviations and their descriptions nicely and automatically structured in your document.

But only with the generated LaTeX-Code, an example is below. 

# Run
By running

```
python lge.py "Volume Clipping" "VC" "selectively disables or enables rendering operations inside a \Gls{ri}, which is in practice predominantly the intersection of two or more overlapping objects"
```

a full LaTeX glossary entry as

```
\newglossaryentry{VCG}{
    name={VC},
    description={Volume Clipping (VC) selectively disables or enables rendering operations inside a \Gls{ri}, which is in practice predominantly the intersection of two or more overlapping objects}
}
\newglossaryentry{VC}{
    type=\acronymtype,
    name={VC},
    description={Volume Clipping},
    first={Volume Clipping (VC) \glsadd{VCG}},
    see=[Glossary:]{VCG}
}
```
will be printed on the command line for you to verify the result and also copied to your clipboard for direct pasting.

## Dependencies
Make sure you have Python's `pip` and on Ubuntu `xclip` installed. You can install it on Ubuntu with:

```
sudo apt-get install python-pip xclip
```
and [Pyperclip](https://github.com/asweigart/pyperclip) by running:

```
pip install pyperclip
```
or both with
```
sudo apt-get install python-pip xclip && pip install pyperclip
```
