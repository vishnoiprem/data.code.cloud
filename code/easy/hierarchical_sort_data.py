import sys
import csv
from itertools import groupby
from operator import itemgetter


def hierarchical_sort_data(input_file, output_file, sort_metric):
    #Read the input file and convert it to a list of dictionaries
    with open(input_file, 'r') as f:
        reader = csv.DictReader(f, delimiter='|')
        #created to json format {'property0': 'bar', 'property1': '$total', 'net_sales': '-200'}, {'property0': 'foo', 'property1': 'sauce', 'net_sales': '300'},
        rows = list(reader)

    # find property columns which start with property eg property1 or property0 come here
    property_columns = []
    for col in reader.fieldnames:
        if col.startswith('property'):
            property_columns.append(col)
    # print(property_columns)
    # ['property0', 'property1']

    # function to determine if a row is having filed value  $total row
    def is_total_row(row):
        for prop in property_columns:
            if row[prop] == '$total':
                return True
        return False

    # Helper function to sort rows within a group
    def sort_group(rows):
        # Separate total and non-total rows
        total_rows = []
        for row in rows:
            if is_total_row(row):
                total_rows.append(row)

        # print(total_rows)

        non_total_rows = []
        for row in rows:
            if not is_total_row(row):
                non_total_rows.append(row)
        # print(non_total_rows)

        # Sort non-total rows by the metric in descending order data
        non_total_rows.sort(key=lambda x: float(x[sort_metric]), reverse=True)
        return total_rows + non_total_rows

    # Sort rows by property columns to group them properly
    rows.sort(key=itemgetter(*property_columns))

    # Hierarchically sort the data by progressively grouping and sorting by properties
    for i in range(len(property_columns)):
        grouped_rows = []

        # Group rows by the first i+1 property columns
        for key, group in groupby(rows, key=itemgetter(*property_columns[:i + 1])):
            group_list = list(group)
            sorted_group = sort_group(group_list)

            for row in sorted_group:
                grouped_rows.append(row)

        rows = grouped_rows

    # write to output file with | delimiter
    with open(output_file, 'w') as f:
        writer = csv.DictWriter(f, fieldnames=reader.fieldnames, delimiter='|')
        writer.writeheader()
        writer.writerows(rows)


if __name__ == '__main__':
    #     input arg from paramter
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    sort_metric = sys.argv[3]

    # call to function
    hierarchical_sort_data(input_file, output_file, sort_metric)