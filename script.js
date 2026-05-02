// Smooth scrolling for navigation links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute('href'));
        if (target) {
            target.scrollIntoView({
                behavior: 'smooth',
                block: 'start'
            });
        }
    });
});

// Highlight active navigation link on scroll
window.addEventListener('scroll', () => {
    let current = '';
    
    const sections = document.querySelectorAll('section');
    sections.forEach(section => {
        const sectionTop = section.offsetTop;
        const sectionHeight = section.clientHeight;
        if (pageYOffset >= sectionTop - 200) {
            current = section.getAttribute('id');
        }
    });

    document.querySelectorAll('.nav-link').forEach(link => {
        link.classList.remove('active');
        if (link.getAttribute('href').slice(1) === current) {
            link.classList.add('active');
        }
    });
});

// Project data structure - you can populate this with your projects
const projects = {
    undergraduate: [
        {
            title: "Atmospheric Extinction",
            description: "Analysis of atmospheric extinction effects on stellar observations. This practical investigates how Earth's atmosphere absorbs and scatters light from stars, affecting observations at different wavelengths and altitudes. Uses observational data to determine extinction coefficients and atmospheric transparency.",
            tags: ["Python", "Data Analysis", "Astronomy", "Report"],
            pdf: "For_Website/Atmospheric_extincion/ATM-EXT3.pdf",
            code: ["For_Website/Atmospheric_extincion/Atmos.py"],
            folder: "For_Website/Atmospheric_extincion"
        },
        {
            title: "Bragg Reflection",
            description: "Study of X-ray diffraction and Bragg's law applied to crystal structures. This practical investigates the diffraction of X-rays by atomic planes in crystals, determining crystal parameters and spacing. Includes analysis of diffraction patterns and application of Bragg's law to various materials.",
            tags: ["Python", "X-ray Diffraction", "Crystallography", "Report"],
            pdf: "For_Website/Bragg_reflection/38655349_CA_Schoeman_XST.pdf",
            code: ["For_Website/Bragg_reflection/absorb.py", "For_Website/Bragg_reflection/bragg.py", "For_Website/Bragg_reflection/linear.py"],
            folder: "For_Website/Bragg_reflection"
        },
        {
            title: "Brewster's Angle and Polarization",
            description: "Investigation of polarization of light and Brewster's angle. This practical examines how light becomes polarized when reflected at specific angles, determining Brewster's angle for different surfaces and analyzing polarization states of light.",
            tags: ["Python", "Optics", "Polarization", "Report"],
            pdf: "For_Website/Brewsters_angle_and_Polarization/38655349_CA_Schoeman_POL.pdf",
            code: ["For_Website/Brewsters_angle_and_Polarization/resultsOne.py", "For_Website/Brewsters_angle_and_Polarization/resultsTwo.py", "For_Website/Brewsters_angle_and_Polarization/resultsThree.py"],
            folder: "For_Website/Brewsters_angle_and_Polarization"
        },
        {
            title: "Cosmic Rays",
            description: "Investigation of cosmic ray detection and analysis using advanced data processing techniques. This project analyzes cosmic ray events, their energy distributions, and arrival patterns. Multiple data processing scripts handle different aspects of cosmic ray event analysis and correlation.",
            tags: ["Python", "Data Processing", "Physics", "Report"],
            pdf: "For_Website/Cosmic_rays/Schoeman_38655349_KOS.pdf",
            code: ["For_Website/Cosmic_rays/dataStuff.py", "For_Website/Cosmic_rays/evenMoreData.py", "For_Website/Cosmic_rays/moreDataStuff.py"],
            folder: "For_Website/Cosmic_rays"
        },
        {
            title: "Diffraction and Slits",
            description: "Analysis of single and double slit diffraction patterns. This practical investigates diffraction phenomena using various slit configurations, measuring diffraction patterns and comparing with theoretical predictions. Includes analysis of intensity distributions and wavelength determination.",
            tags: ["Python", "Diffraction", "Optics", "Report"],
            pdf: "For_Website/Diffraction_and_slits/DIF_CA_SCHOEMAN_38655349.pdf",
            code: ["For_Website/Diffraction_and_slits/data.py"],
            folder: "For_Website/Diffraction_and_slits"
        },
        {
            title: "Electron Charge to Mass Ratio",
            description: "Determination of the electron charge-to-mass ratio using various experimental methods. This practical measures fundamental properties of electrons through deflection in electric and magnetic fields, calculating the e/m ratio and comparing with accepted values.",
            tags: ["Python", "Particle Physics", "Measurement", "Report"],
            pdf: "For_Website/Electron_charge_to_mass_ratio/38655349_CA_Schoeman_BEM.pdf",
            code: ["For_Website/Electron_charge_to_mass_ratio/data.py", "For_Website/Electron_charge_to_mass_ratio/linReg.py"],
            folder: "For_Website/Electron_charge_to_mass_ratio"
        },
        {
            title: "HiSPARC Cosmic Ray Detector",
            description: "Analysis of cosmic ray events using the HiSPARC detector network. This project processes event data from cosmic ray detectors, examining coincidence patterns between multiple detector stations. Includes data analysis of detector responses and event reconstruction.",
            tags: ["Python", "Detector Physics", "Data Analysis", "Report"],
            pdf: "For_Website/Hispark_cosmic_ray_detector/Report.pdf",
            code: ["For_Website/Hispark_cosmic_ray_detector/hisparc.py"],
            folder: "For_Website/Hispark_cosmic_ray_detector"
        },
        {
            title: "Numerical Methods",
            description: "Implementation and analysis of numerical methods for solving differential equations. This practical covers Euler's method and other numerical integration techniques, demonstrating their application to physics problems with comparative error analysis.",
            tags: ["Python", "Numerical Methods", "Computational Physics", "Report"],
            pdf: "For_Website/Numerical_Method/Schoeman_38655349_NUMMET.pdf",
            code: ["For_Website/Numerical_Method/euler.py", "For_Website/Numerical_Method/temp.py"],
            folder: "For_Website/Numerical_Method"
        },
        {
            title: "Solar Telescope",
            description: "Analysis of solar observations using telescope imagery. This project involves processing telescopic observations of the Sun, measuring solar features and their evolution. Includes photometric analysis and image processing techniques applied to solar data.",
            tags: ["Astronomy", "Image Analysis", "Solar Physics", "Report"],
            pdf: "For_Website/Solar_telescope/Schoeman_38655349.pdf",
            code: [],
            folder: "For_Website/Solar_telescope"
        },
        {
            title: "Spectral Lines",
            description: "Analysis of atomic spectral lines and emission spectra. This project identifies and characterizes spectral lines from various elements using spectroscopy techniques. Includes analysis of Helium, Hydrogen, Neon, and Sodium spectra to determine atomic properties and transitions.",
            tags: ["Python", "Spectroscopy", "Atomic Physics", "Report"],
            pdf: "For_Website/Spectal_lines/38655349_CA_Schoeman_SPK.pdf",
            code: ["For_Website/Spectal_lines/Helium.py", "For_Website/Spectal_lines/Hydrogen.py", "For_Website/Spectal_lines/Neon.py", "For_Website/Spectal_lines/SodiumData.py"],
            folder: "For_Website/Spectal_lines"
        },
        {
            title: "Statistical Fluctuations of Radioactive Substances",
            description: "Investigation of statistical fluctuations in radioactive decay events. This practical examines the statistical nature of radioactive decay, testing predictions of quantum mechanics and probability distributions. Includes analysis of near and far field measurements.",
            tags: ["Python", "Statistics", "Radioactivity", "Report"],
            pdf: "For_Website/Statistical_fluctuations_of_radioactive_substances/STATFLUX%20-%20Group%202.pdf",
            code: [],
            folder: "For_Website/Statistical_fluctuations_of_radioactive_substances"
        }
    ],
    honours: [
        // Waiting for honours projects
    ],
    ancillary: [
        // Waiting for ancillary projects
    ]
};

// Function to create and display project cards
function displayProjects(category, sectionId) {
    const grid = document.querySelector(`#${sectionId} .projects-grid`);
    const projectList = projects[category];

    if (projectList.length === 0) {
        grid.innerHTML = '<p style="grid-column: 1/-1; text-align: center; color: #5f6368;">Projects coming soon...</p>';
        return;
    }

    grid.innerHTML = projectList.map((project, index) => `
        <div class="project-card" onclick="navigateToProject('${category}', ${index})">
            <h3>${project.title}</h3>
            <p>${project.description}</p>
            <div class="project-tags">
                ${project.tags.map(tag => `<span class="tag">${tag}</span>`).join('')}
            </div>
        </div>
    `).join('');
}

// Function to navigate to project detail page
function navigateToProject(category, index) {
    const project = projects[category][index];
    const projectSlug = project.title.toLowerCase().replace(/\s+/g, '-').replace(/[()]/g, '');
    window.location.href = `project.html?category=${category}&index=${index}&slug=${projectSlug}`;
}

// Initialize projects on page load
document.addEventListener('DOMContentLoaded', () => {
    displayProjects('undergraduate', 'undergraduate');
    displayProjects('honours', 'honours');
    displayProjects('ancillary', 'ancillary');
});
