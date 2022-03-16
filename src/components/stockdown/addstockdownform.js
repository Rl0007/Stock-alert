import React, { useState } from 'react'
import Alert from 'react-bootstrap/Alert';

export const Addstockdownform = (props) => {
  
    const[stockdown,setstockdown] = useState([''])
    const[price,setprice]= useState([''])
     const[showalert,setshowalert] = useState(false)
    const[showalert1,setshowalert1] = useState(false)
  
    const handlesubmit = (e)=>{
        e.preventDefault();
        fetch(`/createstockdown`,{
            method :"POST",
            body : JSON.stringify({
                stock : stockdown,
                price : price
            })
        }).then(response=>response.json()).then((data)=>console.log(data)).then(()=>props.refresh())
        setstockdown([''])
        setprice([''])
    }
     const handlestartstreaming =()=>
    {fetch(`/startstreaming`).then(response => response.json()).then((data) =>{
      if (data['22']==='streaming'){
        setshowalert(true)
      }
    } ).then(props.refresh());
      }

    const handlestopstreaming =()=>
    {fetch(`/stopstreaming`).then(response => response.json()).then((data) =>{
      if(data['23']==='streaming stopped'){
        setshowalert1(true)
      }
    } ).then(props.refresh())}
   
    if (showalert) {
    return (
      <Alert variant="success" onClose={() => setshowalert(false)} dismissible>
        <Alert.Heading>Stream</Alert.Heading>
        <p>
streaming started successfully!!!        </p>
      </Alert>
    );
  }
   if (showalert1) {
    return (
      <Alert variant="danger" onClose={() => setshowalert1(false)} dismissible>
        <Alert.Heading>Stream</Alert.Heading>
        <p>
streaming stopped successfully!!!        </p>
      </Alert>
    );
  }
   
   return (<>

     <div className="container"> 
   <form onSubmit={handlesubmit}>
  <div className="mb-3">
    <label htmlFor="stockdown" className="form-label" >Stock name</label>
    <input type="text" className="form-control" required='required' value={stockdown} onChange={(e)=>setstockdown(e.target.value)} id="stockname" aria-describedby="emailHelp"/>
  </div>
  <div className="mb-3">
    <label htmlFor="price" className="form-label" >stock price</label>
    <input type="number step=0.01" className="form-control"required='required' value={price} onChange={(e)=>{setprice(e.target.value)}} id="price" aria-describedby="emailHelp"/>
  </div>
 
  <button type="submit" className="btn btn-success my-2">Submit</button> <button type="button"onClick={handlestartstreaming} class="btn btn-warning mx-1">Start</button> <button onClick={handlestopstreaming} type="button" class="btn btn-danger"> Stop </button>
</form>

</div>
    </>
    
  )
}
