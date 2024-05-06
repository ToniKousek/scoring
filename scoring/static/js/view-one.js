elements = document.getElementsByTagName('input')
for (let i = 0; i < elements.length; i++) {
    const element = elements[i];
    element.nextElementSibling.value = element.value;
}
    
