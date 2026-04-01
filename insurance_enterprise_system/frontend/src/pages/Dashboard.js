import React from 'react';
import Claim from './Claim';
import Accident from './Accident';

export default function Dashboard(){
  return (
    <div>
      <h1>보험 대시보드</h1>
      <Claim/>
      <Accident/>
    </div>
  )
}