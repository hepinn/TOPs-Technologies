import React from 'react'
import { Link } from 'react-router-dom'
const Menu = () => {
  return (
    <div>
     <h3>  
        <Link to='/lifecycle'> Lifecycle - Class</Link> ||    
        <Link to='/lifecyclefunc'> Lifecycle - Function</Link>  ||       
        <Link to='/StyleComponent'> Style-Component</Link>         
        </h3>
    </div>
  )
}

export default Menu