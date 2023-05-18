class FlexboxTutorialsUtils:

    dic = {
        "Default-Flexbox":"""<div class="d-flex bg-dark">
            \n<div class="text-white p-2 bg-success">Item 1</div>
            \n<div class="text-white p-2 bg-primary">Item 2</div>
            \n<div class="text-white p-2 bg-danger">Item 3</div>
        \n</div>""",

        "Justify-Content-Center": """<div class="d-flex justify-content-center bg-dark">
            \n<div class="text-white p-2 bg-success">Item 1</div>
            \n<div class="text-white p-2 bg-primary">Item 2</div>
            \n<div class="text-white p-2 bg-danger">Item 3</div>
        </div>""",

        "Justify-Content-Between": """<div class="d-flex justify-content-between bg-dark">
                \n<div class="text-white p-2 bg-success">Item 1</div>
                \n<div class="text-white p-2 bg-primary">Item 2</div>
                \n<div class="text-white p-2 bg-danger">Item 3</div>
            </div>""",

        "Justify-Content-Around": """<div class="d-flex justify-content-around bg-dark">
                    \n<div class="text-white p-2 bg-success">Item 1</div>
                    \n<div class="text-white p-2 bg-primary">Item 2</div>
                    \n<div class="text-white p-2 bg-danger">Item 3</div>
                </div>""",

        "Justify-Content-Around-Order": """<div class="d-flex justify-content-around bg-dark">
            \n<div class="text-white p-2 bg-success order-3">Item 1</div>
            \n<div class="text-white p-2 bg-primary order-1">Item 2</div>
            \n<div class="text-white p-2 bg-danger order-2">Item 3</div>
        \n</div>""",

    }

    def getCodeFromFlexboxTutorialName(self, tutorialName):
        return self.dic.get(tutorialName)