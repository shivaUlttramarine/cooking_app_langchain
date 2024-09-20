
document.addEventListener('DOMContentLoaded', function () {
    const submitBtn = document.getElementById('submitBtn');
    const selectedItemsList = document.getElementById('selectedItemsList');
    const cookingTimeSelect = document.getElementById('items_cooking_time');
    const imagesContainer = document.getElementById('imagesContainer');

 
    submitBtn.addEventListener('click', function() {
        // Clear the previous list of selected items
        selectedItemsList.innerHTML = "  ";

        // Get all checked checkboxes
        const selectedCheckboxes = document.querySelectorAll('input[type="checkbox"]:checked');
        
       

        // Display the selected items
        selectedCheckboxes.forEach(checkbox => {
            const listItem = document.createElement('li');
            listItem.textContent = checkbox.id;  // Use the value of the checkbox
            selectedItemsList.appendChild(listItem);            
        });
        console.log("selectedItemsList ", selectedItemsList);

        const selectedCookingTimes = Array.from(cookingTimeSelect.selectedOptions).map(option => option.value);
        console.log("selectedCookingTimes ", selectedCookingTimes);
        

        const formData = new FormData();
        selectedCheckboxes.forEach(checkbox => {
            formData.append('selected_items', checkbox.id); 
        });

        console.log("1...formData ", formData);
        selectedCookingTimes.forEach(time => {
            formData.append('selected_cooking_time', time);
        });
        // formData.append('selected_cooking_time', selectedCookingTimes);
        console.log("2...formData ", formData);
        for (const [key, value] of formData.entries()) {
            console.log(`${key}: ${value}`);
        }
        console.log("3... formData ", formData);

        // Send the selected items to the backend via AJAX
        fetch('/generate', {
            method: 'POST',
            body: formData,  // Send the FormData object directly
        })
        .then(response => response.json())
        .then(data => {
            // console.log("data ");
            // console.log("data ", data);
            // console.log("data.generated_images ", data.generated_images);
            // Clear the container before adding new images
            imagesContainer.innerHTML = '';

            // // Loop through the images_with_descriptions data and create elements
            data.generated_images.forEach(item => {
                // Create image element
                console.log("item ");
                console.log("item ", item.filename);
                const img = document.createElement('img');
                img.src = item.filename;
                img.alt = item.description;
                img.style.width = '200px';  // Style the image if needed

                // Create description paragraph
                const description = document.createElement('p');
                description.textContent = item.description;

                // Append the image and description to the container
                imagesContainer.appendChild(img);
                imagesContainer.appendChild(description);
            });
        })
        .catch(error => {
            console.log('Error fetching images:', error);
            console.log('Error fetching images:', error);
            });
        });


    //     // Handle carbohydrate selection
    //     diarySquares.forEach(square => {
    //     square.addEventListener('click', function () {
    //         const itemName = this.getAttribute('data-name');

    //         // Toggle selected class
    //         if (this.classList.contains('selected')) {
    //             this.classList.remove('selected');
    //             const index = selectedDiary.indexOf(itemName);
    //             if (index > -1) {
    //                 selectedDiary.splice(index, 1);
    //             }
    //         } else {
    //             this.classList.add('selected');
    //             selectedDiary.push(itemName);
    //         }

    //         console.log("Selected Diary: ", selectedDiary);
    //     });
    // });
        

    //     // Handle carbohydrate selection
    //     carbohydrateSquares.forEach(square => {
    //     square.addEventListener('click', function () {
    //         const itemName = this.getAttribute('data-name');

    //         // Toggle selected class
    //         if (this.classList.contains('selected')) {
    //             this.classList.remove('selected');
    //             const index = selectedCarbohydrates.indexOf(itemName);
    //             if (index > -1) {
    //                 selectedCarbohydrates.splice(index, 1);
    //             }
    //         } else {
    //             this.classList.add('selected');
    //             selectedCarbohydrates.push(itemName);
    //         }

    //         console.log("Selected Carbohydrates: ", selectedCarbohydrates);
    //     });
    // });

    //     // Handle carbohydrate selection
    //     meatSquares.forEach(square => {
    //     square.addEventListener('click', function () {
    //         const itemName = this.getAttribute('data-name');

    //         // Toggle selected class
    //         if (this.classList.contains('selected')) {
    //             this.classList.remove('selected');
    //             const index = selectedMeat.indexOf(itemName);
    //             if (index > -1) {
    //                 selectedMeat.splice(index, 1);
    //             }
    //         } else {
    //             this.classList.add('selected');
    //             selectedMeat.push(itemName);
    //         }

    //         console.log("Selected Meat: ", selectedMeat);
    //     });
    // });

    
    //     // Handle Vegetable selection
    //     vegetableSquares.forEach(square => {
    //     square.addEventListener('click', function () {
    //         const itemName = this.getAttribute('data-name');

    //         // Toggle selected class
    //         if (this.classList.contains('selected')) {
    //             this.classList.remove('selected');
    //             const index = selectedVegetable.indexOf(itemName);
    //             if (index > -1) {
    //                 selectedVegetable.splice(index, 1);
    //             }
    //         } else {
    //             this.classList.add('selected');
    //             selectedVegetable.push(itemName);
    //         }

    //         console.log("Selected Vegetable: ", selectedVegetable);
    //     });
    // });


    //     // Handle Other selection
    //     otherSquares.forEach(square => {
    //     square.addEventListener('click', function () {
    //         const itemName = this.getAttribute('data-name');

    //         // Toggle selected class
    //         if (this.classList.contains('selected')) {
    //             this.classList.remove('selected');
    //             const index = selectedOther.indexOf(itemName);
    //             if (index > -1) {
    //                 selectedOther.splice(index, 1);
    //             }
    //         } else {
    //             this.classList.add('selected');
    //             selectedOther.push(itemName);
    //         }

    //         console.log("Selected other: ", selectedOther);
    //     });
    // });


    

    


    


    
    // // Handle form submission
    // const form = document.getElementById('selectedForm');
    // const selectedProteinsInput = document.getElementById('selectedProteinsInput');
    // const selectedCarbohydratesInput = document.getElementById('selectedCarbohydratesInput');

    // form.addEventListener('submit', function (event) {
    //     event.preventDefault();  // Prevent normal form submission

    //     // Update hidden input values with selected items
    //     selectedProteinsInput.value = JSON.stringify(selectedProteins);
    //     selectedCarbohydratesInput.value = JSON.stringify(selectedCarbohydrates);

    //     // Submit the form
    //     form.submit();
    // });
});
 