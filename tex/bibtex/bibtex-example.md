## Example of using `bibtex` for generating bibliography

1. Make a `.bib` file with all bibliography entries `mybib.bib`
2. In the `.tex` file, make a bibliography by adding the following two lines before `\end{document}`:
    ```
    \bibliography{mybib}{}
    \bibliographystyle{amsalpha}    % amsalpha
    ```
3. In the same file, cite the articles in `mybib.bib` as `\cite{MR3968914}`.
4. Compile `latex` → `bibtex` → `latex` → `latex` to generate output. 
