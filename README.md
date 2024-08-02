
# CPT Generator

This Project allows you to create CPT File formats for colormaps to use in plotting frameworks such as Panoply or Python frameworks like Matplotlib in runtime, it uses an interactive interface made with tkinter
![image](https://github.com/user-attachments/assets/6dbc0777-8602-4219-b49a-847f5c1e7be3)


# Usage

Install colorgen.py in any directory you like and import the ColorToolApp class from it

```python
from colorgen import ColorToolApp #Import the class
CPTGen = ColorToolApp() #Create an instance
CPTGen.mainloop() #Run The Interface
print(CPTGen)

#Output Will be a CPT format of what you have chose and created inside the app,
#To save it as a variable click on "Save CPT As Class __str__" or click on Save As CPT To save it as a file.
```

# Examples
Check [These 2 Notebook examples using matplotlib](https://github.com/Mohameme7/CPT-Generator/tree/master/examples)


# Credits
This project is completely inspired by Mr. Khalid-Al-Otaibi or [@AlJareerMJO](https://x.com/AljareerMJO) on twitter,
I got the idea from one of the inventions he made on his website and reinvented the wheel with Python and made it as a usable framework, [Check Out his website](https://www.madden-julian-oscillation.com/researchers-tools.html#)
