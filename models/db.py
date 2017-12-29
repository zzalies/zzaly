from models import redis_module as rds

def init():
    rds.make_connection()

# def reg_user():
#     # 유저별 이미지 등록
#     pass
#
# def reg_tag():
#     # 태그별 이미지 등록
#     pass


def reg_image(user_id, tag, url, title, desc, ref_count=0, like=0):

    # userid, tag, url, title , descript, ref_count, like

    image_value = {}
    image_value["user_id"] = user_id
    image_value["tag"] = tag
    image_value["url"] = url
    image_value["title"] = title
    image_value["desc"] = desc
    image_value["ref_count"] = ref_count
    image_value["like"] = like
    rds.hmset("image/"+title, image_value)  #image 정보 저장


    rds.hset("tag/" + tag, title, url)   #tag별 이미지 리스트 저장
    rds.hset("user/"+user_id, title, url)  #user_id별 이미지 리스트 저장
    return


def get_post_by_user(user_id):
    # 유저별 게시물 가져오기
    keylist = rds.hkeys("user/"+user_id)
    result = list()
    for item in keylist :
        result.append(get_image_metadata(item.decode('utf-8')))
    return result


def get_post_by_tag(tag):
    # 태그별 게시물 가져오기
    return rds.hgetall("tag/"+tag)


def get_image_metadata(title):
    # 이미지 메타데이터 가져오기
    return rds.hgetall("image/"+title)


def count_up(title):
    rds.hincr(title,"ref_count",1)
    return


def like_up(title):
    rds.hincr(title,"like",1)
    return


def reg_post(title, content, image):
    rds.hset("post/"+title, "body", content)
    rds.hset("post/"+title, "title", title)
    if image is "" :
        box = "null"
    else:
        print(image)
        split_list = image.split("<img src=")
        print(split_list)
        new_list = list()
        # for item in split_list:
        #     if item.find("src") is not -1:
        #         temp = item.split(",", 1)
        #         # new_list.append(temp[0])
                # for i in box:
                #     if i.find("'") is not -1 or i.find('"') is not -1:
        box = split_list[1].split("=",1)
        box = box[0].split(" ",1)
        box = box[0].replace('"', " ")
        box = box.replace("'", " ")
        box = box[3:-1]
        box = box.strip()
        print(box)
    rds.hset("post/" + title, "image",box)
    return

def get_post():
    post_list = rds.keys("post/*")
    result = list()
    for item in post_list:
        result.append(rds.hgetall(item.decode('utf-8')))
    return result


if __name__ == '__main__':
    init()
    # reg_image("user_id","tag", "url", "happy", "desc")
    #
    # print(get_post_by_user('happy'))
    # print(get_post())
    # sample = "<image src='asdfasdf',sadf>,<image src='asdf2asdf',sadf>,<image src='asdf3asdf',sadf>"
    # split_list=sample.split("<image ")
    # new_list=list()
    # for item in split_list:
    #     if item.find("src") is not -1 :
    #         temp = item.split(",",1)
    #         # new_list.append(temp[0])
    #         box = temp[0].split("=")
    #         for i in box:
    #             if i.find("'") is not -1 or i.find('"') is not -1 :
    #                 i=i.replace('"'," ")
    #                 i=i.replace("'"," ")
    #                 i=i.strip()
    #                 new_list.append(i)
    #
    #
    # print(new_list)