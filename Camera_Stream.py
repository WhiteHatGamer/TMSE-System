from detect_mask import mask_ipvideo,mask_video
from talkback import TTstr

mask,perc=mask_ipvideo('192.168.0.100')
perc = str(perc)
perc = float(perc) * 100
if mask==1:
    TTstr("Mask Detected")
    print("Mask Found with "+str(perc)+"% Percentage")
else:
    TTstr("Mask Not Detected")
    print("Mask Not Detected")
