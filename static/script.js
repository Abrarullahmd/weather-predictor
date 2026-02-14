document.addEventListener("DOMContentLoaded", function () {
  const tabBtns = document.querySelectorAll(".tab-btn");
  const locationOptionInput = document.getElementById("location-option");
  const coordsInputGroup = document.getElementById("coords-input-group");
  const manualInputGroup = document.getElementById("manual-input-group");
  const latitudeInput = document.getElementById("latitude");
  const longitudeInput = document.getElementById("longitude");
  const locationNameInput = document.getElementById("location-name");
  const inputScreen = document.getElementById("input-screen");
  const forecastScreen = document.getElementById("forecast-screen");

  // Tab switching logic
  tabBtns.forEach((btn) => {
    btn.addEventListener("click", function () {
      // Update active tab UI
      tabBtns.forEach((b) => b.classList.remove("active"));
      this.classList.add("active");

      const selected = this.getAttribute("data-value");
      locationOptionInput.value = selected;

      // Handle input group visibility
      if (selected === "coords") {
        coordsInputGroup.classList.remove("hidden");
        manualInputGroup.classList.add("hidden");
      } else if (selected === "manual") {
        coordsInputGroup.classList.add("hidden");
        manualInputGroup.classList.remove("hidden");
      } else if (selected === "auto") {
        coordsInputGroup.classList.add("hidden");
        manualInputGroup.classList.add("hidden");
        getCurrentLocation();
      }
    });
  });

  function getCurrentLocation() {
    if (navigator.geolocation) {
      navigator.geolocation.getCurrentPosition(
        function (position) {
          latitudeInput.value = position.coords.latitude.toFixed(4);
          longitudeInput.value = position.coords.longitude.toFixed(4);
        },
        function (error) {
          alert("Error fetching location. Please enter manually.");
        }
      );
    } else {
      alert("Geolocation is not supported by your browser.");
    }
  }

  window.fetchCoordsFromLocation = function () {
    const locationName = locationNameInput.value;
    if (!locationName) {
      alert("Please enter a location.");
      return;
    }

    fetch(
      `https://nominatim.openstreetmap.org/search?format=json&q=${locationName}`
    )
      .then((response) => response.json())
      .then((data) => {
        if (data.length > 0) {
          latitudeInput.value = parseFloat(data[0].lat).toFixed(4);
          longitudeInput.value = parseFloat(data[0].lon).toFixed(4);
          // After getting coords, show them
          coordsInputGroup.classList.remove("hidden");
        } else {
          alert("Location not found. Please try again.");
        }
      })
      .catch((error) => {
        alert("Error fetching coordinates.");
      });
  };

  window.showInputScreen = function () {
    if (forecastScreen) {
      forecastScreen.classList.add("hidden");
    }
    inputScreen.classList.remove("hidden");
    // Optionally reset the form or scroll to top
    window.scrollTo(0, 0);
  };
});
