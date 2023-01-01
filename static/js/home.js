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
    const custom_cords_1 = document.getElementById('custom_cords_1');
    const makeRouteError = document.getElementById('makeRouteError');
    
    if(routeCords.value){
        makeRoute.classList.remove('active');
        makeRouteError.style.display = 'none';
    }else if (custom_cords_1.value){
        makeRoute.classList.remove('active');
        makeRouteError.style.display = 'none';
    }else{
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
    const dropInput = document.getElementById('waypoint_1_sensor');
    const chooseSensor = document.getElementById('chooseSensor');

    dropInput.style.borderBottomLeftRadius = '0';

    chooseSensor.style.display = 'block';
}
function chooseSensor1(){
    const dropInput = document.getElementById('waypoint_1_sensor');
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

function chooseTimeInterval() {
    const btn1 = document.querySelector('.choose-interal-or-time-btn1');
    const btn2 = document.querySelector('.choose-interal-or-time-btn2');

    const intervalCheckbox = document.getElementById('interval');
    const onetimeCheckbox = document.getElementById('onetime');

    const intervalDiv = document.getElementById('interval_div');
    const onetimeDiv = document.getElementById('onetime_div');

    intervalDiv.classList.add('active');
    onetimeDiv.classList.add('hidden');

    intervalCheckbox.checked = true
    onetimeCheckbox.checked = false

    btn1.classList.remove('active');
    btn2.classList.add('active');
}

function chooseTimeOnetime() {
    const btn1 = document.querySelector('.choose-interal-or-time-btn1');
    const btn2 = document.querySelector('.choose-interal-or-time-btn2');

    const intervalCheckbox = document.getElementById('interval');
    const onetimeCheckbox = document.getElementById('onetime');
    
    const intervalDiv = document.getElementById('interval_div');
    const onetimeDiv = document.getElementById('onetime_div');

    intervalDiv.classList.remove('active');
    onetimeDiv.classList.remove('hidden');

    intervalCheckbox.checked = false
    onetimeCheckbox.checked = true

    btn1.classList.add('active');
    btn2.classList.remove('active');
}




//#region NewWaypoint

function routeAddWaypoint11() {
    const custom_cords = document.getElementById('custom_cords_11');
    const custom_cords_last_btn = document.getElementById('custom_cords_11_btn');
    const custom_cords_new_btn = document.getElementById('custom_cords_12_btn');

    custom_cords.classList.add('visible');

    custom_cords_last_btn.classList.add('hidden')

    custom_cords_new_btn.classList.add('visible')
}

function routeAddWaypoint12() {
    const custom_cords = document.getElementById('custom_cords_12');
    const custom_cords_last_btn = document.getElementById('custom_cords_12_btn');
    const custom_cords_new_btn = document.getElementById('custom_cords_13_btn');

    custom_cords.classList.add('visible');

    custom_cords_last_btn.classList.add('hidden')
    custom_cords_last_btn.classList.remove('visible')
    
    custom_cords_new_btn.classList.add('visible')
}

function routeAddWaypoint13() {
    const custom_cords = document.getElementById('custom_cords_13');
    const custom_cords_last_btn = document.getElementById('custom_cords_13_btn');
    const custom_cords_new_btn = document.getElementById('custom_cords_14_btn');

    custom_cords.classList.add('visible');

    custom_cords_last_btn.classList.add('hidden')
    custom_cords_last_btn.classList.remove('visible')
    
    custom_cords_new_btn.classList.add('visible')
}

function routeAddWaypoint14() {
    const custom_cords = document.getElementById('custom_cords_14');
    const custom_cords_last_btn = document.getElementById('custom_cords_14_btn');
    const custom_cords_new_btn = document.getElementById('custom_cords_15_btn');

    custom_cords.classList.add('visible');

    custom_cords_last_btn.classList.add('hidden')
    custom_cords_last_btn.classList.remove('visible')
    
    custom_cords_new_btn.classList.add('visible')
}

function routeAddWaypoint15() {
    const custom_cords = document.getElementById('custom_cords_15');
    const custom_cords_last_btn = document.getElementById('custom_cords_15_btn');
    const custom_cords_new_btn = document.getElementById('custom_cords_16_btn');

    custom_cords.classList.add('visible');

    custom_cords_last_btn.classList.add('hidden')
    custom_cords_last_btn.classList.remove('visible')
    
    custom_cords_new_btn.classList.add('visible')
}

function routeAddWaypoint16() {
    const custom_cords = document.getElementById('custom_cords_16');
    const custom_cords_last_btn = document.getElementById('custom_cords_16_btn');
    const custom_cords_new_btn = document.getElementById('custom_cords_17_btn');

    custom_cords.classList.add('visible');

    custom_cords_last_btn.classList.add('hidden')
    custom_cords_last_btn.classList.remove('visible')
    
    custom_cords_new_btn.classList.add('visible')
}

function routeAddWaypoint17() {
    const custom_cords = document.getElementById('custom_cords_17');
    const custom_cords_last_btn = document.getElementById('custom_cords_17_btn');
    const custom_cords_new_btn = document.getElementById('custom_cords_18_btn');

    custom_cords.classList.add('visible');

    custom_cords_last_btn.classList.add('hidden')
    custom_cords_last_btn.classList.remove('visible')
    
    custom_cords_new_btn.classList.add('visible')
}

function routeAddWaypoint18() {
    const custom_cords = document.getElementById('custom_cords_18');
    const custom_cords_last_btn = document.getElementById('custom_cords_18_btn');
    const custom_cords_new_btn = document.getElementById('custom_cords_19_btn');

    custom_cords.classList.add('visible');

    custom_cords_last_btn.classList.add('hidden')
    custom_cords_last_btn.classList.remove('visible')
    
    custom_cords_new_btn.classList.add('visible')
}

function routeAddWaypoint19() {
    const custom_cords = document.getElementById('custom_cords_19');
    const custom_cords_last_btn = document.getElementById('custom_cords_19_btn');
    const custom_cords_new_btn = document.getElementById('custom_cords_20_btn');

    custom_cords.classList.add('visible');

    custom_cords_last_btn.classList.add('hidden')
    custom_cords_last_btn.classList.remove('visible')
    
    custom_cords_new_btn.classList.add('visible')
}

function routeAddWaypoint20() {
    const custom_cords = document.getElementById('custom_cords_20');
    const custom_cords_last_btn = document.getElementById('custom_cords_20_btn');
    const custom_cords_new_btn = document.getElementById('custom_cords_21_btn');

    custom_cords.classList.add('visible');

    custom_cords_last_btn.classList.add('hidden')
    custom_cords_last_btn.classList.remove('visible')
    
    custom_cords_new_btn.classList.add('visible')
}

function routeAddWaypoint21() {
    const custom_cords = document.getElementById('custom_cords_21');
    const custom_cords_last_btn = document.getElementById('custom_cords_21_btn');
    const custom_cords_new_btn = document.getElementById('custom_cords_22_btn');

    custom_cords.classList.add('visible');

    custom_cords_last_btn.classList.add('hidden')
    custom_cords_last_btn.classList.remove('visible')
    
    custom_cords_new_btn.classList.add('visible')
}

function routeAddWaypoint22() {
    const custom_cords = document.getElementById('custom_cords_22');
    const custom_cords_last_btn = document.getElementById('custom_cords_22_btn');
    const custom_cords_new_btn = document.getElementById('custom_cords_23_btn');

    custom_cords.classList.add('visible');

    custom_cords_last_btn.classList.add('hidden')
    custom_cords_last_btn.classList.remove('visible')
    
    custom_cords_new_btn.classList.add('visible')
}

function routeAddWaypoint23() {
    const custom_cords = document.getElementById('custom_cords_23');
    const custom_cords_last_btn = document.getElementById('custom_cords_23_btn');
    const custom_cords_new_btn = document.getElementById('custom_cords_24_btn');

    custom_cords.classList.add('visible');

    custom_cords_last_btn.classList.add('hidden')
    custom_cords_last_btn.classList.remove('visible')
    
    custom_cords_new_btn.classList.add('visible')
}

function routeAddWaypoint24() {
    const custom_cords = document.getElementById('custom_cords_24');
    const custom_cords_last_btn = document.getElementById('custom_cords_24_btn');
    const custom_cords_new_btn = document.getElementById('custom_cords_25_btn');

    custom_cords.classList.add('visible');

    custom_cords_last_btn.classList.add('hidden')
    custom_cords_last_btn.classList.remove('visible')
    
    custom_cords_new_btn.classList.add('visible')
}

function routeAddWaypoint25() {
    const custom_cords = document.getElementById('custom_cords_25');
    const custom_cords_last_btn = document.getElementById('custom_cords_25_btn');
    const custom_cords_new_btn = document.getElementById('custom_cords_26_btn');

    custom_cords.classList.add('visible');

    custom_cords_last_btn.classList.add('hidden')
    custom_cords_last_btn.classList.remove('visible')
    
    custom_cords_new_btn.classList.add('visible')
}

function routeAddWaypoint26() {
    const custom_cords = document.getElementById('custom_cords_26');
    const custom_cords_last_btn = document.getElementById('custom_cords_26_btn');
    const custom_cords_new_btn = document.getElementById('custom_cords_27_btn');

    custom_cords.classList.add('visible');

    custom_cords_last_btn.classList.add('hidden')
    custom_cords_last_btn.classList.remove('visible')
    
    custom_cords_new_btn.classList.add('visible')
}

function routeAddWaypoint27() {
    const custom_cords = document.getElementById('custom_cords_27');
    const custom_cords_last_btn = document.getElementById('custom_cords_27_btn');
    const custom_cords_new_btn = document.getElementById('custom_cords_28_btn');

    custom_cords.classList.add('visible');

    custom_cords_last_btn.classList.add('hidden')
    custom_cords_last_btn.classList.remove('visible')
    
    custom_cords_new_btn.classList.add('visible')
}

function routeAddWaypoint28() {
    const custom_cords = document.getElementById('custom_cords_28');
    const custom_cords_last_btn = document.getElementById('custom_cords_28_btn');
    const custom_cords_new_btn = document.getElementById('custom_cords_29_btn');

    custom_cords.classList.add('visible');

    custom_cords_last_btn.classList.add('hidden')
    custom_cords_last_btn.classList.remove('visible')
    
    custom_cords_new_btn.classList.add('visible')
}

function routeAddWaypoint29() {
    const custom_cords = document.getElementById('custom_cords_29');
    const custom_cords_last_btn = document.getElementById('custom_cords_29_btn');
    const custom_cords_new_btn = document.getElementById('custom_cords_30_btn');

    custom_cords.classList.add('visible');

    custom_cords_last_btn.classList.add('hidden')
    custom_cords_last_btn.classList.remove('visible')
    
    custom_cords_new_btn.classList.add('visible')
}

function routeAddWaypoint30() {
    const custom_cords = document.getElementById('custom_cords_30');
    const custom_cords_last_btn = document.getElementById('custom_cords_30_btn');
    const custom_cords_new_btn = document.getElementById('custom_cords_31_btn');

    custom_cords.classList.add('visible');

    custom_cords_last_btn.classList.add('hidden')
    custom_cords_last_btn.classList.remove('visible')
    
    custom_cords_new_btn.classList.add('visible')
}

function routeAddWaypoint31() {
    const custom_cords = document.getElementById('custom_cords_31');
    const custom_cords_last_btn = document.getElementById('custom_cords_31_btn');
    const custom_cords_new_btn = document.getElementById('custom_cords_32_btn');

    custom_cords.classList.add('visible');

    custom_cords_last_btn.classList.add('hidden')
    custom_cords_last_btn.classList.remove('visible')
    
    custom_cords_new_btn.classList.add('visible')
}

function routeAddWaypoint32() {
    const custom_cords = document.getElementById('custom_cords_32');
    const custom_cords_last_btn = document.getElementById('custom_cords_32_btn');
    const custom_cords_new_btn = document.getElementById('custom_cords_33_btn');

    custom_cords.classList.add('visible');

    custom_cords_last_btn.classList.add('hidden')
    custom_cords_last_btn.classList.remove('visible')
    
    custom_cords_new_btn.classList.add('visible')
}

function routeAddWaypoint33() {
    const custom_cords = document.getElementById('custom_cords_33');
    const custom_cords_last_btn = document.getElementById('custom_cords_33_btn');
    const custom_cords_new_btn = document.getElementById('custom_cords_34_btn');

    custom_cords.classList.add('visible');

    custom_cords_last_btn.classList.add('hidden')
    custom_cords_last_btn.classList.remove('visible')
    
    custom_cords_new_btn.classList.add('visible')
}

function routeAddWaypoint34() {
    const custom_cords = document.getElementById('custom_cords_34');
    const custom_cords_last_btn = document.getElementById('custom_cords_34_btn');
    const custom_cords_new_btn = document.getElementById('custom_cords_35_btn');

    custom_cords.classList.add('visible');

    custom_cords_last_btn.classList.add('hidden')
    custom_cords_last_btn.classList.remove('visible')
    
    custom_cords_new_btn.classList.add('visible')
}

function routeAddWaypoint35() {
    const custom_cords = document.getElementById('custom_cords_35');
    const custom_cords_last_btn = document.getElementById('custom_cords_35_btn');
    const custom_cords_new_btn = document.getElementById('custom_cords_36_btn');

    custom_cords.classList.add('visible');

    custom_cords_last_btn.classList.add('hidden')
    custom_cords_last_btn.classList.remove('visible')
    
    custom_cords_new_btn.classList.add('visible')
}

function routeAddWaypoint36() {
    const custom_cords = document.getElementById('custom_cords_36');
    const custom_cords_last_btn = document.getElementById('custom_cords_36_btn');
    const custom_cords_new_btn = document.getElementById('custom_cords_37_btn');

    custom_cords.classList.add('visible');

    custom_cords_last_btn.classList.add('hidden')
    custom_cords_last_btn.classList.remove('visible')
    
    custom_cords_new_btn.classList.add('visible')
}

function routeAddWaypoint37() {
    const custom_cords = document.getElementById('custom_cords_37');
    const custom_cords_last_btn = document.getElementById('custom_cords_37_btn');
    const custom_cords_new_btn = document.getElementById('custom_cords_38_btn');

    custom_cords.classList.add('visible');

    custom_cords_last_btn.classList.add('hidden')
    custom_cords_last_btn.classList.remove('visible')
    
    custom_cords_new_btn.classList.add('visible')
}

function routeAddWaypoint38() {
    const custom_cords = document.getElementById('custom_cords_38');
    const custom_cords_last_btn = document.getElementById('custom_cords_38_btn');
    const custom_cords_new_btn = document.getElementById('custom_cords_39_btn');

    custom_cords.classList.add('visible');

    custom_cords_last_btn.classList.add('hidden')
    custom_cords_last_btn.classList.remove('visible')
    
    custom_cords_new_btn.classList.add('visible')
}

function routeAddWaypoint39() {
    const custom_cords = document.getElementById('custom_cords_39');
    const custom_cords_last_btn = document.getElementById('custom_cords_39_btn');
    const custom_cords_new_btn = document.getElementById('custom_cords_40_btn');

    custom_cords.classList.add('visible');

    custom_cords_last_btn.classList.add('hidden')
    custom_cords_last_btn.classList.remove('visible')
    
    custom_cords_new_btn.classList.add('visible')
}

function routeAddWaypoint40() {
    const custom_cords = document.getElementById('custom_cords_40');
    const custom_cords_last_btn = document.getElementById('custom_cords_40_btn');

    custom_cords.classList.add('visible');

    custom_cords_last_btn.classList.add('hidden')
    custom_cords_last_btn.classList.remove('visible')
}
//#endregion