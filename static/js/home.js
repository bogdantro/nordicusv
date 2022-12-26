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
function chooseSensorDrop(){
    const dropInput = document.getElementById('sensor_1_waypoins');
    const chooseSensor = document.getElementById('chooseSensor');

    dropInput.style.borderBottomLeftRadius = '0';

    chooseSensor.style.display = 'block';
}
function chooseSensor1(){
    const dropInput = document.getElementById('sensor_1_waypoins');
    const chooseSensor = document.getElementById('chooseSensor');

    dropInput.style.borderBottomLeftRadius = '4px';

    dropInput.value = 'Sensor 1';

    chooseSensor.style.display = 'none';
}


// Set date/time
function stepThreeOpen(){
    const setTime = document.getElementById('setTime');
    setTime.classList.add('active');
}
function stepThreeClose(){
    const setTime = document.getElementById('setTime');

    setTime.classList.remove('active');
}
function validateStepThree(){
    const setTime = document.getElementById('setTime');
    const setTimeError = document.getElementById('setTimeError');
    const time = document.getElementById('time');
    
    if(time.value){
        setTime.classList.remove('active');
        setTimeError.style.display = 'none';
    }else{
        setTimeError.style.display = 'block';        
    }
}

// User info
function stepFourOpen(){
    const userInfo = document.getElementById('userInfo');
    userInfo.classList.add('active');
}
function stepFourClose(){
    const userInfo = document.getElementById('userInfo');

    userInfo.classList.remove('active');
}
function validateStepFour(){
    const userInfo = document.getElementById('userInfo');
    const userInfoError = document.getElementById('userInfoError');
    const userInfoInput = document.querySelector('.user-info-input-m');
    
    if(userInfoInput.value){
        userInfo.classList.remove('active');
        userInfoError.style.display = 'none';
    }else{
        userInfoError.style.display = 'block';        
    }
}

// Survey summary 
function stepFiveOpen(){
    const surveySummary = document.getElementById('surveySummary');
    surveySummary.classList.add('active');
}
function stepFiveClose(){
    const surveySummary = document.getElementById('surveySummary');

    surveySummary.classList.remove('active');
}

