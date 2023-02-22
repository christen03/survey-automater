# survey-automater
### Enter your survey code here and receive free food! 

 Thanks for checking out my survey automater! It's a work in progress, but I'm working hard on it and plan to have updates coming frequently. Soon, I hope to have this hosted and open to the public with a variety of survey bots! 

For now, it's stuck as a locally run, McDonald's only bot. 

### Important as this is locally run: 
This repo code is working with **Firefox.** If you want to work another browser, simply edit the `surveyfunctions.py` file.
In line 5, set `driver=webdriver.Firefox()` to:
- `driver=webdriver.Chrome()` for Google Chrome
- `driver=webdriver.Edge()` for Microsoft Edge
- `driver=webdriver.Safari()` for Safari
- `driver=webdriver.Ie()` for Internet Explorer
- `driver=webdriver.Opera()` for Opera

Thankfully running it is pretty easy, all you need is two installs:

``` 
pip install selenium
```
and 
```
pip install flask
```
Once you have those, simply run the `main.py` file. It will start a local server, (you can set the port to whatever you want in `main.py`), but for now it's at port 9000.

Then, simply go to `localhost:9000/` (or whatever your port is), type in your McDonald's survey code, and let the magic happen!

Thanks for checking out my automater, stay tuned for new updates such as error checking, customizable survey inputs, and new companies!