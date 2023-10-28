#结合input、字典、if判断， 做一个查询流行语含义的电子词典程序
slang_dict = { "whv": "澳洲抽签义工" ,
              "新西兰whv": "新西兰打工" }
slang_dict[ "旅游签证" ] = "只能用来旅游的护照，有时间限制。"
slang_dict[ "学签" ] = "用途为去学习的护照。"

print(slang_dict['whv'])
query = input( "请输入查询内容:" )
if query in slang_dict:
    print( "查询内容" + query + "含义如下" )
    print(slang_dict[query])
else:
    print( "查询的流行语暂未收录。" )
    print( "当前词典收录收录为: " + str(len(slang_dict)) + "条。 " )

