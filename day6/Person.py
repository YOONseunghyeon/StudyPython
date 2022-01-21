# Person.py
# Person 클래스
class Person:
    name = '무명이'  #아직 이름이 없다
    age = 0
    height = 0
    gender = ''
    feetsize = 250
    bloodtype = ''

    # 생성자
    def __init__(self, name, age, height, gender) -> None:
        self.name = name
        self.age = age
        self.height = height
        self.gender = gender
        print('Person이 생성되었습니다')
    
    
    
    
    def 소개한다(self):
        greeting = f'''안녕하세요.저는 {self.name} 입니다.
        {self.gender}구요. {self.age}살입니다.
        '''

        print(greeting)

    
    
    def 먹는다(self, food):
        print(f'{food}를 먹는다')

    def 일한다(self, drink):
        print(f'{drink}를 마시면서 일한다')
    
  


if __name__=='__main__':
    ysh = Person('윤승현', 25, 182.3, 'male')    #==__init__(self, name, age):
    # ysh.name = '윤승현'
    # ysh.age = 25
    ysh.height = 182.3
    ysh.gender = '남성'
    ysh.feetsize = 275
    ysh.bloodtype = 'RH+ AB'
    
    ysh.소개한다()
    ysh.먹는다('짜장면')
    ysh.일한다('소주')


    




# if __name__=='__maim__':
#     p = Person()    # p라는 이름의 Person 객체 생성
#     print(type(p))
#     print(id(p))    # id 값

#     p2 = Person()   # p2 객체 생성
#     print(type(p2))
#     print(id(p2))
   