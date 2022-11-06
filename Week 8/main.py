from html import Tag

tag = Tag('simpleTag', 'simpleContent')
tag.temp = 10

tag._temp = 23
tag.__test = 59

# tag.set_temp(68)

tag.tempVariable = 634
print(tag.tempVariable)
print('=' * 40)

tag.sampleString = 'Dayche Python Class'
print(tag.sampleString)
del tag.sampleString
print('=' * 40)
print(globals())
print(tag.__dict__)




