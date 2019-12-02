class EBOOK():
    def __init__(self, title, author, pages_number):
        self.title = title
        self.author = author
        self.pages_number = pages_number
        self.current_page = 1
        self.is_open = False

    def open(self):
        self.is_open = True

    def close(self):
        self.is_open = False

    def next_page(self):
        if self.is_open:
            if self.current_page in range(1, self.pages_number):
                self.current_page += 1

    def previous_page(self):
        if self.is_open:
            if self.current_page in range(1, self.pages_number):
                self.current_page -= 1

    def read(self, pages):
        if self.is_open:
            if self.current_page in range(1, self.pages_number):
                for i in range(pages):
                    self.next_page()

    def show_current_page(self):
        if self.is_open:
            print(self.current_page)
