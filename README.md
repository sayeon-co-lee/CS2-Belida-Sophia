# Travel Fare Calculator

## Description
This program calculates the total travel fare based on the distance in kilometers and the number of passengers at a fixed rate.

## Version 1 - Original code without input validation
* Input: Accepts a passenger's name, distance in kilometers, and number of passengers.
* Process: Calculates the total fare by multiplying distance, passengers, and the fare rate.
* Output: Displays the passenger's name and the computed total fare in PHP.
* Note: Does not include input validation.

## Version 2 - Code with input validation
* Input: Accepts and validates a passenger's name (non-empty), distance in kilometers (greater than 0), and number of passengers (positive whole number).
* Process: Validates inputs using loops and error messages, then calculates the total fare by multiplying distance, passengers, and the fare rate.
* Output: Displays the passenger's name and the computed total fare in PHP.
* Validation Rules: Includes error handling and re-entry prompts for empty names, zero/negative distances, and non-integer or negative passenger counts.
