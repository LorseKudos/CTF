package main

import (
	"fmt"
	"math/big"
	"math/rand"
	"os"
	"time"
)

// P(success by bruteforce) = 1 - e^(blablabla) << 0.001 by birthday paradox
// hope it's correct math...
// anyways, it is impossible to bruteforce :)
const TableSize = 10000

var TableSizeBI = big.NewInt(int64(TableSize))

const MaxCollision = 10

// fake linked list...
type LinkedList struct {
	Content       [MaxCollision]int
	InsertedCount int // count of element in linked list
}

type HashTable struct {
	Content      [TableSize]*LinkedList // array for mapping hash to the linked list
	HashParam1   *big.Int               // p1 for hashing
	HashParam2   *big.Int               // p2 for hashing
	ElementCount int                    // count of all elements in hash table
}

type SystemTimeInfo struct {
	HashTableInitTime int64 // hash table recreate/init time
	StartTime         int64 // system start time
}

var hashTable HashTable
var systemTimeInfo SystemTimeInfo
var FLAG string

// initializations for the hashtable
func (t *HashTable) generateRandForHashing() {
	currentTime := int64(1608419479492130680)
	rand.Seed(currentTime)
	systemTimeInfo.HashTableInitTime = currentTime
	t.HashParam1 = big.NewInt(int64(rand.Intn(1 << 32))) // allow 16 bits, so 16+20 = 32 => no overflow
	t.HashParam2 = big.NewInt(int64(rand.Intn(1 << 32)))
}

func (t *HashTable) recreate() {
	t.generateRandForHashing()
	for !t.HashParam1.ProbablyPrime(0) || !t.HashParam2.ProbablyPrime(0) {
		t.generateRandForHashing()
	}
	for i := 0; i < TableSize; i++ {
		t.Content[i] = &LinkedList{[MaxCollision]int{}, 0}
	}
	t.ElementCount = 0
}

// input: value => a value to be hashed
// output: hash of the value
func (t *HashTable) hash(value int) uint {
	// hash = p1 ** value % p2 % table size
	v := big.NewInt(int64(value))
	var h big.Int
	h.Exp(v, t.HashParam1, t.HashParam2)
	h.Mod(&h, TableSizeBI)
	return uint(h.Uint64())
}

// input: value => a value to be inserted
// output: whether max collision happens (i.e. whether there are
// 		   10 elements in a single slot)
// This is an O(1) operation
func (t *HashTable) insert(value int) bool {
	if t.find(value) {
		return false // already in the table
	}
	var elementHash = t.hash(value)                // get hash
	var linkedListForHash = t.Content[elementHash] // get linked list for the slot
	linkedListForHash.InsertedCount++              // increase count for the linked list
	if linkedListForHash.InsertedCount >= 10 {
		fmt.Printf("%d ", linkedListForHash.Content)
		fmt.Printf("%d\n", value)
		return true // 10 collisions
	}
	t.ElementCount++                                                     // increase count for the hash table
	linkedListForHash.Content[linkedListForHash.InsertedCount-1] = value // insert
	return false                                                         // <10 collisions
}

// input: value => a value to be found
// output: whether this value is inside hash table
// This is an O(1) operation
func (t *HashTable) find(value int) bool {
	var elementHash = t.hash(value)                // get hash
	var linkedListForHash = t.Content[elementHash] // get linked list for the slot
	for i := 0; i < linkedListForHash.InsertedCount; i++ {
		if linkedListForHash.Content[i] == value {
			return true // found
		}
	}
	return false // not found
}

func main() {
	FLAG = os.Getenv("FLAG")                         // flag
	systemTimeInfo.StartTime = time.Now().UnixNano() // system start time
	hashTable.recreate()                             // initialize hash table
	fmt.Printf("%d,%d\n", hashTable.HashParam1, hashTable.HashParam2)
	for i := 1<<12 + 1; i < 1<<20; i++ {
		hashTable.insert(i)
	}
}

// we{6890260a-0fed-48a3-9865-91daa1d0df52@l00ks_l1ke_u_got_an_A+_1n_crypt01o1}
