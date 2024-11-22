function ChangeColor() {
    const box = document.getElementById("first-block");
    first_block =document.querySelector('#first-block');
    
    if($("#first-block").css("background-color")=='rgb(0, 0, 0)')
        $("#first-block").css("background-color", "red");
    else
        $("#first-block").css("background-color", "black");

}

function ChangeNumber() {

    let i;
    let j;
    let tmp;
    let color = ["purple","green","grey","orange","red"]
    let lotto = [];
    let num =[];
    let check = 0;
    tmp = parseInt(Math.random()*45+1);
    num.push(tmp);
    for(i=1;i<7;i++)
    {   
        while(true){
            check = 1;
            tmp = parseInt(Math.random()*45+1);
            for(j=0;j<num.length;j++)
            {
                if(tmp==num[j])
                    check = 0;
            }

            if(check == 1)
                break;
        }
        


        num.push(tmp);   
    }    
    
    num.sort((a, b) => a - b)
    
    lotto[0] = document.getElementById('lotto1');
    lotto[1] = document.getElementById('lotto2');
    lotto[2] = document.getElementById('lotto3');
    lotto[3] = document.getElementById('lotto4');
    lotto[4] = document.getElementById('lotto5');
    lotto[5] = document.getElementById('lotto6');
  

    for(i=0;i<6;i++)
    {
        lotto[i].innerText = num[i];
        lotto[i].style.backgroundColor = color[parseInt(num[i]/10)];    
    }
        


}

function practice_image(){

   image = document.getElementById('practice-image');

   image.src = "https://dummyimage.com/400x400/f00/fff"


}

function practice_ptag(){

    image = document.getElementById('practice-ptag');
 
    image.innerText = "변경됨"
 
 
 }

 function practice_div(){

    image = document.getElementById('practice-div');
 
    image.style.backgroundColor = 'gray'
 
 }