document.addEventListener("DOMContentLoaded",
    function() {

        const contactBox = document.querySelector(".contact-link");

        const image = document.querySelector(".profile-photo");

        const cancel = document.querySelector(".back-to-home");

        contactBox.addEventListener("click",
            function () {

                image.style.display = "none";

            }
        )

        cancel.addEventListener("click",
            function () {
                image.style.display = "block";
            }
        )

    }
)