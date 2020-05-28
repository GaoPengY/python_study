/*
 * @Descripttion:
 * @version: 1.0.0
 * @Author: gaopeng
 */

function run(){
    // 倒计时
    var EndTime = new Date();
    //var NowTime = new Date();
    var min = EndTime.getMinutes();
    EndTime.setMinutes(min + 1);
    EndTime.setSeconds(0);
    var NowTime = new Date();
    NowTime.setSeconds(0);
    var k = 0;
    var tid = setInterval(getTime,1000);    // 倒计时的id
    // 倒计时
    function getTime() {
        if(k<61)
        {
            k++;
        }else {
            // 时间到了，结束moveto 和 getTime
            clearInterval(tid);
            clearInterval(mid);
            // 顺利过关显示信息
            passinfo();

        }
        NowTime.setSeconds(k);
        // 两者之差
        var time = EndTime.getTime() - NowTime.getTime();
        // 计算秒
        var s=Math.floor(time/1000%60);
        //通过getElementById来找到对应元素进行操作
        document.getElementById("time").innerHTML = s + "秒";
    }
    // 生成并移动障碍物
    var score = 0;
    var flag = 0;
    var timecount = 0;
    function moveto() {
        // 绘制canvas图形
        var elem = document.getElementById("cloakbody");
        var c=document.getElementById("cloakcan");
        var ctx=c.getContext("2d");
        var man = document.getElementById("man");
        ctx.fillRect(0,0,10,50);
        // 移动canvas图形
        var pos = 0;
        //移动动画
        var id = setInterval(frame,1);
        function frame() {
            if (pos == 500){
                clearInterval(id);
            }else {
                // 向左移动
                pos++;
                elem.style.right = pos + "px";
                // 碰撞检测
                if(isBump(elem,man))
                {
                    //撞到了
                    timecount++;    //次数+1
                    flag = -2;      // 扣分
                    actionBump();   // 人物被撞动画
                    if (timecount<3)
                        // 仍有血量
                        healthDel();
                    else{
                        // 血量耗尽
                        healthDel();        // 减去血量
                        clearInterval(mid); // 停止障碍物移动
                        gameoverinfo(); //输出游戏结束动画
                        clearInterval(tid); //暂停倒计时
                    }
                    clearInterval(id);
                }else {
                    flag = 1;   // 加分
                }

            }
        }
        // 进行分数统计
        addscore(score+=flag);

    }
    //
    var mid = setInterval(moveto,2000);




}

// 人物跳动
function move() {
    var elem = document.getElementById("man");
    var pos = 0;
    var idup = setInterval(frameup,5);
    // 向上移动
    function frameup() {
        if (pos == 90){
            clearInterval(idup);
            var id =setInterval(framedown,5);
        }else {
            pos++;
            elem.style.bottom = pos + "px";
        }
    }
    // 向下移动
    function framedown() {
        if (pos == 0){
            clearInterval(id);
        }else {
            pos--;
            elem.style.bottom = pos + "px";
        }
    }
}

//score控制
function addscore(score) {

    var elem = document.getElementById("score");
    elem.innerHTML = score;

}

// 碰撞检测
function isBump(obj1,obj2){
    var L1 = obj1.offsetLeft;
    var R1 = obj1.offsetLeft + obj1.offsetWidth;
    var T1 = obj1.offsetTop;
    var B1 = obj1.offsetTop + obj1.offsetHeight;
    var L2 = obj2.offsetLeft+obj2.parentNode.offsetLeft;
    var R2 = obj2.offsetLeft + obj2.offsetWidth + obj2.parentNode.offsetLeft;
    var T2 = obj2.offsetTop + obj2.parentNode.offsetTop;;
    var B2 = obj2.offsetTop + obj2.offsetHeight + obj2.parentNode.offsetTop;
    if( R1<L2 || L1>R2 || T1>B2 || B1<T2 ){
        return false;
    }
    else{
        return true;
    }
}
// 撞击障碍物后人物动画
function actionBump() {
    var elem = document.getElementById("man");
    var pos = 0;
    var idright = setInterval(frameright,5);
    // 向右移动
    function frameright() {
        if (pos == 10){
            clearInterval(idright);
            var id =setInterval(frameleft,5);
        }else {
            pos++;
            elem.style.left = pos + "px";
        }
    }
    // 向左移动
    function frameleft() {
        if (pos == 0){
            clearInterval(id);
        }else {
            pos--;
            elem.style.right = pos + "px";
        }
    }
}

// 生命值检测
function healthDel() {
    var elem = document.getElementById("health");
    elem.removeChild(elem.firstChild);
    elem.removeChild(elem.firstChild);
}

function gameoverinfo() {
    var elem = document.getElementById("info");
    elem.innerHTML= "挑战失败!";
}

function passinfo() {
    var elem = document.getElementById("info");
    elem.innerHTML="恭喜过关！";

}
