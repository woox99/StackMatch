
let selectedBoolBox = document.querySelector('.bool-1')
let selectedBoolBoxNumber = 0

const toggleSelect = (checkbox, category) => {
    const labelElement = document.querySelector(`[data-label="${checkbox.name}"]`);
    
    const placeholderElement = document.querySelector('.placeholder-text')
    placeholderElement.style.display = 'none';
    
    // If tag is not already selected, add tag to bool box, else remove it.
    if (checkbox.checked) {

        console.log(placeholderElement)

        const tagElement = document.createElement('p')
        const orElement = document.createElement('p')

        orElement.innerHTML = 'OR'
        orElement.setAttribute('data-checkbox-name', checkbox.name);
        // orElement.classList.add(checkbox.name)
        orElement.classList.add('or')
        
        tagElement.innerHTML = checkbox.name
        tagElement.setAttribute('data-checkbox-name', checkbox.name);
        // tagElement.classList.add(checkbox.name)
        tagElement.classList.add('tag')
        tagElement.classList.add(category)
    
        selectedBoolBox.appendChild(tagElement)
        selectedBoolBox.appendChild(orElement)

        checkbox.style.opacity = '1'
        labelElement.style.opacity = '1'

        
        // Assigned box number 
        selectedBoolBoxNumber = selectedBoolBox.getAttribute('data-box-number')
        checkbox.value = selectedBoolBoxNumber
        
    } else {
        tagElementsToRemove = document.querySelectorAll(`[data-checkbox-name="${checkbox.name}"]`);
        
        for(const element of tagElementsToRemove){
            element.remove()
        }
        
        checkbox.style.opacity = '0.6'
        labelElement.style.opacity = '0.6'
    }

}

const selectBoolBox = (element) => {
    selectedBoolBox = element

    const boolBoxes = document.querySelectorAll('.bool-box')

    for(const boolBox of boolBoxes){
        boolBox.style.backgroundColor = '#ffffff00'
    }
    element.style.backgroundColor = '#ffffff08'
}

function submitForm() {
    document.getElementById('selectForm').submit();
}

const toggleExpand = element => {
    const categoryElements = document.querySelectorAll('.category')

    for(const category of categoryElements){
        category.style.height = '50px'
    }

    element.style.height = 'unset'
}
