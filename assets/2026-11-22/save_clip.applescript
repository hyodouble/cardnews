on run argv
  set f to open for access POSIX file (item 1 of argv) with write permission
  set eof f to 0
  write (the clipboard as «class PNGf») to f
  close access f
end run
