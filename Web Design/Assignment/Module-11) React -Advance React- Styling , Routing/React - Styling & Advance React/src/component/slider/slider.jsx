import React from 'react'
import Carousel from 'react-bootstrap/Carousel';
import image1 from './images/image1.png'
import image2 from './images/image2.png'


const silder = () => {
  return (
    <div>
    <Carousel data-bs-theme="dark">
    <Carousel.Item>
      <img
        className="d-block w-100"
        src={image1}
        alt="First slide"
      />
      <Carousel.Caption>
      </Carousel.Caption>
    </Carousel.Item>
    <Carousel.Item>
      <img
        className="d-block w-100"
        src={image2}
        alt="Second slide"
      />
      <Carousel.Caption>
      </Carousel.Caption>
    </Carousel.Item>
   
  </Carousel>
    </div>
    
  )
}

export default silder