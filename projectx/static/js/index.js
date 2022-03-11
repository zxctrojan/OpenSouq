
var login=document.getElementById('login');
if(login!=null)
login.addEventListener('click',()=>{
    let a=document.createElement('a');
    a.href='signin';
    a.click();
}) 
var register=document.getElementById('register');
if(register!=null)
register.addEventListener('click',()=>{
    let a=document.createElement('a');
    a.href='signup';
    a.click();  
})

var logout=document.getElementById('logout');
if(logout!=null)
logout.addEventListener('click',()=>{
    console.log('logout')
    let a=document.createElement('a');
    a.href='signout';
    a.click()
})

var seller=document.getElementById('seller');
seller.addEventListener('click',()=>{
    let a=document.createElement('a');
    a.href='seller';
    a.click()
})

