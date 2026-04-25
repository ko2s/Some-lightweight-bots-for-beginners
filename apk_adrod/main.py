from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.filechooser import FileChooserListView
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.popup import Popup
from moviepy.editor import VideoFileClip
import os

class VideoEditorApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')
        
        self.file_chooser = FileChooserListView()
        self.file_chooser.path = os.path.expanduser('~')
        layout.add_widget(self.file_chooser)
        
        self.select_button = Button(text='اختيار الفيديو')
        self.select_button.bind(on_press=self.show_file_chooser)
        layout.add_widget(self.select_button)

        self.info_label = Label(text='')
        layout.add_widget(self.info_label)

        self.cut_start_input = TextInput(hint_text='وقت البداية بالثواني')
        layout.add_widget(self.cut_start_input)

        self.cut_end_input = TextInput(hint_text='وقت النهاية بالثواني')
        layout.add_widget(self.cut_end_input)
        
        self.convert_button = Button(text='تحويل الفيديو')
        self.convert_button.bind(on_press=self.convert_video)
        layout.add_widget(self.convert_button)

        return layout

    def show_file_chooser(self, instance):
        filechooser_popup = Popup(title='اختر ملف الفيديو', content=self.file_chooser,
                                  size_hint=(0.9, 0.9))
        filechooser_popup.open()

    def convert_video(self, instance):
        selected_files = self.file_chooser.selection
        if not selected_files:
            self.info_label.text = 'لم يتم اختيار أي ملف.'
            return

        input_path = selected_files[0]
        output_path = os.path.splitext(input_path)[0] + '_converted.mp4'
        
        start_time = float(self.cut_start_input.text) if self.cut_start_input.text else None
        end_time = float(self.cut_end_input.text) if self.cut_end_input.text else None

        try:
            clip = VideoFileClip(input_path)
            if start_time is None and end_time is None:
                clip.write_videofile(output_path, codec='libx264')
            else:
                if start_time is None:
                    start_time = 0
                if end_time is None:
                    end_time = clip.duration
                new_clip = clip.subclip(start_time, end_time)
                new_clip.write_videofile(output_path)
            self.info_label.text = f'تم تحويل الفيديو إلى {output_path}'
        except Exception as e:
            self.info_label.text = f'حدث خطأ: {e}'

if __name__ == '__main__':
    VideoEditorApp().run()
