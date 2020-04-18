import PIL
import warnings
from autoaugment import SVHNPolicy
warnings.filterwarnings("ignore")
for idx in range(1, 11760):
    for style in range(1, 6):
        img = PIL.Image.open('./bengaliai-cv19/traceImg/'+str(idx)+'.png')
        policy = SVHNPolicy()
        transformed = policy(img)
        # transformed.show()
        transformed.save('./bengaliai-cv19/augmented/'+str(idx)+'_'+str(style)+'.png')