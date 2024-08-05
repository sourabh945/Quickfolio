document.addEventListener('DOMContentLoaded',
    function () {

        const nameElement = (document.getElementById('name')) || null ; 



        let blinked = false;
        let countBlinked = 0 ; 
        const initialBlinks = 10 ; 
        let index = 0 ; 
        let second = true;

        function secondLine(idCursor,idSpace,idArrow){
            reset();
            document.getElementById(idArrow).innerHTML = "> ";
            text = "Welcome to my Portfolio";
            blink(idCursor,idSpace);
        }

        function reset() {
            blinked = false;
            countBlinked = 0;
            index = 0;
        }
        
        function typing(idSpace,idCursor) {
            if (index <= text.length) {
                document.getElementById(idSpace).innerHTML += text.charAt(index);
                index++;
                setTimeout(blink,50,idCursor,idSpace)
            }
            else {
                document.getElementById(idCursor).innerHTML = "";
                if (second) {
                    second = false;
                    if (nameElement){
                        secondLine('cursor-s','space-s','arrow-s');
                    }
                }
            }
            
        }
        
        function blink(idCursor,idSpace) {
            if (blinked) {
                document.getElementById(idCursor).innerHTML = " ";
                blinked = false;
            }
            else {
                document.getElementById(idCursor).innerHTML = "|";
                blinked = true;
            }
            if (countBlinked > initialBlinks) {
                setTimeout(typing,40,idSpace,idCursor);
                countBlinked++;
            }
            else {
                setTimeout(blink,100,idCursor,idSpace);
                countBlinked++;
            }
        
        }

        let text;

        if (nameElement) {
            const name = nameElement.value;
            text = "Hello ! I am "+name;
        }
        else{
            text = (document.getElementById('text')).value;
        }

        setTimeout(function () {
            document.getElementById('arrow').innerHTML = "> ";
        },2);

        blink('cursor','space');

    }

)