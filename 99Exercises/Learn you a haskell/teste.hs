main :: IO ()
main = do
    dpy <- openDisplay ""
    let dflt = defaultScreen dpy
    scr = defaultScreenOfDisplay dpy
    rootw <- rootWindow dpy dflt
    win <- mkUnmanagedWindow dpy scr rootw 0 0 200 100
    setTextProperty dpy win "The Clock" wM_NAME
    mapWindow dpy win
    updateWin dpy win

updateWin :: Display -> Window -> IO ()
updateWin dpy win = do
    drawInWin dpy win =<< date
    sync dpy False
    threadDelay (1 * 1000000)
    updateWin dpy win
