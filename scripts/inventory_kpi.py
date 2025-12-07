def days_of_inventory(ending_stock, daily_usage):
    return ending_stock / daily_usage if daily_usage > 0 else None