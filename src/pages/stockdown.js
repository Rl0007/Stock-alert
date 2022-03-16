import React, { useEffect, useState } from 'react'
import { Addstockdownform } from '../components/stockdown/addstockdownform'
import { Addstockdowntable } from '../components/stockdown/addstockdowntable'

export const Stockdown = () => {
    const[stock,setstock]=useState([''])
    const fetchfunction=()=>{
        fetch(`/showstockdown`).then(response =>{
            if(response.ok)
            return response.json()
        }).then(data => setstock(data))
    }
    useEffect(()=>fetchfunction(),[])
  return (
  <div className="container">
      <h1><u>Add stock for down</u></h1>
      <Addstockdownform refresh = {fetchfunction}/>
      <Addstockdowntable stockdowndata={stock} setstockdowndata={setstock} refresh={fetchfunction}/>
  </div>
  )
}
