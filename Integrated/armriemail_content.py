import json

def load_json_data():
    with open('output/output.json') as f:  # Replace 'output/output.json' with the path to your JSON file
        return json.load(f)

def get_html_content():
    data = load_json_data()
    
    # Define the organization list
    org_list = [
        'US', 'CA', 'UK', 'IN', 'DE', 'FR', 'IT', 'ES', 'MX', 'BR', 'AU',
        'SG', 'JP', 'AE', 'SA', 'EG', 'NL', 'PL', 'SE', 'TR', 'BE', 'ZA'
    ]

    def get_cluster_color(cluster):
        if cluster == "Need attention":
            return "#FFD966"
        elif cluster == "Missed":
            return "#FF0000"
        else:
            return "#A9D08E"

    def generate_table_rows(key):
        rows = []
        for org in org_list:
            org_data = data.get(key, {}).get(org.lower(), {})
            count = org_data.get('count', '0')
            age = org_data.get('age', '00:00:00')
            cluster = org_data.get('status', 'in control')
            cluster_color = get_cluster_color(cluster)
            rows.append(f"""
            <tr>
                <td>{org}</td>
                <td>{count}</td>
                <td>{age}</td>
                <td style="background-color: {cluster_color};">{cluster}</td>
            </tr>
            """)
        return "\n".join(rows)

    return f"""
    <!DOCTYPE html>
    <html>
    <head>
        <style>
            body {{
                font-family: Arial, sans-serif;
            }}
            table {{
                width: 400px; /* Fixed width for the table */
                border-collapse: collapse;
                table-layout: fixed; /* Ensures cells and columns are fixed size */
            }}
            table, th, td {{
                border: 2px solid black;
            }}
            th, td {{
                padding: 8px; /* Adjust padding as needed */
                text-align: center;
                overflow: hidden; /* Ensures text does not overflow */
                text-overflow: ellipsis; /* Adds ellipsis for overflowed text */
                white-space: nowrap; /* Prevents text wrapping */
            }}
            th {{
                background-color: #00B050;
            }}
            tr:nth-child(even) {{
                background-color: #f2f2f2;
            }}
            .outer-table {{
                width: auto;
                border: none;
                margin-bottom: 20px; /* Space between rows */
            }}
            .inner-table {{
                width: 400px; /* Fixed width for inner tables */
                border: none;
                display: inline-block;
                vertical-align: top;
            }}
        </style>
    </head>
    <body>
        <p>PFB the Queue Status Report </p>
        <!-- Row 1 -->
        <table class="outer-table">
            <tr>
                <td class="inner-table">
                    <table id="armri">
                        <tr>
                            <th colspan="4">ARM RI</th>
                        </tr>
                        <tr>
                            <th>Org</th>
                            <th>In Queue</th>
                            <th>Age</th>
                            <th>Status</th>
                        </tr>
                        {generate_table_rows('armri')}
                    </table>
                </td>
            </tr>
        </table>
        
        <h4>Regards,<br>WFM<h4>
    </body>
    </html>
    """

