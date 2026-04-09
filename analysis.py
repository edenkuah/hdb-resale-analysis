import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

def thousands_formatter(x, pos):
    return f"{int(x/1000)}k"
df = pd.read_csv('Resale_Flat_Prices.csv')

# Function that creates a bar chart comparing average prices for HDBs to the towns
def plot_top_towns():
    average_prices = df.groupby('town')['resale_price'].mean().sort_values(ascending=False)

    # Only accept the top 10 most expensive towns
    top_10_avg = average_prices[:10]

    #Set the initial window size (Of the graph)
    plt.figure(figsize=(13, 8))

    #Set the X,Y labels + The graph title
    plt.xlabel("Towns")
    plt.ylabel("Prices")
    plt.title("Top 10 most expensive HDB towns (in terms of resale prices)")

    #Format Y-axis to show up in thousands (k)
    plt.gca().yaxis.set_major_formatter(FuncFormatter(thousands_formatter))

    # Plots the bar chart
    plt.bar(top_10_avg.index, top_10_avg.values, color="#483d7f")

    # Rotate the x-axis labels by 45 degrees for better readability
    plt.xticks(rotation=10, ha='right')
    plt.tight_layout()  # Adjust layout to prevent clipping of labels

    # Save image of the graph
    plt.savefig("images/top_10_towns.png", dpi=300, bbox_inches='tight')

    plt.show()


def plot_price_trend_year():
    # Convert "Month" in dataset to a pandas datetime object and make a new column called year
    df["year"] = pd.to_datetime(df["month"]).dt.year

    # Find the average resale price by year
    yearly_avg = df.groupby("year")["resale_price"].mean()

    # Set the initial window size (Of the graph)
    plt.figure(figsize=(13, 8))

    # Label the X and Y and create the title
    plt.title("Average HDB Resale prices by year")
    plt.ylabel("HDB Resale Price")
    plt.xlabel("Year")

    # Format the Y-axis to show only in thousands (k)
    plt.gca().yaxis.set_major_formatter(FuncFormatter(thousands_formatter))

    # Plot the graph
    plt.plot(yearly_avg.index, yearly_avg.values, color="#2c1e75")

    # Save image of the graph
    plt.savefig("images/price_trend_by_year.png", dpi=300, bbox_inches='tight')

    # Show the graph
    plt.show()

def plot_flat_types():
    # Count the number of each type of flat that is resold
    flat_type_counts = df["flat_type"].value_counts()

    plt.figure(figsize=(13, 8))
    # Format the Y-axis to show only in thousands (k)
    plt.gca().yaxis.set_major_formatter(FuncFormatter(thousands_formatter))

    # Add X + Y labels and graph title
    plt.title("Amount of each flat types for each category")
    plt.ylabel("Amount of each flat type sold")
    plt.xlabel("Types of HDBs")

    # Plot the graph
    plt.bar(flat_type_counts.index, flat_type_counts.values, color="#4c4088")

    # Save image of the graph
    plt.savefig("images/flat_type_distribution.png", dpi=300, bbox_inches='tight')

    # Show the graph
    plt.show()


def main():
    print("1: Plot the top 10 most expensive HDB towns (in terms of resale prices)")
    print("2: Plot the average HDB resale prices by year")
    print("3: Plot the amount of each flat type sold")
    print("4: View all graphs")
    print("5: Exit")

    
    while True:
        user_input = input("Select an option (1 To 5): ").strip().lower()
        try:
            if user_input == "":
                print("Input cannot be empty. Please enter a valid option.")
            else:
                if user_input == "1":
                    plot_top_towns()
                elif user_input == "2":
                    plot_price_trend_year()
                elif user_input == "3":
                    plot_flat_types()
                elif user_input.lower() == "view_all" or user_input == "4":
                    plot_top_towns()
                    plot_price_trend_year()
                    plot_flat_types()
                elif user_input.lower() == "exit" or user_input.lower() == "quit" or user_input == "5":
                    print("Exiting the program. Goodbye!")
                    break
                else:
                    print("Invalid input. Please enter 1, 2, 3, 'view_all', or 'exit'.")
        except KeyboardInterrupt:
            print("\nProgram interrupted. Exiting safely...")
            break
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
