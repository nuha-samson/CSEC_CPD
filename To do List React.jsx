import React from 'react';
import { useState } from 'react'
import 'styles.css'
function App() {
const [value,setValue] = useState("")
const [list, setList] = useState([])
function takeValue(e){
  setValue(e.target.value)
}
function addTask(){
  setList([...list,value])
  setValue("")
}
function delet(index){
  const newList = list.filter((_, i)=> i !== index)
  setList(newList)
}
function edit(index){
  const newTask = prompt("Edit task:", list[index])
  const updatedList = [...list]
  updatedList[index] = newTask
  setList(updatedList)
}
  return (  
     <>
     <div className="todo">
     <div className="container">
     <div className="input">
     <input type="text" placeholder="text.." value={value} onChange={takeValue} />
     <button onClick = {() =>addTask()}> add </button>
     </div>
     <ul>
{
  list.map((task,index) => {
    return (
      <li key={index}>
        {task}
        <button onClick={() => delet(index)}>del</button>
        <button onClick={() => edit(index)}>edit</button>
      </li>
    )
  })
}
</ul>
     </div>
     </div>
     </>
  )
}
export default App
