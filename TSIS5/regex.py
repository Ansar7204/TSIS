import re




file_content = "Aab Aabb, a jbcddsf_sdfa,bbbb   AbcAbcAbc"


pattern = 'ab*' # a followed by zero or more b's
matches = re.findall(pattern, "a ab abbb acdcsdc")
print(matches)


pattern2 = 'ab{2,3}'# a followed by two to three b
matches = re.findall(pattern2, "ab a abb abbb abbbbbb")
print(matches)


pattern3 = '[a-z]+_[a-z]+'#lowercase joined by underscore
matches = re.findall(pattern3, "dsfasdf asdfasdf sadf_dfsdf ASdas_ASDa")
print(matches)


pattern4 ='[A-Z][a-z]+'#one uppercase followed by lowercase letters
matches = re.findall(pattern4, "Afsdfc fsdjhbch Bcdjdj")
print(matches)


pattern5 = 'a.*b'# a followed by anything and ending with b
matches = re.findall(pattern5, "ajgkjsdfb asdfsdfkjs badfa")
print(matches)


print(re.sub("[ ,.]", ":", file_content)) #space,dot,comma to colon


def snake_to_camel(word):
        return ''.join(x.capitalize() or '_' for x in word.split('_')) 
print(snake_to_camel("abcd_abcd"))

pattern6 = '[A-Z][^A-Z]*' #split at uppercase letters
matches = re.findall(pattern6, "AbcdEfghIjkl")
print(matches)


print(re.sub(r"(\w)([A-Z])", r"\1 \2", "AbcAbcGcdfhASdf")) #insert spaces between words starting with capitals


def camel_to_snake(text):
        str1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', text).lower()
        return str1
    
print(camel_to_snake("AbcdAvccc"))