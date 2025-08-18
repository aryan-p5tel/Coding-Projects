# Car Wash Simulation GUI

## Overview

The **Car Wash Simulation GUI** is an interactive desktop application built using Python’s `tkinter` library. This project was designed as my first exploration into GUI programming and simulation creation. It allows users to simulate selecting a car type, service level, optional extras, tipping, and even changing currencies while dynamically calculating the total price of their car wash service.

This project demonstrates a practical application of programming concepts learned from [CSNewbs](https://www.youtube.com/@CSNewbs) tutorials and other online resources, combining GUI design, variable management, event-driven programming, and real-time updates in Python.

---

## Features

### 1. Vehicle Selection
Users can select between **Bike**, **Car**, or **Truck**. Each vehicle type has a different base price:
- **Bike**: £10
- **Car**: £16
- **Truck**: £40
##
### 2. Service Level Selection
After choosing a vehicle, users can select the type of service:
- **Exterior Only** – no additional cost
- **Interior + Exterior** – adds £5
- **Premium** – adds £20

The service selection updates the total price accordingly after the "Final Price" button is clicked.
##
### 3. Extras
Users can add optional extras:
- **Waxing** (£5)
- **Drying** (£3)
- **Polishing** (£10)

Extras are optional and can be toggled independently. Their costs are automatically included in the total once finalized.
##
### 4. Tip Feature
The application includes a **tip adjustment system**:
- Users can increase or decrease the tip using `+` and `-` buttons.
- The tip value is automatically updated in the currently selected currency.
- Tip changes do **not** update the total price in real-time until the "Final Price" button is clicked for the first time.
##
### 5. Currency Conversion
A currency selector is available at the top of the GUI, allowing users to choose between:
- **GBP** (£)
- **EUR** (€)
- **USD** ($)

Key functionalities:
- The base price, service, and extras are converted to the selected currency using current exchange rates.
- The tip is always incremented by 1 in the chosen currency (not converted from GBP).
- After the total has been finalized, switching currencies will **convert the final price to the new currency** automatically.
##
### 6. Real-Time Updates After Finalization
Once the "Final Price" button is clicked:
- Any further changes to the vehicle, service, extras, tip, or currency immediately update the total price in real time.
- This feature demonstrates an **event-driven programming approach**, allowing dynamic updates based on user interaction.

---

## How It Works

The application is built with Python’s `tkinter` library, using the following structure:

1. **Variables** – Tracks vehicle choice, service type, extras selection, tip, currency, and the final price.
2. **Option Menus and Checkbuttons** – Allow the user to select vehicle type, service, and extras.
3. **Tip Buttons** – Provide simple + and - functionality for the tip, updating the total after finalization.
4. **Final Price Button** – Triggers the calculation and display of the total price based on all selections.
5. **Real-Time Updates** – A flag (`final_clicked`) enables automatic updates for all changes once the final price has been calculated.
6. **Currency Handling** – Conversion rates are applied to the base price, services, and extras, while the tip is adjusted in the selected currency.

---

## Learning Journey

This project represents my **first GUI simulation** after learning Python GUI programming through online tutorials such as CSNewbs on YouTube. It was an exercise in integrating multiple features, managing dynamic variables, and implementing real-time interactive updates. It also helped me understand:
- How to structure a GUI application professionally
- How to handle variable updates and event-driven programming
- How to incorporate real-world concepts like currency conversion and tipping into a simulation

Despite being an early project, it demonstrates a clear understanding of programming logic, interface design, and user interaction — skills highly relevant for further academic or professional development.

---

## Future Improvements

While functional, the application could be extended with:
- Persistent storage for past transactions
- Advanced pricing algorithms for promotional discounts
- More sophisticated UI designs using `ttk` or other GUI frameworks
- Graphical representations of services chosen or total price changes over time

---

## Technologies Used

- **Python 3**
- **Tkinter** (built-in GUI library)
- Guidance from **CSNewbs YouTube tutorials**

---
- ## Screenshot

<img width="742" height="777" alt="image" src="https://github.com/user-attachments/assets/205534e0-8fe9-412b-a465-34086bee12f9" />


*(Replace `path-to-your-screenshot.png` with the actual file path of your screenshot)*

---

## Conclusion

This project showcases the integration of GUI design, interactive user input, real-time updates, and dynamic pricing with currency conversion. While created as a learning exercise, it is fully functional, demonstrates careful coding structure, and can be further expanded into more advanced simulations. This project is a strong example of my ability to learn and apply new programming concepts effectively and creatively — qualities appealing to both universities and potential employers.

---

