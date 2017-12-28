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

def reg_image(user_id, tag, url, title, descript, ref_count, like):
    #userid, tag, url, title , descript, ref_count, like

    image_fields = {"user_id","tag","url","title","descript","ref_count", "like"}
    image_values = {user_id, tag, url, title, descript, ref_count, like}
    rds.hset("image/"+title,image_fields,image_values) #image 정보 저장


    rds.hset("tag/"+tag, title, url) #tag별 이미지 리스트 저장
    rds.hset("user/"+user_id, title, url) #user_id별 이미지 리스트 저장
    return

def get_post_by_user(user_id):
    # 유저별 게시물 가져오기
    return rds.hgetall("user/"+user_id)

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