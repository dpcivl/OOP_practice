객체 지향 프로그래밍(OOP)을 연습하기 위한 파이썬 과제로, 다양한 OOP 개념을 적용할 수 있는 예제를 만들어 드리겠습니다. 각 과제는 **클래스, 상속, 다형성, 캡슐화, 추상화** 등의 개념을 다룹니다. 아래 과제들을 통해 객체 지향의 기본 원리를 익힐 수 있을 것입니다.

### 과제 1: 도서관 관리 시스템
**목표**: 클래스 설계, 객체 간 상호작용, 상속

#### 요구사항:
1. `Book` 클래스: 책을 나타내는 클래스입니다.
   - 속성: 제목(`title`), 저자(`author`), ISBN 번호(`isbn`), 상태(`status`: 대출 중인지 여부)
   - 메서드: 책 대출(`borrow`), 반납(`return_book`)
   
2. `Library` 클래스: 도서관을 나타내는 클래스입니다.
   - 속성: 책 리스트(`books`), 도서관 이름(`name`)
   - 메서드:
     - `add_book(book: Book)`: 책을 도서관에 추가
     - `borrow_book(isbn: str)`: ISBN 번호로 책을 찾아 대출
     - `return_book(isbn: str)`: ISBN 번호로 책을 찾아 반납
     - `list_available_books()`: 대출 가능한 책 목록 출력

3. `User` 클래스: 도서관 이용자를 나타내는 클래스입니다.
   - 속성: 이름(`name`), 대출한 책 목록(`borrowed_books`)
   - 메서드:
     - `borrow(book: Book)`: 사용자가 책을 대출
     - `return_book(book: Book)`: 사용자가 책을 반납

#### 구현해야 할 기능:
- 책을 추가하고, 대출 및 반납하는 기능을 구현합니다.
- 대출 중인 책은 다시 대출할 수 없게 처리해야 합니다.

#### 힌트:

```python
class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.status = 'available'
    
    def borrow(self):
        if self.status == 'available':
            self.status = 'borrowed'
            print(f"{self.title} has been borrowed.")
        else:
            print(f"{self.title} is currently unavailable.")
    
    def return_book(self):
        if self.status == 'borrowed':
            self.status = 'available'
            print(f"{self.title} has been returned.")
        else:
            print(f"{self.title} was not borrowed.")
```

### 과제 2: 동물원 관리 시스템
**목표**: 상속, 다형성, 메서드 오버라이딩

#### 요구사항:
1. `Animal` 클래스 (추상 클래스): 모든 동물의 기본 클래스로 사용됩니다.
   - 속성: 이름(`name`), 나이(`age`), 동물 종류(`species`)
   - 메서드:
     - `make_sound()`: 동물 소리를 출력 (추상 메서드)
     - `move()`: 기본적으로 '움직입니다' 출력

2. `Lion`, `Elephant`, `Penguin` 클래스: 각각 `Animal` 클래스를 상속받습니다.
   - 메서드:
     - `make_sound()`: 각 동물의 소리를 출력하도록 오버라이딩
     - `move()`: 각 동물의 움직임을 다르게 오버라이딩

3. `Zoo` 클래스: 동물들을 관리하는 클래스입니다.
   - 속성: 동물 리스트(`animals`)
   - 메서드:
     - `add_animal(animal: Animal)`: 동물을 동물원에 추가
     - `make_all_sounds()`: 동물원에 있는 모든 동물의 소리를 출력

#### 구현해야 할 기능:
- 동물들의 소리와 움직임을 상속과 다형성을 활용해 구현합니다.
- 추상 클래스를 활용하여 `Animal`의 기본적인 행동을 정의하고, 각 동물마다 다른 소리를 내도록 합니다.

#### 힌트:

```python
from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @abstractmethod
    def make_sound(self):
        pass

    def move(self):
        print(f"{self.name} is moving.")

class Lion(Animal):
    def make_sound(self):
        print("Roar!")

class Elephant(Animal):
    def make_sound(self):
        print("Trumpet!")

class Penguin(Animal):
    def make_sound(self):
        print("Squawk!")
    
    def move(self):
        print(f"{self.name} is waddling.")
```

### 과제 3: 쇼핑몰 주문 관리 시스템
**목표**: 상속, 캡슐화, 클래스 간 상호작용

#### 요구사항:
1. `Product` 클래스: 상품을 나타냅니다.
   - 속성: 상품명(`name`), 가격(`price`), 재고량(`stock`)
   - 메서드: 재고 감소(`decrease_stock`), 재고 추가(`increase_stock`)

2. `Order` 클래스: 주문을 나타냅니다.
   - 속성: 주문한 상품(`product`), 주문 수량(`quantity`)
   - 메서드: 주문 총액 계산(`calculate_total`), 주문 완료 처리(`complete_order`)

3. `Customer` 클래스: 고객을 나타냅니다.
   - 속성: 고객 이름(`name`), 장바구니(`cart`: `Order` 객체 리스트)
   - 메서드: 장바구니에 상품 추가(`add_to_cart`), 주문 완료(`checkout`)

4. `Store` 클래스: 쇼핑몰을 나타냅니다.
   - 속성: 상품 리스트(`products`)
   - 메서드: 상품 추가(`add_product`), 상품 검색(`find_product`), 모든 상품 출력(`list_products`)

#### 구현해야 할 기능:
- 쇼핑몰에서 상품을 선택하고, 주문 및 결제하는 기능을 구현합니다.
- 상품 재고를 관리하고, 주문 수량에 따른 재고 감소를 처리합니다.

#### 힌트:

```python
class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

    def decrease_stock(self, quantity):
        if quantity <= self.stock:
            self.stock -= quantity
            return True
        else:
            return False

class Order:
    def __init__(self, product, quantity):
        self.product = product
        self.quantity = quantity

    def calculate_total(self):
        return self.product.price * self.quantity

    def complete_order(self):
        if self.product.decrease_stock(self.quantity):
            print(f"Order for {self.quantity} {self.product.name} completed.")
        else:
            print(f"Not enough stock for {self.product.name}.")
```

### 과제 4: 은행 계좌 관리 시스템
**목표**: 상속, 다형성, 캡슐화

#### 요구사항:
1. `Account` 클래스: 은행 계좌의 기본 클래스입니다.
   - 속성: 계좌 소유자(`owner`), 잔액(`balance`)
   - 메서드: 입금(`deposit`), 출금(`withdraw`)

2. `CheckingAccount`, `SavingsAccount` 클래스: 각각 `Account`를 상속받습니다.
   - `CheckingAccount`: 수표 계좌로, 출금 수수료가 있습니다.
   - `SavingsAccount`: 저축 계좌로, 월 이자율이 있습니다.

3. `Bank` 클래스: 여러 계좌를 관리하는 시스템입니다.
   - 속성: 계좌 리스트(`accounts`)
   - 메서드: 계좌 추가(`add_account`), 잔액 조회(`check_balance`), 이자 적용(`apply_interest`)

#### 구현해야 할 기능:
- 계좌에 입금 및 출금을 처리하고, 수수료와 이자 적용을 구현합니다.

### 과제를 통해 연습할 내용
- **클래스 및 객체 생성**: 각각의 시스템을 다양한 클래스로 나누어 객체 간 상호작용을 연습합니다.
- **상속 및 다형성**: 공통 기능은 상위 클래스에 정의하고, 하위 클래스에서 다형성을 통해 다른 동작을 구현합니다.
- **캡슐화**: 클래스의 속성들을 안전하게 관리하고, 필요한 메서드를 통해서만 접근할 수 있도록 구현합니다.

각 과제를 순차적으로 수행하면서 객체 지향 프로그래밍의 핵심 개념들을 체득해 보세요!