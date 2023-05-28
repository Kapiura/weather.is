var horoscopeData = [
    {% for key in horoscope %}
{ sign: "{{key.sign}}", description: "{{key.description}}" },
{% endfor %}
  ];

function decodeEntities(encodedString) {
    var textarea = document.createElement('textarea');
    textarea.innerHTML = encodedString;
    return textarea.value;
}

function showSelected() {
    var selectElement = document.getElementById("myCombo");
    var selectedValue = selectElement.value;
    var infoContainer = document.getElementById("selectedSignInfo");
    var description = "Daily horoscope...";

    for (var i = 0; i < horoscopeData.length; i++) {
        if (horoscopeData[i].sign === selectedValue) {
            description = decodeEntities(horoscopeData[i].description);
            break;
        }
    }

    infoContainer.innerHTML = description;
}

function startTime() {
    var today = new Date();
    var h = today.getHours();
    var m = today.getMinutes();
    var s = today.getSeconds();
    m = checkTime(m);
    s = checkTime(s);
    document.getElementById('txt').innerHTML =
        "Current time: " + h + ":" + m + ":" + s;
    var t = setTimeout(startTime, 500);
}
function checkTime(i) {
    if (i < 10) { i = "0" + i };
    return i;
}
function generatePhoneNumber() {
    var phoneNumber = '';
    for (var i = 0; i < 10; i++) {
        phoneNumber += Math.floor(Math.random() * 10);
    }
    return phoneNumber.slice(0, 3) + '-' + phoneNumber.slice(3, 6) + '-' + phoneNumber.slice(6);
}

document.addEventListener('DOMContentLoaded', function () {
    var phoneNumberParagraph = document.getElementById('phone-number-paragraph');
    phoneNumberParagraph.textContent = '+48 ' + generatePhoneNumber();
});