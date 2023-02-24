db.books.insert({
  'name':'Blink',
  'publishedDate':new Date(),
  'authors':[
    {'name':'Malcom Chadwell'},
    {'name':'Ghost Writer'}
  ]
});

db.books.insert({
  "name": "Blink",
  "publishedDate": new Date(),
  "authors": [
      { "name": "Malcolm Gladwell", "active": "true" },
      { "name": "Ghost Writer", "active": "true" }
  ]
});

db.books.find(
  {name:'Blink'},
  {
    publishedDate:1,
    name:1,
    'authors.name':1
  }
).pretty()

db.books.find({reviews:{$exits:true}})