import os
import jinja2
import webapp2

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

videos_per_page = 2


class Page(webapp2.RequestHandler):
    page = 'new'
    template = 'index.html'
    videos = [
        "b6YVN9Uzxv0",  
        "zTaY3mg06sU",
        "HA-uK55c82s",
        "JZghx4GCs4k",
        "BHowDHk0GyM",    
        "xPhiDoUcito",   
        "-BlDJ8-9JRE",   
        "zFQuSXUul5I",    
        "hG5GOFUM1nI",   
        "FrrDmuQ1z5E",
        "obyBXbSjyTM",
        "R11FeM1J90U",
        "zjPh5O2tgpc",
        "GSPwplXhvok",
        "4nGHBtSJGzI",
        "QIsak4hWWio",
        "0C_ArE9TxmY",
        "_P7k4k8Ux4s",
        "Tfy1mOT-gEQ",
        "p2RyL8VRj2Y",
        "rXx5VXh4haQ",
        "kkVwR6JQdPI",
        "JY7umgfV8gg",
        "1tuzo8L55WE",
        "466cF1d5V_Q",
        "cm4Fz5c2Dk8",
        "3EyI0CVFv3E",
        "CZDDYFli108",
        "Ua1HTvvS8iw",
        "QCl08rOBsi8",
        "Nxk1g0kbjR4",
        "oTAVEHm69NA",
        "0HMGLvAVEWg",
        "gPPm1k90PBw",
        "Vr0Hs4EZK2g",
        "vRKpaaEGkwQ",
        "o5L91sXqt2g",
        "DEaSCs661h8",
        "By2xQhNViXc",
        "iXoLyn16-s0",
        "ZhZPONSX2XQ",
        "N2EU96xqEk4",
        "mQr3NFY1Y1I",
        "JTgbjLMwUEM",
        "kNc8NTiisUM",
        "BA_bbooO6eA",
        "QfFzqMwOaxQ",
        "yd7p029AGwI",
        "UJVxNfjwP-U",
        "E06yO0kPtis",
        "gRYSSNq5GSc",
        "fLN1aJVx4z4",
        "JbxC3hmr3bY",
        "hm1eL37gDGY",
        "gHlMReTpJXw",
        "tCnWGwn46tQ",
        "2PUVVXZLIrY"]
    
    def get(self):
        template_values = {'videos_per_page': videos_per_page,
                           'num_videos': len(self.videos),
                           'videos': self.videos,
                           'page': self.page}     
        template = JINJA_ENVIRONMENT.get_template(self.template)
        self.response.write(template.render(template_values))
        
        
class Basic(Page):
    page = 'basic'
    videos = ["rXx5VXh4haQ",
        "JZghx4GCs4k", 
        "BHowDHk0GyM",
        "-BlDJ8-9JRE",
        "zFQuSXUul5I",
        "hG5GOFUM1nI",
        "p2RyL8VRj2Y",
        "466cF1d5V_Q",
        "XUAGVToKgLo",
        "Nxk1g0kbjR4",
        "QCl08rOBsi8",
        "Ua1HTvvS8iw",
        "Vr0Hs4EZK2g",
        "DEaSCs661h8",
        "o5L91sXqt2g",
        "By2xQhNViXc",
        "mQr3NFY1Y1I",
        "N2EU96xqEk4",
        "ZhZPONSX2XQ",
        "iXoLyn16-s0",
        "kNc8NTiisUM",
        "JTgbjLMwUEM",
        "BA_bbooO6eA",
        "UJVxNfjwP-U",
        "gRYSSNq5GSc",
        "JjrRO_QrWtY",
        "tCnWGwn46tQ",
        "2PUVVXZLIrY"]

class Advanced(Page):
    page = 'advanced'
    videos = ["GSPwplXhvok", 
        "4nGHBtSJGzI",
        "QIsak4hWWio",
        "0C_ArE9TxmY",
        "Tfy1mOT-gEQ",
        "kkVwR6JQdPI",
        "JY7umgfV8gg",
        "1tuzo8L55WE",
        "cm4Fz5c2Dk8",
        "3EyI0CVFv3E",
        "CZDDYFli108",
        "JjrRO_QrWtY",
        "JbxC3hmr3bY",
        "hm1eL37gDGY",
        "gHlMReTpJXw"]

class Preschool(Page):
    page = 'preschool'
    videos = ["_P7k4k8Ux4s",   
        "HA-uK55c82s", 
        "xPhiDoUcito",
        "zjPh5O2tgpc",
        "obyBXbSjyTM",
        "FrrDmuQ1z5E",
        "R11FeM1J90U",
        "0HMGLvAVEWg",
        "gPPm1k90PBw",
        "vRKpaaEGkwQ",
        "QfFzqMwOaxQ",
        "hG5GOFUM1nI",
        "yd7p029AGwI",
        "E06yO0kPtis",
        "fLN1aJVx4z4",
        "JjrRO_QrWtY"]

class Art(Page):
    page = 'art'
    videos = ["0C_ArE9TxmY", 
        "vRKpaaEGkwQ",
        "JjrRO_QrWtY",
        "Yz36rUzLKh8",
        "Figiu_ldVFE",
        "GS9VSL__b6A",
        "BSfl1Xez_n0",
        "zbd-WPiSfp8",
        "e8wRr1ULx8A"]

class Literature(Page):
    page = 'literature'
    videos = ["p2RyL8VRj2Y", 
        "466cF1d5V_Q", 
        "Ua1HTvvS8iw", 
        "QCl08rOBsi8", 
        "Nxk1g0kbjR4", 
        "By2xQhNViXc"]

class Government(Page):
    page = 'government'    
    videos = ["hG5GOFUM1nI", 
        "kkVwR6JQdPI", 
        "JY7umgfV8gg", 
        "cm4Fz5c2Dk8", 
        "3EyI0CVFv3E", 
        "CZDDYFli108", 
        "UJVxNfjwP-U"]

class Geography(Page):
    page = 'geography'
    videos = ["xPhiDoUcito", 
        "-BlDJ8-9JRE",
        "zFQuSXUul5I",
        "rXx5VXh4haQ",
        "XUAGVToKgLo",
        "JTgbjLMwUEM",
        "kNc8NTiisUM",
        "BA_bbooO6eA",
        "UJVxNfjwP-U",
        "gRYSSNq5GSc",
        "fLN1aJVx4z4"]

class History(Page):
    page = 'history'
    videos = ["HA-uK55c82s", 
        "JZghx4GCs4k", 
        "BHowDHk0GyM", 
        "By2xQhNViXc"]

class Misc(Page):
    page = 'misc'
    videos = ["R11FeM1J90U",
        "QIsak4hWWio",
        "4nGHBtSJGzI",
        "GSPwplXhvok",
        "fH5-vGTgU4k",
        "oTAVEHm69NA",
        "0HMGLvAVEWg",
        "gPPm1k90PBw",
        "Vr0Hs4EZK2g",
        "hG5GOFUM1nI",
        "QfFzqMwOaxQ",
        "yd7p029AGwI",
        "tCnWGwn46tQ",
        "2PUVVXZLIrY"]
        
class Science(Page):
    page = 'science'
    videos = ["QIsak4hWWio",   
        "4nGHBtSJGzI",
        "GSPwplXhvok",
        "Tfy1mOT-gEQ", 
        "1tuzo8L55WE",
        "XUAGVToKgLo",
        "Vr0Hs4EZK2g",
        "DEaSCs661h8",
        "o5L91sXqt2g",
        "mQr3NFY1Y1I",
        "N2EU96xqEk4",
        "ZhZPONSX2XQ",
        "iXoLyn16-s0",
        "QfFzqMwOaxQ",
        "E06yO0kPtis",
        "gHlMReTpJXw",
        "hm1eL37gDGY",
        "JbxC3hmr3bY"]

class Letters(Page):
    page = 'letters'
    videos = ["zjPh5O2tgpc", 
        "obyBXbSjyTM", 
        "FrrDmuQ1z5E"]

class Popular(Page):
    #58
    page = 'popular'    
    videos = ["2PUVVXZLIrY", "gHlMReTpJXw"]

class Readingbear(Page):
    #18
    page = 'readingbear'    
    videos = ["fqXBcQFgh3Q", "H3HNcG7HhQc"]


class About(Page):
    template = 'about.html'
    page = 'about'     
    videos = []
        
        
app = webapp2.WSGIApplication([
    ('/', Page),

    ('/basic', Basic),    
    ('/advanced', Advanced),    
    ('/preschool', Preschool),    
    ('/art', Art), 
    ('/literature', Literature), 
    ('/government', Government), 
    ('/geography', Geography),   
    ('/history', History),    
    ('/misc', Misc),    
    ('/science', Science),   
    ('/26letters', Letters),   
    ('/popular', Popular),    
    ('/readingbear', Readingbear),   

    ('/about', About), 
    
]) #, debug=True)

