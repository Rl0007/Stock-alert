import React, { useEffect, useState } from 'react'

export const Notify = () => {

    const[message,setmessage]= useState([''])
   const regisnotify=()=>{
        fetch(`/registernotify`).then((val)=>val.json()).then(data => setmessage(data))
    }

  return (
      <div className="conatiner">
  <h3>check if working :- <button type="button"onClick={()=>{fetch(`/send`)}} className="btn btn-warning mx-1">send</button></h3>
  <h3>to regiser new :- <button type="button"onClick={regisnotify} className="btn btn-success mx-1 my-2">Register</button> </h3>

  <p className='mx-2 my-2'>{message}</p>
  </div>
  )
}
