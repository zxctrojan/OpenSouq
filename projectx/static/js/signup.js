let submit=document.getElementById('btn-submit')
submit.addEventListener('click',()=>
{
    let password=document.getElementById('password').value;
    let confirmpassword=document.getElementById('confirmpassword').value;
    
    if(password!=confirmpassword)
    alert('Passwords Mismatch')

    
    else if(password.length<8)
    alert('Password should be 8 character min')
    
    else{
        console.log('submit');
    let form=document.getElementById('form');
    form.submit();
    console.log('submit123');

    }
})