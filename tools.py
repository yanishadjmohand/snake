if __name__=="__main__":
    print("oui")
def addition (n,m):
    return(n+m)

def tracer_serpent(snake):
    for z in snake:
        x=z[0]*20
        y=z[1]*20
        width=20
        height=20
        rect=pg.Rect(x, y, width, height)
        pg.draw.rect(screen, (255,0,0), rect)