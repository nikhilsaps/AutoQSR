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
            cluster = org_data.get('status', 'in control')
            cluster_color = get_cluster_color(cluster)
            rows.append(f"""
            <tr>
                <td>{org}</td>
                <td>{count}</td>
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
                width: 100%;
                border: none;
                margin-bottom: 20px; /* Space between rows */
            }}
            .inner-table {{
                width: 400px; /* Fixed width for inner tables */
                border: 2px solid black;
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
                    <table id="emails">
                        <tr>
                            <th colspan="3">Emails</th>
                        </tr>
                        <tr>
                            <th>Org</th>
                            <th>In Queue</th>
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
                            <th>Status</th>
                        </tr>
                        {generate_table_rows('rcr')}
                    </table>
                </td>
                <td class="inner-table">
                    <table id="armeq">
                        <tr>
                            <th colspan="4">ARM Appeals</th>
                        </tr>
                        <tr>
                            <th>Org</th>
                            <th>In Queue</th>
                            <th>Status</th>
                        </tr>
                        {generate_table_rows('armeq')}
                    </table>
                </td>
                <td class="inner-table">
                    <table id="maa">
                        <tr>
                            <th colspan="4">MAA Appeals</th>
                        </tr>
                        <tr>
                            <th>Org</th>
                            <th>In Queue</th>
                            <th>Status</th>
                        </tr>
                        {generate_table_rows('maa')}
                    </table>
                </td>
                <td class="inner-table">
                    <table id="ltaeq">
                        <tr>
                            <th colspan="4">LTA Appeals</th>
                        </tr>
                        <tr>
                            <th>Org</th>
                            <th>In Queue</th>
                            <th>Status</th>
                        </tr>
                        {generate_table_rows('ltaeq')}
                    </table>
                </td>
            </tr>
        </table>
        <!-- Row 2 -->
        <table class="outer-table">
            <tr>
                <td class="inner-table">
                    <table id="atoz">
                        <tr>
                            <th colspan="4">A to Z</th>
                        </tr>
                        <tr>
                            <th>Org</th>
                            <th>In Queue</th>
                            <th>Status</th>
                        </tr>
                        {generate_table_rows('atoz')}
                    </table>
                </td>
                <td class="inner-table">
                    <table id="sgd">
                        <tr>
                            <th colspan="4">Order Level</th>
                        </tr>
                        <tr>
                            <th>Org</th>
                            <th>In Queue</th>
                            <th>Status</th>
                        </tr>
                        {generate_table_rows('sgd')}
                    </table>
                </td>
                <td class="inner-table">
                    <table id="ri">
                        <tr>
                            <th colspan="4">RI</th>
                        </tr>
                        <tr>
                            <th>Org</th>
                            <th>In Queue</th>
                            <th>Status</th>
                        </tr>
                        {generate_table_rows('ri')}
                    </table>
                </td>
                <td class="inner-table">
                    <table id="conc">
                        <tr>
                            <th colspan="4">ConcessionLevel</th>
                        </tr>
                        <tr>
                            <th>Org</th>
                            <th>In Queue</th>
                            <th>Status</th>
                        </tr>
                        {generate_table_rows('conc')}
                    </table>
                </td>
                <td class="inner-table">
                    <table id="acct">
                        <tr>
                            <th colspan="4">Account Level</th>
                        </tr>
                        <tr>
                            <th>Org</th>
                            <th>In Queue</th>
                            <th>Status</th>
                        </tr>
                        {generate_table_rows('acct')}
                    </table>
                </td>
            </tr>
        </table>
        <!-- Row 3 -->
        <table class="outer-table">
            <tr>
                <td class="inner-table">
                    <table id="hrqsgd">
                        <tr>
                            <th colspan="4">HRQ Order Level</th>
                        </tr>
                        <tr>
                            <th>Org</th>
                            <th>In Queue</th>
                            <th>Status</th>
                        </tr>
                        {generate_table_rows('hrqsgd')}
                    </table>
                </td>
                <td class="inner-table">
                    <table id="hrqri">
                        <tr>
                            <th colspan="4">HRQ RI</th>
                        </tr>
                        <tr>
                            <th>Org</th>
                            <th>In Queue</th>
                            <th>Status</th>
                        </tr>
                        {generate_table_rows('hrqri')}
                    </table>
                </td>
                <td class="inner-table">
                    <table id="hrqconc">
                        <tr>
                            <th colspan="4">HRQ Concession</th>
                        </tr>
                        <tr>
                            <th>Org</th>
                            <th>In Queue</th>
                            <th>Status</th>
                        </tr>
                        {generate_table_rows('hrqconc')}
                    </table>
                </td>
                <td class="inner-table">
                    <table id="hrqacct">
                        <tr>
                            <th colspan="4">HRQ Account Level</th>
                        </tr>
                        <tr>
                            <th>Org</th>
                            <th>In Queue</th>
                            <th>Status</th>
                        </tr>
                        {generate_table_rows('hrqacct')}
                    </table>
                </td>
            </tr>
        </table>
        <h4>Regards,<br>WFM<h4>
    </body>
    </html>
    """

