import csv

def main():
    with open("data.csv", "w", newline="") as csv_file:
        csv_writer = csv.writer(csv_file)
        for ii in range(60):
            for jj in range(60):
                if ii + jj > 15:
                    result = ii + 2 * jj
                else:
                    result = 2 * ii + jj
                csv_writer.writerow([ii, jj, result])


if __name__ == "__main__":
    main()
