import React from 'react'

export const Editrow = (props) => {
  return (
    <tr >
      <td>{props.editformdata.id}</td>
 <td><input type="text" required = 'required' placeholder='enter stockname...'
            name='stock'value={props.editformdata.stock} onChange={props.handleEditFormChange}/></td>
        <td>
            <input type="number step=0.01" required = 'required' placeholder='enter price'
            name='price' value={props.editformdata.price} onChange={props.handleEditFormChange}/>
        </td>
       
    <td>
            <button type='submit' className='btn btn-outline-success btn-small'><i className="bi bi-save"></i>save</button>
          </td>

    </tr>
  )
}
