import json

def load_json_data():
    with open('data.json') as f:  # Replace 'data.json' with the path to your JSON file
        return json.load(f)
def get_html_content():
    data = load_json_data()
    
    # Define the organization lis
    org_list = [
        'US', 'CA', 'UK', 'IN', 'DE', 'FR', 'IT', 'ES', 'MX', 'BR', 'AU',
        'SG', 'JP', 'AE', 'SA', 'EG', 'NL', 'PL', 'SE', 'TR', 'BE', 'ZA'
    ]

    def generate_table_rows(key):
        rows = []
        for org in org_list:
            org_data = data.get(key, {}).get(org.lower(), {})
            count = org_data.get('count', 'N/A')
            age = org_data.get('age', 'N/A')
            cluster = org_data.get('cluster', 'N/A')
            rows.append(f"""
            <tr>
                <td>{org}</td>
                <td>{count}</td>
                <td>{age}</td>
                <td>{cluster}</td>
            </tr>
            """)
        return "\n".join(rows)

    return f"""
    <!DOCTYPE html>
    <html>
    <head>
        <style>
            table {{
                width: 100%;
                border-collapse: collapse;
            }}
            table, th, td {{
                border: 1px solid black;
            }}
            th, td {{
                padding: 10px;
                text-align: left;
            }}
            th {{
                background-color: #f2f2f2;
            }}
            tr:nth-child(even) {{
                background-color: #f2f2f2;
            }}
            .outer-table {{
                width: 100%;
                border: none;
                margin-bottom: 20px; /* Space between rows */
            }}
            .inner-table {{
                width: 18%; /* Adjust width to fit five tables in a row */
                border: none;
                display: inline-block;
                vertical-align: top;
            }}
            .outer-table tr {{
                display: flex;
                justify-content: space-between;
            }}
        </style>
    </head>
    <body>
        <h1>Three Rows of Five Tables</h1>
        <!-- Row 1 -->
        <table class="outer-table">
            <tr>
                <td class="inner-table">
                    <table id="emails">
                        <tr>
                            <th colspan="4">Emails</th>
                        </tr>
                        <tr>
                            <th>Org</th>
                            <th>In Queue</th>
                            <th>Age</th>
                            <th>Status</th>
                        </tr>
                        {generate_table_rows('emails')}
                    </table>
                </td>
                <td class="inner-table">
                    <table id="rcr">
                        <tr>
                            <th colspan="4">CRT</th>
                        </tr>
                        <tr>
                            <th>Org</th>
                            <th>In Queue</th>
                            <th>Age</th>
                            <th>Status</th>
                        </tr>
                        {generate_table_rows('rcr')}
                    </table>
                </td>
                <!-- Add other tables here following the same pattern -->
            </tr>
        </table>
        <!-- Row 2 -->
        <table class="outer-table">
            <tr>
                <td class="inner-table">
                    <table id="emails">
                        <tr>
                            <th colspan="4">Emails</th>
                        </tr>
                        <tr>
                            <th>Org</th>
                            <th>In Queue</th>
                            <th>Age</th>
                            <th>Status</th>
                        </tr>
                        {generate_table_rows('emails')}
                    </table>
                </td>
                <td class="inner-table">
                    <table id="rcr">
                        <tr>
                            <th colspan="4">CRT</th>
                        </tr>
                        <tr>
                            <th>Org</th>
                            <th>In Queue</th>
                            <th>Age</th>
                            <th>Status</th>
                        </tr>
                        {generate_table_rows('rcr')}
                    </table>
                </td>
                <!-- Add other tables here following the same pattern -->
            </tr>
        </table>
        <!-- Row 3 -->
        <table class="outer-table">
            <tr>
                <td class="inner-table">
                    <table id="emails">
                        <tr>
                            <th colspan="4">Emails</th>
                        </tr>
                        <tr>
                            <th>Org</th>
                            <th>In Queue</th>
                            <th>Age</th>
                            <th>Status</th>
                        </tr>
                        {generate_table_rows('emails')}
                    </table>
                </td>
                <td class="inner-table">
                    <table id="rcr">
                        <tr>
                            <th colspan="4">CRT</th>
                        </tr>
                        <tr>
                            <th>Org</th>
                            <th>In Queue</th>
                            <th>Age</th>
                            <th>Status</th>
                        </tr>
                        {generate_table_rows('rcr')}
                    </table>
                </td>
                <!-- Add other tables here following the same pattern -->
            </tr>
        </table>
    </body>
    </html>
    """
