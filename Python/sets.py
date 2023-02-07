tags_one = {
  'python',
  'coding',
  'tutorials',
  'coding'
}

tags_two = {
  'ruby',
  'coding',
  'tutorials',
  'development'
}

#fusionar los 2 sets
""" merged_tags=tags_one | tags_two

print(merged_tags) """

#tags en tags_one pero no en tags_two (exclusivas de tags_one)
exclusive_tags_one=tags_one-tags_two
print(exclusive_tags_one)

#tags que están en los 2 sets (compartidos)
universal_tags=tags_one & tags_two
print(universal_tags)

