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
            
    lotto[0] = document.getElementById('lotto1');
    lotto[1] = document.getElementById('lotto2');
    lotto[2] = document.getElementById('lotto3');
    lotto[3] = document.getElementById('lotto4');
    lotto[4] = document.getElementById('lotto5');
    lotto[5] = document.getElementById('lotto6');
    lotto[6] = document.getElementById('lotto7');
  
    for(i=0;i<7;i++)
    {
        lotto[i].innerText = num[i]; 
        lotto[i].style.backgroundColor = color[parseInt(num[i]/10)];
    }
        


}