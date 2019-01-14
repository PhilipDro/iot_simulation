import Simulation from './Simulation';
import Visualisation from './Visualisation';
import './app.scss';

window.Simulation = Simulation;

// set up WebSocket
let ws = new WebSocket('ws://172.20.10.3:5679');
let response;

let received = false;

ws.onmessage = event => {

    if(!received) {
        received = true;

        const markers = JSON.parse(event.data);

        // start the simulation
        const sim = new Simulation(markers);
        window.sim = sim;

        sim.getChairControl().start();

        // make astar api available to window
        window.path = sim.path();

        // make chairs available
        window.chairs = sim.getChairControl().getChairs();

        // move all chairs to set position
        for (var i = 0; i < chairs.length; i++) {
            chairs[i].moveToTarget();
        }

        var formationOneButton = document.querySelector('.formation-one');
        var formationTwoButton = document.querySelector('.formation-two');
        var formationThreeButton = document.querySelector('.formation-three');
        var formationFourButton = document.querySelector('.formation-four');

        formationOneButton.addEventListener('click', function (e) {
            sim.formationOne();
        });

        formationTwoButton.addEventListener('click', function (e) {
            sim.formationTwo();
        });

        formationThreeButton.addEventListener('click', function (e) {
            sim.formationThree();
        });

        formationFourButton.addEventListener('click', function (e) {
            sim.formationFour();
        });
    }
};