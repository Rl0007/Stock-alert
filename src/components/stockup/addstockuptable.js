import React, { useState } from 'react'
import { Readrow } from './readrow'
import { Fragment } from 'react'
import { Editrow } from './editrow'
export const Addstockuptable = (props) => {
  
  const[editstockid,seteditstockid]= useState([''])
   const handleEdit = (event,stock)=>{
       event.preventDefault();
       seteditstockid(stock.id);
       const formvalues = {
           id : stock.id,
           stock : stock.stock,
           price : stock.price
       }
       seteditformdata(formvalues)
    }
       const[editformdata,seteditformdata]= useState({
           id : "",
           stock : "",
           price : ""
       })
       const handleEditFormChange = (e)=>{
           e.preventDefault();
           const fieldName = e.target.getAttribute('name');
           const filedValue = e.target.value;
           const newFormData = {...editformdata};
    newFormData[fieldName] = filedValue;
    newFormData['id'] = editstockid;
    seteditformdata(newFormData);
       }
       const handleEditformSubmit = (e)=>{
           e.preventDefault();
           fetch(`/updatestockup`,{method:"POST",
        body: JSON.stringify({
            id :editformdata.id,
            stock : editformdata.stock,
            price : editformdata.price
        })})
        .then(response => response.json()).then(data => console.log(data)).then(()=>props.refresh())
        seteditstockid(null)
    }
   
    return (
        <>
         <div className="container">
        <form onSubmit={handleEditformSubmit}>
   <table className="table table-hover table-bordered my-2">
  <thead>
    <tr>
    <th scope="col">Id</th>

      <th scope="col">Stock name</th>
      <th scope="col">Price</th>
      <th scope="col">Action</th>

    </tr>
  </thead>
  <tbody>
 {props.stockupdata.map((stock) =>
 
 
 <Fragment>
   {editstockid === stock.id ? <Editrow editformdata={editformdata} handleEditFormChange={handleEditFormChange} stockupdata = {props.stockupdata} refresh={props.refresh}/>:<Readrow refresh={props.refresh} stock = {stock}  handleEdit={handleEdit} />}
  
  
  
   </Fragment> 
   )}
  </tbody>
</table>
</form>
  </div>
        </>
  
  )
}
