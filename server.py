{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "2739761b-deec-4c9b-8b7e-e78dd3715c73",
   "metadata": {},
   "outputs": [],
   "source": [
    "from machinetranslation import translator\n",
    "from flask import Flask, render_template, request\n",
    "import json\n",
    "\n",
    "app = Flask('Web Translator')\n",
    "\n",
    "@app.route('/englishToFrench')\n",
    "def englishToFrench():\n",
    "    textToTranslate = request.args.get('textToTranslate')\n",
    "    frenchText = translator.english_to_french(textToTranslate)\n",
    "    return frenchText\n",
    "\n",
    "@app.route('/frenchToEnglish')\n",
    "def frenchToEnglish():\n",
    "    textToTranslate = request.args.get('textToTranslate')\n",
    "    englishText = translator.french_to_english(textToTranslate)\n",
    "    return englishText\n",
    "\n",
    "\n",
    "@app.route('/')\n",
    "def renderIndexPage():\n",
    "    return render_template('index.html')\n",
    "\n",
    "if __name__ == '__main__':\n",
    "    app.run(port=8000)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python",
   "language": "python",
   "name": "conda-env-python-py"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.12"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
