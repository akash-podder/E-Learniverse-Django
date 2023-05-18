class FlexboxTutorialsUtils:

    dic = {

        # HORIZONTAL Tutorials
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



        # VERTICAL Tutorials
        "Justify-Content-Start": """<div class="d-flex justify-content-start bg-dark" style="height: 100px;">
            \n<div class="text-white p-2 bg-success">Item 1</div>
            \n<div class="text-white p-2 bg-primary">Item 2</div>
            \n<div class="text-white p-2 bg-danger">Item 3</div>
        </div>""",

        "Align-Items-Start": """<div class="d-flex align-items-start bg-dark" style="height: 100px;">
            \n<div class="text-white p-2 bg-success">Item 1</div>
            \n<div class="text-white p-2 bg-primary">Item 2</div>
            \n<div class="text-white p-2 bg-danger">Item 3</div>
        </div>""",

        "Align-Items-End": """<div class="d-flex align-items-end bg-dark" style="height: 100px;">
                \n<div class="text-white p-2 bg-success">Item 1</div>
                \n<div class="text-white p-2 bg-primary">Item 2</div>
                \n<div class="text-white p-2 bg-danger">Item 3</div>
            </div>""",

        "Align-Items-Center": """<div class="d-flex align-items-center bg-dark" style="height: 100px;">
                    \n<div class="text-white p-2 bg-success">Item 1</div>
                    \n<div class="text-white p-2 bg-primary">Item 2</div>
                    \n<div class="text-white p-2 bg-danger">Item 3</div>
                </div>""",

        "Align-Items-Center-Justy-Content-Center": """<div class="d-flex align-items-center justify-content-center bg-dark" style="height: 100px;">
            \n<div class="text-white p-2 bg-success">Item 1</div>
            \n<div class="text-white p-2 bg-primary">Item 2</div>
            \n<div class="text-white p-2 bg-danger">Item 3</div>
        </div>""",

        "Justy-Content-No-Wrap": """<div class="d-flex justify-content-around flex-nowrap bg-dark">
            \n<div class="text-white p-2 bg-success">Item 1</div>
            \n<div class="text-white p-2 bg-primary">Item 2</div>
            \n<div class="text-white p-2 bg-danger">Item 3</div>
            \n<div class="text-white p-2 bg-success">Item 1</div>
            \n<div class="text-white p-2 bg-primary">Item 2</div>
            \n<div class="text-white p-2 bg-danger">Item 3</div>
        </div>""",

        "Justy-Content-Wrap": """<div class="d-flex justify-content-around flex-wrap bg-dark">
                \n<div class="text-white p-2 bg-success">Item 1</div>
                \n<div class="text-white p-2 bg-primary">Item 2</div>
                \n<div class="text-white p-2 bg-danger">Item 3</div>
                \n<div class="text-white p-2 bg-success">Item 1</div>
                \n<div class="text-white p-2 bg-primary">Item 2</div>
                \n<div class="text-white p-2 bg-danger">Item 3</div>
            </div>""",
    }

    def getCodeFromFlexboxTutorialName(self, tutorialName):
        return self.dic.get(tutorialName)