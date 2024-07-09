import React from 'react';
import Card from 'react-bootstrap/Card';
import ListGroup from 'react-bootstrap/ListGroup';
import Button from 'react-bootstrap/Button';
import { Container, Row, Col } from 'react-bootstrap';
import 'bootstrap/dist/css/bootstrap.min.css'; 
import product1 from '../card/image/product1.jpg'; 
import product2 from '../card/image/product2.jpg'; 
import product3 from '../card/image/product3.jpg'; 
import product4 from '../card/image/product4.jpg'; 
import product5 from '../card/image/product5.jpg'; 

function CustomCard() {
  return (
    <div>
      <h1>Popular Products</h1>
      <Container className="my-4"> {/* Adds margin to the top and bottom */}
      <Row>
        <Col className="mb-4"> {/* mb-4 adds margin-bottom */}
          <Card style={{ width: '14rem' , border: "none" }}>
            <Card.Img variant="top" src={product1} />
              <ListGroup.Item >Seeds of Change Organic Quinoa, Brown</ListGroup.Item> <br />
              <ListGroup.Item>By <span style={{color :'#3bb77e'}}>NestFood</span></ListGroup.Item> <br />
              <ListGroup.Item> <span style={{color :'#3bb77e', fontWeight : '700'}}>$238.85</span>
                   <Button  style={{margin:'0 50px'  , background:'#3bb77e' , border : 'none'}}> Add</Button>
            </ListGroup.Item>
          </Card>
        </Col>

        <Col className="mb-4"> {/* mb-4 adds margin-bottom */}
          <Card style={{ width: '14rem' , border: "none" }}>
            <Card.Img variant="top" src={product2} />
              <ListGroup.Item>All Natural Italian-Style Chicken Meatballs</ListGroup.Item> <br />
              <ListGroup.Item>By <span style={{color :'#3bb77e'}}>NestFood</span> </ListGroup.Item> <br />
              <ListGroup.Item><span style={{color :'#3bb77e', fontWeight : '700'}}>$78</span>
              <Button  style={{margin:'0 70px'  , background:'#3bb77e' , border : 'none'}}> Add</Button>
              </ListGroup.Item>
          </Card>
        </Col>

        <Col className="mb-4"> {/* mb-4 adds margin-bottom */}
          <Card style={{ width: '14rem' , border: "none" }}>
            <Card.Img variant="top" src={product3} />
            
              <ListGroup.Item>Angie’s Boomchickapop Sweet & Salty</ListGroup.Item> <br />
              <ListGroup.Item>By <span style={{color :'#3bb77e'}}>NestFood</span> </ListGroup.Item> <br />
              <ListGroup.Item><span style={{color :'#3bb77e', fontWeight : '700'}}>$35</span>
              <Button  style={{margin:'0 50px'  , background:'#3bb77e' , border : 'none'}}> Add</Button>
              </ListGroup.Item>
              
          </Card>
        </Col>

        <Col className="mb-4"> {/* mb-4 adds margin-bottom */}
          <Card style={{ width: '14rem' , border: "none" }}>
            <Card.Img variant="top" src={product4} />
            
              <ListGroup.Item>Foster Farms Takeout Crispy Classic</ListGroup.Item> <br />
              <ListGroup.Item>By <span style={{color :'#3bb77e'}}>NestFood</span> </ListGroup.Item> <br />
              <ListGroup.Item><span style={{color :'#3bb77e', fontWeight : '700'}}>$55</span>
              <Button  style={{margin:'0 50px'  , background:'#3bb77e' , border : 'none'}}> Add</Button>
              </ListGroup.Item>

          </Card>
        </Col>

        <Col className="mb-4"> {/* mb-4 adds margin-bottom */}
          <Card style={{ width: '14rem' , border: "none" }}>
            <Card.Img variant="top" src={product5} />
              <ListGroup.Item>Green Diamond Almonds Lightly From Oska</ListGroup.Item> <br />
              <ListGroup.Item>By <span style={{color :'#3bb77e'}}>NestFood</span> </ListGroup.Item> <br />
              <ListGroup.Item><span style={{color :'#3bb77e', fontWeight : '700'}}>$110</span>
              <Button  style={{margin:'0 50px'  , background:'#3bb77e' , border : 'none'}}> Add</Button>
              </ListGroup.Item>
          </Card>
        </Col>
      </Row>
    </Container>
    </div>
    

    
  );
}

export default CustomCard;


