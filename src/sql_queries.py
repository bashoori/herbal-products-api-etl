queries = {
    "top_5_expensive": """
        SELECT name, category, price
        FROM herbal_products
        WHERE price IS NOT NULL
        ORDER BY price DESC
        LIMIT 5;
    """,

    "avg_price_by_category": """
        SELECT category, ROUND(AVG(price), 2) AS avg_price, COUNT(*) AS product_count
        FROM herbal_products
        WHERE price IS NOT NULL
        GROUP BY category
        ORDER BY avg_price DESC;
    """,

    "missing_prices": """
        SELECT id, name, category, price
        FROM herbal_products
        WHERE price IS NULL OR price <= 0
        ORDER BY category;
    """
}
