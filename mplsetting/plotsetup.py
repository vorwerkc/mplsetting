#!/usr/bin/python
import matplotlib.pyplot as plt


def set_plot(ws, hs):
    #set_latex_plot()
    plt.style.use(['seaborn-deep'])
    plt.rcParams['axes.grid'] = True
    plt.rcParams['grid.color'] = "grey"
    plt.rcParams['grid.linewidth'] = 1
    plt.rcParams['grid.linestyle'] = "-"
    plt.rcParams['grid.alpha'] = "0.3"
    plt.rcParams['figure.figsize'] = (ws, hs)
    plt.rcParams['axes.linewidth'] = 2
    plt.rcParams['lines.linewidth']=2
    plt.rcParams['xtick.major.width']=2
    plt.rcParams['ytick.major.width']=2
    plt.rcParams['font.size'] = 10
    plt.rcParams['axes.labelsize'] = 11
    plt.rcParams['axes.titlesize'] = 11
    plt.rcParams['xtick.labelsize'] = plt.rcParams['font.size']
    plt.rcParams['ytick.labelsize'] = plt.rcParams['font.size']
    plt.rcParams['legend.fontsize'] = plt.rcParams['font.size']
    plt.rcParams['text.latex.preamble'] = [
       r'\usepackage{siunitx}',   # i need upright \micro symbols, but you need...
       r'\usepackage{physics}',
       r'\usepackage[sfdefault,lf]{carlito}',
       r'\sisetup{ locale= DE, detect-mode= false, detect-family= true, mode= text } ',   # ...this to force siunitx to actually use your fonts
       r'\usepackage{sansmath}',  # load up the sansmath so that math -> helvet
       r'\sansmath'               # <- tricky! -- gotta actually tell tex to use!
    ]  
    
def set_presentation_plot(ws, hs):
    #set_latex_plot()
    plt.style.use(['seaborn-notebook'])
    plt.rcParams['axes.grid'] = True
    plt.rcParams['grid.color'] = "grey"
    plt.rcParams['grid.linewidth'] = 2
    plt.rcParams['grid.linestyle'] = "-"
    plt.rcParams['grid.alpha'] = "0.3"
    plt.rcParams['figure.figsize'] = (ws, hs)
    plt.rcParams['axes.linewidth'] = 4
    plt.rcParams['patch.linewidth'] = 4
    plt.rcParams['lines.linewidth']=4
    plt.rcParams['xtick.major.width']=4
    plt.rcParams['xtick.major.size']=5
    plt.rcParams['ytick.major.width']=4
    plt.rcParams['ytick.major.size']=5
    plt.rcParams['xtick.minor.width']=2
    plt.rcParams['xtick.minor.size']=5
    plt.rcParams['ytick.minor.width']=2
    plt.rcParams['ytick.minor.size']=5
    plt.rcParams['font.size'] = 24
    plt.rcParams['axes.labelsize'] = 24
    plt.rcParams['axes.titlesize'] = 24
    plt.rcParams['xtick.labelsize'] = plt.rcParams['font.size']
    plt.rcParams['ytick.labelsize'] = plt.rcParams['font.size']
    plt.rcParams['legend.fontsize'] = 20
    plt.rcParams['text.latex.preamble'] = [
       r'\usepackage{siunitx}',   # i need upright \micro symbols, but you need...
       r'\usepackage{physics}',
       r'\usepackage[sfdefault,lf]{carlito}',
       r'\sisetup{ locale= DE, detect-mode= false, detect-family= true, mode= text } ',   # ...this to force siunitx to actually use your fonts
       r'\usepackage{sansmath}',  # load up the sansmath so that math -> helvet
       r'\sansmath'               # <- tricky! -- gotta actually tell tex to use!
    ]  

def set_plot_A4(ws, hs):
    #set_latex_plot()
    plt.style.use(['seaborn-notebook'])
    plt.rcParams['axes.grid'] = True
    plt.rcParams['grid.color'] = "grey"
    plt.rcParams['grid.linewidth'] = 1
    plt.rcParams['grid.linestyle'] = "-"
    plt.rcParams['grid.alpha'] = "0.3"
    plt.rcParams['figure.figsize'] = (ws, hs)
    plt.rcParams['axes.linewidth'] = 2
    plt.rcParams['lines.linewidth']=2
    plt.rcParams['xtick.major.width']=2
    plt.rcParams['ytick.major.width']=2
    plt.rcParams['font.size'] = 11
    plt.rcParams['axes.labelsize'] = 12
    plt.rcParams['axes.titlesize'] = 12
    plt.rcParams['xtick.labelsize'] = plt.rcParams['font.size']
    plt.rcParams['ytick.labelsize'] = plt.rcParams['font.size']
    plt.rcParams['legend.fontsize'] = plt.rcParams['font.size']
    plt.rcParams['text.latex.preamble'] = [
       r'\usepackage{siunitx}',   # i need upright \micro symbols, but you need...
       r'\usepackage{physics}',
       r'\usepackage[sfdefault,lf]{carlito}',
       r'\sisetup{ locale= DE, detect-mode= false, detect-family= true, mode= text } ',   # ...this to force siunitx to actually use your fonts
       r'\usepackage{sansmath}',  # load up the sansmath so that math -> helvet
       r'\sansmath'               # <- tricky! -- gotta actually tell tex to use!
    ]  
