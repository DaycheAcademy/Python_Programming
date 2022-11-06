
# top-down
# bottom-up
import sys


class Tag(object):

    def __init__(self, n, c, **att):
        self.name = n
        self.start_tag = '<{}>'.format(n)
        self.end_tag = '</{}>'.format(n)
        self.content = c
        self.attributes = list()
        if att:
            for k in att:
                self.attributes.append(f'{str(k)}="{att[k]}"')

    def __str__(self):  # str()
        if self.attributes:
            att = ' '.join(self.attributes)
            self.start_tag = '<{} {}>'.format(self.name, att)
        return '{0.start_tag}{0.content}{0.end_tag}'.format(self)

    def display(self, dump=False, file=None):
        if dump:
            print(self)
        if file:
            print(self, file=file)
        return str(self)


class DocType(Tag):

    def __init__(self, version=5):

        if version == 1:
            name = '!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.1//EN" ' \
                   '"http://www.w3.org/TR/xhtml11/DTD/xhtml11.dtd"'
        elif version == 4:
            name = '!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" ' \
                   '"http://www.w3.org/TR/html4/loose.dtd"'
        elif version == 5:
            name = '!DOCTYPE html'
        else:
            print('HTML Version is not accepted')
            sys.exit(-1)
        super().__init__(n=name, c='')
        self.end_tag = ''

    # def display(self):
    #     pass


class Head(Tag):

    def __init__(self):
        super().__init__(n='head', c='\n')
        self.head_contents = list()

    # def __init__(self, name='head', content=''):
    #     super().__init__(name=name, content=content)

    def add_content(self, n, c, single=False, **att):
        # add contents to self.head_contents
        new_tag = Tag(n=n, c=c, **att)
        if single:
            new_tag.content = ''
            new_tag.end_tag = ''
        self.head_contents.append(str(new_tag))

    def display(self, dump=False, file=None):
        for item in self.head_contents:
            self.content += item + '\n'
        # self.content = '\n'.join(self.head_contents)
        super().display(dump=dump, file=file)
        return str(self)


class Body(Tag):

    def __init__(self):
        super().__init__(n='body', c='\n')
        self.body_contents = list()

    @staticmethod
    def define_child(n, c, single=False, child=None, **att):
        new_tag = Tag(n=n, c=c, **att)
        if single:
            new_tag.content = ''
            new_tag.end_tag = ''
        if child:
            for ch in child:
                new_tag.content += '\n\t' + ch
                new_tag.end_tag = '\n' + new_tag.end_tag
        return str(new_tag)

    def add_content(self, n, c, single=False, child=None, **att):
        # add contents to self.body_contents
        new_tag = Tag(n=n, c=c, **att)
        if single:
            new_tag.content = ''
            new_tag.end_tag = ''
        if child:
            for ch in child:
                new_tag.content += '\n' + ch
                new_tag.end_tag = '\n' + new_tag.end_tag
        self.body_contents.append(str(new_tag))

    def display(self, dump=False, file=None):
        for item in self.body_contents:
            self.content += item + '\n'
        # self.content = '\n'.join(self.head_contents)
        super().display(dump=dump, file=file)
        return str(self)


class Html(object):

    def __init__(self, version=5):
        self.doc = DocType(version=version)
        self.head = Head()
        self.body = Body()

    # Delegation
    def add_content(self, n, c, single=False, child=None, section='body', **att):
        if section.lower() == 'head':
            if child:
                raise NotImplementedError('Head section may not contain any child')
            else:
                self.head.add_content(n=n, c=c, single=single, **att)
        elif section.lower() == 'body':
            self.body.add_content(n=n, c=c, single=single, child=child, **att)
        else:
            raise NotImplementedError('Selected section is not supported')

    def define_child(self, n, c, single=False, child=None, **att):
        return self.body.define_child(n=n, c=c, single=single, child=child, **att)

    def display(self, dump=False, file='index.html'):
        new_tag = Tag('html', '\n')
        if dump:
            self.doc.display(dump=True)
            new_tag.content += self.head.display(dump=False) + '\n'
            new_tag.content += self.body.display(dump=False) + '\n'
            print(str(new_tag))

        if file:
            with open(file, 'a+') as h_file:
                self.doc.display(dump=False, file=h_file)
                new_tag.content += self.head.display(dump=False) + '\n'
                new_tag.content += self.body.display(dump=False) + '\n'
                print(str(new_tag), file=h_file)


if __name__ == '__main__':

    html = Html(version=5)
    html.add_content('meta', '', single=True, section='head', charset='utf-8')
    html.add_content('meta', '', single=True, section='head', name='viewport', content="width=device-width, initial-scale=1")
    html.add_content('meta', '', single=True, section='head', name="generator", content="Hugo 0.98.0")
    html.add_content('title', 'Dayche datasience class', section='head')
    a1 = html.define_child('a', 'Skip to main content', Class='d-inline-flex p-2 m-1', href="#content")
    div1 = html.define_child('div', '', child=(a1,), id="container")
    html.add_content('div', '', child=(div1,), Class="container-xl")
    html.add_content('h1', 'Welcome to Dayche Python Class')
    html.add_content('h2', 'You are Viewing HTML File')
    html.display()






    # simpleTag = Tag('myTag', 'Simple Content', id='myID', Class='navbar-nav')
    # htmlHead = Head()
    # htmlHead.add_content('meta', '', single=True, charset='utf-8')
    # htmlHead.add_content('meta', '', single=True, name='viewport', content="width=device-width, initial-scale=1")
    # htmlHead.add_content('meta', '', single=True, name="generator", content="Hugo 0.98.0")
    # htmlHead.add_content('title', 'Dayche datasience class')
    # htmlHead.display()

    # < meta charset = "utf-8" >
    # < meta name = "viewport" content = "width=device-width, initial-scale=1" >
    # < meta name = "generator" content = "Hugo 0.98.0" >
    # <title>Dayche datasience class</title>

    # htmlBody = Body()
    # a1 = htmlBody.define_child('a', 'Skip to main content', Class='d-inline-flex p-2 m-1', href="#content")
    # div1 = htmlBody.define_child('div', '', child=(a1,), id="container")
    # htmlBody.add_content('div', '', child=(div1,), Class="container-xl")
    # htmlBody.display()

    # <div class ="container-xl">
    #     <div id="container">
    #         <a class ="d-inline-flex p-2 m-1" href="#content" >Skip to main content</a>
    #     </div>
    # </div>



    # simpleTag.display()

    # doc = DocType(3)
    # doc.display()




