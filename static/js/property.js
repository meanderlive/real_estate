$(document).ready(function() {
    $.ajax({
        url: 'http://127.0.0.1:8000/api/properties/',  // Your API endpoint
        method: 'GET',
        success: function(data) {
            let htmlContent = '';
            data.forEach(property => {
                if (property.property_type.name === 'Rent') {
                    htmlContent += `
                        <div class="col mb-30px">
                            <div class="border-radius-6px overflow-hidden box-shadow-large">
                                <div class="image position-relative">
                                    <a href="demo-real-estate-property-details.html">
                                        <img src="${property.image}" alt="">
                                    </a>
                                    <div class="col-auto bg-orange border-radius-50px ps-15px pe-15px text-uppercase alt-font fw-600 text-white fs-12 lh-24 position-absolute left-20px top-20px">${property.property_type.name}</div>
                                </div>
                                <div class="bg-white">
                                    <div class="content ps-40px pe-40px pt-35px pb-35px md-p-25px border-bottom border-color-transparent-dark-very-light">
                                        <div class="d-flex align-items-center">
                                            <a href="demo-real-estate-property-details.html" class="alt-font text-dark-gray fw-700 fs-22 me-10px">${property.name}</a>
                                        </div>
                                        <p class="mb-20px">${property.address}</p>
                                        <div class="row g-0">
                                            <div class="col">
                                                <div class="d-flex align-items-center">
                                                    <img src="{% static 'images/demo-real-estate-icon-bed-small.svg' %}" class="me-5px h-20px" alt="">
                                                    <span class="fw-600 alt-font text-dark-gray">${property.bedroom}</span>
                                                </div>
                                                <span class="d-block lh-18 fs-15">Bedrooms</span> 
                                            </div>
                                            <div class="col">
                                                <div class="d-flex align-items-center">
                                                    <img src="{% static 'images/demo-real-estate-icon-bath-small.svg' %}" class="me-5px h-20px" alt="">
                                                    <span class="fw-600 alt-font text-dark-gray">${property.bathroom}</span>
                                                </div>
                                                <span class="d-block lh-18 fs-15">Bathrooms</span> 
                                            </div>
                                            <div class="col">
                                                <div class="d-flex align-items-center">
                                                    <img src="{% static 'images/demo-real-estate-icon-size-small.svg' %}" class="me-5px h-20px" alt="">
                                                    <span class="fw-600 alt-font text-dark-gray">${property.living_area}m<sup>2</sup></span>
                                                </div>
                                                <span class="d-block lh-18 fs-15">Living area</span> 
                                            </div>
                                        </div>
                                    </div>
                                    <div class="row ps-35px pe-35px pt-20px pb-20px md-ps-25px md-pe-25px align-items-center">
                                        <div class="col">
                                            <a href="demo-real-estate-property-details.html" class="btn btn-dark-gray btn-very-small btn-round-edge fw-600">View details</a>
                                        </div>
                                        <div class="col text-end">
                                            <span class="fs-24 alt-font text-dark-gray fw-700 mb-0">$${property.price}</span>
                                        </div> 
                                    </div>
                                </div>
                            </div>
                        </div>
                    `;
                }
            });
            $('#property-container').html(htmlContent);
        },
        error: function(xhr, status, error) {
            console.error("Error fetching data: ", error);
        }
    });
});

$(document).ready(function() {
    $.ajax({
        url: 'http://127.0.0.1:8000/api/properties/',  // Your API endpoint
        method: 'GET',
        success: function(data) {
            let htmlContent = '';
            data.forEach(property => {
                if (property.property_type.name === 'Sell') {  // Check if property type is "Sell"
                    htmlContent += `
                        <div class="col mb-30px">
                            <div class="border-radius-6px overflow-hidden box-shadow-large">
                                <div class="image position-relative">
                                    <a href="demo-real-estate-property-details.html">
                                        <img src="${property.image}" alt="">
                                    </a>
                                    <div class="col-auto bg-orange border-radius-50px ps-15px pe-15px text-uppercase alt-font fw-600 text-white fs-12 lh-24 position-absolute left-20px top-20px">${property.property_type.name}</div>
                                </div>
                                <div class="bg-white">
                                    <div class="content ps-40px pe-40px pt-35px pb-35px md-p-25px border-bottom border-color-transparent-dark-very-light">
                                        <div class="d-flex align-items-center">
                                            <a href="demo-real-estate-property-details.html" class="alt-font text-dark-gray fw-700 fs-22 me-10px">${property.name}</a>
                                        </div>
                                        <p class="mb-20px">${property.address}</p>
                                        <div class="row g-0">
                                            <div class="col">
                                                <div class="d-flex align-items-center">
                                                    <img src="{% static 'images/demo-real-estate-icon-bed-small.svg' %}" class="me-5px h-20px" alt="">
                                                    <span class="fw-600 alt-font text-dark-gray">${property.bedroom}</span>
                                                </div>
                                                <span class="d-block lh-18 fs-15">Bedrooms</span> 
                                            </div>
                                            <div class="col">
                                                <div class="d-flex align-items-center">
                                                    <img src="{% static 'images/demo-real-estate-icon-bath-small.svg' %}" class="me-5px h-20px" alt="">
                                                    <span class="fw-600 alt-font text-dark-gray">${property.bathroom}</span>
                                                </div>
                                                <span class="d-block lh-18 fs-15">Bathrooms</span> 
                                            </div>
                                            <div class="col">
                                                <div class="d-flex align-items-center">
                                                    <img src="{% static 'images/demo-real-estate-icon-size-small.svg' %}" class="me-5px h-20px" alt="">
                                                    <span class="fw-600 alt-font text-dark-gray">${property.living_area}m<sup>2</sup></span>
                                                </div>
                                                <span class="d-block lh-18 fs-15">Living area</span> 
                                            </div>
                                        </div>
                                    </div>
                                    <div class="row ps-35px pe-35px pt-20px pb-20px md-ps-25px md-pe-25px align-items-center">
                                        <div class="col">
                                            <a href="demo-real-estate-property-details.html" class="btn btn-dark-gray btn-very-small btn-round-edge fw-600">View details</a>
                                        </div>
                                        <div class="col text-end">
                                            <span class="fs-24 alt-font text-dark-gray fw-700 mb-0">$${property.price}</span>
                                        </div> 
                                    </div>
                                </div>
                            </div>
                        </div>
                    `;
                }
            });
            $('#property-list').html(htmlContent);  // Updated ID
        },
        error: function(xhr, status, error) {
            console.error("Error fetching data: ", error);
        }
    });
});
