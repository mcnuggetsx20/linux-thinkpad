function ExecuteToWindow(command)
  --sprawdzamy czy taki bufor juz istnieje zeby go w razie w wyjebac
  local existing_bufnr = vim.fn.bufnr("output")
  if existing_bufnr ~= -1 and vim.fn.bufexists(existing_bufnr) == 1 then
    -- Bufor już istnieje, przełącz się do niego
    vim.api.nvim_buf_delete(existing_bufnr, { force = true })
    print('Buffer "output" already exists. Shell command ' .. command .. ' executed.')
  end

  local output = vim.fn.systemlist(command) --output komendy
  vim.cmd('botright 50 vnew') --tworzenie okna

  local winnr = vim.api.nvim_get_current_win() --po poprzedniej komendzie wjechalismy do nowego okna
  local bufnr = vim.api.nvim_win_get_buf(winnr) --zdobywanie bufora w tym nowym oknie

  --jakies luzne ustawienia bufora
  vim.api.nvim_buf_set_option(bufnr, 'swapfile', false)
  vim.api.nvim_buf_set_option(bufnr, 'filetype', 'shelloutput')
  vim.api.nvim_buf_set_option(bufnr, 'buftype', 'nofile')
  vim.api.nvim_buf_set_option(bufnr, 'bufhidden', 'wipe')

  vim.api.nvim_buf_set_name(bufnr, "output") --zmiana nazwy bufora
  vim.api.nvim_buf_set_lines(bufnr, 0, -1, false, output) --wstawienie wyniku komendy do okna

  vim.cmd('wincmd h')
end

vim.cmd('command! -complete=shellcmd -nargs=+ Shell call v:lua.ExecuteToWindow(<q-args>)')
vim.cmd [[command WW silent! :w !sudo tee %]]

function custom_action()
  local file_type = vim.bo.filetype --current filetype
  local current_file = vim.fn.expand('%:p')

  vim.cmd(":w")

  if file_type == 'python' then
      vim.cmd("silent Shell python -B " .. current_file)

  elseif file_type == 'java' then
      vim.cmd("silent Shell javac " .. current_file .. " && java " .. current_file)

  else
      --default case
    ExecuteInShell('w | !echo "Default command"')
  end
end
