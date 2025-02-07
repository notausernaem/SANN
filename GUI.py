from kivy.lang import Builder

from kivymd.app import MDApp


KV = '''
MDScreenManager:

    MDScreen:
        name: "front_page"
        md_bg_color: "cadetblue"
        
        MDButton:
            pos_hint: {"center_x": .5,"center_y": .5}
            on_release:
                root.current = "first_input_page"

            MDButtonText:
                text: "Start"
                
                
    MDScreen:
        name: "first_input_page"
        md_bg_color: self.theme_cls.backgroundColor
        MDLabel:
            text: "Enter Duration(Days)"
            pos_hint: {"center_x": .75, "center_y": .69}
        MDLabel:
            text: "Enter Max People"
            pos_hint: {"center_x": .75, "center_y": .47}
            
        MDBoxLayout:
            orientation: "vertical"
            spacing: "80dp"
            adaptive_height: True
            size_hint_x: .5
            pos_hint: {"center_x": .5, "center_y": .6}
          
            MDSlider:
                id: duration_slider
    
                step: 1
                max: 30
                min:1
                value: 1
    
                MDSliderHandle:
    
                MDSliderValueLabel:
        MDBoxLayout:
            orientation: "vertical"
            spacing: "80dp"
            adaptive_height: True
            size_hint_x: .5
            pos_hint: {"center_x": .5, "center_y": .4}
          
            MDSlider:
                id: people_slider
    
                step: 1
                max: 15
                min:1
                value: 1
    
                MDSliderHandle:
    
                MDSliderValueLabel:
    
        MDButton:
            style: "outlined"
            pos_hint: {"center_x": .3, "center_y": .26}
            on_release:
                root.current = "front_page"
            MDButtonText:
                text: "Back"
                   
        MDButton:
            style: "filled"
            pos_hint: {"center_x": .42, "center_y": .26}
            on_press: app.save_values()
            MDButtonText:
                text: "Enter"

'''


class Example(MDApp):
    def save_values(self):
        duration = self.root.ids.duration_slider.value
        max_people = self.root.ids.people_slider.value

        print(f"Duration: {duration} days")
        print(f"Max People: {max_people}")

        self.duration = duration
        self.max_people = max_people

    def build(self):
        self.theme_cls.primary_palette = "Blue"
        return Builder.load_string(KV)


Example().run()
