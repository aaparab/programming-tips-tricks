## Using `amsrefs` to compile bibliography:

### Example 1: Just one file
```
% mytex.tex
\documentclass{article}

\usepackage{amsrefs}
\begin{document}

This is a paragraph. I am citing article \cite{MR3968914}. This ends the amsrefs example. 

\begin{bibdiv}
\begin{biblist}

\bib{MR3968914}{article}{
   author={Parab, Abhishek},
   title={Absolute convergence of the twisted trace formula},
   journal={Math. Z.},
   volume={292},
   date={2019},
   number={1-2},
   pages={529--567},
   issn={0025-5874},
   review={\MR{3968914}},
   doi={10.1007/s00209-019-02290-0},
}

\end{biblist}
\end{bibdiv}

\end{document}
```

### Example 2: Different `.ltb` file
```
% myamsrefs.ltb
\bib{MR3968914}{article}{
   author={Parab, Abhishek},
   title={Absolute convergence of the twisted trace formula},
   journal={Math. Z.},
   volume={292},
   date={2019},
   number={1-2},
   pages={529--567},
   issn={0025-5874},
   review={\MR{3968914}},
   doi={10.1007/s00209-019-02290-0},
}
```

```
% mytex.tex
\documentclass{article}

\usepackage{amsrefs}
\begin{document}

This is a paragraph. I am citing article \cite{MR3968914}. This ends the amsrefs example. 

\begin{bibdiv}
\begin{biblist}
\bibselect{myamsrefs}
\end{biblist}
\end{bibdiv}

\end{document}
```

### Notes: [Source](http://www.bakoma-tex.com/doc/latex/amsrefs/amsrdoc.pdf)

- Each `\bibcommand` in the `.ltb` file must begin on a new line, and the first  two 
arguments  and  the  open  brace  of  the  third  argument  must  beon  that  same  line. 
Failure  to  follow  this  format  may  result  in `amsrefs` getting terribly confused 
and aborting the processing of your document.

- Because all processing is being handled by LATEX, the contents of `thebibliography` 
can be printed on the first pass; citation labels, consequently, are resolved on the second pass.

