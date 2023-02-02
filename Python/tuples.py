#la tupla
post = ('Python Basics', 'published','Intro guide to python', 'Some cool python content')

#quitar un ele. desde el final

post=list(post)
post.remove('published')
post=tuple(post)
#print(post)


#tupla como key de un dictionary
priority_index = {
  (1, 'premier'): [1, 34, 12],
  (1, 'mvp'): [84, 22, 24],
  (2, 'standard'): [93, 81, 3],
}

print(list(priority_index.keys()))