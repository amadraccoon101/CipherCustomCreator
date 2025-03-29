from PIL import Image, ImageFont, ImageDraw
from base_editor_helper import skillname_text_creator, get_rows, drawCharBorder   

def createSkills(skills, cardName, border, fname, fntsize, rwln):
    ###############################################################################################################
    ###############################################################################################################
    #Parse Input
    ###############################################################################################################
    # f = open("input.txt", "r", encoding="utf-8")

    # cardName = f.readline().strip()
    # print(cardName)

    # nextline = f.readline()
    # while nextline:
    #     skills.append(nextline.strip())
    #     nextline = f.readline()
    #print(skills)
    #print(supskl)
    ###############################################################################################################

    ###############################################################################################################
    ###############################################################################################################
    #Constants
    ###############################################################################################################
    skillatr = ['lis','bs','hs','es','cp','db','dv','ts','fs','ccs','cf','sts','gs','us','is','as','lvs2','lvs3','lvs4','lvs5','lvs7']
    skilltypes = ['act','auto','cont','bond','spec','supp','hand']

    attributes = ['armor','axe','beast','black','blue','bow','brawl','brown','dragon','dragonstone','knife',
                'fang','female','flier','green','lance','male','mirage','monster','purple','red', 'cyan',
                'staff','sword','tome','white','yellow','emblem',
                'act','auto','cont','bond','spec','supp','hand','opt',
                #'lis','bs','hs','cp','db','dv','ts','fs','ccs','cf','us','is','as','lvs2','lvs3','lvs4','lvs5','lvs7',
                'flip1','flip2','flip3','flip4','flip5','tap']

    actions = ['flip1','flip2','flip3','flip4','flip5','tap']
    ###############################################################################################################

    full = Image.open('attributes/full2.png')

    output = full.copy()
    #output.paste(bot, (0, h - h2), bot)

    #output.paste(top, (0, 0), top)

    #attributes
    y = 470
    i = 0
    # for a in attr:
    #     atrpic = Image.open('attributes/' + a + '.png')
    #     output.paste(atrpic, (29, y))
    #     y = y + 97


    ### adding the skills
    # line character limit 60, pixel length is 1090
    # get rows
    fontsize = fntsize
    font = ImageFont.truetype('georgiab.ttf', fontsize)
    charwid = 3
    rowheight = 12
    rowextra = 2
    rowlen = rwln
    rows = get_rows(skills, charwid, rowheight, rowextra, fontsize, attributes, font, rowlen-25)
    print("ROWS:")
    print(rows)

    # set up space on the card for effects
    boty = 200
    bgcx, bgcy = output.size
    skillx = 18
    skilly = bgcy - boty - (rows * rowheight) - (len(skills) * rowextra)
    skilltitle = False
    #font = ImageFont.truetype('Cousine-Regular.ttf', 40)

    # draw the effects on the card
    sklcnt = 0
    ypos = skilly
    for i in skills:
        if i != '':
            xpos = skillx
            skilltext = i.split('|')
            idx = 0
            while idx < len(skilltext):
                #print(idx)
                if idx == 0:
                    skillname_text_creator(skilltext[0], charwid, rowheight, rowextra, fontsize, 'default')
                    imskl = Image.open('skillname.png', mode = "r")
                    imsklend = Image.open('rightSkl.png', mode = "r")
                    imsklstrt = Image.open('leftSkl.png', mode = "r")
                    x,y = imskl.size
                    if '*' not in skilltext[0]:
                        output.paste(imsklstrt, (xpos,ypos), imsklstrt)
                        output.paste(imskl, (xpos+4,ypos))
                        output.paste(imsklend, (xpos+x+4,ypos), imsklend)
                        xpos = xpos + x + 14
                    else:
                        output.paste(imskl, (xpos,ypos))
                        output.paste(imsklend, (xpos+x,ypos), imsklend)
                        xpos = xpos + x + 10
                    ypos = ypos + rowextra
                    #print(ypos)
                elif skilltext[idx].lower() in attributes:
                    xpos = xpos - charwid
                    skltxt = skilltext[idx].lower()
                    imskl = Image.open('icons/'+ skltxt +'.png')
                    if border == False:
                        imskl = Image.open('icons_borderless/'+ skltxt +'.png')
                    x,y = imskl.size
                    xpos = xpos + x
                    ypos = ypos - rowextra
                    print(skilltext[idx].lower())
                    if xpos > rowlen:
                        xpos = skillx
                        ypos = ypos + rowheight
                        #print(ypos)
                        if y == 30:     # for smaller images
                            output.paste(imskl, (xpos,ypos + 10), imskl)
                        else:
                            output.paste(imskl, (xpos,ypos + 1), imskl)
                        xpos = xpos + x
                    else:
                        if y == 30:     # for smaller images
                            output.paste(imskl, (xpos - x, ypos + 10), imskl)
                        else:
                            output.paste(imskl, (xpos - x, ypos), imskl)
                    ypos = ypos + rowextra
                elif skilltext[idx].lower() in skillatr:
                    xpos = xpos - charwid
                    if fntsize < 8:
                        ypos = ypos - 1
                    skltxt = skilltext[idx].lower()
                    imskl = Image.open('skillheaders/'+ skltxt +'.png')
                    if fntsize < 8:
                        imskl = Image.open('skillheaders/text/'+ skltxt +'.png')
                    x,y = imskl.size
                    if y > rowheight:
                        #print(y)
                        ratio = rowheight/y
                        imskl = imskl.resize((int(ratio * x),rowheight))
                        x,y = imskl.size
                    elif y < rowheight:
                        ratio = rowheight/y
                        imskl = imskl.resize((int(ratio * x),rowheight))
                        x,y = imskl.size
                    xpos = xpos + x
                    if xpos > rowlen:
                        xpos = skillx
                        ypos = ypos + rowheight
                        #print(ypos)
                        output.paste(imskl, (xpos,ypos), imskl)
                        xpos = xpos + x
                    else:
                        output.paste(imskl, (xpos - x,ypos), imskl)
                    if fntsize < 8:
                        ypos = ypos + 1
                else:
                    strskl = skilltext[idx].split(' ')
                    j = 0
                    while j < len(strskl):
                        xpos = xpos + int(font.getlength(strskl[j]))
                        if xpos > rowlen:
                            xpos = skillx
                            ypos = ypos + rowheight

                            draw = ImageDraw.Draw(output)
                            drawCharBorder(draw, xpos, ypos, strskl[j], font, border)
                            xpos = xpos + int(font.getlength(strskl[j]))
                            #print(ypos)
                        else:
                            xpos = xpos - int(font.getlength(strskl[j]))

                            draw = ImageDraw.Draw(output)
                            drawCharBorder(draw, xpos, ypos, strskl[j], font, border)
                            xpos = xpos + int(font.getlength(strskl[j]))
                        # accounting for the space after each word
                        xpos = xpos + charwid
                        j = j + 1
                idx = idx + 1
            ypos = ypos + rowheight

    charwid = 18
    rowheight = 33
    rowextra = 3
    fontsize = 30
    font = ImageFont.truetype('Cousine-Regular.ttf', 30)

    output.save("output/" + fname + "/" + cardName + ".png", quality=95)