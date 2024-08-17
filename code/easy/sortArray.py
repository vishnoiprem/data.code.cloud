import csv
import sys

def hierarchical_sort(input_file, output_file, sort_metric):
    with open(input_file, 'r') as f:
        reader = csv.DictReader(f, delimiter='|')
        rows = list(reader)

    property_columns = [col for col in reader.fieldnames if col.startswith('property')]

    def sort_key(row):
        is_total_first = row['property0'] == '$total'
        is_total_second = row['property1'] == '$total'
        return (
            -float(row[sort_metric]),  # Primary: Sort by metric in descending order
            is_total_first,  # Secondary: Sort by whether it's a $total row in property0
            is_total_second,  # Tertiary: Sort by whether it's a $total row in property1
            row['property0'],  # Sort by property0 alphabetically
            row['property1'],  # Sort by property1 alphabetically
        )

    sorted_rows = sorted(rows, key=sort_key)

    with open(output_file, 'w') as f:
        writer = csv.DictWriter(f, fieldnames=reader.fieldnames, delimiter='|')
        writer.writeheader()
        writer.writerows(sorted_rows)

if __name__ == '__main__':
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    sort_metric = sys.argv[3]
    hierarchical_sort(input_file, output_file, sort_metric)