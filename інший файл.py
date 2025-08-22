import json
with open("my.json","r",encoding="utf-8") as file:
    data=json.load(file)
    print(data)
    for i in data:
        print(i)
        if i["age"]=="222":
            i["age"]="456"
            print(data)
# # with open("my.json","w",encoding="utf-8") as file:
# #     pelmen = {"бобрики такі милі правда якщо ти скажеш ні я тебе зроблю пельменьоа:)"}
# #     json.dump(data,file,ensure_ascii=False,indent=2)
# # with open("my.json", "r",encoding="utf-8") as file:
# #     data=json.load(file)
# #     print(data)
# with open("my.json", "w",encoding="utf-8") as file:
#     pass
#     json.dump(data,file,ensure_ascii=False,indent=2)
#     newbreaver={"name":"who are you im a ellia:)"}
#     data.append(newbreaver)
#     json.dump(data,file,ensure_ascii=False,indent=2)
