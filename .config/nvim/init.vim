colorscheme desert

let g:currentmode={
       \ 'n'  : 'NORMAL ',
       \ 'v'  : 'VISUAL ',
       \ 'V'  : 'V·Line ',
       \ "\<C-V>" : 'V·Block ',
       \ 'i'  : 'INSERT ',
       \ 'R'  : 'R ',
       \ 'Rv' : 'V·Replace ',
       \ 'c'  : 'Command ',
       \ 't'  : 'TERMINAL ',
       \}

set langmenu=en_US
let $LANG = 'en_US'
set hls
set is
set cb=unnamedplus
"set gfn=Fixedsys\ Excelsior\ 3.01-L2\ Mono\ 18
set gfn=8514oem\ 14
set expandtab
set tabstop=4
set shiftwidth=4
set si
set noshowmode
set guicursor=n:blinkon100,i:hor15-blinkon100
inoremap { {}<Left>
inoremap {<CR> {<CR>}<Esc>O
inoremap {{ {
inoremap {} {}
set backup
set undofile
set ignorecase

set scrollback=1000

set undodir=/home/mcnuggetsx20/Documents/vimfiles/undo
set backupdir=/home/mcnuggetsx20/Documents/vimfiles/backup
set directory=/home/mcnuggetsx20/Documents/vimfiles/swp

"set guioptions -=m 
"set guioptions -=T
"set guioptions-=r

:lcd %:p:h

set belloff=all

set laststatus=2

set statusline+=%#keyword#
set statusline+=\ %{(g:currentmode[mode()])}

set statusline+=%#statusline#
set statusline+=\ %F\ %=\ 

set statusline+=%#number#
set statusline+=\ %L\ lines

set statusline+=%#string#
set statusline+=\ %{wordcount().words}\ words

set statusline+=%#function#
set statusline+=\ [NVIM]

function! s:ExecuteInShell(command)
  let command = join(map(split(a:command), 'expand(v:val)'))
  let winnr = bufwinnr('^' . command . '$')
  silent! execute  winnr < 0 ? 'botright 50 vnew ' . fnameescape(command) : winnr . 'wincmd w'
  setlocal buftype=nowrite bufhidden=wipe nobuflisted noswapfile nowrap number
  echo 'Execute ' . command . '...'
  silent! execute 'silent %!'. command
  silent! execute 'resize '
  silent! redraw
  silent! execute 'au BufUnload <buffer> execute bufwinnr(' . bufnr('#') . ') . ''wincmd w'''
  silent! execute 'nnoremap <silent> <buffer> <LocalLeader>r :call <SID>ExecuteInShell(''' . command . ''')<CR>'
  echo 'Shell command ' . command . ' executed.'
endfunction
command! -complete=shellcmd -nargs=+ Shell call s:ExecuteInShell(<q-args>)

" Open multiple tabs at once
fun! OpenMultipleTabs(pattern_list)
    for p in a:pattern_list
        for c in glob(l:p, 0, 1)
            execute 'tabnew ' . l:c
        endfor
    endfor
endfun

command! -bar -bang -nargs=+ -complete=file Tabsnew call OpenMultipleTabs([<f-args>])


autocmd VimEnter * :silent exec "!kill -s SIGWINCH $PPID"
:autocmd BufNewFile *.cpp 0r /home/mcnuggetsx20/.config/ClassicTemplate.txt
nnoremap <F5> :w <bar> !brave % & <cr> 
nnoremap <F4> :w <bar> Shell python -B % <cr>
command WW silent! :w !sudo tee %

nnoremap x "_x
vmap x "_d
nnoremap dd "_dd
nnoremap c "_c
nnoremap cc "_cc
tnoremap <Esc> <C-\><C-n>

noremap s "_ddko

nnoremap <F2> :%y+ <cr>

nnoremap <C-j> :tabprevious <CR>
nnoremap<C-k> :tabnext <CR>
nnoremap <C-x> :tabclose <CR>

set nu
augroup numbertoggle
    autocmd!
    autocmd BufEnter,FocusGained,InsertLeave * set rnu
    autocmd BufLeave,FocusLost,InsertEnter * set nornu
	autocmd BufLeave,FocusLost,InsertEnter * set nu
augroup END

call plug#begin()

Plug 'neovim/nvim-lspconfig'
Plug 'hrsh7th/nvim-compe'
Plug 'ayu-theme/ayu-vim' " or other package manager
Plug 'blueshirts/darcula'
Plug 'lifepillar/vim-solarized8'
Plug 'NLKNguyen/papercolor-theme'
Plug 'nvim-treesitter/nvim-treesitter'

call plug#end()

set termguicolors
set background=light
"let ayucolor="light"
"colorscheme ayu
colorscheme solarized8_high
"colorscheme PaperColor

lua << EOF
    require('lspconfig').pyright.setup{
    handlers = {
            ['textDocument/publishDiagnostics'] = function(...) end
        },

      settings = {
        python = {
          analysis = {
            autoSearchPaths = true,
            useLibraryCodeForTypes = true
          }
        }
      }
    }
EOF

set completeopt=menuone,noselect
let g:compe = {}
let g:compe.enabled = v:true
let g:compe.autocomplete = v:true
let g:compe.debug = v:false
let g:compe.min_length = 1
let g:compe.preselect = 'enable'
let g:compe.throttle_time = 80
let g:compe.source_timeout = 200
let g:compe.incomplete_delay = 400
let g:compe.max_abbr_width = 100
let g:compe.max_kind_width = 100
let g:compe.max_menu_width = 100
let g:compe.documentation = v:true
let g:compe.source = {}
let g:compe.source.path = v:true
let g:compe.source.buffer = v:true
let g:compe.source.calc = v:true
let g:compe.source.nvim_lsp = v:true
let g:compe.source.nvim_lua = v:true
let g:compe.source.vsnip = v:true
let g:compe.source.ultisnips = v:true

inoremap <silent><expr> <C-Space> compe#complete()
inoremap <silent><expr> <CR>      compe#confirm('<CR>')
inoremap <silent><expr> <C-e>     compe#close('<C-e>')
inoremap <silent><expr> <C-f>     compe#scroll({ 'delta': +4 })
inoremap <silent><expr> <C-d>     compe#scroll({ 'delta': -4 })
