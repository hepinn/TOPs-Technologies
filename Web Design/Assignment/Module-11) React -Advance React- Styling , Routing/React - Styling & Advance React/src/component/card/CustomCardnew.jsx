import React from 'react'
import Card from 'react-bootstrap/Card';
import ListGroup from 'react-bootstrap/ListGroup';
import Button from 'react-bootstrap/Button';
import { Container, Row, Col } from 'react-bootstrap';
import 'bootstrap/dist/css/bootstrap.min.css'; 
import product6 from '../card/image/product6.jpg'; 
import product7 from '../card/image/product7.jpg'; 
import product8 from '../card/image/product8.jpg'; 
import product9 from '../card/image/product9.jpg'; 
import product10 from '../card/image/product10.jpg'; 


const CustomCardnew = () => {
  return (
    <div>
     <div>
     
      <Container className="my-4"> {/* Adds margin to the top and bottom */}
      <Row>
        <Col className="mb-4"> {/* mb-4 adds margin-bottom */}
          <Card style={{ width: '14rem' , border: "none" }}>
            <Card.Img variant="top" src={product6} />
              <ListGroup.Item >Chobani Complete Vanilla Greek Yogurt</ListGroup.Item> <br />
              <ListGroup.Item>By <span style={{color :'#3bb77e'}}>NestFood</span></ListGroup.Item> <br />
              <ListGroup.Item > <span style={{color :'#3bb77e', fontWeight : '700'}}>$150</span>
                   <Button  style={{margin:'0 50px'  , background:'#3bb77e' , border : 'none'}}> Add</Button>
            </ListGroup.Item>
          </Card>
        </Col>

        <Col className="mb-4"> {/* mb-4 adds margin-bottom */}
          <Card style={{ width: '14rem' , border: "none" }}>
            <Card.Img variant="top" src={product7} />
              <ListGroup.Item>Canada Dry Ginger Ale – 2 L Bottle</ListGroup.Item> <br />
              <ListGroup.Item>By <span style={{color :'#3bb77e'}}>NestFood</span> </ListGroup.Item> <br />
              <ListGroup.Item><span style={{color :'#3bb77e', fontWeight : '700'}}>$98</span>
              <Button  style={{margin:'0 70px'  , background:'#3bb77e' , border : 'none'}}> Add</Button>
              </ListGroup.Item>
          </Card>
        </Col>

        <Col className="mb-4"> {/* mb-4 adds margin-bottom */}
          <Card style={{ width: '14rem' , border: "none" }}>
            <Card.Img variant="top" src={product8} />
              <ListGroup.Item>Encore Seafoods Stuffed Alaskan</ListGroup.Item> <br />
              <ListGroup.Item>By <span style={{color :'#3bb77e'}}>NestFood</span> </ListGroup.Item> <br />
              <ListGroup.Item><span style={{color :'#3bb77e', fontWeight : '700'}}>$24</span>
              <Button  style={{margin:'0 50px'  , background:'#3bb77e' , border : 'none'}}> Add</Button>
              </ListGroup.Item>
          </Card>
        </Col>

        <Col className="mb-4"> {/* mb-4 adds margin-bottom */}
          <Card style={{ width: '14rem' , border: "none" }}>
            <Card.Img variant="top" src={product9} />
              <ListGroup.Item>Gorton’s Beer Battered Fish Fillets</ListGroup.Item> <br />
              <ListGroup.Item>By <span style={{color :'#3bb77e'}}>NestFood</span> </ListGroup.Item> <br />
              <ListGroup.Item><span style={{color :'#3bb77e', fontWeight : '700'}}>$146</span>
              <Button  style={{margin:'0 50px'  , background:'#3bb77e' , border : 'none'}}> Add</Button>
              </ListGroup.Item>
          </Card>
        </Col>

        <Col className="mb-4"> {/* mb-4 adds margin-bottom */}
          <Card style={{ width: '14rem' , border: "none" }}>
            <Card.Img variant="top" src={product10} />
              <ListGroup.Item>Haagen-Dazs Caramel Cone Ice Cream</ListGroup.Item> <br />
              <ListGroup.Item>By <span style={{color :'#3bb77e'}}>NestFood</span> </ListGroup.Item> <br />
              <ListGroup.Item><span style={{color :'#3bb77e', fontWeight : '700'}}>$67</span>
              <Button  style={{margin:'0 50px'  , background:'#3bb77e' , border : 'none'}}> Add</Button>
              </ListGroup.Item>
          </Card>
        </Col>
      </Row>
    </Container>
    </div>

    </div>
  )
}

export default CustomCardnew