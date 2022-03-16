import React, { useState } from 'react';


export const Readrow = ({stock,handleEdit,refresh}) => {
  // const history = useNavigate();
  const handleDelete=(e,id)=>{
   e.preventDefault();
   fetch(`/deletestockup/${id}`).then(response => response.json()).then(data => console.log(data)).then(()=>refresh())
 
    // history('/');
  
 }
 
  return (<>
       

      
    <tr key={stock.id}>
    <td>{ stock.id}</td>


    <td>{ stock.stock}</td>
    <td>{stock.price} </td>
    
    <td>
      <button type="button" onClick={(e)=>handleDelete(e,stock.id)} className="btn btn-sm btn-outline-danger mx-1 my-1" > <i className="bi bi-trash"></i>Delete</button>
      <button type="button" onClick={(e)=> handleEdit(e,stock)} className="btn btn-outline-warning btn-sm mx-1 my-1"><i className="bi bi-brush "></i>Update</button>
    </td>
    </tr>
    </>
  )
}
