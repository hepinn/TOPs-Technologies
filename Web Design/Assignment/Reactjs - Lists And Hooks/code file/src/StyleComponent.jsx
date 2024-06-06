import React from 'react'
import styled from 'styled-components'
import './Style.css'
const StyleComponent = () => {
    const myCustomStyle = {
        color:'green',
        height:'300px',
        width:'500px',
        border:'1px solid black'
    }
    const H2 = styled.h2 `
            color:blue
    `
    const Title = styled.h1`
        font-size: 1.5em;
        text-align: center;
        color: palevioletred;
        `;

    const Wrapper = styled.section`
        padding: 4em;
        background: papayawhip;
      `;
  return (
    <div>
        <H2>Styled Component Example</H2>
      <h3 style={{color:'red',backgroundColor:'yellow'}}>Hello - Style Component Called...</h3>
      <div style={myCustomStyle}>
            <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Earum, exercitationem reprehenderit nihil voluptate culpa a magnam dolor, quas accusamus quos assumenda neque nesciunt quasi odio sed illo dolorum! Tempora, obcaecati.</p>
      </div>
      <div className='box'>
            <p>Lorem ipsum dolor sit amet consectetur, adipisicing elit. Consectetur, saepe? Sint, vero autem. Fuga assumenda quibusdam quasi nulla cupiditate odit aperiam doloremque pariatur facere voluptate provident, vero blanditiis? Illum possimus nemo accusantium ducimus ex ea, quam provident facilis obcaecati natus impedit! Obcaecati laudantium exercitat</p>
      </div>
      <Wrapper>
      <Title>Hello World, this is my first styled component!</Title>
    </Wrapper>
    </div>
  )
}

export default StyleComponent