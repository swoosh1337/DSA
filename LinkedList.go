package main

import "fmt"

type node struct {
	data int
	next *node
}

type LinkedList struct {
	head   *node
	length int
}

func (l *LinkedList) add(data int) {
	newNode := &node{data: data}
	if l.head == nil {
		l.head = newNode
	} else {
		currentNode := l.head
		for currentNode.next != nil {
			currentNode = currentNode.next
		}
		currentNode.next = newNode
	}
	l.length++
}

func (L LinkedList) print() {
	currentNode := L.head
	for currentNode != nil {
		fmt.Println(currentNode.data)
		currentNode = currentNode.next
	}
}

func (l *LinkedList) delete(data int) {
	if l.head.data == data {
		l.head = l.head.next
		l.length--
		return
	}
	currentNode := l.head
	for currentNode.next != nil {
		if currentNode.next.data == data {
			currentNode.next = currentNode.next.next
			l.length--
			return
		}
		currentNode = currentNode.next
	}
}

func main() {

	l := LinkedList{}
	l.add(1)
	l.add(2)
	l.add(3)
	l.add(4)
	l.add(5)
	l.print()
	l.delete(3)
	l.print()
	l.delete(1)
	l.print()
	l.delete(5)
	l.print()
	l.delete(2)
	l.print()
	l.delete(4)
	l.print()

}
