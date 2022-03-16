const wrapper = document.querySelector('.wrapper'),
      form    = document.querySelectorAll('.form'),
      submitInput = form[0].querySelector('input[type="submit"]')

function getDataForm(e){
    e.preventDefault();

   var formData = new FormData(form[0]);
   alert(formData.get('textField') + ' - ' + formData.get('radioField') + ' - ' + formData.get('selectField'))

   //document.getElementById('evento').innerHTML= `<iframe src="entrada.html" width="500" //height="500">${formData.get('textField')}</iframe>`;
}

   document.addEventListener('DOMContentLoaded',function(){
       submitInput.addEventListener('click',getDataForm,false); 
   },false);
