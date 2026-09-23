from jetson_inference import detectNet
from jetson_utils import videoSource, videoOutput

net = detectNet("ssd-mobilenet-v2", threshold=0.5)

input = videoSource('/home/nvidia/jetson-inference/examples/black_bear.jpg')
output = videoOutput('my-detection-out.jpg')

img = input.Capture()
d = net.Detect(img)
output.Render(img)

print(d)

