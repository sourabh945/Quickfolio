document.addEventListener('DOMContentLoaded',
    function () {
        const name = (document.getElementById('name')).value ; 

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
                    secondLine('cursor-s','space-s','arrow-s');
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

        let text = "Hello ! I am "+name;

        document.getElementById('arrow').innerHTML = "> "

        blink('cursor','space');

    }

)