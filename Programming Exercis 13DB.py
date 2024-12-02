import sqlite3
import matplotlib.pyplot as plt


# Create and set up the database
def setup_database():
    db_name = "population_YI.db"
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS population (
            city TEXT,
            year INTEGER,
            population INTEGER
        )
    """)
    cities = [
        ('Miami', 2023, 454279),
        ('Orlando', 2023, 321427),
        ('Tampa', 2023, 407599),
        ('Jacksonville', 2023, 954614),
        ('Tallahassee', 2023, 197212),
        ('St. Petersburg', 2023, 261338),
        ('Kissimmee', 2023, 79226),
        ('Fort Lauderdale', 2023, 183445),
        ('Gainesville', 2023, 146637),
        ('Sarasota', 2023, 54757)
    ]
    cursor.executemany("INSERT INTO population VALUES (?, ?, ?)", cities)
    conn.commit()
    conn.close()
    return db_name


# Simulate population growth
def simulate_population_growth(db_name):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    growth_rate = 0.02
    cursor.execute("SELECT DISTINCT city FROM population")
    cities = [row[0] for row in cursor.fetchall()]

    for city in cities:
        cursor.execute("SELECT population FROM population WHERE city = ? AND year = 2023", (city,))
        base_population = cursor.fetchone()[0]
        for year in range(2024, 2044):
            base_population = int(base_population * (1 + growth_rate))
            cursor.execute("INSERT INTO population VALUES (?, ?, ?)", (city, year, base_population))
    conn.commit()
    conn.close()


# Plot population growth
def plot_population_growth(db_name, city):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    cursor.execute("SELECT year, population FROM population WHERE city = ?", (city,))
    data = cursor.fetchall()
    conn.close()

    years = [row[0] for row in data]
    populations = [row[1] for row in data]

    plt.plot(years, populations, marker='o')
    plt.title(f"Population Growth of {city}")
    plt.xlabel("Year")
    plt.ylabel("Population")
    plt.grid()
    plt.show()


# Main function
def main():
    db_name = setup_database()
    simulate_population_growth(db_name)

    cities = ['Miami', 'Orlando', 'Tampa', 'Jacksonville', 'Tallahassee',
              'St. Petersburg', 'Kissimmee', 'Fort Lauderdale', 'Gainesville', 'Sarasota']

    while True:
        print("Available cities:", ", ".join(cities))
        city = input("Choose a city to view its population growth (or type 'exit' to quit): ")
        if city.lower() == 'exit':
            print("Goodbye!")
            break
        elif city in cities:
            plot_population_growth(db_name, city)
        else:
            print("Invalid city. Please choose from the available options.")


if __name__ == "__main__":
    main()