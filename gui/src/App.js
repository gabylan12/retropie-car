import React,{Component} from 'react';
import arrow from './arrow.png';
import stop_button from './stop-button.png';
import './App.css';
import axios from 'axios'


class App extends Component{

    constructor(){
      super()
      this.handleClick = this.handleClick.bind(this)
    }

    handleClick(e){
        console.log ('http://'+window.location.hostname+':5000/' + e.target.id)
        axios.get('http://'+window.location.hostname+':5000/' + e.target.id)
    }

    render() {
      return (
        <>
            <div align="center"  >
                <div align="right" >
                    <a id="blue" href="#" className="myButton-blue" onClick={this.handleClick}>blue</a>
                    <a id="green" href="#" className="myButton-green" onClick={this.handleClick}>green</a>
                    <a id="yellow" href="#" className="myButton-yellow" onClick={this.handleClick}>yellow</a>

                </div>
                <img id="forward" src={arrow}  onClick={this.handleClick} />
                <div>
                    <img id="left" src={arrow}  className="arrow-left" onClick={this.handleClick}/>
                    <img id="stop" src={stop_button} onClick={this.handleClick} />
                    <img id="right" src={arrow} className="arrow-right" onClick={this.handleClick} />
                </div>
                <img id="backward" src={arrow}  className="arrow-down" onClick={this.handleClick} />
            </div>
          </>
      );
    }
}

export default App;
