def centre_text(*args):
    # text=""
    # for arg in args:
    #     text += str(arg) + "-"
    text ="-".join([str(arg) for arg in args])
    left_margin = (80 - len(text)) // 2
    print(" " * left_margin, text)
    
    
centre_text("spam and eggs")
centre_text(12)
centre_text("VICTORY")
centre_text("WHAT IS LIFE WITHOUT PURPOSE?")