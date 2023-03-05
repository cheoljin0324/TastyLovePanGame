# 이 파일에 게임 스크립트를 입력합니다.

# image 문을 사용해 이미지를 정의합니다.
# image eileen happy = "eileen_happy.png"

# 게임에서 사용할 캐릭터를 정의합니다.
define meeyoung = Character("미영", color="#B18904")
define player = Character("[playerName]",color="#ffffff")
define manone = Character("지나가던 남자A", color="#ffffff")
define mantwo = Character("지나가던 남자B", color="#ffffff")
define seeman = Character("알바생A", color="#ffffff")
define seemantwo = Character("알바생B", color="#ffffff")
define seemanThree = Character("알바생C" , color = "#ffffff")

define persistent.End = False


python:
    renpy.musig.register_channel("music",mixer="music", loop=True)
    renpy.Sound.register_channel("sound",mixer="sound", loop=True)


image Angry:
    im.FactorScale("images/Standing/AMee.png",1.1)
    yalign -0.5

image Smile:
    im.FactorScale("images/Standing/SMee.png",1.1)
    yalign -0.5

image Normal:
    im.FactorScale("images/Standing/NMee.png",1.1)
    yalign -0.5

image NormalZoom:
    im.FactorScale("images/Standing/NMee.png",1.5)
    yalign -0.2

image SmileZoom:
    im.FactorScale("images/Standing/SMee.png",1.5)
    yalign -0.2

image AngryZoom:
    im.FactorScale("images/Standing/AMee.png",1.5)
    yalign -0.2

image Zhq:
    im.FactorScale("images/EventCG/zh.png",1.4)
    yalign 0.5

image bg myhouse = "images/backGround/myroom.png"
image bg myhousenight = "images/backGround/myroom_night.png"
image bg cafe_front = "images/backGround/cafe_front.png"
image bg cafe_frontnight = "images/backGround/cafe_front_night.png"
image bg cafe_inside = "images/backGround/cafe_inside.png"
image bg everandDoor = "images/backGround/everandDoor.png"
image bg inCar = "images/backGround/inCar.png"
image bg magicTree = "images/backGround/magicTree.png"
image bg blackOut = "images/backGround/blackScreen.png"
image bg RollingXTrin = "images/backGround/RollingXTrain.png"
image bg RollingXTrinExit = "images/backGround/RollingXTrain exit.png"
image bg RollerIn = "images/backGround/RollerIn.png"
image bg foodCoatfront = "images/backGround/hangaram.png"
image bg foodRoom = "images/backGround/FoodRoom.png"
image bg turnRoomA = "images/backGround/turnHorseFrontS.png"
image bg turnRoomN = "images/backGround/turnHorseFrontN.png"
image bg bumper = "images/backGround/bumper.png"
image bg horseing = "images/backGround/turnHorseIng.png"
image bg icecream = "images/backGround/IceCream.png"
image bg inturn = "images/backGround/gwanra.png"

image eventCG MeeTurn = "images/EventCG/EventCG1.png"

image eventCG MeeTrue2:
    im.FactorScale("images/EventCG/EventCG1.png",4)
    xalign 0.47 yalign 0.3

image eventCG MeeSum1:
    im.FactorScale("images/EventCG/EventCG2.png",4)
    xalign 0.47 yalign 0.3

image eventCG MeeSum2:
    im.FactorScale("images/eventCG/EventCG2.png",4)
    xalign 0.6 yalign 0.65

image eventCG MeeSum3:
    im.FactorScale("images/eventCG/EventCG2.png", 4)
    xalign 0.53 yalign 0.2

image eventCG MeeSum4 = "images/eventCG/EventCG2.png"

define name = "백주원"

transform EventEffect:
        xalign 0.35 yalign 0.7
        linear 30.0 xalign 0.4 yalign 0.2

transform EventEffect2:
        xalign 0.5 yalign 0.2
        linear 20.0 yalign 0.7
            

transform text_effect:
        block:
            linear 0.1 xoffset -2 yoffset 2
            linear 0.1 xoffset 3 yoffset -3
            linear 0.1 xoffset 2 yoffset -2
            linear 0.1 xoffset -3 yoffset 3
            linear 0.1 xoffset 0 yoffset 0

transform callEffect:
        block:
            linear 0.1 xoffset -2 yoffset 2
            linear 0.1 xoffset 3 yoffset -3
            linear 0.1 xoffset 2 yoffset -2
            linear 0.1 xoffset -3 yoffset 3
            linear 0.1 xoffset 0 yoffset 0
            pause 1.0
            repeat


screen set_name(title, init_name):
    frame:
         xpadding 50
         ypadding 50
         xalign 0.5 yalign 0.5
         vbox:
            spacing 20
            text title xalign 0.5
            input default init_name xalign 0.5

# 여기에서부터 게임이 시작합니다.
label start:

    $ name = renpy.call_screen("set_name",title="                           당신의 이름은 뭔가요?\n(이름을 정하지 않을 경우 백주원 으로 설정됩니다)", init_name="")
    $ player = Character(name , color="#ffffff")

    if name == "":
        $ player = Character("백주원" , color="#ffffff")
    if name == "":
        $ name = "백주원"

    "[name]... 맞나요?"

    menu:
        "네":
            jump ingame

        "아니요":
            jump start
        

    return

label ingame:
    
    play music "audio/startGame.mp3"

    scene bg myhouse with fade

    "오늘은 토요일, 학교에 가지 않는 날이다."
    "곧 있으면 시험이지만 난 별 신경 쓰지 않고 게임 폴더를 열었다."
    show Zhq with dissolve
    "내가 킨 게임은 혼자 하기 좋은 알만툴 공포게임."
    "원래 시험 기간이면 공부를 하는 게 맞지만, 이미 고등학교 서류를 넣어서 결과만 기다리면 되기도 했고."
    "시험 하나 망친다고 딱히 내신도 달라질 게 없어서 마음 편히 게임을 켰다."
    "예전에 언젠가 인터넷에서 방송하는 걸 보고 무료로 깔아뒀던 게임이다."
    "다른 애들이 공부하고 있을 때 게임이라니 심장이 살짝 쫄깃해진다."
    hide Zhq with dissolve

    play sound "audio/SoundEffect/806150_휴대폰 진동소리.mp3"
    scene bg myhouse at callEffect
    "(위이잉)"
    stop sound 
    scene bg myhouse at default
    player "어 미영 누나네?"

    scene bg blackOut with fade

    meeyoung "[name]?"
    player "예 무슨 일인가요."
    meeyoung "뭐해?"
    player "그냥 뭐 컴퓨터로 이것저것...."
    meeyoung "게임 하고 있었구나! 또, 이것저것은 무슨."
    
    "미영 눈나는 우리 집 근처 카페 누벨바그를 운영하는 눈나이다."
    "내가 어렸을 때 부터 자주 우리 집에서 나를 돌봐주던 놀랄지도 모르겠지만 금발 외국인이다."
    "물론 그렇다고 아예 외국인인 건 아니고 누나 부모님이 한국에서 미영 누나를 낳으셨다고 들었다."
    "그래서인지는 몰라도 이름도 한국 이름답게 외자로 영이라고 지었다는데."
    "본래는 미식스 영(Meeseeks Young)인가 그랬던 것 같다."
    "그런데 그렇게 부르긴 힘드니 미영눈나라고 부르고 있다."

    player "그래서 왜, 무슨 일임?"
    meeyoung "너희 어머니한테 들었어. 이번에, 학교에 접수했다며? 자소서."
    player "응, 했지? 직접 학교 가서."
    meeyoung "뭐였더라? 그 학교 이름. 게임마이스터고등학교?"
    player "경기게임마이스터고등학교일걸?"
    meeyoung "그거나 그거나."
    meeyoung "어쨌든 딱 봐도 공부 안 하고 있을 것 같아서."
    meeyoung "혹시, 지금 시간 괜찮아?"
    player "괜찮은데, 왜 그러십니까?"
    meeyoung "놀이공원이나 갈까 해서."
    player "오~ 놀러가는 거임? 어디?"
    meeyoung "그.. 어디더라? OO랜드?"
    player "아하 거기~ 웬일로?"
    meeyoung "어, 표가 좀 생겨서."
    meeyoung "마침 자유 이용권을 줬거든, 대학교 친구가."
    player "오~ 착한 사람이다. 거기 자유이용권 비싸지 않아?"
    meeyoung "그래서, 갈 거야?"
    player "이건 못 참지. 갑니다."
    meeyoung "알았어. 그럼, 누벨바그로 와."
    player "오키, 알았음."
    meeyoung "늦지 말고 와?"
    player "아이 설마 제가 늦겠습니까? 미영씨."
    meeyoung "쓰읍, 또? 영이 누나라고 하라니까."
    meeyoung "성이 미고 이름이 영이라고 몇 번을 말해?"
    player "아이 참 미영씨도, 왜 이러실까~ 내 마음 잘 알면서."
    meeyoung "진짜 때릴지도 모른다, 자꾸 그러면?"
    player "넵 죄송합니다."
    meeyoung "말로 하면 들어주세요?"
    player "넵."
    meeyoung "늦으면 안 돼? 늦으면 사람 많아서 기다려야 하니까."
    player "알겠습니다."

    scene bg myhouse with fade

    "(뚝)"

    "전화가 끊겼다."
    "놀이공원 OO랜드"
    "한국에서 큰 놀이공원 하면 무조건 생각되는 놀이공원 중 하나이다."
    "엄청나게 커서 걸어 다니는 것만 해도 다리가 아플 정도로 크다고 하는데."
    "이렇게 큰 놀이공원은 초등학교 현장 체험학습으로 가보고 간 적 없어서 그런지 기대가 된다."
    "미영 누나가 이런 데를 먼저 보내주겠다고 하다니."
    "오랜만에 놀이공원이라 그런지 조금 설레는 것 같기도 하다."
    "늦지 않게.... 오라고 했는데 언제까지 가면 되려나."
    player "..."
    player "일단 옷부터 입어야 하나?"
    "혼잣말을 중얼거리며 손에 잡히는 옷을 대충 갈아입었다."

    scene bg cafe_inside with fade

    play music "audio/Mee/Mee Rules.mp3"

    show Normal with dissolve

    meeyoung "빨리 왔네? [name]."
    "누벨바그에 도착하니 미영 누나는 테이블에 자리 잡고 앉아있었다."
    player "공짜인데 빨리 와야죠."
    hide Normal
    show Angry 
    meeyoung "공짜 아닐 때도 좀 빨리 와주면 덧나나?"
    hide Angry
    show Normal
    meeyoung "그래도 덕분에 늦지는 않을 것 같네."
    "시계를 봤다."
    "시간은 누나와 통화를 끝내고 10분이 지난 후였다."
    player "누나는 뭐 하고 있었어?"
    hide Normal
    show Smile
    meeyoung "그냥 뭐 기다리고 있었지. [name] 너."
    player "아하!"
    player "그런데 OO랜드 어떻게 갈거임?"
    player "잠만 생각해보니 OO랜드 꽤 멀지 않아?"
    hide Smile
    show Normal
    meeyoung "차 타고."
    player "누나 차도 있었음?"
    hide Normal
    show Angry
    meeyoung "있어 차, 누나 카페 맨날 오면서 그것도 몰라?"
    player "아니, 내가 누나 차 있는 걸 어케 압니까?"
    hide Angry
    show Normal
    meeyoung "내가 한 번도 안 태워줬었나?"
    player "그런 듯."
    meeyoung "걱정말고 따라오기나 해."
    player "누나 운전은 할 줄 알지?"
    hide Normal
    show Smile
    "웃으면서 주머니에 차 키를 꺼내는 미영 누나"
    meeyoung "무시하는 거야, 지금?"
    player "아니 무시가 아니라 걱정 정도는 할 수 있죠! 목숨이 달린 일인데."
    hide Smile
    show Normal
    meeyoung "걱정하지마."
    meeyoung "아마도, 꽤 할 걸 운전."
    menu:
        "이게 맞나?":
            meeyoung "빨리 가자 이러다 늦겠어."
    player "넵"

    scene bg cafe_front with fade

    show Normal with dissolve
    "누나는 자연스럽게 누벨바그 앞에 주차되어있는 차의 문을 열었다."
    "차를 잘 모르는 내가 봐도 누나의 차는 상당히 좋아 보인다."
    "누나 같으면 작은 경차를 탈 것 같았는데..."
    player "이 차가 누나 차라고?"
    hide Normal 
    show Smile 
    meeyoung "뭘 그렇게 놀라고 그래?"
    player "아니 그냥 너무 좋아보여서요"
    hide Smile 
    show Normal
    meeyoung "어때? 놀랍지? 예쁜데 이런 차까지 있고."
    player "..."

    hide Normal with dissolve

    scene bg inCar with fade

    "누나는 운전하는게 아무렇지 않다는 듯 여유롭게 골목길을 빠져나오며 운전한다.."
    "생각해보니 누나가 운전하는 모습은 처음 보는건가?"
    "맨날 일을 땡땡이 치던 누나의 모습만 봐오다가 운전하는 모습을 보니"
    "조금은 듬직하다는 생각도 든다."

    show Normal with dissolve

    meeyoung "뭘 그렇게 멍때리고 있어?"
    player "아 아무것도 아님."
    meeyoung "그거나 매, 안전벨트"
    player "불편한데 걍 안매면 안 됨?"
    hide Normal
    show Angry
    meeyoung "어허"
    meeyoung "네가 안 매면, 내가 내야 한단 말이야. 벌금."
    player "알았어"
    "미영눈나의 말에 나는 조심스레 안전벨트를 맸다."
    "그리고 창밖을 멍하니 바라봤다."
    "멍하니 있으니 누나의 차 안에서는 묘하게 향수와도 같은 진한 달콤한 냄새가 났다."
    hide Angry
    show Normal
    meeyoung "그래서 혹시 있어? 타고 싶은 건."
    "정작 생각해보니, 공짜 놀이공원이라 좋아라 하며 나오긴 했지만..."
    "지금 내가 타고 싶은 놀이기구를 아예 생각해보지도 않고 나왔다는 것을 깨달았다."
    player "잘 모르겠다."
    hide Normal
    show Angry
    meeyoung "뭐야, [name]? 놀이공원 가겠다고 했으면서 탈 놀이기구도 생각 안 했어?"
    player "생각나는 게 없다고 해야 하나."
    player "가면서 생각해봄."
    hide Angry
    show Normal
    meeyoung "흠 그래?"
    player "누나야말로, 생각나는 거 없어?"
    meeyoung "글쎄다..."
    "누나는 조금 고민하는가 싶더니"
    "금방 생각 났다는 듯 나를 살짝 바라보고는 미소를 슬쩍 지어 보였다."
    meeyoung "그거였나... T..?"
    player "T?"
    hide Normal
    show Smile
    meeyoung "재미있어 보이더라, 티익스프레스."
    player "누나 무서운 거 좋아했음?"
    meeyoung "응, 좋아해 무서운 거."
    player "오 이런."
    hide Smile
    show Normal
    meeyoung "넌 잘 타 [name]?"
    player "못 타는 거 뻔히 알면서 왜 물어봄?"
    "실제로 나는 무서운 걸 굉장히 못 탄다."
    "바이킹도 겨우 타는 정도"
    "솔직히, 누나가 말하는 롤코는 커녕 작은 열차도 탈 생각 안하고 있었는데..."
    "그래도 놀이공원 자유이용권도 누나가 주는 건데"
    "꾹 참고 타야하나...?"
    meeyoung "귀엽기는."
    player "농담이 너무 무섭습니다."
    hide Normal
    show Smile
    meeyoung "장난으로 말한 거 아닌데?"
    player "장난 아니라고?"
    hide Smile
    show Normal
    meeyoung "글쎄? 잘 생각해봐"
    player "..."
    hide Normal
    show Smile
    meeyoung "진짜 너무 웃겨."
    hide Smile
    show Normal
    meeyoung "역시, 놀리는 맛이 있다니까? [name] 넌."
    player "그 말 놀릴 때면 꼭 하는 것 같은데."
    meeyoung "안 하면 너 삐칠 거잖아."
    player "진짜 삐집니다?"
    hide Normal
    show Angry
    meeyoung "아이, 왜 그래 진짜~"
    meeyoung "이렇게, 응? 놀이공원도 직접 모셔다드리는 예쁜 누나가 어디 있다고."
    player "이러고 있네. 스스로 예쁘다는 말은 취소하시죠?"
    hide Angry
    show Smile
    meeyoung "나 예쁘지 않아?"
    meeyoung "매번 솔직하게 말을 못 한다니까?"
    player "운전이나 똑바로 하십쇼 선생님."
    hide Smile
    show Angry
    meeyoung "으이구, 말 돌리고 있어 진짜. 얄밉게시리."
    hide Angry

    scene bg inCar with fade

    "간단한 대화를 주고받는 중"
    "잠시 대화할 소재가 떨어졌는지 미영 누나도 나도 조용히 침묵을 지켰다."
    "창밖을 바라보니 처음에는 모르는 건물들만 보였지만."
    "보면 볼 수록 예전에 봤던 것 같은 익숙한 건물들이 몇 채 보인다."
    "초등학교 때 버스에서나 봤던 풍경을 이렇게 다시 보니 뭔가 그리운 듯한 기분이 들었다."
    player "오 엄청 오랜만인데?"
    show Normal with dissolve
    meeyoung "갑자기 왜 이렇게 신났어?"
    player "그냥 예전에 봤던 곳이라."
    hide Normal 
    show Smile
    meeyoung "오호라 와본적 있어? 여기."
    player "초등학교 때, 현장 체험 학습으로 온 적 있었던 거 같은데."
    hide Smile 
    show Normal
    meeyoung "아 생각해보니 나도 예전에 네가 여기 간다고 하던 거 기억 나는 것 같기도..."
    player "헐 누나 그런 것도 기억함?"
    hide Normal
    show Angry
    meeyoung "헐은 뭐야?"
    meeyoung "사람을 뭐로 보고."
    player "그야 누나 자주 깜빡깜빡하잖아."
    hide Angry
    show Smile
    meeyoung "[name] 너도 자주 까먹잖아 여러 가지."
    player "그랬었나?"
    hide Smile
    show Normal
    meeyoung "진짜 기억 안 나는거야?"
    "누나는 진지하게 내 눈을 바라본다."
    "진심이냐는 듯한 눈빛을 보이기에 나는 조심스레 눈을 피했다."
    meeyoung "어쨌든 거의 다 온 것 같은데?"
    meeyoung "저기 보인다, 놀이공원."
    hide Normal with dissolve

    scene bg everandDoor with fade

    "나무가 보이는 길을 지나 넓은 놀이공원 입구가 보였다."
    "그곳에는 입장을 기다리는 사람과 지금 막 들어오고 있는 버스들이 보였다."

    scene bg inCar with fade

    show Normal with dissolve
    meeyoung "나름 일찍 오려고 한건데, 사람 엄청 많네."
    player "그러게 저기 언제 들어갈 수 있을까?"
    "가을이라 그런지 많이 덥지는 않았지만, 괜히 사람이 저렇게 많이 있는걸 보니 더워지는 것 같은 기분이 든다."
    "실제로 가을이라고는 해도 아직 낮에는 꽤 햇빛이 쨍쨍하다."
    "누나는 조심히 주차장 한구석에 차를 세웠다."
    "입구에서 조금 떨어져 있는 곳이다."

    scene bg everandDoor with fade

    meeyoung "주차할 곳도 마땅치 않네..."
    player "자리가 없으니, 걸어가야지 뭐."
    hide Normal
    show Smile
    meeyoung "오 그래도 투정 부리지 않네 [name]?"
    player "나를 무슨 애로 알고 있어 이 누나가."
    meeyoung "애 맞지 않아? [name] 너 정도면."
    player "곧 있으면 고등학교 들어가는 학생한테 못 하는 말이 없으시네요 미영씨."
    hide Smile
    show Normal
    meeyoung "나한테는 아직 애 맞는데?"
    player "그건 누나 기준에서지."
    hide Normal
    show Angry
    meeyoung "놀리는 거야 지금~? 나이 많다고?"
    meeyoung "그리고 또 미영이라 부른다."
    hide Angry
    show Normal
    meeyoung "포기한 거야? 영이라고 부르는 건."
    player "포기한 게 아니라 미영 누나가 더 편해서 그러지."
    hide Normal
    show Angry
    meeyoung "에휴 그래 내가 졌다 졌어."
    meeyoung "빨리 줄이나 서자 이상한 소리 말고."
    "조금이라도 더 이상한 소리를 했다가는 그대로 나를 여기 두고 미영 누나가 도망갈 것 같다."
    "나이 가지고 놀리는건 이쯤해야할 것 같다."
    "나와 미영 누나는 빠르게 맨 뒤에 줄에 자리를 잡고 섰다."
    
    hide Angry with dissolve

    scene bg magicTree with fade

    play music "audio/titleamended-1.mp3"
   
    "예상했던 것과 다르게 빠르게 줄은 줄어들었고."
    "누나와 나는 점심시간이 되기 전에 무사히 입장 할 수 있었다."
    show Smile with dissolve
    meeyoung "그래도 빨리 들어온 것 같은데? 생각보다는."
    player "그러게 생각보다 줄 금방 없어지더라."
    "들어왔는데도 사람은 여전히 바글바글하다."
    "점심시간 직전이라 빠르게 점심을 먹으러 가는 사람들하고 빨리 놀이기구를 타려고 가는 사람들이 뒤섞여 꽤나 인파가 혼란스럽다."
    "길은 또 왜 이렇게 커서 혼란스러운지..."
    player "여기도 똑같이 정신없네, 일단 밥부터 먹어야 하나."
    hide Smile
    show Normal
    meeyoung "너 배고파?"
    player "딱히? 배고프진 않은 듯."
    hide Normal
    show Angry
    meeyoung "배고프지도 않으면서 왜 먹자고 해."
    hide Angry
    show Smile
    meeyoung "지금은 식당에 사람도 많을 테니까 놀이기구 먼저 타자."
    player "그러는 게 좋을 것 같은데, 뭐 타야 하지 진짜."
    hide Smile
    show Normal
    meeyoung "오는 동안 타고 싶은 거 생각 안 했어?"
    player "흠..."
    "차에서 뭘 타고 싶은지 고민해보겠다고 말했지만"
    "지금까지 생각해본 결과 끝내 생각나는 건 없다."
    hide Normal
    show Angry
    meeyoung "으이구 생각해놓겠다고 해놓고 멍때리고 있었지?"
    player "아니.... 생각은 하고 있었는데 그...뭐가 있는지 기억이 안 나서."
    meeyoung "찾아봤어야지 인터넷."
    player "아니 찾아봐도 모르겠고 애초에 없을 수도 있죠. 안온지도 꽤 됐는데."
    hide Angry
    show Normal
    meeyoung "정 타고 싶은 거 없으면 내가 타고 싶었던 거 타볼래?"
    "순간 미영누나의 말에 심장이 놀라 시큰거린다."
    "분명 이 누나가 타고 싶은 건 아까도 잠시 들었지만 거의 다 무서운 거였으니까..."
    "난 그런 거 못 타는데 진짜."
    "일단 급한 대로 가장 가까운 데라도 가서 타보자고 해야겠다."
    player "OO랜드는 엄청 넓으니까."
    player "일단 가까운 곳에 있는 놀이기구부터 타면 되는 거 아님?"
    hide Normal
    show Smile
    meeyoung "오 똑똑한데 [name]?"
    hide Smile
    show Normal
    meeyoung "그래 그러면 일단 가까운 곳 먼저 들릴까?"
    player "엉 그런데 볼만한 지도 같은 거 있으려나..."
    hide Normal
    show Smile
    meeyoung "보면되는거 아니야? 휴대폰."
    player "아 그러네."
    "잠시 휴대폰으로 OO랜드 지도를 검색했다."
    "지도에는 다양한 놀이기구와 여러 시설의 위치가 보인다."
    hide Smile
    show Normal
    meeyoung "놀이기구 어떤 게 가까워?"
    "그리고 가장 가까운 놀이기구는 미영누나가 말하던 티익스프레스보다 비교적 작아 보이는 롤코같다."
    "아무리 그래도 작지만 무서울 것 같은ㄷ..."
    meeyoung "오 롤러코스터?"
    meeyoung "못탄다 하지 않았어? 무서운 거."
    player "그렇긴한데, 그래도 이 정도면 탈 수 있지 않을까 싶은데."
    meeyoung "지도로는 작게 보여도 꽤 클 텐데 이 놀이기구."
    meeyoung "안타는게 좋지 않을까? 이거."
    player "아무리 그래도 이정도는 탈 수 있습니다."
    meeyoung "오호라 그렇단 말이지?"
    player "그 말투 뭐임?"
    hide Normal
    show Smile
    meeyoung "그냥 용감하다 싶어서."
    player "나를 뭐로 알고 있는 거야 이 누나는?"
    hide Smile
    show Normal
    meeyoung "겁쟁이 [name]?"
    player "이 누나가 참 너무 나를 무시하는데."
    "그렇게 잠시 대화를 나누고 있을 때."
    "누군가 천천히 다가왔다."
    "하늘색 와이셔츠와 검은색 바지를 멀끔하게 입은 청년이다."
    "딱 봐도 성인으로 보이는 듯한 분위기를 풍기고 있었다."
    "옆에는 몸이 좋아 보이는 남자 또한 보였다."
    hide Normal with dissolve
    manone "ㅈ,저기 그...쓰읍."
    mantwo "야이 새끼야 답답하게 뭘 그러냐 빨랑 말해."
    manone "아 꼬우면 네가 말해 병X아."
    mantwo "하아 그래 비켜봐."
    mantwo "저 혹시 마음에 들어서 그런데 번호 좀 주실 수 있으신가요?"
    mantwo "괜찮으시면 같이 노는 것도 좋을 것 같은데요?"
    "하늘색 와이셔츠를 입은 사람은 부끄러운지 다른 곳을 보고 있었고, 답답해서 질문하는 역할을 낚아챈 몸이 좋은 남자도 누나의 눈을 똑바로 바라보지 못했다."
    "누나한테 헌팅하는건가 참 운도 지지리도 없어 보인다."
    show Normal with dissolve
    meeyoung "아아 그런데 어떻게 하죠?"
    "누나는 갑자기 아깝다는 듯 한 뉘앙스로 그렇게 말하고는 나를 본다."
    hide Normal
    show Smile
    meeyoung "저기 쟤 보여요? 쟤가 제 남친이라서요."
    mantwo "네..? 아 그러세요?"
    hide Smile
    show Normal
    meeyoung "죄송해요 제가 연하를 좋아해서."
    mantwo "아, 네..."
    manone "네 저희 나이는 아직."
    mantwo "야 새끼야 가자..."
    manone "아 왜?"
    mantwo "보면 몰라? 까인 거잖아 씨X."
    hide Normal with dissolve
    "그렇게 말하며 두 남자는 빠르게 어디 기념품 가게에 들어가 버렸다."
    "하긴 저렇게 대놓고 거절하면 나라도 쪽팔릴 듯 하다."
    menu:
        "그래서 내가 진짜 남친임?":
            hide Normal
    show Angry 
    meeyoung "쪼그만게 못 하는 소리가 없네."
    player "아니 본인이 그렇게 말씀하셨잖수."
    hide Angry
    show Smile
    meeyoung "어머 사실 기대하고 있었구나?"
    player "빨리 놀이기구 타러 가시죠~"
    hide Smile
    show Normal
    meeyoung "알았어."
    hide Normal
    show Smile
    meeyoung "부끄러움이 많구나 [name]."
    player "뭐라는 거야 이 누나가? 빨리 가자고."
    "계속해서 나를 추궁하려는 듯 말을 걸어오는 누나를 애써 무시하면서 아까 봤던 롤러코스터가 있는 곳으로 향했다."
    "말을 최대한 무시하면서 말이다."

    scene bg RollingXTrin with fade

    play music "audio/Mee/MEE Rules.mp3"

    "도착하니 사람들이 꽤 많이 서 있었다."
    "표지판에는 대기시간 40분이라는 팻말도 붙어있었다."
    player "오 이런, 사람이 생각보다 많네."
    show Normal with dissolve
    meeyoung "그러게 얼마나 기다려야 하려나."
    hide Normal
    show Smile
    meeyoung "일단 서야지 줄."
    player "그런데 줄 서면 40분 동안 뭐함?"
    hide Smile
    show Normal
    meeyoung "글쎄~ 대화라던가...?"
    player "피곤하겠다."
    hide Normal
    show Smile
    meeyoung "끈기 없이 왜 그래 [name]?"
    player "끈기 없어서 죄송합니다~"
    hide Smile
    show Normal
    meeyoung "빨리 줄이나 서자 줄 더 늘어나기 전에."
    meeyoung "지금은 그래도 점심시간이라 조금 덜 한 것 같은데?"
    player "오 이런, 더 길어진다고?"
    meeyoung "놀이공원 와봤던 거 맞아?"
    meeyoung "줄 서는 건 당연하잖아."
    player "예전에 왔을때는 사람 별로 안 많아 보이던데..."
    meeyoung "현장체험학습으로 온 거 아니야?"
    player "그렇지?"
    meeyoung "평일에 왔던거니까 당연히 사람이 적지."
    hide Normal
    show Angry
    meeyoung "빨리 서기나 해 줄."
    meeyoung "계속 여기서 수다만 떨 거야?"
    player "넵..."
    hide Angry with dissolve

    "그렇게 미영누나와 나는 자리를 잡고 줄을 섰다."
    "가을인데도 불구하고 꽤 날씨가 후텁지근해서 그런지 땀을 흘리고 있는 사람도 몇 명 보였다."
    "미영누나도 마찬가지였다."

    play music "audio/Silent Night - DJ Williams.mp3"

    scene eventCG MeeSum1 at EventEffect with fade 

    "더워서 그런지 땀을 흘리면서 입고 온 가디건을 벗고 있었다."
    "지금 보니까 이 누나 얇은 흰색 면티를 입고 있다."
    "이 누나가 부끄럽지도 않나 그런 옷을 입고..."

    scene eventCG MeeSum3 at EventEffect2 with fade

    "괜스레 누나에게서 시선을 피하게 된다."

    scene eventCG MeeSum4 with fade

    meeyoung "뭐 봐 [name]?"
    player "아무것도 안 보는데."
    player "그그 ... 누나 더운가 봐?"
    "나는 다시 한 번 누나 쪽으로 시선을 맞춘다."
    meeyoung "그러게 오늘 춥다고 해서 입었는데 가디건..."
    meeyoung "이렇게 더운 줄 알았으면 안입었을텐데..."
    "누나는 그렇게 말하며 얇은 면티를 손으로 팔랑거린다."
    "분명 더워서 그러는 거겠지..."
    "그렇게 생각하며 뜨거워지는 얼굴을 애써 찬 손으로 비비며 식혀본다."
    meeyoung "푸흡..."
    "잠시 손으로 얼굴을 식히고 누나를 다시 바라보니 재미있다는 듯 누나는 웃고 있다."
    player "놀리니까 재미있음?"
    meeyoung "응 완전."
    player "이 누나가 하루에 몇 번을 놀리는 거야 오늘?"
    "내 말은 아랑곳하지 않고 누나는 능글거리게 다른 곳을 바라본다."
    meeyoung "너는? 안 더워?"
    player "난 잘 모르겠는데?"
    player "근데 평소보다 춥진 않은 듯."
    meeyoung "부럽네 [name] 더위 안 타서."
    player "아이고 칭찬 감사합니다."

    scene bg RollingXTrinExit with fade

    play music "audio/titleamended-1.mp3"

    "그렇게 잠시 수다를 떠는 동안 시간은 꽤나 빠르게 지나가고 있었다."
    "줄을 선지 25분 쯤 지났고 그때 쯤 나하고 누나 앞에 줄은 거의 사라졌었다."
    "어느새 놀이기구 입장을 기다리고 있었다."
    "그런데 생각보다 레일이 큰데...?"
    player "뭐야 이거 레일 왜 이렇게 큼?"
    show Smile with dissolve
    meeyoung "뭐야 [name] 겁먹은거야?"
    meeyoung "귀엽네~"
    hide Smile
    show Normal
    meeyoung "무서우면 다시 내려갈래?"
    player "괘,괜찮음 여기까지 왔는데 무슨."
    seeman "다음 손님 입장하실게요."
    player "..."
    hide Normal with dissolve

    scene bg blackOut with fade

    "큰일이다. 이미 열차에는 탑승해버렸고."
    "알바생 분들은 안전바를 체크해주고 계신다."
    player "(어쩌지...어쩌지...)"
    "그렇게 떨며 다리를 벌벌 떨고 있을 때"
    "옆에 있는 미영누나가 갑자기 손을 잡았다."

    scene bg RollingXTrinExit at text_effect

    player "앗 깜짝이야!"

    scene bg RollingXTrinExit at default

    show Smile with dissolve

    meeyoung "왜 그래?"
    player "아잇 놀랐잖아 누나!"
    hide Smile 
    show Normal
    meeyoung "왜 그렇게 놀라고 그래?"
    meeyoung "컨디션 안 좋아 보이는 것 같은데, 어디 아파?"
    hide Normal
    show Smile
    meeyoung "아니면 많이 무섭나봐 [name]?"
    player "아니 애초에 올 때 이런 거 탈 생각 없었으니까 조금 무섭긴 하지."
    meeyoung "어쩔 수 없네~"
    meeyoung "저기 여기 좀 내 ㄹ..."
    scene bg RollingXTrinExit at text_effect
    "철컹"
    scene bg RollingXTrinExit at default
    player "으아악!!"
    "내가 소리 지르자 뒤에 있던 초등학생 정도로 보이는 애들이 키득키득 웃는다."
    "부끄러워서 귀가 다 빨개지는 것 같다."
    show Normal with dissolve
    meeyoung "하아...안되겠다 이번 건 타야겠네."
    player "네?"
    "열차는 내가 놀라든 말든 천천히 올라갔다."
    "생각보다 올라가는 길이 길어 보이진 않는다."
    "그럼에도 꽤 높아보인다."
    player "으아악..."
    hide Normal with dissolve
    show SmileZoom with dissolve
    meeyoung "즐겨 [name]."
    meeyoung "이미 늦었으니까."
    meeyoung "꽉 잡고 정신."
    player "예? 미영 씨?"

    scene bg RollerIn with fade

    play sound "audio/SoundEffect/[Track 01] Roller Coaster Sound Effect.wav" volume 0.05

    "그리고 열차는 급격하게 꺾여 내려가기 시작했다."
    "그 순간 아랫배가 묘하게 간질거리는 감각이 느껴진다."

    player "으아아아아악!!!"
    "정신없이 요동치는 시야 속 계속해서 돌아가는 롤러코스터 때문에 정신이 없다."
    "그런데 왜 인지 나만 소리 지르는 것 같은데?"
    "나는 계속 돌아가는 고개를 겨우 고정하고 누나를 봤다."

    show NormalZoom with dissolve

    meeyoung "..."
    "누나는 아무렇지도 않다는 듯이 맹한 표정으로 하늘을 볼 뿐이었다."
    "지금 나만 무서운 거야?"
    "그리고 열차는 다시 한 바퀴 돈다."
    player "으아아아악!!!!!"
    hide NormalZoom
    show SmileZoom
    meeyoung "하하하하"
    "미영 누나는 이런 내 모습이 재미있는지 갑자기 빵 터진다."
    player "ㅁ,뭐임 비웃느는 거임?"
    "아랫배가 간지러워서 말도 제대로 안 나온다."
    meeyoung "눈이나 똑바로 떠."
    meeyoung "지금 너 완전히 눈 돌아갔어."
    player "ㅁ,무슨 으아아악!!!"
    "열차가 움직이는 동안 나는 아무 말도 할 수 없었다."
    "그렇게 두 바퀴 정도 레일을 돌고 열차는 멈췄다."
    "열차가 멈추자 다리는 후들거려서 서는 것도 힘들다."

    stop sound

    scene bg RollingXTrin with fade

    player "흐어어어..."
    show Normal with dissolve
    meeyoung "많이 힘들어?"
    player "다리가 움직이지 않음."
    hide Normal
    show Smile
    meeyoung "하하 잡아 손."
    meeyoung "생각보다 많이 못 타는구나 무서운 거"
    "미영누나 손을 잡고 움직이려고 하는데 다리가 휘청거린다."
    player "악!"
    meeyoung "하하 똑바로 못 서?"
    hide Smile
    show Normal
    meeyoung "어릴 때 처럼 엎어줄까 예쁜 누나가?"
    player "아니 뭔 내가 애야?"
    meeyoung "아까도 하지 않았나 말?"
    hide Normal
    show Smile
    meeyoung "너 정도면 아직 애지."
    player "하긴 미영 씨 나이 생각하면 확실히 내가 애긴 하 ㅈ.."
    "순간 미영 누나는 내 손을 놔버렸다."
    player "악!"
    player "왜 갑자기 손을 놔 위험하게!"
    hide Smile
    show Normal
    meeyoung "아이쿠 미안 실수로 손이 미끄러졌네."
    player "아니 아무리 봐도 고의잖아!"
    meeyoung "맞아 실수."
    hide Normal
    show Angry
    meeyoung "너도 방금 말 그거 한 거지 실수?"
    "순간 미영 누나의 눈빛에, 약간에 위협을 느꼈다."
    "지금 이대로 실수라고 하지 않으면 평생 후회할 것만 같은 그런..."
    player "죄송합니다, 실수입니다."
    hide Angry
    show Normal
    meeyoung "후..그래서 어디 갈 거야 우리?"
    "미영 누나는 고개를 갸웃거리며 나를 바라봤다."
    "다음 놀 곳도 내가 정해야하는건가?"
    player "흠 방금은 내가 정했으니 이번에는 누나가 정하면 안 됨?"
    hide Normal
    show Angry
    meeyoung "그치만 난 자주 안 와봤는데 여기."
    player "누가 보면 저는 많이 와본줄 알겠는데요."
    hide Angry
    show Normal
    meeyoung "그래도 많이 와봤잖아 나보단?"
    player "누나 몇 번 왔는데?"
    meeyoung "이번이 두 번째인데."
    player "나도 두 번."
    hide Normal
    show Smile
    meeyoung "그럼 거기서 거기네."
    player "그럼 누나도 타고 싶은 거 말하면 되겠네."
    hide Smile
    show Normal
    meeyoung "그럼 티익스프레스..."
    player "아니 그건 내가 못 타잖아요."
    meeyoung "왜? [name] 키 140 안 넘어?"
    player "아니 그런 말이 여기서 왜 나옴."
    player "애초에 딱 보면 140 넘잖아요."
    meeyoung "그랬어 [name]?"
    hide Normal
    show Smile
    meeyoung "전혀 몰랐네~"
    player "이 누나가 말이 되는 농담을 해야지."
    hide Smile
    show Normal
    meeyoung "왜 말이 안돼? 140일 수도 있지"
    player "너무 막 뱉는 거 아님?"
    meeyoung "그래서 뭐 탈거야?"
    player "저기요?"
    player "(꼬르륵)"
    "그렇게 대화하려던 참에 갑자기 나오는 꼬르륵 소리."
    meeyoung "배고픈 모양이네."
    player "음, 그런 듯."
    meeyoung "그럼 밥 먹을까?"
    player "오 그러게 뭐 먹을거임?"
    meeyoung "생각 안 해왔어? 뭐 먹을지?"
    player "엉 안 했는디."
    hide Normal
    show Angry
    meeyoung "그래 기대도 안했다~"
    hide Angry
    show Normal
    meeyoung "여기서 좀만 가면 맛있는 집 있데."
    meeyoung "가보자 많이 안 머니까."
    player "오 맛있는 곳, 군침이 싹 도는데?"
    "생각해보니 놀이공원에서는 보통 뭘 먹지?"
    "간식이라면 츄러스나 아이스크림을 먹겠지만."
    "정작 놀이공원 같은 데서 밥을 먹어본 적은 없는 것 같다."
    player "무슨 음식 하는 곳임?"
    meeyoung "글쎄 잘은 모르겠는데 어쨌든 맛있다는데?"
    player "말 안 하니까 무서운데..."
    hide Normal
    show Angry
    meeyoung "내가 사는 건데 안 먹을 거야?"
    player "감사히 먹겠습니다."
    hide Angry
    show Smile
    meeyoung "옳지 착하네!"
    meeyoung "따라와 아마 5분 정도면 걸으면 될 거야."
    player "넵"
    
    scene bg foodRoom with fade
    play music "audio/shop.wav"

    player "누나"
    show Normal with dissolve
    meeyoung "응? 왜 [name] ?"
    player "여기 한식집 아님...?"
    hide Smile
    show Normal
    meeyoung "응 맞아 한식집."
    hide Normal
    show Smile
    meeyoung "인터넷에서 보니까 여기 굉장히 맛있다더라."
    player "아니 한식은 집에서 먹을 수 있는데."
    player "여기까지 와서 먹어야 함?"
    hide Smile
    show Normal
    meeyoung "그런데 여기 진짜 맛있데."
    meeyoung "칭찬이 엄청 많던데?"
    player "아니 그래도 놀이공원까지 와서 한식을 굳이 먹어야겠수?"
    hide Normal
    show Angry
    meeyoung "누구 덕분에 여기 온 건데?"
    hide Angry
    show Smile
    meeyoung "굶고 싶구나! 우리 [name]~"
    player "앗, 거 참 이 누나가 참..."
    player "메뉴가 뭐가 있나."
    hide Smile
    show Angry
    meeyoung "또 말 돌리기...하아 이제 화내는 것도 잊어버릴 것 같네."
    meeyoung "빨리 골라 메뉴, 이러다가 놀이기구 다른 거 못 타겠다."
    menu:
        "네 알겠습니다~":
            hide Angry with dissolve

    "딱 눈에 띄는 건 고등어구이 반상이라고 쓰여있는 메뉴."
    "그리고 돼지고기 김치찌개 정식이 딱 눈에 띈다."
    "이 두 개가 가장 위에 있네 제일 맛있는 건가?"
    "아무리 봐도 누나는 김치찌개 먹을 것 같은데..."
    "고등어구이 반상이 나으려나..."
    "김치찌개는 얻어먹을 수도 있으니까."


    player "나는 고등어구이 반상, 누난?"
    show SmileZoom with dissolve
    meeyoung "난 김치찌개."
    "역시나 라는 생각과 함께 입꼬리가 살짝 올라갔다."
    hide SmileZoom
    show NormalZoom
    meeyoung "표정 수상하다, [name]?"
    player "어어?"
    meeyoung "입 끝이 야무지지 못하게 실룩거리는 거 하고는."
    hide NormalZoom
    show SmileZoom
    meeyoung "응큼한 거 생각하는 거야, 밥 먹으면서?"
    player "내가 누나인 줄 아십니까."
    player "참 알기 쉬운 사람이라고 생각함 누나 보고."
    hide SmileZoom
    show AngryZoom
    meeyoung "아 그러셔? 진짜 그게 다야?"
    player "어허 빨리 주문이나 하셈."
    hide AngryZoom
    show NormalZoom
    meeyoung "너가 주문하는 거 아니었어?"
    player "그럼 제가 왜 말했겠습니까?"
    meeyoung "어휴 그래 알았다."
    hide NormalZoom
    show SmileZoom
    meeyoung "주문해줄게 예쁜 누나가"
    player "아 예."
    hide SmileZoom
    show NormalZoom
    meeyoung "그래도 너 주문 안 해버릇 하면 나중에 사회생활 힘들텐데..."
    player "제 미래는 제가 알아서 하겠음."
    meeyoung "아 그러셔?"
    meeyoung "그래 뭐 내가 졌다~"
    hide NormalZoom with dissolve
    show Normal with dissolve
    meeyoung "저기요?"
    hide Normal with dissolve

    "미영누나는 내가 말한 고등어 반상과 김치찌개를 시켰다."
    "그렇게 잠시"
    "주문하고 멍때리고 있다가, 다시 메뉴판을 보니 뒤늦게 김치찌개 반상이 2인분이라는 괄호에 문구를 봤다."
    player "잠만 누나 여기 2인분이라고 적혀있는데"

    show Normal with dissolve

    meeyoung "그치? 그래서?"
    player "아니 누나 혼자 2인분 다 먹을 수 있어?"
    meeyoung "먹을 수 있어. 내가 먹는 거 잊은 거야 [name]?"
    player "아니 그래도 2인분이라는데?"
    hide Normal
    show Smile
    meeyoung "괜찮아 [name] 그리고 남겨도 어차피 내가 사는거 잖아?"
    player "그렇긴 한데 이게 맞나?"
    hide Smile
    show Normal
    meeyoung "걱정말고 너나 남기지마 음식"
    player "나야 뭐 걱정은 없긴 한데."
    "그렇게 잠시 대화를 하던 도중 음식들이 나왔다."
    "내 앞에는 고등어구이 반상 누나 앞에는 김치찌개 정식이 있었다."
    "공깃밥에 여러 밑반찬 그리고 메인 요리, 딱 봐도 엄청 양 많아보이는데..."
    meeyoung "아 맞다 음료 같은 건, 필요 없으려나?"
    player "커피집 사장님 아니랄까 봐 여기서도 음료 찾네."
    meeyoung "없으면 목 메이잖아, 밥 먹을 때."
    player "콜라도 되나?"
    hide Normal
    show Angry
    meeyoung "왜 많고 많은 음료 중에 콜라야, 하필이면?"
    player "콜라는 누나가 못 만들잖수."
    player "뭐 가끔 콜라도 마시고 싶을 수도 있지."
    hide Angry
    show Normal
    meeyoung "내가 사주는 거니까, 몸에 좋은 거 마셔."
    meeyoung "내 돈 내가 쓰는 거니까 토 달지 말고, 알았지?"
    player "아 예."
    hide Normal
    show Smile
    meeyoung "귀엽기는~"
    hide Smile
    show Normal
    meeyoung "콜라는 안 좋으니까 몸에, 다른 거 시켜줄게."
    meeyoung "과일주스?"
    player "응 알겠음"
    meeyoung "자 그러면 주문해놓을테니까 먼저 먹자."
    player "응"

    scene bg foodRoom with dissolve

    "잠시 나와 미영 누나는 조용히 주문한 음식들을 먹었다."
    "맛있는 집이라고 했던 미영 누나 말 대로 음식 맛은 굉장히 좋았다."
    "고등어구이도 많이 짜지 않고 살도 많아서 맛있다."
    player "(우물우물)"
    meeyoung "맛있지 생각보다?"
    player "그런 듯 그냥 집에서 밥 먹는 느낌일 줄 알았는데 조금 다른 느낌."
    meeyoung "거봐 내 말 믿어서 나쁠 것 없지?"
    player "그런 거치고는 누나 업보가."
    meeyoung "어허."
    player "맛있는 것 같네. 확실히."
    player "오길 잘한 것 같다."
    meeyoung "그치?"
    meeyoung "데려와 주셔서 감사합니다. 예쁜 누나라고 해주면 되겠네."
    player "예쁜은 빼시죠?"
    meeyoung "거참 쩨쩨하네 [name]."
    meeyoung "먹기나 하자 밥."
    "그런식에 짧은 대화를 하고 음식은 금방 바닥을 드러냈다."
    "내가 음식을 다 먹고 미영 누나의 음식을 봤 을때 모든 그릇이 바닥을 드러내고 있었다."
    "다시 깨닫는 거지만 누나, 음식을 엄청나게 잘 먹었지..."

    scene bg foodCoatfront with fade

    player "후 잘 먹었다."
    show Normal with dissolve
    meeyoung "배부르네. 나도."
    meeyoung "이제 어디 갈까? [name]?"
    player "글쎄..."
    player "일단 정하고 움직이는 게 좋을 듯?"
    player "걸어 다니면서 정하면 불편할 것 같음."
    meeyoung "배부르다는 거 핑계로 앉아서 휴대폰 보게?"
    player "아니 왜 이야기가 그렇게 흘러감?"
    hide Normal
    show Smile
    meeyoung "농담이야~"
    hide Smile
    show Normal
    meeyoung "그래서 뭐 놀이기구 타고 싶은 거 있는거야 [name]?"
    player "흠...잘 모르겠는데."
    player "뭔가 있던 것 같기도 하고 없는 것 같기도 한..."
    meeyoung "역시 티익스프레스나..."
    player "아이 이 누나가 또 왜 그러실까."
    player "잠깐만 기다려보시죠?"
    player "흠...아 범퍼카 어떰?"
    player "예전에 타고 싶었는데 줄 길어서 못 탔던 거 같은데."
    meeyoung "오 그런 거 재미있어하는구나"
    player "재미있다기보다는 타보고 싶다...?"
    meeyoung "거기서 거기 아닌가?"
    hide Normal
    show Smile
    meeyoung "그래 가보자 나도 안타 본 지 꽤 된 거 같아."
    "휴 일단 티익스프레스는 안타도 돼서 다행이다."
    "만약 진짜로 타는 곳까지 갔으면 얼마나 피곤할지..."

    scene bg turnRoomA with fade

    play music "audio/titleamended-1.mp3"
    
    "그렇게 누나와 나는 범퍼카가 있는 곳으로 왔다."
    "꽤 멀어서 30분 넘게 헤맸던 것 같았지만, 다행히 중간에 지도로 겨우 찾아올 수 있었다."
    "하지만..."
    player "아...다리 아프다."
    show Normal with dissolve
    meeyoung "벌써?"
    player "아니 30분 동안 걷기만 했잖아."
    meeyoung "이 정도면 30분밖에 아니야?"
    player "30분 씩 이 나지!"
    hide Normal
    show Smile
    meeyoung "나약하기는, [name]."
    player "나약해서 죄송합니다."
    "그렇게 잠시 나는 아픈 다리가 편해질때까지 쭈그려 앉기로 했다."
    "내 바로 앞에는 회전목마가 있었다."
    "궁금해서 잠깐 스마트폰을 바라보니 시간은 3시쯤이었다."
    "밥 먹고 나왔을 때 시간을 안보긴 했는데 점심을 늦게 먹긴 했구나."
    hide Smile
    show Normal
    meeyoung "부끄럽지도 않아 [name]?"
    player "왜 부끄러움?"
    hide Normal
    show Smile
    meeyoung "회전목마 앞이라 애들도 많은데 그렇게 쭈그려있는 거 부끄러울 만한데."
    player "오 이런."
    "다리가 너무 아파서 생각을 안 하고 있었는데."
    "지금 여기 놀이공원 한복판이었지."
    "뒤늦게 주위를 돌아보니 나를 멍하니 바라보는 아이들, 그리고 지나가는 사람들도 묘하게 나를 보고 가는 듯한 느낌이 들었다."
    "오 이런."
    player "아 잊고 있었네."
    "약간 귀가 붉어지며 열감이 느껴지는 듯하다."
    meeyoung "하하."
    player "동생을 놀리는 게 재미있음?"
    meeyoung "너무?"
    hide Smile
    show Normal
    meeyoung "반응이 재미있어, [name] 너는."
    player "거 참 이 사람이."
    meeyoung "그래도 이제 다리 안 아파 보이는데?"
    player "엉 이제 안 아프긴 한 듯."
    meeyoung "빨리 가자 사람 많아지겠다."
    player "오키."
    hide Normal with dissolve

    scene bg bumper with fade

    "예상했던 대로 범퍼가 앞에는 사람이 꽤 많았다."
    "대충 봐도 아까 탔던 롤코보다 2배는 되어 보이는 길이에 줄이다."
    "줄 옆에는 대기시간이 적혀있었다."
    "1시간..."
    player "..."
    show Normal with dissolve
    meeyoung "자 빨리 서자 줄."
    player "아니 근데...누나 이거."
    meeyoung "응 무슨 일인데 그래?"
    player "1시간은 너무 줄이 긴 거 아님?"
    player "1시간인데."
    meeyoung "타고싶다 하지 않았어?"
    player "그렇긴 한데."
    hide Normal
    show Smile
    meeyoung "그럼 줄 서면 되는 거지~"
    player "그냥 귀찮지 않나?"
    hide Smile
    show Angry
    meeyoung "설마 여기까지 와놓고 타기 싫다고 말할 거야?"
    player "아니요. 그건 아닌..."
    meeyoung "그러면 빨리 줄이나 서."
    hide Angry
    show Normal
    meeyoung "설마 이런 기회를 놓칠 거야?"
    player "뭔 기회요?"
    hide Normal
    show Smile
    meeyoung "나같이 예쁜 누나하고 같이 줄 서볼 기회?"
    player "아까 섰잖아요."
    meeyoung "좀 더 오래 줄 서는 것도 새롭겠지~"
    player "아 옙."
    hide Smile
    show Angry
    meeyoung "뭐야 그 반응은?"
    player "아무것도 아님~"
    meeyoung "뭐임 그 말투 뭔가 놀리는 것 같은데."
    player "그런 거 아니에요~"
    meeyoung "아 그러셔?"
    player "일단 빨리 줄 섭시다."

    scene bg bumper with dissolve

    "줄을 서기 시작했다."
    "시간은 오후 3시."
    "슬슬 오늘 온도는 최고온도를 향해 가고 있는 듯했다."
    "스마트폰을 보니 온도가 12도라고 쓰여있다."
    "하지만 해가 쨍쨍해서 체감 온도는 좀 더 큰 듯했다."
    "미영 누나는 더운 듯 가디건은 진작에 벗은 이후였다."
    player "누나 많이 더움?"
    show Normal with dissolve
    meeyoung "그러게."
    "생각해보니 미영 누나는 굉장히 더위를 많이 타는 것 같은데..."
    "미영 눈나 부모님 고향이 어디라고 그랬더라? 동유럽인가 북유럽인가 대충 어디라고 그랬는데."
    "암튼 추운 나라 인종이라고 그랬다."
    hide Normal
    show Angry
    meeyoung "오늘은 춥다고 한 거 분명히 들었는데, 혹시 했더니만 역시나 쌀쌀하지도 않잖아."
    player "레알 요즘 일기예보 맞는 거 본 적 한 번도 없는 듯."
    hide Angry
    show Normal
    meeyoung "안 더워?"
    player "난 뭐 원래 더위 별로 안타니까."
    player "땀은 종종 난 것 같긴 한데 더운 건 잘 못 느낀 것 같은데?"
    meeyoung "부럽네 더위 많이 안 타서."
    player "하하 별말씀을."
    hide Normal
    show Angry
    meeyoung "칭찬 아니거든?"
    player "넵."
    player "그나저나 누나 이 표 어떤 친구한테 받은 거야?"
    "지금 와서 생각해보니 미영 누나 친구라고 하면 딱 그려지는 얼굴이 없다."
    "보통 이 사람의 친구라 하면 이럴 것 같은데 하고 그려지는 외형이 있는데."
    "물론 막 깡패나 무서운 사람이랑 친구를 할 것 같진 않은 미영 누나지만."
    "그렇다고 해서 딱 다른 분위기가 그려지는 느낌도 아니란 말이지."
    hide Angry
    show Normal
    meeyoung "아 대학교 남자 후배가 줬어."
    player "누나한테 연락하는 후배도 있었음?"
    meeyoung "아 응 그 이름이... 김 뭐였나...?"
    player "후배 이름도 모르는 거임?"
    meeyoung "아니야 알아 그 김..."
    player "아이고 됐습니다."
    player "그래도...뭔가 멋있는데."
    meeyoung "뭐가 말인데?"
    player "그냥 뭐 미영 누나가 선배같이 막 행동하는 후배가 있다는 거 조금 멋있어 보임."
    meeyoung "멋있어? 그게?"
    meeyoung "글쎄..."
    meeyoung "후배가 갑자기 놀이공원 가자고 하면서 표 받았는데."
    meeyoung "갑자기 취소 됐어 약속."
    player "엥? 약속한 거였어?"
    hide Normal
    show Smile
    meeyoung "응 그런데 걔가 만나자고 한 날 지금 보니까 내가 바빠서."
    meeyoung "오늘 다녀오고 못 갈 것 같다고 하게."
    player "아하..."
    player "응?"
    hide Smile
    show Normal
    meeyoung "왜 그래?"
    player "아니 잠만 그럼 취소 된 약속이 아니잖수!!"
    hide Normal
    show Smile
    meeyoung "취소 된거지 약속 날 안된다니까."
    player "아니 거참 그래도 말은 해야지!"
    meeyoung "말했으면 여기 못 왔거든~"
    hide Smile
    show Angry
    meeyoung "고마워해도 모자랄 판에."
    player "그건 그렇긴한데..."
    "뭔가 미영 누나한테 바람맞은 그 김...후배 씨 한테 괜히 미안한 느낌이 든다."
    "이런 여우 같은 미영 누나한테 걸려서..."
    "이 누나는 또 그걸 그대로 이용한다는 게 참..."
    hide Angry
    show Normal
    meeyoung "왜 그래 [name]?"
    player "아무것도 아님."
    "다시 한번 바람맞은 김후배 씨한테 사과 인사를 속마음으로 드렸다."
    
    scene bg bumper with fade

    "줄이 줄이다 보니 범퍼카 줄은 확실히 롤러코스터 줄보다 느리게 줄어들었다."
    "시간은 어느새 3시 30분이었다."
    show Angry with dissolve
    meeyoung "진짜 길긴 하네 줄."
    player "그렇게 이렇게 길 줄 알았으면 마실 거라도 사 올걸 그랬다."
    "그 대화를 이후로 잠시 누나와 대화하다가 폰보다가 대화하다가 폰 보다가를 반복했다."

    "폰을 줄 설 때마다 계속 봐서 그런지 아니면 오래돼서 그런지 모르겠지만."
    "폰 배터리는 대부분 떨어졌다는 알람이 울렸다."
    "그때 이후로는 스마트폰은 주머니에 집어넣고 나는 멍하니 다른 사람이 범퍼카 타는 걸 바라보기만 했다."
    hide Angry
    show Normal
    meeyoung "심심해?"
    player "아, 응 그런 듯."
    meeyoung "심심한데 가위바위보 할래?"
    player "뭐임 누나 완전 유치함."
    hide Normal
    show Smile
    meeyoung "동심이 살아있는 거지."
    player "동심 따지기에는 누나 나이가 좀..."
    hide Smile
    show Angry
    meeyoung "어허 혼날래?"
    hide Angry
    show Normal
    meeyoung "어차피 할 거 없잖아 지금."
    player "그렇긴 한데."
    hide Normal
    show Smile
    meeyoung "그럼 결정~"
    player "아니 거참."
    meeyoung "가위바위"
    player "아 앗 보!"
    "미영누나는 주먹 나는 보자기를 냈다."
    hide Smile
    show Normal
    meeyoung "아 뭐야 졌네..."
    player "아니 이 누나가 하기 싫다니까 꼭..."
    hide Normal
    show Smile
    meeyoung "그래도 결국에는 냈잖아? 보자기."
    meeyoung "뭔가 아쉽네"
    hide Smile
    show Normal
    meeyoung "한 판 더 할까?"
    player "아 또?"
    hide Normal
    show Smile
    meeyoung "왜 할만하지 않아?"
    meeyoung "해보자 재미있지 않아?"
    menu:
        "한번 해보죠 그럼.":
            player "안내면 진 거 가위 바위 보!"
    "이번에는 내가 주먹 누나가 보자기다."
    player "아 뭐야 졌네."
    "그리고 그 순간."

    scene bg blackOut with fade

    "미영누나는 내 손을 잡고는 자신의 쪽으로 당겼다."
    "그런데 잠만 이렇게 되면 여기저기 닿을 텐데."
    "그대로 계속해서 거리가 가까워질 때."
    "미영 누나는 두 손가락으로 내 손목을 후려쳤다."

    scene bg bumper at text_effect

    "아야!!!"
    show Smile with dissolve
    meeyoung "푸흐흐 좋았어 [name]?"
    player "악 뭐야! 아프잖아! 누나"
    hide Smile
    show Normal
    meeyoung "내가 있다고 하지 않았나 벌칙?"
    hide Normal
    show Smile
    meeyoung "이래서 내가 [name]놀리는 걸 끊지를 못해요."
    player "안 했거든요 그런 말!"
    hide Smile
    show Normal
    meeyoung "까먹은 거 아니야 [name]?"
    player "뭐래 이 누나가 다시 해!"
    hide Normal
    show Smile
    meeyoung "하하 알았어."

    hide Smile with dissolve

    "그렇게 잠시 계속해서 가위바위보를 했다."
    "서로 질 때마다 손목을 맞는데 너무 아프다."
    player "아 팔에 자국나겠다."
    show Normal with dissolve
    meeyoung "별로 세게 안 때렸어."
    player "이게 세게 안 때린거라고?"
    meeyoung "많이 아팠어?"
    hide Normal
    show Smile
    meeyoung "귀엽네 그래서 삐졌어요? 우리 [name]?"
    player "뭐래 이 누나는."
    player "안 삐졌거든."
    meeyoung "하하 다시 봐도 귀엽다니까?"
    hide Smile
    show Normal
    meeyoung "곧 있으면 줄 끝날 것 같은데."
    player "오 그러면 이제 슬슬."
    hide Normal with dissolve
    show NormalZoom with dissolve
    meeyoung "마지막으로 한 번만 더 할래?"
    player "예 곧 끝나는데."
    meeyoung "한 번 더."
    player "아니 거 참 그만했으면 좋겠는데."
    hide NormalZoom with dissolve
    show SmileZoom with dissolve
    meeyoung "이번에는 이기면 소원 들어주는 거로 하는 건 어때?"
    player "오 뭐든?"
    meeyoung "뭐든!"
    "오 진짜 뭐든이면..."
    hide SmileZoom
    show NormalZoom
    meeyoung "어 혹시 이상한 생각하고 있는 거 아니야?"
    player "예? 아무 생각도 안 했는데요?"
    player "이 누나가 갑자기 왜 그럼."
    hide NormalZoom
    show SmileZoom
    meeyoung "엉큼하잖아, 그럴 거라고 생각했지."
    player "거참 너무하시네요."
    player "알았어 하자."
    meeyoung "하하 좋았어."
    hide SmileZoom with dissolve
    show Normal with dissolve
    meeyoung "안내면 진 거 가위바위보."
    "하지만 안타깝게도 내가 졌다."
    player "아 진짜 이게 지네."
    hide Normal
    show Smile
    meeyoung "내가 이겼네?"
    player "아이 진짜...누나 뭐할 건데."
    meeyoung "어머 기대하고 있는 거야 [name]?"
    player "아니 뭐래누 이 누나가."
    seemantwo "다음 분 들어가겠어요?"
    meeyoung "네."

    scene bg blackOut with fade

    "그렇게 범퍼카 중 가장 모서리에 있던 차에 탔다."
    "생각보다 자리가 불편하다."
    "앉으면 푹신할 것 같다고 생각했던 과 다르게 플라스틱 의자라 불편하다."
    player "억 왜 이렇게 불편함 이거."
    "그렇게 말 해도 시끄러워서 그런지 미영 누나는 듣지 못하는 듯했다."
    "그리고 어느 순간부터 멈춰있던 자동차는 움직이기 시작했다."
    "시작한 지 몇초도 채 지나지 않아 누나가 나에게 미친 듯이 달려오는 게 보였다."

    scene bg bumper with fade

    "쿵"
    player "으악!! 아 누나 뭐해!"
    meeyoung "뭐야 이렇게 하는 거 아니었어?"
    player "아니 씨.. 맞긴한데 처음부터 공격하는 게 어디 있음?"
    meeyoung "그러라고 타는 게 범퍼카거든?"
    "실제로 주위를 둘러보니 다른 사람들은 서로 부딪히며 깔깔거리고 있었다."
    player "아니 아무리 그래도 그렇지, 누나는 너무 나만 노리잖아!"
    meeyoung "시끄러워서 잘 안 들려 [name]~"
    "저건 백 퍼센트 다 들리는데 모르는 척하고 있는 거다."
    "미영누나는 계속 강렬하게 내 범퍼카의 뒤를 치고 있다."
    player "악 억!"
    "강한 진동 속에서 계속해서 맞기만 했고."
    "내가 정신 차리고 그나마 여유를 찾았을 때 이미 범퍼카는 끝나있었다."

    scene bg bumper with fade

    show Smile with dissolve
    meeyoung "생각보다 재미있네. 범퍼카."
    player "아...그러신가요?"
    hide Smile
    show Normal
    meeyoung "왜 그래 몸 많이 안 좋아?"
    player "아닙니다..아니에요."
    "계속해서 부딪히기만 해서 그런지 중간부터는 정신이 하나도 없어서 기억 남는 장면이 거의 없지만."
    "누나가 계속 날 공격하는 장면만큼은 선명하게 났다."
    player "누나 진짜 못된듯."
    hide Normal
    show Smile
    meeyoung "응? 내가 무슨 짓 했나?"
    menu:
        "아무것도 아님.":
            "모르는 척도 완전 잘한다. 표정 보면 연기해도 되겠네 진짜..."
    hide Smile
    show Normal
    meeyoung "벌써 4시다."
    "미영누나 말을 듣고 시계를 보니 시간은 4시 18분."
    "여기에 몇 시까지 있을 계획인지는 못 들었지만 그래도 폐장 전에는 나가야 하겠지?"
    "폐장 시간이...몇시였더라...?"
    "분명 폐장시간을 들어오는 입구에서 봤지만 하루 종일 돌아다녀서 그런지 머릿속에는 남아있지 않았다."
    player "누나 여기 폐장 몇시였더라?"
    meeyoung "글쎄 입구에서는 봤던 것 같은데."
    "기억이 잘 안나는건 누나도 마찬가지인 모양이었다."
    "나는 스마트폰을 켜서 OO랜드 폐장시간 이라고 검색했다."
    "배터리가 얼마 없는데 와이파이도 없어서 느린 인터넷 속도에 속터진다..."
    "그렇게 잠시 후 나타난 페이지에는 폐장시간이 19:00분 이라는 글자가 써 있었다."
    "아직은 시간이 꽤 있는 모양이였다."
    player "7시 폐장이라는데?"
    meeyoung "그럼 아직 시간 꽤 있네."
    meeyoung "지금 집에 가기는 좀 그런데 뭔가 더 할 만한게 없으려나..."
    player "흠 그러게."
    hide Normal
    show Angry
    meeyoung "여전히 넌 생각나는게 더 없고?"
    player "여전히라뇨 범퍼가 제가 생각한건데."
    hide Angry
    show Smile
    meeyoung "아~ 맞다 그랬었지?"
    "10월이라 해가 짧아져서 그런지 슬슬 하늘에는 노란빛이 보이기 시작했다."

    scene bg turnRoomN with fade

    "그리고 잠시 보니 아까 내가 쭈그려앉아있던 회전목마에 불빛이 더욱 더 화려하게 들어왔다."

    scene bg bumper with fade

    show Smile with dissolve
    meeyoung "오 예쁘다 회전목마."
    player "오 그러게"
    hide Smile
    show Normal
    meeyoung "가볼래 [name]?"
    player "오키 빨리 가보자."

    scene bg turnRoomN with fade

    "회전목마 앞에 도착하니 대부분 어린애들이 줄을 서고 있었다."
    "종종 어른이 보이긴 했지만, 어른들은 거의 커플들 아니면 애들 부모님으로 보인다."
    player "여긴 그래도 줄이 안 길어서 다행이네."
    show Normal with dissolve
    meeyoung "그러게 계속 줄 긴 것만 탔으니까."
    "나하고 누나는 재빨리 회전목마 줄에서 섰다."
    "어린애들이나 커플들이 있는데 우두커니 서 있는 게 뭔가 부끄러운 것 같기도 하고..."
    "(쌔앵)"
    player "아.... 춥다."
    meeyoung "날씨가 많이 쌀쌀해지긴 했네."
    "그러고 보니 어느 순간부터 굉장히 놀이공원이 쌀쌀해진 것 같은 느낌이 들었다."
    "누나도 손에 들고 있는 가디건을 지금 보니 다시 입고 있었다."
    hide Normal
    show Smile
    meeyoung "일기예보가 웬일로 맞을 때도 있네. 최근 틀리기만 했는데."
    hide Smile
    show Normal
    meeyoung "많이 추워 [name]?"
    player "ㅇ,아니야 괜찮은 듯."
    "날씨가 많이 쌀쌀해졌는지 회전목마를 탈까 하던 아이들과 부모님들도 놀이공원 출구로 이동하는듯 했다."
    "갑자기 확 추워져서 나도 입고 있던 후드집업에 지퍼를 꼭 올렸다."
    hide Normal
    show Smile
    meeyoung "추우면 손잡을까? 누나랑"
    player "아니 추워죽겠는데 선생님은 또 뭔 농담이래?"
    hide Smile
    show Normal
    meeyoung "어라? 농담 아닌데?"
    player "됐습니다요 그리고 진짜 많이 안춥다니까"
    hide Normal
    show Angry
    meeyoung "이그! 눈치 없기는 앞으로 다른 여자애가 이렇게 말해주면 잡아주면 되는거야 손"
    hide Angry
    show Normal
    meeyoung "알겠어?"
    player "알겠습니다~"
    hide Normal
    show Angry
    meeyoung "진짜 둔해가지고는..."
    hide Angry
    show Normal
    meeyoung "그러다 여친은 사귀겠어?"
    player "아니 그래도 나 모솔은 아님 누나 알지 않아?"
    "실제로 나는 모솔이 아니다."
    "지금까지 운 좋게 고백해서 사귄 적이 2번 정도 있으니까 말이다."
    meeyoung "아~ 그거."
    player "그거라뇨?"
    meeyoung "그게 연애야?"
    player "연애지 그럼!"
    hide Normal
    show Smile
    meeyoung "에휴 아서라 아서."
    player "거참 이 누나가 사람을 바보로 알고 있어."
    "회전목마는 누나와 내가 대화하는 동안 금방 멈췄고."
    "범퍼카나 처음에 탔던 롤러코스터와는 다르게 거의 바로 우리 차례가 왔다."
    "회전목마에는 탈게 두 가지가 있었다."
    "서로 마주 보면서 타는 호박 마차와 말이었다."
    "신데렐라가 컨셉인건가? 아무튼."
    "나는 가장 가까운 말에 자리를 잡고 앉았다."
    "미영누나도 바로 내 옆에 있는 말에 앉았다."
    "나하고 미영누나의 뒤에 있던 커플들은 조용히 호박마차에 서로 마주 보고 앉았다."
    "분위기가 엄청 좋아 보이는데?"

    
    meeyoung "왜 계속 뚫어져라 봐?"
    player "어 내가? 뭐를?"
    meeyoung "보고 있잖아 호박마차."
    meeyoung "뭔가 굉장히 슬프게 보는 것 같아서."
    hide Normal
    show Smile
    meeyoung "누나랑 타고 싶었니? 호박마차."
    player "ㅁ,뭔소리래 아니거든?"
    meeyoung "귀엽기는"
    player "아니 진짜 이 누나 아까부터 계속 뭐라는 거야 이상한 소리만 하고."
    hide Smile with dissolve

    scene bg horseing with fade

    "그렇게 잠깐 대화하는 사이 입구 문이 닫혔고."
    "곧이어 호박마차와 말은 움직이기 시작했다."
    "회전목마를 타는 동안 나와 누나는 잠시 아무 말도 하지 않았다."
    "회전목마 특유의 분위기가 있어, 그 분위기를 깨기 싫어서도 있지만."
    "가장 큰 건 내가 피곤해서 그런 것 같다."
    "누나도 내가 피곤한 게 보였는지 딱히 말을 걸지 않았다."
    "그대로 조용히 계속해서 회전하는 불빛과 마차를 바라봤다."

    scene bg turnRoomN with fade 

    show Smile with dissolve
    meeyoung "휴 재미있었다."
    "회전목마가 멈추고 나오자 다시 차가운 바람이 얼굴을 때린다."
    player "으 추워."
    hide Smile
    show Normal
    meeyoung "잠 깼어?"
    player "안 잤거든?"
    meeyoung "하지만 너 반쯤 감고 있었는데? 눈."
    hide Normal
    show Smile
    meeyoung "그런데도 안 졸린다고 할거야?"
    "...."
    player "확실히...졸리긴 한가봄."

    scene bg icecream with fade

    "회전목마의 출구로 나오니 구슬 아이스크림 가게가 보였다."
    "밥을 조금 늦게 먹어 아직 배가 부르긴했지만 그래도 오랜만에 보는 구슬 아이스크림이라 약간 호기심이 생겼다."

    scene bg turnRoomN with fade

    player "오 나 구슬 아이스크림 사 먹을까?"
    show Normal with dissolve
    meeyoung "아까까지만 해도 춥다고 하지 않았어?"
    player "이제 괜찮은 듯?"
    hide Normal
    show Angry
    meeyoung "그러다 감기 걸리면 어쩌려고 그래?"
    meeyoung "너 감기 걸리면 죄송해서 어떻게 보라고 네 어머니."
    meeyoung "엄청나게 걱정하실텐데."
    player "아이 거참 먹을 수도 있는거죠."
    player "걱정마 누나 때문이라고 절대 안 함."
    meeyoung "불안한데..."
    player "거참 우리 엄마가 누나를 혼내겠어? 먹은 나를 혼내지."
    hide Angry
    show Normal
    meeyoung "그게 문제가 아닌데..."
    player "오 여기 스윗멜로우? 맛도 있음."
    hide Normal
    show Angry
    meeyoung "또 말 돌렸어 으...짜증나."

    scene bg blackOut with fade

    "나는 누나 말을 애써 돌리며 구슬아이스크림 가게 앞으로 걸어갔다."
    player "스윗멜로우 맛 하나 주세요!"

    scene bg turnRoomN with fade

    show Normal with dissolve
    
    meeyoung "맛있니?"
    player "어 존맛인듯."
    hide Normal
    show Angry
    meeyoung "맛있냐고. 말 돌리고 먹으니까."
    player "응 완전 개꿀맛."
    meeyoung "아오 진짜."
    player "누나도 드실?"
    hide Angry
    show Normal
    meeyoung "아니 괜찮아 나 찬 거 별로 안 좋아하니까."
    player "맛있는데..."

    scene bg blackOut with fade

    "나는 약간은 고슬거리면서도 단맛이 나는 아이스크림을 계속 넣었다."
    "숟가락이 작아 한 번에 조금밖에 퍼지지 않는 건 조금 불편했지만."
    "아이스크림을 먹을수록 날씨는 점점 추워졌고 거의 다 먹었을 때는 바람도 계속해서 쌩쌩 불었다."

    scene bg turnRoomN with fade

    menu:
        "으...추워.":
            show Angry with dissolve
    meeyoung "으이구 내가 말했지? 추울거 라고."
    player "죄송합니다."
    meeyoung "하여간 못살아요. 진짜."
    hide Angry
    show Smile
    meeyoung "뭐 더 타고 싶은 건 없는 거지?"
    player "응 거의 없는 듯 이제?"
    hide Smile
    show Normal
    meeyoung "거의는 대체 뭐야?"
    meeyoung "혹시 뭐 더 탈 놀이기구라도 더 있는 거야?"
    player "아니 그건 아닌 것 같긴한데 뭔가 예전에 타고 싶었는데 못 탔던 게 있었던 것 같단 말이지..."
    hide Normal
    show Smile
    meeyoung "역시 자주 까먹네 [name]."
    player "엥 무슨 소리임?"
    player "역시라니?"
    hide Smile
    show Normal
    meeyoung "아니야 아무것도."
    meeyoung "빨리 고민해봐 얼마 없어 이제 시간."
    "분명 예전에 엄청 타고 싶어 했었는데, 못 탔던 게 하나 있었다."
    "초등학교때 였나 여기 왔을 때 타고 싶었지만, 폐쇄 되있어서 못 탔던 놀이기구가 하나 있던 것 같은데..."
    "워낙 오래 되서 기억이 잘..."
    "뭐였더라..."
    "그렇게 생각할 때쯤 내 위에 있던 놀이기구들도 하나 둘 불이 들어왔다."
    "아이스크림을 먹으며 누나와 수다를 떨다 보니 시간은 어느새 5시가 넘었다."
    "이대로 기억 못하고 집으로 돌아가서 기억나면 엄청 아쉬울 것 같은데..."
    hide Normal
    show Smile
    meeyoung "생각나는 거 없으면 이제 갈까?"
    player "응 그래야 할 듯."

    scene bg blackOut with fade

    "그렇게 말하고는 아쉬운 느낌을 애써 달래며 일어나려고 할 때"
    "회전목마 위 언덕에 있는 모든 놀이기구 불들이 켜졌고 그 맨 위에 커다란 관람차가 한 눈에 들어왔다."
    player "관람차인가?"

    scene bg turnRoomN with fade

    show Normal with dissolve
    meeyoung "응? 뭐라고 [name]?"
    player "나 관람차 타고 싶었던 것 같은데."
    hide Normal
    show Angry
    meeyoung "타고 싶은 거 같은데는 또 뭐야."
    player "아 엉 나 관람차 타고 싶음."
    hide Angry
    show Smile
    meeyoung "관람차 괜찮은데?"
    meeyoung "지금 딱 해도 지고 예쁠 것 같은데?"
    meeyoung "그럼 마지막으로 저거 타고 가자 관람차."
    player "응 빨리 가자."
    hide Smile
    show Normal
    meeyoung "그나저나 피곤하지 않아?"
    player "그래도 아이스크림 먹어서 이제 피곤하진 않은 듯."
    hide Normal
    show Smile
    meeyoung "그래, 빨리 가자."

    scene bg inturn with fade
    play music "audio/Mee/Mee Rules.mp3"
    
    "나와 누나는 서둘러서 관람차에 도착했다."
    "사람이 없을거라 생각했지만 지금 해도 딱 이쁘게 떠 있어서 관람차를 타고 싶었던 사람이 많았다."
    "물론 거의 다 커플들밖에 없는 듯 보이지만."

    show Normal with dissolve

    meeyoung "그런데 관람차는 왜 타고 싶은 거야?"
    player "아니 그냥 초등학교 때 못 타본 것 같아서?"
    meeyoung "그때 못 탔던 것에 대한 아쉬움인가 보네."
    player "그런 듯?"
    hide Normal
    show Smile
    meeyoung "나름 유치한 구석이 있었네"
    player "유치해서 죄송합니다~"
    hide Smile
    show Normal
    meeyoung "유치한 거 알면 앞으로 신경 써서 행동해~"
    "회전목마 범퍼카 포함해서 줄이 가장 느리게 사라지는 것 같았다."
    "한 번에 타는 사람은 꽤 많았지만 그만큼 천천히 한 바퀴를 돌았기 때문에 다음 차례가 오는 데 시간이 꽤나 걸리는듯 했다."
    meeyoung "그래도 오늘 재미있었지?"
    "미영 누나는 내 앞에서 앞줄을 멍하니 바라보다가 갑자기 뒤를 돌아보고는 물었다."
    player "어 음..."
    meeyoung "응? 재미없었어?"
    player "아니 그냥 뭐 재미있었다면 재미있고 그런 느낌?"
    hide Normal
    show Angry
    meeyoung "뭔 말이 그러니?"
    player "나름 노력한 겁니다."
    meeyoung "나는 그래도 나름대로 무서운 거 안 타고 맞춰준 것 같은데"
    player "아이고 감사합니다."
    hide Angry
    show Smile
    meeyoung "그래 더 감사해"
    player "그런 거치고는 후배한테 삥뜯어서 얻은 표 아니었는지?"
    hide Smile
    show Angry
    meeyoung "혼난다?"
    player "농담이었는데."
    meeyoung "재미없어 그런 농담."
    player "나름 자신 있는 농담이었는데 아쉽네요."
    hide Angry
    show Normal
    meeyoung "그게 웃겨?"
    player "재미없었나."
    hide Normal
    show Angry
    meeyoung "재미없어 하나도."
    player "넵 죄송합니다."
    meeyoung "나 참 데려와 준 보람 없게..."
    player "아니 그래도 나름 재미있었음."
    hide Angry
    show Normal
    meeyoung "인제 와서?"
    player "아니 진짜로 재미있게 논 듯?"
    meeyoung "그래 너 재미있으라고 데려온 건데 네가 재미 없으면 안되지."
    player "누나는 재미 없었음?"
    hide Normal
    show Smile
    meeyoung "아니? 나름 재미있었는데?"
    meeyoung "귀여운 [name]하고 와서?"
    player "ㅁ,뭉ㅇㄴㄻㄻㅎ뭐요?"
    "와 진짜 이 누나 말 너무 무섭게 하네."
    "개인적인 생각이지만 방금 나 아니었으면 분명 대부분 남자는 넘어갔을거다."
    player "농담 좀 그만해."
    meeyoung "왜 그래 너도 좋지 않았어? 예쁘고 밥 사주는 누나랑 와서."
    player "또또 맨날 은근슬쩍 본인 예쁘다고."
    player "오늘이 몇 번째임?"
    hide Smile
    show Normal
    meeyoung "왜 그래 언제쯤 인정할래?"
    player "인정할 생각 없습니다."
    hide Normal
    show Smile
    meeyoung "아이고 아쉬워라~"
    "어느 순간 앞을 보니 관람차가 덜컹하는 소리가 들렸다."
    "나하고 누나 앞까지 온 듯했다."

    hide Smile with dissolve

    seemanThree "혹시 일행분이세요?"
    meeyoung "네."
    seemanThree "넵 관람차 안에서는 되도록 앉아 주시고요 차례 돌아오시면 내려주시면 됩니다."
    meeyoung "알겠습니다."
    seemanThree "네 그럼 타 주실게요."

    scene bg blackOut with fade
    

    "그렇게 다음 칸이 내려오기 전에 나하고 누나는 재빨리 관람차 안으로 들어갔다."
    "겉만 보고 굉장히 따뜻할거라 생각했던 예상과 다르게 의자도 그렇고 벽도 그렇고 쇠로 돼 있어서 굉장히 차가웠다."
    player "하아...여기가 더 추운 것 같은데?"
    show Normal with dissolve
    meeyoung "많이 추워 내려가달라고 할까?"
    player "안 되는 거 뻔히 알면서 이 누나는."
    hide Normal
    show Smile
    meeyoung "그래도 위로가 될까 싶어서 말해준 건데."
    player "됐습니다요. 그리고 춥긴 한데 견딜만함."
    hide Smile
    show Normal
    meeyoung "하하 그래도 많이 큰 것 같네, 힘들다고 찡찡대지 않고."
    player "제가 언제 그랬다고 말을 그러십니까?"
    meeyoung "내가 말했잖아~ 너 기억 많이 까먹는다고."
    "그렇게 대화 한 번이 끝나고는 더 이상 대화가 맺어지지 않았다."
    "관람차는 천천히 올라갔고 노을이 딱 져서 꽤나 예쁘다."

    hide Normal
    scene bg blackOut with fade

    stop music

    meeyoung "시간 참 빠르네."
    player "응?"
    meeyoung "너 초등학생 때 막 나한테 애교부리던 때가 엊그제 같은데."
    player "내가 애교를 부렸다고?"
    meeyoung "응 부렸어."
    player "아이고 참 말은 똑바로 하시죠?"
    player "내가 어릴 때 뭔 애교를 부렸다고."
    meeyoung "진짜인데?"
    player "내가 속을걸 속아야지."
    meeyoung "그래 나중에 어머님께 여쭤봐."



    "..."
    "진짜인가?"
    "그러면 상당히 쪽팔릴 것 같은데."
    "혹시나 지금 엄마한테 물어볼까 해서 스마트폰을 꺼내봤지만."
    "스마트폰은 어느새 꺼져있었다."
    player "어 폰 꺼졌네."
    meeyoung "여기까지 와서 또 폰이야?"
    player "아니 그냥 확인해보려고."
    meeyoung "아..."
    meeyoung "걱정하지 마 어머님께는 말씀드리고 왔으니까."
    meeyoung "아마 너한테 전화 왔다면 나한테도 전화 주실 거야."
    player "그런가?"
    "그렇게 말하고는 다시 아무 말도 하지 않는다."
    meeyoung "그럼 그 경기게임마이스터고등학교? 입학하면 기숙사 입학하는 건가?"
    player "그런 듯? 애초에 알아보니까 마이스터고등학교는 다 기숙사 생활하는 것 같더라고?"
    meeyoung "그래? 그럼 우리 [name] 자주 못 봐서 어떻게 해?"
    player "뭘 그리 슬퍼하십니까, 주말마다 볼 수는 있지 않나?"
    meeyoung "고등학생인데 주말마다 바쁘지 않을까?"
    player "그런가?"
    meeyoung "그래도 이제 다 컸네 기숙사 생활도 하고."
    player "거참 언제까지 애 취급 할겁니까? 미영 씨."
    meeyoung "넌 아직 내 눈에는 애야."
    player "아 구러쉐요?"
    meeyoung "말투가 왜 그래?"
    player "아무것도 아닙니다."
    meeyoung "아닌 게 아닌 것 같은데..."

    scene eventCG MeeTurn with fade
    play music "audio/Mee/MEE TRUE.mp3"

    "대화가 이어지는 동안 관람차는 계속해서 올라갔고 지고 있는 햇빛도 점점 붉게 변해갔다."
    "하늘은 이제 하늘색이 아니라 남색에 더 가까운 색이었고 별도 조금씩 보이는듯 하다."
    meeyoung "그렇구나 벌써 고등학생..."
    player "? 왜 그럼 누나 분위기 잡고?"
    meeyoung "그냥 뭔가 새롭다고 해야 하나?"
    meeyoung "그렇게 애 같던 [name] 너가 이제 고등학생이라니."
    player "그런 거 갖고 뭔 분위기를 잡고 그러십니까?"
    meeyoung "있지 [name]?"
    player "응?"
    meeyoung "너는 고등학교 들어가서 연애 같은 거 할 것 같아?"
    "누나는 갑자기 진지하게 분위기를 잡고 그런 말을 꺼낸다."
    player "그게 무슨 소리야 누나 연애 같은걸 할 것 같냐고?"
    "연애라."
    "딱히 생각해본 적은 없는 것 같다."
    "겜마고(경기게임마이스터고등학교) 같은 경우에는 남학생 비율이 더 많기도 하고."
    "만약 떨어져서 일반 고등학교에 가도 고등학생이니까... 연애할 확률은 적지 않을까 라고 생각하고 있는데."
    "정작 생각해보면 가능성이 아예 없 는건 아닌 것 같고..."
    player "잘 모르겠는데...?"
    meeyoung "그래...뭐 너답네 [name]."
    player "저 답다는 게 뭐죠?"
    meeyoung "그냥 평소에는 맹하면서 이상한 상황에 눈치는 엄청 빠른?"
    player "칭찬임?"
    meeyoung "칭찬이지 당연히~"
    player "그런 거치고는 기분 나쁜데요?"
    meeyoung "어머 딱히 노린 건 아닌데."
    player "거 참 이 양반이 진짜."
    "..."
    player "그래도 연애는 못 하지 않을까?"
    meeyoung "응? 왜 그렇게 생각하는데?"
    player "그야 지원한 고등학교 되면 남학생이 더 많으니까 힘들고, 일반고에 가면 공부하느라 바쁠 거 아니야?"
    meeyoung "흠 그래?"
    player "왜 그런 눈으로 봐?"
    meeyoung "그냥 뻥 잘 친다는 생각이 드네."
    player "그걸 어떻게 압니까?"
    meeyoung "뻥쟁이 [name]."
    player "아니 내일 일도 모르면서 고등학교 때 제가 연애할지 안 할지를 어떻게 압니까."
    meeyoung "척 보면 척이지."
    player "사실 미영 씨 예언이라도 할 줄 아는 건 아닌지요?"
    meeyoung "하하 그럴지도."
    "그리고 다시 한번 침묵이 시작되었다."
    "관람차는 계속 올라가 곧 있으면 가장 높은 지점에 도착할 시기였다."
    meeyoung "있지 [name]?"
    player "어? 왜 그럼?"
    meeyoung "있지 만약에..."
    "잠시 뜸을 들이는 누나."
    "자신이 하고 싶은 말을 정리하는 듯했다."
    meeyoung "생각해보니까 아직 범퍼카 벌칙 생각 안 했네?"
    player "오 이런."
    meeyoung "안 잊고 있다?"
    player "하아...대체 뭘 원하시는 것임?"
    meeyoung "흠...돈?"
    player "없습니다."
    meeyoung "농담이야~"
    meeyoung "일단 하나 만 물어볼게"
    player "응?"
    meeyoung "만약에 네가 연애하게 된다면 어떨 것 같아?"
    player "좋지 않을까?"
    meeyoung "그래? 그렇구나?"
    meeyoung "그게 끝?"
    player "응? 뭐 더 있음?"
    meeyoung "사랑해줘야겠다 라거나 그런 거 있을 거 아니야? 그 사귀는 애를."
    player "흠..."
    "내 대답이 오기도 전에."
    "누나는 답답하다는 듯 다음 말을 이었다."
    meeyoung "이걸로 할게 내 소원은."
    player "응? 뭔데?"
    scene eventCG MeeTrue2 at EventEffect with fade
    meeyoung "앞으로 진짜 네가 누군가와 사귀게 된다면."
    meeyoung "아니면 누군가 너를 좋아하게 된다면."
    meeyoung "넌 그 아이를 버리지 않고 행복하게 해줄래?"
    scene eventCG MeeTurn with fade
    "누나는 그러고는 더 이상 할 말이 없다는 듯 한숨을 쉬었다."
    "왜 갑자기 소원을 그런 말을 하는 거지?"
    "난 뭐 가게일 도와주거나 그런 건 줄 알았는데..."
    "하지만 어째서일까..."
    "나는 미영 누나의 말에 당당히 대답할 자신이 없었다."
    "나는 대답을 잊지 못하고 그대로 바닥을 바라봤다."
    "그런 나를 미영 누나는 웃으면서 바라보고 있을 뿐이었다."
    "어느새 관람차는 꼭대기를 넘어 내려가기 시작했고."
    "해는 딱 저물어 하늘은 보랏빛으로 물들어 별들 몇 개가 점처럼 보이고 있었다."
    player "예쁘네."
    "나는 웃는 미영누나와 하늘을 보며 그렇게 말했다."
    meeyoung "그러게"
    meeyoung "재미있었지, 오늘?"
    "재차 확인하는 듯한 누나."
    player "네 만족스럽습니다."
    meeyoung "그래? 다행이네."
    meeyoung "내가 한 말 잘 생각해 [name]."
    "미영누나는 결국 평소와 비슷하게."
    "알 수 없는 말들을 마구 하면서."
    "놀이공원에서의 하루를 마무리 했다."
    "그 말은 이상하리 만치 머릿속에 깊게 박혔음에도."
    "크게 와닿지 않았다."
    meeyoung "내가 한 말 잘 생각해 [name]."

    play music "audio/TastyLove2.mp3"


    jump ending


    return

label ending:

    $ narrator = nvl_narrator

    narrator "그 말을 마지막으로 관람차가 내려올때까지 누나는 아무말도 하지 않았다."
    narrator "하루종일 피곤했기 때문에 나도 더 이상 입술을 뗄 힘이 없어서 침묵을 지켰다."
    narrator ""
    narrator ""
    narrator "점점 해는 저물고 보랏빛 하늘은"
    narrator "어느새 검은색으로 변해서 별빛만이 하늘을 꾸며주고 있었다."
    narrator "그대로 나는 걷는건지 흐느적 거리는 건지 모르겠다는 느낌으로 움직여"
    narrator "겨우 에버랜드 입구에 도착했다."
    narrator ""
    narrator ""
    narrator "그날은 그렇게 딱히 큰일 없이 집으로 돌아갔다."
    narrator "관람차에서 나오는 동안 미영 누나의 표정을 보지 못했다."
    narrator "하지만 뭔가 평소에 맹한 표정과는 다른 표정을 짓고 있었던 게 분명했다."
    narrator ""
    narrator ""
    narrator "놀이공원에서 집에 오는 동안은 피곤해서 잠을 자느라 거의 기억이 나지 않는다."
    narrator "하지만 차에 타고 눈을 한 번 감았다 뜨니 누벨바그에 도착해있었다."
    narrator ""
    narrator ""
    narrator "내가 한 말 잘 생각해 [name]."
    narrator "미영 누나는 나에게 관람차에서 마지막에 했던 말을 다시 한번 되뇌일 뿐이었다."
    narrator "분명 중요한 말인 것 같지만, 머릿속에 잘 남지 않았다."
    narrator ""
    narrator ""
    narrator "그날은 결국 피곤한 일만 잔뜩 겪으며 지나갔다."
    narrator "고등학교가 되면 바빠서 이런 일 다시 겪기는 힘들겠지...?"
    narrator ""
    narrator ""
    narrator "고등학교 생활이 걱정되지만, 일단은 오늘 즐겼던 시간을 되새겨 봐야겠다고 생각했다."

    call crdit from _call_crdit

    return

init:
    transform txt_up:
        yalign -5.0
        linear 15.0 yalign 10.0
label crdit:
    scene bg blackOut with dissolve
    $gui.main_menu_background = "gui/SecondMain.png"
    show text "팀장  김철진\n\n\n\n시나리오  김철진\n\n\n\n개발  김철진\n\n\n\n스탠딩 CG   쵸양 \n\n\n\n 이벤트CG   쵸양,무토 \n\n\n\n 음향   유타랩터\n\n\n\n 도움을 주신 분들\n\n시바쌤  정정배\n\n\n\n" at txt_up
    pause 12

    $ persistent.End = True;
    $ persistent.setMusic = "audio/Mee/MEE TRUE.mp3"

    return