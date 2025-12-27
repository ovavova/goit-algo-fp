""" Завдання 1. Структури даних. Сортування. Робота з однозв'язним списком



Для реалізації однозв'язного списку (приклад реалізації можна взяти з конспекту) необхідно:

написати функцію, яка реалізує реверсування однозв'язного списку, змінюючи посилання між вузлами;
розробити алгоритм сортування для однозв'язного списку, наприклад, сортування вставками або злиттям;
написати функцію, що об'єднує два відсортовані однозв'язні списки в один відсортований список. """

import random

class Node:
    '''Клас вузла однозв'язного списку'''
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    '''Клас однозв'язного списку'''
    def __init__(self):
        self.head = None

    def append(self, data):
        '''Додає новий вузол в кінець списку'''
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def print_list(self):
        '''Виводить вміст списку'''
        current_node = self.head
        result = ""
        while current_node:
            result += str(current_node.data) + " -> "
            current_node = current_node.next
        print(result + "None")

    def reverse_list(self):
        '''Реверсує однозв'язний список'''
        prev_node = None
        current_node = self.head
        
        while current_node:
            next_node = current_node.next  # Зберігаємо наступний вузол
            current_node.next = prev_node   # Реверсуємо посилання поточного вузла
            
            # Переміщуємо вказівники на одну позицію вперед
            prev_node = current_node
            current_node = next_node
            
        self.head = prev_node  # Нова голова списку - останній елемент
    
    def merge_sort(self):
        '''Метод для запуску сортування злиттям'''
        self.head = self._merge_sort_recursive(self.head)

    def _merge_sort_recursive(self, head):
        '''Рекурсивна реалізація сортування злиттям'''
        # Базовий випадок: список порожній або має один елемент
        if not head or not head.next:
            return head

        # Розділення списку на дві половини
        left_half, right_half = self._split_list(head)

        # Рекурсивне сортування кожної половини
        left = self._merge_sort_recursive(left_half)
        right = self._merge_sort_recursive(right_half)

        # Злиття відсортованих половин
        return self._merge_sorted_lists(left, right)
    
    def _split_list(self, head):
        '''Розділяє список на дві частини'''
        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        mid = slow.next
        slow.next = None
        return head, mid
    
    def _merge_sorted_lists(self, list1_head, list2_head):
        '''Об'єднує два відсортовані списки в один відсортований'''
        dummy = Node()
        tail = dummy

        l1 = list1_head
        l2 = list2_head

        while l1 and l2:
            if l1.data < l2.data:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next

        # Додаємо залишок одного зі списків
        if l1:
            tail.next = l1
        elif l2:
            tail.next = l2

        return dummy.next
    
def merge_two_lists(list1, list2):
    '''Функція для об'єднання двох екземплярів LinkedList'''
    merged_list = LinkedList()
    merged_list.head = list1._merge_sorted_lists(list1.head, list2.head)
    return merged_list
    
if __name__ == '__main__':
    vidst = 10
    random.seed(40)
    rnd_list = [random.randint(1, 100) for _ in range(10)]



    print(f" {vidst*"*-"} Реверсування списку {vidst*"-*"}")
    linked_reverse = LinkedList()
    for num in rnd_list:
        linked_reverse.append(num)
 
    
    print("Початковий список:")
    linked_reverse.print_list()
    
    linked_reverse.reverse_list()
    
    print("Реверсований список:")
    linked_reverse.print_list()
    print("-" * vidst)

    print(f"{vidst * '*-'} Сортування списку {vidst * '*-'}")
    linked_sort = LinkedList()
    for num in rnd_list: 
        linked_sort.append(num)


    print("Несортований список:")
    linked_sort.print_list()
    linked_sort.merge_sort()

    print("Відсортований список:")
    linked_sort.print_list()
    print("-" * 25)

    print(f"\n {vidst * "*-"} Об'єднання двох відсортованих списків {vidst * "-*"}")
    list1 = LinkedList()
    list1.append(60)
    list1.append(90)
    list1.append(10)
    list1.append(100)

    list2 = LinkedList()
    list2.append(20)
    list2.append(150)
    list2.append(80)
    list2.append(70)

    print("Перший відсортований список:")
    list1.merge_sort()
    list1.print_list()

    print("Другий відсортований список:")
    list2.merge_sort()
    list2.print_list()

    merged = merge_two_lists(list1, list2)
    print("Об'єднаний відсортований список:")
    merged.print_list()