import React,{useState} from 'react';
import axios from 'axios';

export default function Claim(){
  const [amount,setAmount]=useState('');

  const submit=async()=>{
    await axios.post('http://localhost:5000/claim',{amount});
    alert('청구 완료');
  }

  return (
    <div>
      <h3>보험금 청구</h3>
      <input onChange={e=>setAmount(e.target.value)} placeholder="금액"/>
      <button onClick={submit}>청구</button>
    </div>
  )
}