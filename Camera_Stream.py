from detect_mask import mask_ipvideo,mask_video
from talkback import TTstr

mask,perc=mask_video()#ipvideo('192.168.79.5')
if mask==1:
    TTstr("Mask Detected")
    print("Mask Found with "+perc+"% Percentage")
else:
    TTstr("Mask Not Detected")
    print("Mask Not Detected")
