import React, { useEffect, useState } from 'react'

const LifecycleFunc = () => {
    const [name,setName] = useState("FuncName")
    useEffect(()=>{
        console.log('useeffect calling...');
        setTimeout(()=>{
            setName("Testing use effect")
        },3000)
    },[name])
  return (
    <div>
      <h4>Name is -- {name}</h4>
      <button onClick={()=>setName("Patel")}>Change name</button>
    </div>
  )
}

export default LifecycleFunc