from pymongo import MongoClient

client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.project

수원돈까스맛집 = ({
    '돈까스상회': 27,
    '고릴라수재돈까스': 14,
    '친구정': 19,
    '고돈': 14,
    '동명카츠': 6,
    '테루': 6,
    '수원 토끼정': 5,
    '최고당돈까스': 3,
    '아주대 한조카츠': 2,
    '정돈': 2,
    '키무카츠': 2,
    '경양카츠': 2,
    '카츠만': 2,
    '동경카츠': 1,
    '도쿄하야시라이스클럽': 1,
    '쑝쑝돈까스': 1,
    '황금돈가스': 1,
    '일호식당': 1,
    '로마레스토랑': 1,
    '남바완돈카츠': 1,
})

수원파스타맛집 = ({
    '겟 201광교점': 5,
    '수원 꿍팟퐁커리': 1,
    '돈까스상회 ': 1,
    '레이크퀴진 ': 1,
    '롤링파스타 ': 5,
    '리틀노작 ': 22,
    '마노디셰프': 1,
    '매디포갈릭 ': 2,
    '모노폴1982행궁동 ': 4,
    '미식가의주방 ': 2,
    '바닐라비스트로 ': 1,
    '수원역토끼정 ': 5,
    '수원트라토리아 ': 23,
    '트라토리아베이커리카페 ': 24,
    '심야스테이크매탄점 ': 1,
    '아름다운땅 ': 1,
    '운멜로 ': 3,
    '운멜로랩2': 2,
    '인계동트라토리아 ': 20,
    '정성식탁 ': 4,
    '제이와이테일리  ': 2,
    '지구본부제문화식당  ': 1,
    '홍라드  ': 1,
    '화양가옥  ': 3,
})

수원맛집추천 = ({
    'iambarista': 1,
    'mukbang': 2,
    '고기남녀 ': 1,
    '수원이베리코 까망꽃돼지  ': 2,
    '꼬꼬아찌  ': 18,
    '누디마카롱카페  ': 4,
    '당초고추치킨  ': 2,
    '대가주점 ': 4,
    '라비아화덕피자  ': 5,
    '리틀노작  ': 3,
    '망개떡  ': 1,
    '매향통닭  ': 1,
    '미분당  ': 1,
    '수인선닭발  ': 2,
    '올림선  ': 1,
    '세컨트트랙 ': 1,
    '압구정곱떡 ': 4,
    '아름다운땅 ': 1,
    '어거스트구스토  ': 1,
    '지코바  ': 4,
    '카자구루마   ': 1,
    '커러디   ': 3,
    '태영생막창   ': 1,
    '투파인드피터   ': 2,
    '한신우동    ': 1,
    '월야    ': 1,
    '노포    ': 1,
    '산청자매훠궈수원북문점    ': 1,
})

강릉돈까스맛집 = ({
    '자스민 ': 5,
    '나모야 ': 8,
    '루이식당  ': 2,
    '룽성   ': 1,
    '소영이네돈까스물회   ': 52,
    '오렌지글로우   ': 2,
    '거기   ': 1,
    '하이돈까스  ': 4,
    '학사식당   ': 3,
    '갤러리밥시   ': 4,
    '돈까스마당   ': 1,
    '블루키친   ': 2,
    '성왕돈까스   ': 3,
    '강릉소담골   ': 1,
    '요남자   ': 1,
    '자연비  ': 1,
    '정혜영쿡  ': 1,
    '포시즌버거앤펍  ': 2,
    '핫밀   ': 2,
})

강릉파스타맛집 = ({
    '100브랜드  ': 3,
    '금학가온  ': 7,
    '늘쿡   ': 2,
    '명주배롱    ': 1,
    '미트컬쳐    ': 1,
    '부오나피자    ': 26,
    '썸머키친   ': 5,
    '포지타노   ': 1,
    '나폴리선생    ': 2,
    '아뜨9    ': 1,
    '다이닝블루    ': 2,
    '더식탁    ': 4,
    '라라옥 강릉별장   ': 1,
    '라몬타냐    ': 4,
    '리틀다이너   ': 1,
    '블루키친   ': 1,
    '테이블오브레지나   ': 4,
    '안목롱브레드    ': 1,
    '올리앤     ': 1,
    '인비토     ': 1,
    '파머스키친     ': 1,
    '포모도로     ': 2,
    '포지타노     ': 2,
    '피터콤마      ': 1,
    '스테이크n석봉      ': 2,
    '러브레터      ': 1,

})

강릉맛집추천 = ({
    '강릉라라옥   ': 1,
    '강릉풍년갈비   ': 1,
    '동화가든짬뽕순두부    ': 1,
    '어화횟집     ': 2,
    '예가낙지마당     ': 1,
    '콩새야     ': 13,
    '풍호맛뜨락    ': 5,
    '방학골    ': 1,
    '러브레터     ': 1,
    '커피커퍼박물관     ': 6,

})
db.realFood.insert_one({
        '돈까스상회': '27',
    '고릴라수재돈까스': '14',
    '친구정': '19',
    '고돈': '14',
    '동명카츠': '6',
    '테루': '6',
    '수원 토끼정': '5',
    '최고당돈까스': '3',
    '아주대 한조카츠': '2',
    '정돈': '2',
    '키무카츠': '2',
    '경양카츠': '2',
    '카츠만': '2',
    '동경카츠': '1',
    '도쿄하야시라이스클럽': '1',
    '쑝쑝돈까스': '1',
    '황금돈가스': '1',
    '일호식당': '1',
    '로마레스토랑': '1',
    '남바완돈카츠': '1',
    'local': '수원',
    'food': '돈까스맛집'
})
