--jakis wygladzik ni
vim.o.termguicolors = true
vim.cmd [[colorscheme gruvbox]]

--bazyczne ustawienia
LANG = 'en_US'
vim.opt.hls = true
vim.opt.is = true
vim.opt.cb = 'unnamedplus'
vim.opt.expandtab = true
vim.opt.tabstop = 4
vim.opt.shiftwidth = 4
vim.opt.ignorecase = true
vim.opt.si = true
vim.opt.showmode = false
vim.opt.scrollback = 1000
vim.opt.belloff = "all"

--te dziwne rozne foldery co se vim robi
vim.opt.backup = true
vim.opt.undofile = true
vim.opt.undodir = "/home/mcnuggetsx20/Documents/vimfiles/undo"
vim.opt.backupdir = "/home/mcnuggetsx20/Documents/vimfiles/backup"
vim.opt.directory = "/home/mcnuggetsx20/Documents/vimfiles/swp"

--kursor
vim.o.guicursor="n:blinkon100,i:hor15-blinkon100"

--jakies luzne autocmd
vim.cmd [[autocmd BufEnter * silent! lcd %:p:h]]
vim.cmd [[autocmd BufNewFile *.cpp 0r /home/mcnuggetsx20/.config/ClassicTemplate.txt]]
vim.cmd [[autocmd VimEnter * :silent exec "!kill -s SIGWINCH $PPID"]]

--numerki od williama lina
vim.o.number = true

vim.cmd([[
  augroup numbertoggle
    autocmd!
    autocmd BufEnter,FocusGained,InsertLeave * set relativenumber
    autocmd BufLeave,FocusLost,InsertEnter * set norelativenumber
    autocmd BufLeave,FocusLost,InsertEnter * set number
  augroup END
]])
