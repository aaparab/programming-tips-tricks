" Paste without indentation by default
" Solution here - https://stackoverflow.com/a/38258720

let &t_SI .= "\<Esc>[?2004h"
let &t_EI .= "\<Esc>[?2004l"

inoremap <special> <expr> <Esc>[200~ XTermPasteBegin()

function! XTermPasteBegin()
  set pastetoggle=<Esc>[201~
  set paste
  return ""
endfunction

" Use dark background (so comments are not dark blue)
set background=dark
" Changes color from `peachpuff` (default for light) to `ron` (default for dark)

" Vim color themes: https://unix.stackexchange.com/a/88880
