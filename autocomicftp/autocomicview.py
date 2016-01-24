import math
import autocomicftp.exceptions

class AutocomicView(object):

    def __init__(self, comic, columns=3):
        self.comic = comic
        self.columns = columns
        self.rows = math.ceil( len(comic.panels) / columns )

    def prepare_layout(self):
        self.layout = self._layout()
        
    def _layout(self):        

        layout = []
        try:
            for row in range(self.rows):
                row_layout = []
                for column in range(self.columns):
                    panel  = self.comic.panels[row*self.columns + column]
                    row_layout.append((panel.art, panel.text))
                if not row_layout:
                    raise autocomicftp.exceptions.EmptyComicLayout()
                layout.append(row_layout)
        except IndexError:
            if row_layout:
                layout.append(row_layout)
        
        if not layout:
            raise autocomicftp.exceptions.EmptyComicLayout()

        return layout

    def __getattr__(self, attribute):
        return getattr(self.comic, attribute)


   #layout = [[ getattr(self.comic.panels[j*self.columns + i], type) for i in range(self.columns) ] 
                #for j in range(self.rows)]
