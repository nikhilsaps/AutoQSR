def get_html_content():
    values = ["us", "ca", "uk", "in", "de", "fr", "it", "es", "mx", "br", "au", "sg", "jp", "ae", "sa", "eg", "nl", "pl", "se", "tr", "be", "za"]
    table_ids = ["emails", "rcr", "maa", "armeq", "ltaeq", "atoz", "sgd", "ri", "conc", "acct", "hrqsgd", "hrqri", "hrqconc", "hrqacct", "table15"]
    table_titles = ["Emails", "CRT", "MAA Appeals", "ARM Appeals", "LTA Appeals", "A to Z", "Order Level", "RI", "Concession Level", "Account Level", "HRQ Order Level", "HRQ RI", "HRQ Concession", "HRQ Account Level", "Table 15"]

    def generate_table(table_id, title):
        return f"""
        <td class="inner-table">
            <table id="{table_id}">
                <tr>
                    <th colspan="4">{title}</th>
                </tr>
                <tr>
                    <th>Header 1</th>
                    <th>Header 2</th>
                    <th>Header 3</th>
                    <th>Header 4</th>
                </tr>
                {''.join(f'<tr><td>{value}</td><td>Cell 2</td><td>Cell 3</td><td>Cell 4</td></tr>' for value in values)}
            </table>
        </td>
        """

    tables_html = ''.join(generate_table(table_id, title) for table_id, title in zip(table_ids, table_titles))

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
                {tables_html[:5]}
            </tr>
        </table>

        <!-- Row 2 -->
        <table class="outer-table">
            <tr>
                {tables_html[5:10]}
            </tr>
        </table>

        <!-- Row 3 -->
        <table class="outer-table">
            <tr>
                {tables_html[10:]}
            </tr>
        </table>
    </body>
    </html>
    """
