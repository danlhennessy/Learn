package main

import (
	"database/sql"
	"fmt"
	"log"
	"net/url"
	"os"
	"time"

	"github.com/joho/godotenv"
	_ "github.com/lib/pq"
)

func main() {
	err := godotenv.Load()
	if err != nil {
		log.Fatal("Error loading .env file")
	}

	environment := os.Getenv("ENVIRONMENT")
	if environment == "" {
		log.Fatal("ENVIRONMENT environment variable is not set.")
	}

	password := os.Getenv("DB_PASSWORD")
	if password == "" {
		log.Fatal("DB_PASSWORD environment variable is not set.")
	}
	encodedPassword := url.QueryEscape(password)

	connStr := fmt.Sprintf(`postgres://pgadmin:%s@sandboxpg.postgres.database.azure.com/postgres?sslmode=verify-full`,
		encodedPassword,
	)
	db, err := sql.Open("postgres", connStr)
	if err != nil {
		panic(err)
	}
	defer db.Close()

	if environment == "development" {
		return
	}

	for {
		var count int
		lastname := `Doe`
		qerr := db.QueryRow(`SELECT COUNT(*) FROM customers WHERE last_name LIKE '%' || $1 || '%'`, lastname).Scan(&count)
		if qerr != nil {
			panic(qerr)
		}
		if count == 0 {
			break
		}
		fmt.Println(`Rows count:`, count)

		time.Sleep(2 * time.Second)
	}

}
