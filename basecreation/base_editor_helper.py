from PIL import Image, ImageFont, ImageDraw, ImageFilter

def skillname_text_creator(skillname, charwid, rowheight, rowextra, fontsize, color):
    fontsize = 9
    # line character limit 60, pixel length is 1150
    bgcol = (25,13,100)
    if color == 'default':
        bgcol = (25,13,100)
    font = ImageFont.truetype('georgiab.ttf', fontsize)
    if '*' in skillname:
        namesplit = skillname.split('*')
        skillicon = Image.open('skillheaders/'+namesplit[0]+'.png')
        x,y = skillicon.size
        # if y < (rowheight + rowextra):
        #     ratio = (rowheight + rowextra)/y
        #     skillicon = skillicon.resize((int(ratio * x),rowheight + rowextra))
        #     x,y = skillicon.size
        #print("GS ICON SIZE")
        #print(x)
        im = Image.new('RGBA', (x + int(font.getlength(namesplit[1]))+3, rowheight), color=(255,255,255,0)) # clear strip
        im0 = Image.new(mode = "RGBA", size = (x + int(font.getlength(namesplit[1])), rowheight-2), color=bgcol)  # background color strip
        image = Image.new(mode = "RGBA", size = (x + int(font.getlength(namesplit[1])), rowheight), color=(255,255,255))  # white strip
        im.paste(image, (3,0), image)
        im.paste(im0, (3,1), im0)
        draw = ImageDraw.Draw(im)
        im.paste(skillicon, (0,0), skillicon)
        draw.text((x + 3,1), namesplit[1], (255, 255, 255), font=font)
        if (x + int(charwid*len(namesplit[1])) + 10) > 1150:
            im = im.resize((1150,rowheight+rowextra)) 
        im.save("skillname.png", quality=95)
    else:
        #im = Image.new(mode = "RGB", size = (int(charwid*len(skillname)) + 10, rowheight + rowextra), color=bgcol)
        #print('rowheight')
        #print(rowheight)
        im = Image.new(mode = "RGBA", size = (int(font.getlength(skillname)),rowheight), color=(255,255,255))
        im0 = Image.new(mode = "RGBA", size = (int(font.getlength(skillname)),rowheight-2), color=bgcol)
        im.paste(im0, (0,1), im0)
        draw = ImageDraw.Draw(im)
        #draw.text((5,2), skillname, (255, 255, 255), font=font)
        draw.text((1,0), skillname, (255, 255, 255), font=font)
        #print(int(font.getlength(skillname)[0]) + 20)
        if (int(font.getlength(skillname)) + 6) > 280:
            #print('enter')
            im = im.resize((280,rowheight+rowextra))
        im.save("skillname.png", quality=95)

def get_rows(skills, charwid, rowheight, rowextra, fontsize, attributes, font, rowlen):
    rows = 0
    for i in skills:
        if i != '':
            skilltext = i.split('|')
            idx = 0
            while idx < len(skilltext):
                if idx == 0:
                    skillname_text_creator(skilltext[0], charwid, rowheight, rowextra, fontsize, 'default')
                    imskl = Image.open('skillname.png')
                    x,y = imskl.size
                    x = x + 20
                    rowlen = rowlen - x
                #elif skilltext[idx] in attributes:
                #    rowlen = rowlen - 30
                #    if rowlen < 0:
                #        rowlen = 1150
                #        rows = rows + 1
                #        rowlen = rowlen - 30
                elif  skilltext[idx].lower() in attributes:
                    skltxt = skilltext[idx].lower()
                    imskl = Image.open('icons/'+ skltxt +'.png')
                    x,y = imskl.size
                    if y > 40:
                        #print(y)
                        imskl = imskl.resize((rowheight,rowheight))
                        x,y = imskl.size
                    rowlen = rowlen - x
                    if rowlen < 0:
                        rowlen = 1150
                        rows = rows + 1
                        rowlen = rowlen - x
                else:
                    strskl = skilltext[idx].split(' ')
                    j = 0
                    while j < len(strskl):
                        # decreasing row length per character
                        rowlen = rowlen - (int(font.getlength(strskl[j])))
                        if rowlen < 0:
                            rowlen = 1150
                            rows = rows + 1
                            rowlen = rowlen - (int(font.getlength(strskl[j])))
                        else:
                            # accounting for the space after each word
                            rowlen = rowlen - int(font.getlength(' '))
                        j = j + 1
                idx = idx + 1
            rows = rows + 1
    return rows

def drawCharBorder(draw, xpos, ypos, inpchar, font, border):
    if border:
        # layer 1
        draw.text((xpos, ypos), inpchar, font=font, fill=(255,255,255))

        draw.text((xpos, ypos-1), inpchar, font=font, fill=(255,255,255))
        draw.text((xpos, ypos+1), inpchar, font=font, fill=(255,255,255))
        draw.text((xpos-1, ypos), inpchar, font=font, fill=(255,255,255))
        draw.text((xpos+1, ypos), inpchar, font=font, fill=(255,255,255))

        draw.text((xpos-1, ypos-1), inpchar, font=font, fill=(255,255,255))
        draw.text((xpos+1, ypos-1), inpchar, font=font, fill=(255,255,255))
        draw.text((xpos-1, ypos+1), inpchar, font=font, fill=(255,255,255))
        draw.text((xpos+1, ypos+1), inpchar, font=font, fill=(255,255,255))

    # layer 2
    # draw.text((xpos, ypos-2), inpchar, font=font, fill=(255,255,255))
    # draw.text((xpos, ypos+2), inpchar, font=font, fill=(255,255,255))
    # draw.text((xpos-2, ypos), inpchar, font=font, fill=(255,255,255))
    # draw.text((xpos+2, ypos), inpchar, font=font, fill=(255,255,255))

    # draw.text((xpos-2, ypos-1), inpchar, font=font, fill=(255,255,255))
    # draw.text((xpos+2, ypos-1), inpchar, font=font, fill=(255,255,255))
    # draw.text((xpos-2, ypos+1), inpchar, font=font, fill=(255,255,255))
    # draw.text((xpos+2, ypos+1), inpchar, font=font, fill=(255,255,255))

    # draw.text((xpos-1, ypos-2), inpchar, font=font, fill=(255,255,255))
    # draw.text((xpos+1, ypos-2), inpchar, font=font, fill=(255,255,255))
    # draw.text((xpos-1, ypos+2), inpchar, font=font, fill=(255,255,255))
    # draw.text((xpos+1, ypos+2), inpchar, font=font, fill=(255,255,255))

    # draw.text((xpos-2, ypos-2), inpchar, font=font, fill=(255,255,255))
    # draw.text((xpos+2, ypos-2), inpchar, font=font, fill=(255,255,255))
    # draw.text((xpos-2, ypos+2), inpchar, font=font, fill=(255,255,255))
    # draw.text((xpos+2, ypos+2), inpchar, font=font, fill=(255,255,255))

    # writing
    draw.text((xpos, ypos), inpchar, font=font, fill=(0,0,0))
    #draw.text((xpos-1, ypos-1), inpchar, font=font, fill=(0,0,0))
    #draw.text((xpos+1, ypos-1), inpchar, font=font, fill=(0,0,0))
    #draw.text((xpos-1, ypos+1), inpchar, font=font, fill=(0,0,0))
    #draw.text((xpos+1, ypos+1), inpchar, font=font, fill=(0,0,0))
