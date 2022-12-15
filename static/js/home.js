// Make route
function stepOneOpen(){
    const makeRoute = document.getElementById('makeRoute');

    makeRoute.classList.add('active');
}
function stepOneClose(){
    const makeRoute = document.getElementById('makeRoute');

    makeRoute.classList.remove('active');
}
function validateStepOne(){
    const makeRoute = document.getElementById('makeRoute');
    const routeCords = document.getElementById('routeCords');
    const customCords = document.getElementById('customCords');
    const makeRouteError = document.getElementById('makeRouteError');
    
    if(routeCords.value){
        makeRoute.classList.remove('active');
        makeRouteError.style.display = 'none';
        customCords.style.pointerEvents = 'none';
    }else if (customCords.value){
        makeRoute.classList.remove('active');
        makeRouteError.style.display = 'none';
    }else{
        customCords.style.pointerEvents = 'visible';
        makeRouteError.style.display = 'block';        
    }
}

// Add sensors
function stepTwoOpen(){
    const addSensors = document.getElementById('addSensors');

    addSensors.classList.add('active');
}
function stepTwoClose(){
    const addSensors = document.getElementById('addSensors');

    addSensors.classList.remove('active');
}
function validateStepTwo(){
    const addSensors = document.getElementById('addSensors');
    const addSensorError = document.getElementById('addSensorError');
    const sensorInput = document.querySelector('.sensor-input');
    
    if(sensorInput.value){
        addSensors.classList.remove('active');
        addSensorError.style.display = 'none';
    }else{
        addSensorError.style.display = 'block';        
    }
}