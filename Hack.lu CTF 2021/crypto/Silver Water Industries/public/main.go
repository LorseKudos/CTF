package main

import (
	"bufio"
	"crypto/rand"
	"fmt"
	"math"
	"math/big"
	"os"
)

func genN() *big.Int {
	var p *big.Int
	var q *big.Int
	var err error

	// p % 4 = 1 の素数p
	for {
		p, err = rand.Prime(rand.Reader, 64)
		if err != nil {
			panic(err)
		}
		res := new(big.Int)
		if res.Mod(p, big.NewInt(4)); res.Cmp(big.NewInt(1)) == 0 {
			break
		}
	}

	// q % 4 = 3 の素数q
	for {
		q, err = rand.Prime(rand.Reader, 64)
		if err != nil {
			panic(err)
		}
		res := new(big.Int)
		if res.Mod(q, big.NewInt(4)); res.Cmp(big.NewInt(3)) == 0 {
			break
		}
	}

	N := new(big.Int)
	N.Mul(p, q)
	return N
}

func genX(N *big.Int) *big.Int { // Nと互いに素なxを生成
	for {
		x, err := rand.Int(rand.Reader, N)
		if err != nil {
			panic(err)
		}
		g := new(big.Int)
		g.GCD(nil, nil, x, N)
		if g.Cmp(big.NewInt(1)) == 0 {
			return x
		}
	}
}

func encryptByte(b uint8, N *big.Int) []*big.Int {
	z := big.NewInt(-1)
	enc := make([]*big.Int, 8)
	for i := 0; i < 8; i++ {
		bit := b & uint8(math.Pow(2, float64(7-i))) // b(2進数表記8bit)の上からi番目
		x := genX(N) // Nと互いに素なx
		x.Exp(x, big.NewInt(2), N) // x^2 % N
		if bit != 0 {
			x.Mul(x, z)
			x.Mod(x, N) // x^2*(-1) % N
		}
		enc[i] = x
	}
	return enc
}

func generateRandomString(n int) string {
	const letters = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz-"
	ret := make([]byte, n)
	for i := 0; i < n; i++ {
		num, err := rand.Int(rand.Reader, big.NewInt(int64(len(letters))))
		if err != nil {
			panic(err)
		}
		ret[i] = letters[num.Int64()]
	}

	return string(ret)
}

func main() {
	N := genN() // N = PQ = (4p+1)(4q-1)

	token := []byte(generateRandomString(20))
	fmt.Println(string(token))

	fmt.Println(N)
	for _, b := range token {
	    fmt.Println(uint8(b))
		fmt.Println(encryptByte(uint8(b), N))
	}
	fmt.Println("")

    // 入力がtokenと一致するか
	reader := bufio.NewReader(os.Stdin)

	input, err := reader.ReadString('\n')
	if err != nil {
		panic(err)
	}
	input = input[:len(input)-1]

	if string(token) == input {
		fmt.Println("flag{<YOUR_FLAG_HERE>}")
	}
}
