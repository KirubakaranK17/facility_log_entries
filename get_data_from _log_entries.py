import re
with open('/Users/kirubakaran/Desktop/facility-service.txt') as myfile:
	content = myfile.read()
text = re.findall(r'q=(.*?)&sdk', content, re.DOTALL)
print(text)

with open("/Users/kirubakaran/Desktop/Output.txt", 'w') as filehandle:
	for listitem in text:
		filehandle.write('%s\n' % listitem)
		print("Updated")