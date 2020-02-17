
n = int(input('Введите число n:'))
data = [
  {
    "id": 59,
    "name": "Cristina Mcleod",
    "gender": "female"
  },
  {
    "id": 61,
    "name": "Yvette Wagner",
    "gender": "female"
  },
  {
    "id": 74,
    "name": "Harding Anthony",
    "gender": "male"
  },
  {
    "id": 69,
    "name": "Levine Morales",
    "gender": "male"
  },
  {
    "id": 16,
    "name": "Francine Cooper",
    "gender": "female"
  },
  {
    "id": 55,
    "name": "Schultz Valentine",
    "gender": "male"
  },
  {
    "id": 99,
    "name": "Oneill Sanchez",
    "gender": "male"
  },
  {
    "id": 99,
    "name": "Sanford Hampton",
    "gender": "male"
  },
  {
    "id": 71,
    "name": "Edith Vinson",
    "gender": "female"
  },
  {
    "id": 42,
    "name": "Herrera Bass",
    "gender": "male"
  },
  {
    "id": 56,
    "name": "Summer Todd",
    "gender": "female"
  },
  {
    "id": 78,
    "name": "Lottie Talley",
    "gender": "female"
  },
  {
    "id": 37,
    "name": "Lucy Rutledge",
    "gender": "female"
  },
  {
    "id": 12,
    "name": "Cleveland Holman",
    "gender": "male"
  },
  {
    "id": 33,
    "name": "Rae Mason",
    "gender": "female"
  },
  {
    "id": 42,
    "name": "Donovan Paul",
    "gender": "male"
  },
  {
    "id": 19,
    "name": "Francis Sharpe",
    "gender": "female"
  },
  {
    "id": 19,
    "name": "Sparks Wilkerson",
    "gender": "male"
  },
  {
    "id": 30,
    "name": "Hall Sexton",
    "gender": "male"
  },
  {
    "id": 65,
    "name": "Doris Harrison",
    "gender": "female"
  }
]
y = 0
quantity = 0
for item in data:
  y = item.get('id') % n
  if y == 0:
    print(item.get('name'))
for item in data:
  gender_ = item.get('gender')
  if gender_ == 'female':
    quantity += 1
print(f'Количество людей женского пола: {quantity}')
