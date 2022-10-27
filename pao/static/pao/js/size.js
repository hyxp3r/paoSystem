window.onload = resize;


window.addEventListener('resize', resize)

  function resize () {

    const one = document.getElementById("one").offsetHeight
    const two = document.getElementById("two").offsetHeight
    const three = document.getElementById("three").offsetHeight
    const four = document.getElementById("four").offsetHeight
    
    let max = Math.max(one, two, three, four)

    document.getElementById("one").style.height = max + "px" ;
    document.getElementById("two").style.height = max + "px";
    document.getElementById("three").style.height = max + "px";
    document.getElementById("four").style.height = max + "px";
    

  }