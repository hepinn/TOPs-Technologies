import { Suspense, lazy, useState } from 'react'
import './App.css'
import styled from 'styled-components'
const Home = lazy(()=>import('./Home'))
const Contact = lazy(()=>import('./Contact'))


function App() {
  const [name, setName] = useState("")
  const [id, setId] = useState("")
  const [data,setData] = useState([])
  const saveData = ()=>{
    setData([...data,name])
    console.log(data);
    setName('')
  }
  const H1 = styled.h1 `
  font-size: 1.5em;
  text-align: center;
  color: #BF4F74;
  `

  const deleteData = (id)=>{
    let a = window.confirm("Are you sure you want to delete?")
    
    if(a){
      let data1 = data.filter((i,index)=>{
                    return index!=id
                  }) 
      setData(data1)
      alert("Data successfully deleted..")
    }
    
  }
  const editData = (id)=>{
    setId(id)
    let data1 = data.filter((i,index)=>{
        return index == id
    })
    setName(data1[0])   
  }
  const updateData = ()=>{
    let data1 = data.map((i,index)=>{
        if(index==id){
            i = name
        }
        return i;
    })
    setData(data1)
    setName('')
    setId('')
  }
  return (
    <>
      <div>
        <H1>CRUD Example</H1>
        <input type="text" name="name" id="name" value={name} onChange={(e)=>setName(e.target.value)}/>
        <input type="button" value={id ? "Update Data" : "Save Data"}  onClick={id ? updateData :saveData}/>
        <br /><br />

        <table border={'1'}>
          <tr>
            <td>Id</td>
            <td>Name</td>
            <td>Action</td>
          </tr>
          {
            data.map((i,index)=>{
              return (
                <tr>
                  <td>{index+1}</td>
                  <td>{i}</td>
                  <td>
                    <button onClick={()=>editData(index)}>Edit</button> 
                    <button onClick={()=>deleteData(index)}>Delete</button>
                  </td>
                </tr>
              )
            })
          }
        </table>
      </div>
      
      
    </>
  )
}

export default App