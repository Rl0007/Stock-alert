import React, { useEffect, useState } from 'react'
import { Addstockupform } from '../components/stockup/addstockupform'
import { Addstockuptable } from '../components/stockup/addstockuptable'

export const Stockup = () => {
    const[stock,setstock]=useState([''])
    const fetchfunction=()=>{
        fetch(`/showstockup`).then(response =>{
            if(response.ok)
            return response.json()
        }).then(data => setstock(data))
    }
    useEffect(()=>fetchfunction(),[])
  return (
  <div className="container">
      <h1><u>Add stock up</u></h1>
      <Addstockupform refresh = {fetchfunction}/>
      <Addstockuptable stockupdata={stock} setstockupdata={setstock} refresh={fetchfunction}/>
  </div>
  )
}
