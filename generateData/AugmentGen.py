import PIL
import warnings
from autoaugment import SVHNPolicy
warnings.filterwarnings("ignore")
for idx in range(1, 2):#11760
    for style in range(1, 6):
        img = PIL.Image.open('./traceImg/'+str(idx)+'.png')
        policy = SVHNPolicy()
        transformed = policy(img)
        transformed.show()
        # transformed.save('./augmented/'+str(idx)+'_'+str(style)+'.png')