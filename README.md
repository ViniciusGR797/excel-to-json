# Excel to Json

<div align="center">
  <img alt="GitHub repo size" src="https://img.shields.io/github/repo-size/ViniciusGR797/excel-to-json?style=for-the-badge">
  <img alt="GitHub language count" src="https://img.shields.io/github/languages/count/ViniciusGR797/excel-to-json?style=for-the-badge">
  <img alt="GitHub forks" src="https://img.shields.io/github/forks/ViniciusGR797/excel-to-json?style=for-the-badge">
  <img alt="Bitbucket open issues" src="https://img.shields.io/bitbucket/issues/ViniciusGR797/excel-to-json?style=for-the-badge">
  <img alt="Bitbucket open pull request" src="https://img.shields.io/bitbucket/pr-raw/ViniciusGR797/excel-to-json?style=for-the-badge">
</div>

<div align="center">
  <img src="https://cdn.discordapp.com/attachments/1089358473483006105/1089358536728924230/excel-to-json.png?ex=661b2fb2&is=6608bab2&hm=431684c92e3cd6347456416e8efad1cdabbed105030b6f8a40797ade0579ffe0&" alt="logo HappyFit">
</div>
  
> This Python software is capable of converting Excel files into JSON objects. Using the Pandas library, data is read from an Excel file and then converted into a dictionary which is, in turn, transformed into a JSON object. This process is useful for integrating Excel spreadsheet data into web applications and other software solutions.

## 🐍 How to use with virtual environment (recommended)

This tutorial is designed for Windows users with a PowerShell terminal:
* Clone this repository through the terminal.
```
git clone https://github.com/ViniciusGR797/excel-to-json.git
```

* Place your Excel file you want to convert in place of 'test.xlsx', change the code by putting the name of your Excel file in the variable 'filename' and put the name of the Json file you want to get in the variable 'json_filename'. For example I have the file 'school.xlsx', I replace the file, I put the following values in the variables:

```
filename = 'school.xlsx'
json_filename = 'school.json'
```

* Activate the virtual environment through the terminal, you will notice that '(env)' appears.
```
.\env\Scripts\activate
```

* Run the program through the terminal.
```
python app.py
```

* Deactivate the virtual environment through the terminal, you will notice that '(env)' will be gone.
```
deactivate
```

That's it, you've successfully converted Excel to Json.

## 🐍 How to use locally on your machine

If you don't want to use a virtual environment and use your own machine's environment:

* Remembering that you need to have downloaded Python, if you haven't.

* Repeat the previous steps, the difference is that you don't need to activate or deactivate the virtual environment, just download the dependencies through the terminal after cloning the repository.
```
pip install -r requirements.txt
```

## 📝 Licença

Esse projeto está sob licença. Veja o arquivo [LICENÇA](LICENSE) para mais detalhes.
