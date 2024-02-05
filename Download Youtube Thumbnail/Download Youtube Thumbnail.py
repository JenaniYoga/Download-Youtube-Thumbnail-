import wget 
import webbrowser 
url=input("Enter Video URL:")
k=url.replace("https://www.youtube.com/watch?v=","")
thumbnail='https://img.youtube.com/vi/'+ k +'/maxresdefault.jpg'

print('Downloading..,')
k = wget.download(thumbnail)
print("Downloaded")




