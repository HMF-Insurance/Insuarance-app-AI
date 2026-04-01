import React,{useState} from 'react';
import axios from 'axios';

export default function Login(){
  const [email,setEmail]=useState('');
  const [password,setPassword]=useState('');

  const login=async()=>{
    const res=await axios.post('http://localhost:5000/auth/login',{email,password});
    localStorage.setItem('token',res.data.token);
    window.location.reload();
  }

  return (
    <div>
      <h2>Login</h2>
      <input onChange={e=>setEmail(e.target.value)} placeholder="email"/>
      <input type="password" onChange={e=>setPassword(e.target.value)} placeholder="password"/>
      <button onClick={login}>Login</button>
    </div>
  )
}