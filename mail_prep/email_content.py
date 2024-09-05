import json

def load_json_data():
    with open('data.json') as f:  # Replace 'data.json' with the path to your JSON file
        return json.load(f)

def get_html_content():
    data = load_json_data()
    
    # Define the organization list
    org_list = [
        'US', 'CA', 'UK', 'IN', 'DE', 'FR', 'IT', 'ES', 'MX', 'BR', 'AU',
        'SG', 'JP', 'AE', 'SA', 'EG', 'NL', 'PL', 'SE', 'TR', 'BE', 'ZA'
    ]

    def get_cluster_color(cluster):
        if cluster == "need attention":
            return "yellow"
        elif cluster == "missed":
            return "red"
        else:
            return "green"

    def generate_table_rows(key):
        rows = []
        for org in org_list:
            org_data = data.get(key, {}).get(org.lower(), {})
            count = org_data.get('count', '0')
            age = org_data.get('age', '00:00')
            cluster = org_data.get('status', '0')
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
                <td class="inner-table">
                    <table id="armeq">
                        <tr>
                            <th colspan="4">ARM Appeals</th>
                        </tr>
                        <tr>
                            <th>Org</th>
                            <th>In Queue</th>
                            <th>Age</th>
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
                            <th>Age</th>
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
                            <th>Age</th>
                            <th>Status</th>
                        </tr>
                        {generate_table_rows('ltaeq')}
                    </table>
                </td>
                <!-- Add other tables here following the same pattern -->
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
                            <th>Age</th>
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
                            <th>Age</th>
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
                            <th>Age</th>
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
                            <th>Age</th>
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
                            <th>Age</th>
                            <th>Status</th>
                        </tr>
                        {generate_table_rows('acct')}
                    </table>
                </td>
                <!-- Add other tables here following the same pattern -->
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
                            <th>Age</th>
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
                            <th>Age</th>
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
                            <th>Age</th>
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
                            <th>Age</th>
                            <th>Status</th>
                        </tr>
                        {generate_table_rows('hrqacct')}
                    </table>
                </td>
                <!-- Add other tables here following the same pattern -->
            </tr>
        </table>
    </body>
    </html>
    """
