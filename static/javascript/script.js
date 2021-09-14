function validateForm(){
    let passwordVal = document.getElementById("password").value;
    let flag = 1;
    if(passwordVal.length < 8){
        password_match_error.style.visibility = "visible";
        password_match_error.innerText = "Password must contain atleast 8 digit..";
        flag = 0;
    }else if(passwordVal != re_password.value){
        password_match_error.style.visibility = "visible";
        password_match_error.innerText = "Password didn't matched... Please try again...";
        flag = 0;
    }else{
        password_match_error.style.visibility = "hidden";
        password_match_error.innerText = "SignUp sucessfull... Login now..."
        flag = 1;
    }   

    if(flag){
        return true;
    }else{
        return false;
    }
};

function validateText(){
   if(addTxt.value === ""){
    blankError.style.visibility = "visible";
   }else{
    blankError.style.visibility = "hidden";
   }
};

if(notes.innerText === ""){
    notes.innerText = "Nothing to show here... Add a note first...";
}