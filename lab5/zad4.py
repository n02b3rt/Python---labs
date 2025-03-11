"""
Zadanie 4 - Klasy Abstrakcyjne

Stwórz abstrakcyjną klasę `Powiadomienie` z metodą `wyslij(self, wiadomosc)`, a następnie klasy:

- **`EmailPowiadomienie`**
- **`SMSPowiadomienie`**
- **`PushPowiadomienie`**

Każda powinna implementować `wyslij()`, wypisując sposób wysyłki.

### Do zrobienia

1. Spróbuj utworzyć instancję `Powiadomienie` – co się stanie?
2. Utwórz instancje konkretne i wywołaj `wyslij()`.
3. Dodaj atrybut `priorytet` do `Powiadomienie`.
"""

from abc import ABC, abstractmethod

class Powiadomienie(ABC):
    def __init__(self, priorytet):
        self.priorytet = priorytet

    @abstractmethod
    def wyslij(self, wiadomosc):
        pass

class EmailPowiadomienie(Powiadomienie):
    def wyslij(self, wiadomosc):
        print(f"[EMAIL] Priorytet {self.priorytet}: {wiadomosc}]")

class SMSPowiadomienie(Powiadomienie):
    def wyslij(self, wiadomosc):
        print(f"[SMS] Priorytet {self.priorytet}: {wiadomosc}]")

class PushPowiadomienie(Powiadomienie):
    def wyslij(self, wiadomosc):
        print(f"[PUSH] Priorytet {self.priorytet}: {wiadomosc}]")


# powiadomienie = Powiadomienie(1)
"""
TypeError: Can't instantiate abstract class Powiadomienie without an implementation for abstract method 'wyslij'
!Nie można tworzyć obiektu klasy abstrakcyjnej!
"""

email = EmailPowiadomienie(2)
sms = SMSPowiadomienie(1)
push = PushPowiadomienie(3)

email.wyslij("Powiadomienie e-mail")
sms.wyslij("Powiadomienie sms")
push.wyslij("Powiadomienie psuh")