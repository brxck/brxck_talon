work <number_small>: user.desktop(number_small)
work (next|right): user.desktop_next()
work (last|left): user.desktop_last()
work show: user.desktop_show()
send <number_small>: user.window_move_desktop(number_small)
send (last|left): user.window_move_desktop_left()
send (next|right): user.window_move_desktop_right()
carry <number_small>:
  user.window_move_desktop(number_small)
  user.desktop(number_small)
carry (last|left):
  user.window_move_desktop_left()
  user.desktop_last()
carry (next|right):
  user.window_move_desktop_right()
  user.desktop_next()
