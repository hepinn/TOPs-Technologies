import React, { Component } from 'react'

class Lifecycle extends Component {
    constructor(props){
        super(props)
        this.state = {
            name:"hepin"
        }
        console.log('constructor called...'+this.state.name);
    }
    componentDidMount(){
        setTimeout(()=>{
            this.setState({
                name:"Testing..."
            })
        },2000)
        console.log('component did mount called..'+this.state.name);
    }
    static getDerivedStateFromProps(props,state){
        console.log('getDerived state from props called...'+state.name);
    }
    shouldComponentUpdate(){
        return true;
    }
    getSnapshotBeforeUpdate(prevProps,prevState){
        console.log("Prev name is "+prevState.name);
        return prevState;
    }
    componentDidUpdate(){
        console.log('component updated...');
    }
    componentWillUnmount(){
        console.log('destroyed...');
    }
  render() {
    const handleChange = ()=>{
        this.setState({
            name:"Kalakni"
        })
    }
    console.log('render func calling..');
    return (
      <div>
        <h3>Name is : {this.state.name}</h3>
        <button onClick={handleChange}>Change Name</button>
      </div>
    )
  }
}
export default  Lifecycle;