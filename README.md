# Northcliff SenseHat Level
This simple project uses a Raspberry Pi and a SenseHat as a two-dimensional level indicator.

It uses the SenseHat IMU to measure pitch and roll and then translates the pitch and roll into a two dimensional display on the SenseHat. The four centre pixels are set to white and the four corner pixels are set to red, when the SenseHat is level in both dimensions. The red pixels are extinguished and the white pixels shift as the SenseHat is tilted. Two corner pixels are set to red if the SenseHat is level in only one dimension.

The sensitivity of the level can be adjusted by changing the tilt_range variable.

## License

This project is licensed under the MIT License - see the LICENSE.md file for details
