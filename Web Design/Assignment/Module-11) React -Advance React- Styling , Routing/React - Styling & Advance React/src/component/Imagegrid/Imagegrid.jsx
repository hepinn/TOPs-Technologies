import React from 'react';
import { Container, Row, Col } from 'react-bootstrap';
import 'bootstrap/dist/css/bootstrap.min.css'; 
import banner1 from '../Imagegrid/image/banner1.png'; 
import banner2 from '../Imagegrid/image/banner2.png';
import banner3 from '../Imagegrid/image/banner3.png';  

const Imagegrid = () => {
  return (
    <div>
      <Container className="my-4">  
        <Row>
          <Col className="p-2"> 
            <img src={banner1} alt="Image 1" className="img-fluid" />
            
          </Col>
          <Col className="p-2">
            <img src={banner2} alt="Image 2" className="img-fluid" />
          </Col>
          <Col className="p-2">
            <img src={banner3} alt="Image 3" className="img-fluid" />
          </Col>
        </Row>
      </Container>
    </div>
  );
}

export default Imagegrid;