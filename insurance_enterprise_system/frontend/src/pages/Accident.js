import React,{useState} from 'react';
import axios from 'axios';

export default function Accident(){
  const [desc,setDesc]=useState('');

  const submit=async()=>{
    await axios.post('http://localhost:5000/accident',{desc});
    alert('사고 접수 완료');
  }

  return (
    <div>
      <h3>사고 접수</h3>
      <input onChange={e=>setDesc(e.target.value)} placeholder="사고 내용"/>
      <button onClick={submit}>접수</button>
    </div>
  )
}