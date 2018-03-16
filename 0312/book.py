import requests
response=request.get("http://www.novelscape.net/wxxs/j/jingyong/ffwz/001.htm")
response.encoding="big5"
book1=response.text
novel='大廳外的窗口，伏著一個少女、一個青年漢子。兩人在窗紙上挖破了兩個小孔，各用右眼湊著向里偷窺。兩人見那少年身手不凡，發鏢甚准，不由得互相對望了一眼，臉上都露出訝异的神色'
print(novel)
