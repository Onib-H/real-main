def test():
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    if conn.is_connected:
        return 'Database successful'
    conn.close()