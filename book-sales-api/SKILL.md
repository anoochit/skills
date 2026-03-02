---
name: book-sales-api
description: Access book inventory and sales data. Use for retrieving book details, sales transactions, and author/sales summary reports from the internal API.
---

# Book and Sales Data API

This skill allows you to query the internal Book and Sales API.

**Base URL**: `http://192.168.1.36:8000`

## Endpoints

### Books
- **List all books**: `GET /books`
- **Get specific book**: `GET /books/{book_id}`

### Sales
- **List all sales**: `GET /sales` (includes joined book details)

### Reports
- **Summary by Book & Author**: `GET /summary/book_author` (Quantity & Revenue per book)
- **Summary by Author**: `GET /summary/author` (Total Quantity & Revenue per author)

## Usage

Use `curl` to fetch data. The API returns JSON.

### Examples

**Get all books:**
```bash
curl -s "http://192.168.1.36:8000/books"
```

**Get a specific book (ID 5):**
```bash
curl -s "http://192.168.1.36:8000/books/5"
```

**Get sales summary by author:**
```bash
curl -s "http://192.168.1.36:8000/summary/author"
```

## Data Fields (Key schemas)

- **Book**: `Book_ID`, `Book_Title`, `Author`, `ISBN`
- **Sale**: `Transaction_ID`, `Quantity`, `Actual_Revenue_THB`, `Payment_Method`, plus Book details.
- **Summary**: `Total_Quantity_Sold`, `Total_Revenue_THB`

See `references/api-spec.json` for full schema details if needed.
