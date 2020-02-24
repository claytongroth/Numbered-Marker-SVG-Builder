import json
from subprocess import Popen, PIPE

stdout = Popen('node svgToText.js', shell=True, stdout=PIPE).stdout
output = stdout.read()
arrayOfPaths = output.split(",")

colors = [
    '#ff3823',
    '#2196f3',
    '#5cb85c',
    '#ffc40d',
    '#7a43b6',
    '#ff6624',
    '#e91e63',
    '#26c6da',
    '#c0ca33',
    '#ffa000',
    '#7a163c',
    '#033076',
    '#bd362f',
    '#0055cc',
    '#468847',
    '#f89406',
    '#795548', 
    '#c09853', 
    '#008db1', 
    '#8c8525',
]
for number in range(0, 41):
    newSVG = open('%s_pin.svg' % str(number+1), 'w+')
    #fontsize = 16 if len(str(number))<1 else 14
    translation = -9.5 if len(str(number+1))==2 else -4.68
    print("translation", translation, number)
    template_svg = '''
        <svg xmlns="http://www.w3.org/2000/svg" width="30" height="42" viewBox="0 0 30 42">
            <g fill="none" fill-rule="evenodd" transform="scale(1.3125)">
            <path 
                d="M22 11c0 1.42-.226 2.585-.677 3.496l-7.465 15.117c-.218.43-.543.77-.974 1.016-.43.246-.892.37-1.384.37-.492 0-.954-.124-1.384-.37-.43-.248-.75-.587-.954-1.017L1.677 14.496C1.227 13.586 1 12.42 1 11c0-2.76 1.025-5.117 3.076-7.07C6.126 1.977 8.602 1 11.5 1c2.898 0 5.373.977 7.424 2.93C20.974 5.883 22 8.24 22 11z" 
                stroke="none" 
                fill="{color}" 
                fill-rule="nonzero"
            />
            </g>
            <g transform="translate({trans},0)">
                {path}
            </g>
        </svg>
    '''.format(path=arrayOfPaths[number+1], trans=translation,color=colors[number % len(colors)])
    newSVG.write(template_svg)

# <text 
#     font-family= "Segoe UI"
#     x="50%" 
#     y="50%" 
#     fill="#ffffff"
#     font-size="{fontsize}" 
#     text-anchor="middle"
# >{text}</text>