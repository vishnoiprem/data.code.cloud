import csv
import sys
from itertools import groupby
from operator import itemgetter


def hierarchical_sort(input_file, output_file, sort_metric):
    # Read the input file
    with open(input_file, 'r') as f:
        reader = csv.DictReader(f, delimiter='|')
        rows = list(reader)

    # Identify property columns
    property_columns = [col for col in reader.fieldnames if col.startswith('property')]

    # Helper function to determine if a row is a $total row
    def is_total_row(row):
        return any(row[prop] == '$total' for prop in property_columns)

    # Helper function to sort rows within a group
    def sort_group(rows):
        total_rows = [row for row in rows if is_total_row(row)]
        non_total_rows = [row for row in rows if not is_total_row(row)]
        # Sort non-total rows by the metric in descending order
        non_total_rows.sort(key=lambda x: float(x[sort_metric]), reverse=True)
        return total_rows + non_total_rows

    # Sort by property columns first to group properly
    rows.sort(key=itemgetter(*property_columns))

    # Group by the higher levels in the hierarchy
    for i in range(len(property_columns)):
        rows = [
            row
            for key, group in groupby(rows, key=itemgetter(*property_columns[:i + 1]))
            for row in sort_group(list(group))
        ]

    # Write the sorted rows to the output file
    with open(output_file, 'w') as f:
        writer = csv.DictWriter(f, fieldnames=reader.fieldnames, delimiter='|')
        writer.writeheader()
        writer.writerows(rows)


if __name__ == '__main__':
    # Get arguments from command line
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    sort_metric = sys.argv[3]

    # Run the hierarchical sort
    hierarchical_sort(input_file, output_file, sort_metric)