const task = document.querySelector('input') as HTMLInputElement;
const add = document.querySelector('button') as HTMLButtonElement;
add.addEventListener('click',function addTask(){
   if (task.value != ""){
     const container = document.querySelector('.tasks ul') as HTMLUListElement;
     const li = document.createElement('li');
     const removebtn = document.createElement('button');
        li.textContent = task.value;
     removebtn.textContent = "remove"
      container.prepend(li);
     li.append(removebtn)
        task.value = "";
     removebtn.addEventListener("click", function removeTask(){
       li.remove();
       
     })
 
   }
})
