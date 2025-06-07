function digitBtnPressed(value) {
    const display = document.getElementById('display');
    if (display.value === '0' && value !== '.') {
        display.value = value;
    } else {
        display.value += value;
    }
}

// Add functionality for AC and =
document.querySelectorAll('.calculator td').forEach(td => {
    if (td.textContent === '=') {
        td.onclick = () => {
            try {
                const display = document.getElementById('display');
                display.value = eval(display.value.replace('x', '*'));
            } catch (e) {
                alert('Invalid expression');
            }
        };
    } else if (td.textContent === 'AC') {
        td.onclick = () => {
            document.getElementById('display').value = '0';
        };
    }
});