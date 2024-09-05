def get_html_content():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <style>
            table {
                width: 100%;
                border-collapse: collapse;
            }
            table, th, td {
                border: 1px solid black;
            }
            th, td {
                padding: 10px;
                text-align: left;
            }
            th {
                background-color: #f2f2f2;
            }
            tr:nth-child(even) {
                background-color: #f2f2f2;
            }
            .outer-table {
                width: 100%;
                border: none;
                margin-bottom: 20px; /* Space between rows */
            }
            .inner-table {
                width: 18%; /* Adjust width to fit five tables in a row */
                border: none;
                display: inline-block;
                vertical-align: top;
            }
            .outer-table tr {
                display: flex;
                justify-content: space-between;
            }
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
                        <tr>
                            <td>US</td>
                            <td>Cell 2</td>
                            <td>Cell 3</td>
                            <td>Cell 4</td>
                        </tr>
                        <tr>
                            <td>CA</td>
                            <td>Cell 6</td>
                            <td>Cell 7</td>
                            <td>Cell 8</td>
                        </tr>
                        <tr>
                            <td>UK</td>
                            <td>Cell 6</td>
                            <td>Cell 7</td>
                            <td>Cell 8</td>
                        </tr>
                        <tr>
                            <td>IN</td>
                            <td>Cell 6</td>
                            <td>Cell 7</td>
                            <td>Cell 8</td>
                        </tr>
                        <tr>
                            <td>DE</td>
                            <td>Cell 6</td>
                            <td>Cell 7</td>
                            <td>Cell 8</td>
                        </tr>
                        <tr>
                            <td>FR</td>
                            <td>Cell 6</td>
                            <td>Cell 7</td>
                            <td>Cell 8</td>
                        </tr>
                        <tr>
                            <td>IT</td>
                            <td>Cell 6</td>
                            <td>Cell 7</td>
                            <td>Cell 8</td>
                        </tr>
                        <tr>
                            <td>ES</td>
                            <td>Cell 6</td>
                            <td>Cell 7</td>
                            <td>Cell 8</td>
                        </tr>
                        <tr>
                            <td>MX</td>
                            <td>Cell 6</td>
                            <td>Cell 7</td>
                            <td>Cell 8</td>
                        </tr>
                        <tr>
                            <td>BR</td>
                            <td>Cell 6</td>
                            <td>Cell 7</td>
                            <td>Cell 8</td>
                        </tr>
                        <tr>
                            <td>AU</td>
                            <td>Cell 6</td>
                            <td>Cell 7</td>
                            <td>Cell 8</td>
                        </tr>
                        <tr>
                            <td>SG</td>
                            <td>Cell 6</td>
                            <td>Cell 7</td>
                            <td>Cell 8</td>
                        </tr>
                        <tr>
                            <td>JP</td>
                            <td>Cell 6</td>
                            <td>Cell 7</td>
                            <td>Cell 8</td>
                        </tr>
                        <tr>
                            <td>AE</td>
                            <td>Cell 6</td>
                            <td>Cell 7</td>
                            <td>Cell 8</td>
                        </tr>
                        <tr>
                            <td>SA</td>
                            <td>Cell 6</td>
                            <td>Cell 7</td>
                            <td>Cell 8</td>
                        </tr>
                        <tr>
                            <td>EG</td>
                            <td>Cell 6</td>
                            <td>Cell 7</td>
                            <td>Cell 8</td>
                        </tr>
                        <tr>
                            <td>NL</td>
                            <td>Cell 6</td>
                            <td>Cell 7</td>
                            <td>Cell 8</td>
                        </tr>
                        <tr>
                            <td>PL</td>
                            <td>Cell 6</td>
                            <td>Cell 7</td>
                            <td>Cell 8</td>
                        </tr>
                        <tr>
                            <td>SE</td>
                            <td>Cell 6</td>
                            <td>Cell 7</td>
                            <td>Cell 8</td>
                        </tr>
                        <tr>
                            <td>TR</td>
                            <td>Cell 6</td>
                            <td>Cell 7</td>
                            <td>Cell 8</td>
                        </tr>
                        <tr>
                            <td>BE</td>
                            <td>Cell 6</td>
                            <td>Cell 7</td>
                            <td>Cell 8</td>
                        </tr>
                        <tr>
                            <td>ZA</td>
                            <td>Cell 6</td>
                            <td>Cell 7</td>
                            <td>Cell 8</td>
                        </tr>
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
                        <tr>
                            <td>US</td>
                            <td>Cell 2</td>
                            <td>Cell 3</td>
                            <td>Cell 4</td>
                        </tr>
                        <tr>
                            <td>CA</td>
                            <td>Cell 6</td>
                            <td>Cell 7</td>
                            <td>Cell 8</td>
                        </tr>
                        <tr>
                            <td>UK</td>
                            <td>Cell 6</td>
                            <td>Cell 7</td>
                            <td>Cell 8</td>
                        </tr>
                        <tr>
                            <td>IN</td>
                            <td>Cell 6</td>
                            <td>Cell 7</td>
                            <td>Cell 8</td>
                        </tr>
                        <tr>
                            <td>DE</td>
                            <td>Cell 6</td>
                            <td>Cell 7</td>
                            <td>Cell 8</td>
                        </tr>
                        <tr>
                            <td>FR</td>
                            <td>Cell 6</td>
                            <td>Cell 7</td>
                            <td>Cell 8</td>
                        </tr>
                        <tr>
                            <td>IT</td>
                            <td>Cell 6</td>
                            <td>Cell 7</td>
                            <td>Cell 8</td>
                        </tr>
                        <tr>
                            <td>ES</td>
                            <td>Cell 6</td>
                            <td>Cell 7</td>
                            <td>Cell 8</td>
                        </tr>
                        <tr>
                            <td>MX</td>
                            <td>Cell 6</td>
                            <td>Cell 7</td>
                            <td>Cell 8</td>
                        </tr>
                        <tr>
                            <td>BR</td>
                            <td>Cell 6</td>
                            <td>Cell 7</td>
                            <td>Cell 8</td>
                        </tr>
                        <tr>
                            <td>AU</td>
                            <td>Cell 6</td>
                            <td>Cell 7</td>
                            <td>Cell 8</td>
                        </tr>
                        <tr>
                            <td>SG</td>
                            <td>Cell 6</td>
                            <td>Cell 7</td>
                            <td>Cell 8</td>
                        </tr>
                        <tr>
                            <td>JP</td>
                            <td>Cell 6</td>
                            <td>Cell 7</td>
                            <td>Cell 8</td>
                        </tr>
                        <tr>
                            <td>AE</td>
                            <td>Cell 6</td>
                            <td>Cell 7</td>
                            <td>Cell 8</td>
                        </tr>
                        <tr>
                            <td>SA</td>
                            <td>Cell 6</td>
                            <td>Cell 7</td>
                            <td>Cell 8</td>
                        </tr>
                        <tr>
                            <td>EG</td>
                            <td>Cell 6</td>
                            <td>Cell 7</td>
                            <td>Cell 8</td>
                        </tr>
                        <tr>
                            <td>NL</td>
                            <td>Cell 6</td>
                            <td>Cell 7</td>
                            <td>Cell 8</td>
                        </tr>
                        <tr>
                            <td>PL</td>
                            <td>Cell 6</td>
                            <td>Cell 7</td>
                            <td>Cell 8</td>
                        </tr>
                        <tr>
                            <td>SE</td>
                            <td>Cell 6</td>
                            <td>Cell 7</td>
                            <td>Cell 8</td>
                        </tr>
                        <tr>
                            <td>TR</td>
                            <td>Cell 6</td>
                            <td>Cell 7</td>
                            <td>Cell 8</td>
                        </tr>
                        <tr>
                            <td>BE</td>
                            <td>Cell 6</td>
                            <td>Cell 7</td>
                            <td>Cell 8</td>
                        </tr>
                        <tr>
                            <td>ZA</td>
                            <td>Cell 6</td>
                            <td>Cell 7</td>
                            <td>Cell 8</td>
                        </tr>
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
                        <tr>
                            <td>US</td>
                            <td>Cell 2</td>
                            <td>Cell 3</td>
                            <td>Cell 4</td>
                        </tr>
                        <tr>
                            <td>CA</td>
                            <td>Cell 6</td>
                            <td>Cell 7</td>
                            <td>Cell 8</td>
                        </tr>
                        <tr>
                            <td>UK</td>
                            <td>Cell 6</td>
                            <td>Cell 7</td>
                            <td>Cell 8</td>
                        </tr>
                        <tr>
                            <td>IN</td>
                            <td>Cell 6</td>
                            <td>Cell 7</td>
                            <td>Cell 8</td>
                        </tr>
                        <tr>
                            <td>DE</td>
                            <td>Cell 6</td>
                            <td>Cell 7</td>
                            <td>Cell 8</td>
                        </tr>
                        <tr>
                            <td>FR</td>
                            <td>Cell 6</td>
                            <td>Cell 7</td>
                            <td>Cell 8</td>
                        </tr>
                        <tr>
                            <td>IT</td>
                            <td>Cell 6</td>
                            <td>Cell 7</td>
                            <td>Cell 8</td>
                        </tr>
                        <tr>
                            <td>ES</td>
                            <td>Cell 6</td>
                            <td>Cell 7</td>
                            <td>Cell 8</td>
                        </tr>
                        <tr>
                            <td>MX</td>
                            <td>Cell 6</td>
                            <td>Cell 7</td>
                            <td>Cell 8</td>
                        </tr>
                        <tr>
                            <td>BR</td>
                            <td>Cell 6</td>
                            <td>Cell 7</td>
                            <td>Cell 8</td>
                        </tr>
                        <tr>
                            <td>AU</td>
                            <td>Cell 6</td>
                            <td>Cell 7</td>
                            <td>Cell 8</td>
                        </tr>
                        <tr>
                            <td>SG</td>
                            <td>Cell 6</td>
                            <td>Cell 7</td>
                            <td>Cell 8</td>
                        </tr>
                        <tr>
                            <td>JP</td>
                            <td>Cell 6</td>
                            <td>Cell 7</td>
                            <td>Cell 8</td>
                        </tr>
                        <tr>
                            <td>AE</td>
                            <td>Cell 6</td>
                            <td>Cell 7</td>
                            <td>Cell 8</td>
                        </tr>
                        <tr>
                            <td>SA</td>
                            <td>Cell 6</td>
                            <td>Cell 7</td>
                            <td>Cell 8</td>
                        </tr>
                        <tr>
                            <td>EG</td>
                            <td>Cell 6</td>
                            <td>Cell 7</td>
                            <td>Cell 8</td>
                        </tr>
                        <tr>
                            <td>NL</td>
                            <td>Cell 6</td>
                            <td>Cell 7</td>
                            <td>Cell 8</td>
                        </tr>
                        <tr>
                            <td>PL</td>
                            <td>Cell 6</td>
                            <td>Cell 7</td>
                            <td>Cell 8</td>
                        </tr>
                        <tr>
                            <td>SE</td>
                            <td>Cell 6</td>
                            <td>Cell 7</td>
                            <td>Cell 8</td>
                        </tr>
                        <tr>
                            <td>TR</td>
                            <td>Cell 6</td>
                            <td>Cell 7</td>
                            <td>Cell 8</td>
                        </tr>
                        <tr>
                            <td>BE</td>
                            <td>Cell 6</td>
                            <td>Cell 7</td>
                            <td>Cell 8</td>
                        </tr>
                        <tr>
                            <td>ZA</td>
                            <td>Cell 6</td>
                            <td>Cell 7</td>
                            <td>Cell 8</td>
                        </tr>
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
                        <tr>
                            <td>US</td>
                            <td>Cell 2</td>
                            <td>Cell 3</td>
                            <td>Cell 4</td>
                        </tr>
                        <tr>
                            <td>CA</td>
                            <td>Cell 6</td>
                            <td>Cell 7</td>
                            <td>Cell 8</td>
                        </tr>
                        <tr>
                            <td>UK</td>
                            <td>Cell 6</td>
                            <td>Cell 7</td>
                            <td>Cell 8</td>
                        </tr>
                        <tr>
                            <td>IN</td>
                            <td>Cell 6</td>
                            <td>Cell 7</td>
                            <td>Cell 8</td>
                        </tr>
                        <tr>
                            <td>DE</td>
                            <td>Cell 6</td>
                            <td>Cell 7</td>
                            <td>Cell 8</td>
                        </tr>
                        <tr>
                            <td>FR</td>
                            <td>Cell 6</td>
                            <td>Cell 7</td>
                            <td>Cell 8</td>
                        </tr>
                        <tr>
                            <td>IT</td>
                            <td>Cell 6</td>
                            <td>Cell 7</td>
                            <td>Cell 8</td>
                        </tr>
                        <tr>
                            <td>ES</td>
                            <td>Cell 6</td>
                            <td>Cell 7</td>
                            <td>Cell 8</td>
                        </tr>
                        <tr>
                            <td>MX</td>
                            <td>Cell 6</td>
                            <td>Cell 7</td>
                            <td>Cell 8</td>
                        </tr>
                        <tr>
                            <td>BR</td>
                            <td>Cell 6</td>
                            <td>Cell 7</td>
                            <td>Cell 8</td>
                        </tr>
                        <tr>
                            <td>AU</td>
                            <td>Cell 6</td>
                            <td>Cell 7</td>
                            <td>Cell 8</td>
                        </tr>
                        <tr>
                            <td>SG</td>
                            <td>Cell 6</td>
                            <td>Cell 7</td>
                            <td>Cell 8</td>
                        </tr>
                        <tr>
                            <td>JP</td>
                            <td>Cell 6</td>
                            <td>Cell 7</td>
                            <td>Cell 8</td>
                        </tr>
                        <tr>
                            <td>AE</td>
                            <td>Cell 6</td>
                            <td>Cell 7</td>
                            <td>Cell 8</td>
                        </tr>
                        <tr>
                            <td>SA</td>
                            <td>Cell 6</td>
                            <td>Cell 7</td>
                            <td>Cell 8</td>
                        </tr>
                        <tr>
                            <td>EG</td>
                            <td>Cell 6</td>
                            <td>Cell 7</td>
                            <td>Cell 8</td>
                        </tr>
                        <tr>
                            <td>NL</td>
                            <td>Cell 6</td>
                            <td>Cell 7</td>
                            <td>Cell 8</td>
                        </tr>
                        <tr>
                            <td>PL</td>
                            <td>Cell 6</td>
                            <td>Cell 7</td>
                            <td>Cell 8</td>
                        </tr>
                        <tr>
                            <td>SE</td>
                            <td>Cell 6</td>
                            <td>Cell 7</td>
                            <td>Cell 8</td>
                        </tr>
                        <tr>
                            <td>TR</td>
                            <td>Cell 6</td>
                            <td>Cell 7</td>
                            <td>Cell 8</td>
                        </tr>
                        <tr>
                            <td>BE</td>
                            <td>Cell 6</td>
                            <td>Cell 7</td>
                            <td>Cell 8</td>
                        </tr>
                        <tr>
                            <td>ZA</td>
                            <td>Cell 6</td>
                            <td>Cell 7</td>
                            <td>Cell 8</td>
                        </tr>
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
                        <tr>
                            <td>US</td>
                            <td>Cell 2</td>
                            <td>Cell 3</td>
                            <td>Cell 4</td>
                        </tr>
                        <tr>
                            <td>CA</td>
                            <td>Cell 6</td>
                            <td>Cell 7</td>
                            <td>Cell 8</td>
                        </tr>
                        <tr>
                            <td>UK</td>
                            <td>Cell 6</td>
                            <td>Cell 7</td>
                            <td>Cell 8</td>
                        </tr>
                        <tr>
                            <td>IN</td>
                            <td>Cell 6</td>
                            <td>Cell 7</td>
                            <td>Cell 8</td>
                        </tr>
                        <tr>
                            <td>DE</td>
                            <td>Cell 6</td>
                            <td>Cell 7</td>
                            <td>Cell 8</td>
                        </tr>
                        <tr>
                            <td>FR</td>
                            <td>Cell 6</td>
                            <td>Cell 7</td>
                            <td>Cell 8</td>
                        </tr>
                        <tr>
                            <td>IT</td>
                            <td>Cell 6</td>
                            <td>Cell 7</td>
                            <td>Cell 8</td>
                        </tr>
                        <tr>
                            <td>ES</td>
                            <td>Cell 6</td>
                            <td>Cell 7</td>
                            <td>Cell 8</td>
                        </tr>
                        <tr>
                            <td>MX</td>
                            <td>Cell 6</td>
                            <td>Cell 7</td>
                            <td>Cell 8</td>
                        </tr>
                        <tr>
                            <td>BR</td>
                            <td>Cell 6</td>
                            <td>Cell 7</td>
                            <td>Cell 8</td>
                        </tr>
                        <tr>
                            <td>AU</td>
                            <td>Cell 6</td>
                            <td>Cell 7</td>
                            <td>Cell 8</td>
                        </tr>
                        <tr>
                            <td>SG</td>
                            <td>Cell 6</td>
                            <td>Cell 7</td>
                            <td>Cell 8</td>
                        </tr>
                        <tr>
                            <td>JP</td>
                            <td>Cell 6</td>
                            <td>Cell 7</td>
                            <td>Cell 8</td>
                        </tr>
                        <tr>
                            <td>AE</td>
                            <td>Cell 6</td>
                            <td>Cell 7</td>
                            <td>Cell 8</td>
                        </tr>
                        <tr>
                            <td>SA</td>
                            <td>Cell 6</td>
                            <td>Cell 7</td>
                            <td>Cell 8</td>
                        </tr>
                        <tr>
                            <td>EG</td>
                            <td>Cell 6</td>
                            <td>Cell 7</td>
                            <td>Cell 8</td>
                        </tr>
                        <tr>
                            <td>NL</td>
                            <td>Cell 6</td>
                            <td>Cell 7</td>
                            <td>Cell 8</td>
                        </tr>
                        <tr>
                            <td>PL</td>
                            <td>Cell 6</td>
                            <td>Cell 7</td>
                            <td>Cell 8</td>
                        </tr>
                        <tr>
                            <td>SE</td>
                            <td>Cell 6</td>
                            <td>Cell 7</td>
                            <td>Cell 8</td>
                        </tr>
                        <tr>
                            <td>TR</td>
                            <td>Cell 6</td>
                            <td>Cell 7</td>
                            <td>Cell 8</td>
                        </tr>
                        <tr>
                            <td>BE</td>
                            <td>Cell 6</td>
                            <td>Cell 7</td>
                            <td>Cell 8</td>
                        </tr>
                        <tr>
                            <td>ZA</td>
                            <td>Cell 6</td>
                            <td>Cell 7</td>
                            <td>Cell 8</td>
                        </tr>
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
                            <th>Age</th>
                            <th>Status</th>
                        </tr>
                        <tr>
                            <td>US</td>
                            <td>Cell 2</td>
                            <td>Cell 3</td>
                            <td>Cell 4</td>
                        </tr>
                        <tr>
                            <td>CA</td>
                            <td>Cell 6</td>
                            <td>Cell 7</td>
                            <td>Cell 8</td>
                        </tr>
                        <tr>
                            <td>UK</td>
                            <td>Cell 6</td>
                            <td>Cell 7</td>
                            <td>Cell 8</td>
                        </tr>
                        <tr>
                            <td>IN</td>
                            <td>Cell 6</td>
                            <td>Cell 7</td>
                            <td>Cell 8</td>
                        </tr>
                        <tr>
                            <td>DE</td>
                            <td>Cell 6</td>
                            <td>Cell 7</td>
                            <td>Cell 8</td>
                        </tr>
                        <tr>
                            <td>FR</td>
                            <td>Cell 6</td>
                            <td>Cell 7</td>
                            <td>Cell 8</td>
                        </tr>
                        <tr>
                            <td>IT</td>
                            <td>Cell 6</td>
                            <td>Cell 7</td>
                            <td>Cell 8</td>
                        </tr>
                        <tr>
                            <td>ES</td>
                            <td>Cell 6</td>
                            <td>Cell 7</td>
                            <td>Cell 8</td>
                        </tr>
                        <tr>
                            <td>MX</td>
                            <td>Cell 6</td>
                            <td>Cell 7</td>
                            <td>Cell 8</td>
                        </tr>
                        <tr>
                            <td>BR</td>
                            <td>Cell 6</td>
                            <td>Cell 7</td>
                            <td>Cell 8</td>
                        </tr>
                        <tr>
                            <td>AU</td>
                            <td>Cell 6</td>
                            <td>Cell 7</td>
                            <td>Cell 8</td>
                        </tr>
                        <tr>
                            <td>SG</td>
                            <td>Cell 6</td>
                            <td>Cell 7</td>
                            <td>Cell 8</td>
                        </tr>
                        <tr>
                            <td>JP</td>
                            <td>Cell 6</td>
                            <td>Cell 7</td>
                            <td>Cell 8</td>
                        </tr>
                        <tr>
                            <td>AE</td>
                            <td>Cell 6</td>
                            <td>Cell 7</td>
                            <td>Cell 8</td>
                        </tr>
                        <tr>
                            <td>SA</td>
                            <td>Cell 6</td>
                            <td>Cell 7</td>
                            <td>Cell 8</td>
                        </tr>
                        <tr>
                            <td>EG</td>
                            <td>Cell 6</td>
                            <td>Cell 7</td>
                            <td>Cell 8</td>
                        </tr>
                        <tr>
                            <td>NL</td>
                            <td>Cell 6</td>
                            <td>Cell 7</td>
                            <td>Cell 8</td>
                        </tr>
                        <tr>
                            <td>PL</td>
                            <td>Cell 6</td>
                            <td>Cell 7</td>
                            <td>Cell 8</td>
                        </tr>
                        <tr>
                            <td>SE</td>
                            <td>Cell 6</td>
                            <td>Cell 7</td>
                            <td>Cell 8</td>
                        </tr>
                        <tr>
                            <td>TR</td>
                            <td>Cell 6</td>
                            <td>Cell 7</td>
                            <td>Cell 8</td>
                        </tr>
                        <tr>
                            <td>BE</td>
                            <td>Cell 6</td>
                            <td>Cell 7</td>
                            <td>Cell 8</td>
                        </tr>
                        <tr>
                            <td>ZA</td>
                            <td>Cell 6</td>
                            <td>Cell 7</td>
                            <td>Cell 8</td>
                        </tr>
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
                        <tr>
                            <td>US</td>
                            <td>Cell 2</td>
                            <td>Cell 3</td>
                            <td>Cell 4</td>
                        </tr>
                        <tr>
                            <td>CA</td>
                            <td>Cell 6</td>
                            <td>Cell 7</td>
                            <td>Cell 8</td>
                        </tr>
                        <tr>
                            <td>UK</td>
                            <td>Cell 6</td>
                            <td>Cell 7</td>
                            <td>Cell 8</td>
                        </tr>
                        <tr>
                            <td>IN</td>
                            <td>Cell 6</td>
                            <td>Cell 7</td>
                            <td>Cell 8</td>
                        </tr>
                        <tr>
                            <td>DE</td>
                            <td>Cell 6</td>
                            <td>Cell 7</td>
                            <td>Cell 8</td>
                        </tr>
                        <tr>
                            <td>FR</td>
                            <td>Cell 6</td>
                            <td>Cell 7</td>
                            <td>Cell 8</td>
                        </tr>
                        <tr>
                            <td>IT</td>
                            <td>Cell 6</td>
                            <td>Cell 7</td>
                            <td>Cell 8</td>
                        </tr>
                        <tr>
                            <td>ES</td>
                            <td>Cell 6</td>
                            <td>Cell 7</td>
                            <td>Cell 8</td>
                        </tr>
                        <tr>
                            <td>MX</td>
                            <td>Cell 6</td>
                            <td>Cell 7</td>
                            <td>Cell 8</td>
                        </tr>
                        <tr>
                            <td>BR</td>
                            <td>Cell 6</td>
                            <td>Cell 7</td>
                            <td>Cell 8</td>
                        </tr>
                        <tr>
                            <td>AU</td>
                            <td>Cell 6</td>
                            <td>Cell 7</td>
                            <td>Cell 8</td>
                        </tr>
                        <tr>
                            <td>SG</td>
                            <td>Cell 6</td>
                            <td>Cell 7</td>
                            <td>Cell 8</td>
                        </tr>
                        <tr>
                            <td>JP</td>
                            <td>Cell 6</td>
                            <td>Cell 7</td>
                            <td>Cell 8</td>
                        </tr>
                        <tr>
                            <td>AE</td>
                            <td>Cell 6</td>
                            <td>Cell 7</td>
                            <td>Cell 8</td>
                        </tr>
                        <tr>
                            <td>SA</td>
                            <td>Cell 6</td>
                            <td>Cell 7</td>
                            <td>Cell 8</td>
                        </tr>
                        <tr>
                            <td>EG</td>
                            <td>Cell 6</td>
                            <td>Cell 7</td>
                            <td>Cell 8</td>
                        </tr>
                        <tr>
                            <td>NL</td>
                            <td>Cell 6</td>
                            <td>Cell 7</td>
                            <td>Cell 8</td>
                        </tr>
                        <tr>
                            <td>PL</td>
                            <td>Cell 6</td>
                            <td>Cell 7</td>
                            <td>Cell 8</td>
                        </tr>
                        <tr>
                            <td>SE</td>
                            <td>Cell 6</td>
                            <td>Cell 7</td>
                            <td>Cell 8</td>
                        </tr>
                        <tr>
                            <td>TR</td>
                            <td>Cell 6</td>
                            <td>Cell 7</td>
                            <td>Cell 8</td>
                        </tr>
                        <tr>
                            <td>BE</td>
                            <td>Cell 6</td>
                            <td>Cell 7</td>
                            <td>Cell 8</td>
                        </tr>
                        <tr>
                            <td>ZA</td>
                            <td>Cell 6</td>
                            <td>Cell 7</td>
                            <td>Cell 8</td>
                        </tr>
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
                        <tr>
                            <td>US</td>
                            <td>Cell 2</td>
                            <td>Cell 3</td>
                            <td>Cell 4</td>
                        </tr>
                        <tr>
                            <td>CA</td>
                            <td>Cell 6</td>
                            <td>Cell 7</td>
                            <td>Cell 8</td>
                        </tr>
                        <tr>
                            <td>UK</td>
                            <td>Cell 6</td>
                            <td>Cell 7</td>
                            <td>Cell 8</td>
                        </tr>
                        <tr>
                            <td>IN</td>
                            <td>Cell 6</td>
                            <td>Cell 7</td>
                            <td>Cell 8</td>
                        </tr>
                        <tr>
                            <td>DE</td>
                            <td>Cell 6</td>
                            <td>Cell 7</td>
                            <td>Cell 8</td>
                        </tr>
                        <tr>
                            <td>FR</td>
                            <td>Cell 6</td>
                            <td>Cell 7</td>
                            <td>Cell 8</td>
                        </tr>
                        <tr>
                            <td>IT</td>
                            <td>Cell 6</td>
                            <td>Cell 7</td>
                            <td>Cell 8</td>
                        </tr>
                        <tr>
                            <td>ES</td>
                            <td>Cell 6</td>
                            <td>Cell 7</td>
                            <td>Cell 8</td>
                        </tr>
                        <tr>
                            <td>MX</td>
                            <td>Cell 6</td>
                            <td>Cell 7</td>
                            <td>Cell 8</td>
                        </tr>
                        <tr>
                            <td>BR</td>
                            <td>Cell 6</td>
                            <td>Cell 7</td>
                            <td>Cell 8</td>
                        </tr>
                        <tr>
                            <td>AU</td>
                            <td>Cell 6</td>
                            <td>Cell 7</td>
                            <td>Cell 8</td>
                        </tr>
                        <tr>
                            <td>SG</td>
                            <td>Cell 6</td>
                            <td>Cell 7</td>
                            <td>Cell 8</td>
                        </tr>
                        <tr>
                            <td>JP</td>
                            <td>Cell 6</td>
                            <td>Cell 7</td>
                            <td>Cell 8</td>
                        </tr>
                        <tr>
                            <td>AE</td>
                            <td>Cell 6</td>
                            <td>Cell 7</td>
                            <td>Cell 8</td>
                        </tr>
                        <tr>
                            <td>SA</td>
                            <td>Cell 6</td>
                            <td>Cell 7</td>
                            <td>Cell 8</td>
                        </tr>
                        <tr>
                            <td>EG</td>
                            <td>Cell 6</td>
                            <td>Cell 7</td>
                            <td>Cell 8</td>
                        </tr>
                        <tr>
                            <td>NL</td>
                            <td>Cell 6</td>
                            <td>Cell 7</td>
                            <td>Cell 8</td>
                        </tr>
                        <tr>
                            <td>PL</td>
                            <td>Cell 6</td>
                            <td>Cell 7</td>
                            <td>Cell 8</td>
                        </tr>
                        <tr>
                            <td>SE</td>
                            <td>Cell 6</td>
                            <td>Cell 7</td>
                            <td>Cell 8</td>
                        </tr>
                        <tr>
                            <td>TR</td>
                            <td>Cell 6</td>
                            <td>Cell 7</td>
                            <td>Cell 8</td>
                        </tr>
                        <tr>
                            <td>BE</td>
                            <td>Cell 6</td>
                            <td>Cell 7</td>
                            <td>Cell 8</td>
                        </tr>
                        <tr>
                            <td>ZA</td>
                            <td>Cell 6</td>
                            <td>Cell 7</td>
                            <td>Cell 8</td>
                        </tr>
                    </table>
                </td>
                <td class="inner-table">
                    <table id="conc">
                        <tr>
                            <th colspan="4">Concession Level</th>
                        </tr>
                         <tr>
                            <th>Org</th>
                            <th>In Queue</th>
                            <th>Age</th>
                            <th>Status</th>
                        </tr>
                        <tr>
                            <td>US</td>
                            <td>Cell 2</td>
                            <td>Cell 3</td>
                            <td>Cell 4</td>
                        </tr>
                        <tr>
                            <td>CA</td>
                            <td>Cell 6</td>
                            <td>Cell 7</td>
                            <td>Cell 8</td>
                        </tr>
                        <tr>
                            <td>UK</td>
                            <td>Cell 6</td>
                            <td>Cell 7</td>
                            <td>Cell 8</td>
                        </tr>
                        <tr>
                            <td>IN</td>
                            <td>Cell 6</td>
                            <td>Cell 7</td>
                            <td>Cell 8</td>
                        </tr>
                        <tr>
                            <td>DE</td>
                            <td>Cell 6</td>
                            <td>Cell 7</td>
                            <td>Cell 8</td>
                        </tr>
                        <tr>
                            <td>FR</td>
                            <td>Cell 6</td>
                            <td>Cell 7</td>
                            <td>Cell 8</td>
                        </tr>
                        <tr>
                            <td>IT</td>
                            <td>Cell 6</td>
                            <td>Cell 7</td>
                            <td>Cell 8</td>
                        </tr>
                        <tr>
                            <td>ES</td>
                            <td>Cell 6</td>
                            <td>Cell 7</td>
                            <td>Cell 8</td>
                        </tr>
                        <tr>
                            <td>MX</td>
                            <td>Cell 6</td>
                            <td>Cell 7</td>
                            <td>Cell 8</td>
                        </tr>
                        <tr>
                            <td>BR</td>
                            <td>Cell 6</td>
                            <td>Cell 7</td>
                            <td>Cell 8</td>
                        </tr>
                        <tr>
                            <td>AU</td>
                            <td>Cell 6</td>
                            <td>Cell 7</td>
                            <td>Cell 8</td>
                        </tr>
                        <tr>
                            <td>SG</td>
                            <td>Cell 6</td>
                            <td>Cell 7</td>
                            <td>Cell 8</td>
                        </tr>
                        <tr>
                            <td>JP</td>
                            <td>Cell 6</td>
                            <td>Cell 7</td>
                            <td>Cell 8</td>
                        </tr>
                        <tr>
                            <td>AE</td>
                            <td>Cell 6</td>
                            <td>Cell 7</td>
                            <td>Cell 8</td>
                        </tr>
                        <tr>
                            <td>SA</td>
                            <td>Cell 6</td>
                            <td>Cell 7</td>
                            <td>Cell 8</td>
                        </tr>
                        <tr>
                            <td>EG</td>
                            <td>Cell 6</td>
                            <td>Cell 7</td>
                            <td>Cell 8</td>
                        </tr>
                        <tr>
                            <td>NL</td>
                            <td>Cell 6</td>
                            <td>Cell 7</td>
                            <td>Cell 8</td>
                        </tr>
                        <tr>
                            <td>PL</td>
                            <td>Cell 6</td>
                            <td>Cell 7</td>
                            <td>Cell 8</td>
                        </tr>
                        <tr>
                            <td>SE</td>
                            <td>Cell 6</td>
                            <td>Cell 7</td>
                            <td>Cell 8</td>
                        </tr>
                        <tr>
                            <td>TR</td>
                            <td>Cell 6</td>
                            <td>Cell 7</td>
                            <td>Cell 8</td>
                        </tr>
                        <tr>
                            <td>BE</td>
                            <td>Cell 6</td>
                            <td>Cell 7</td>
                            <td>Cell 8</td>
                        </tr>
                        <tr>
                            <td>ZA</td>
                            <td>Cell 6</td>
                            <td>Cell 7</td>
                            <td>Cell 8</td>
                        </tr>
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
                        <tr>
                            <td>US</td>
                            <td>Cell 2</td>
                            <td>Cell 3</td>
                            <td>Cell 4</td>
                        </tr>
                        <tr>
                            <td>CA</td>
                            <td>Cell 6</td>
                            <td>Cell 7</td>
                            <td>Cell 8</td>
                        </tr>
                        <tr>
                            <td>UK</td>
                            <td>Cell 6</td>
                            <td>Cell 7</td>
                            <td>Cell 8</td>
                        </tr>
                        <tr>
                            <td>IN</td>
                            <td>Cell 6</td>
                            <td>Cell 7</td>
                            <td>Cell 8</td>
                        </tr>
                        <tr>
                            <td>DE</td>
                            <td>Cell 6</td>
                            <td>Cell 7</td>
                            <td>Cell 8</td>
                        </tr>
                        <tr>
                            <td>FR</td>
                            <td>Cell 6</td>
                            <td>Cell 7</td>
                            <td>Cell 8</td>
                        </tr>
                        <tr>
                            <td>IT</td>
                            <td>Cell 6</td>
                            <td>Cell 7</td>
                            <td>Cell 8</td>
                        </tr>
                        <tr>
                            <td>ES</td>
                            <td>Cell 6</td>
                            <td>Cell 7</td>
                            <td>Cell 8</td>
                        </tr>
                        <tr>
                            <td>MX</td>
                            <td>Cell 6</td>
                            <td>Cell 7</td>
                            <td>Cell 8</td>
                        </tr>
                        <tr>
                            <td>BR</td>
                            <td>Cell 6</td>
                            <td>Cell 7</td>
                            <td>Cell 8</td>
                        </tr>
                        <tr>
                            <td>AU</td>
                            <td>Cell 6</td>
                            <td>Cell 7</td>
                            <td>Cell 8</td>
                        </tr>
                        <tr>
                            <td>SG</td>
                            <td>Cell 6</td>
                            <td>Cell 7</td>
                            <td>Cell 8</td>
                        </tr>
                        <tr>
                            <td>JP</td>
                            <td>Cell 6</td>
                            <td>Cell 7</td>
                            <td>Cell 8</td>
                        </tr>
                        <tr>
                            <td>AE</td>
                            <td>Cell 6</td>
                            <td>Cell 7</td>
                            <td>Cell 8</td>
                        </tr>
                        <tr>
                            <td>SA</td>
                            <td>Cell 6</td>
                            <td>Cell 7</td>
                            <td>Cell 8</td>
                        </tr>
                        <tr>
                            <td>EG</td>
                            <td>Cell 6</td>
                            <td>Cell 7</td>
                            <td>Cell 8</td>
                        </tr>
                        <tr>
                            <td>NL</td>
                            <td>Cell 6</td>
                            <td>Cell 7</td>
                            <td>Cell 8</td>
                        </tr>
                        <tr>
                            <td>PL</td>
                            <td>Cell 6</td>
                            <td>Cell 7</td>
                            <td>Cell 8</td>
                        </tr>
                        <tr>
                            <td>SE</td>
                            <td>Cell 6</td>
                            <td>Cell 7</td>
                            <td>Cell 8</td>
                        </tr>
                        <tr>
                            <td>TR</td>
                            <td>Cell 6</td>
                            <td>Cell 7</td>
                            <td>Cell 8</td>
                        </tr>
                        <tr>
                            <td>BE</td>
                            <td>Cell 6</td>
                            <td>Cell 7</td>
                            <td>Cell 8</td>
                        </tr>
                        <tr>
                            <td>ZA</td>
                            <td>Cell 6</td>
                            <td>Cell 7</td>
                            <td>Cell 8</td>
                        </tr>
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
                            <th>Age</th>
                            <th>Status</th>
                        </tr>
                        <tr>
                            <td>US</td>
                            <td>Cell 2</td>
                            <td>Cell 3</td>
                            <td>Cell 4</td>
                        </tr>
                        <tr>
                            <td>CA</td>
                            <td>Cell 6</td>
                            <td>Cell 7</td>
                            <td>Cell 8</td>
                        </tr>
                        <tr>
                            <td>UK</td>
                            <td>Cell 6</td>
                            <td>Cell 7</td>
                            <td>Cell 8</td>
                        </tr>
                        <tr>
                            <td>IN</td>
                            <td>Cell 6</td>
                            <td>Cell 7</td>
                            <td>Cell 8</td>
                        </tr>
                        <tr>
                            <td>DE</td>
                            <td>Cell 6</td>
                            <td>Cell 7</td>
                            <td>Cell 8</td>
                        </tr>
                        <tr>
                            <td>FR</td>
                            <td>Cell 6</td>
                            <td>Cell 7</td>
                            <td>Cell 8</td>
                        </tr>
                        <tr>
                            <td>IT</td>
                            <td>Cell 6</td>
                            <td>Cell 7</td>
                            <td>Cell 8</td>
                        </tr>
                        <tr>
                            <td>ES</td>
                            <td>Cell 6</td>
                            <td>Cell 7</td>
                            <td>Cell 8</td>
                        </tr>
                        <tr>
                            <td>MX</td>
                            <td>Cell 6</td>
                            <td>Cell 7</td>
                            <td>Cell 8</td>
                        </tr>
                        <tr>
                            <td>BR</td>
                            <td>Cell 6</td>
                            <td>Cell 7</td>
                            <td>Cell 8</td>
                        </tr>
                        <tr>
                            <td>AU</td>
                            <td>Cell 6</td>
                            <td>Cell 7</td>
                            <td>Cell 8</td>
                        </tr>
                        <tr>
                            <td>SG</td>
                            <td>Cell 6</td>
                            <td>Cell 7</td>
                            <td>Cell 8</td>
                        </tr>
                        <tr>
                            <td>JP</td>
                            <td>Cell 6</td>
                            <td>Cell 7</td>
                            <td>Cell 8</td>
                        </tr>
                        <tr>
                            <td>AE</td>
                            <td>Cell 6</td>
                            <td>Cell 7</td>
                            <td>Cell 8</td>
                        </tr>
                        <tr>
                            <td>SA</td>
                            <td>Cell 6</td>
                            <td>Cell 7</td>
                            <td>Cell 8</td>
                        </tr>
                        <tr>
                            <td>EG</td>
                            <td>Cell 6</td>
                            <td>Cell 7</td>
                            <td>Cell 8</td>
                        </tr>
                        <tr>
                            <td>NL</td>
                            <td>Cell 6</td>
                            <td>Cell 7</td>
                            <td>Cell 8</td>
                        </tr>
                        <tr>
                            <td>PL</td>
                            <td>Cell 6</td>
                            <td>Cell 7</td>
                            <td>Cell 8</td>
                        </tr>
                        <tr>
                            <td>SE</td>
                            <td>Cell 6</td>
                            <td>Cell 7</td>
                            <td>Cell 8</td>
                        </tr>
                        <tr>
                            <td>TR</td>
                            <td>Cell 6</td>
                            <td>Cell 7</td>
                            <td>Cell 8</td>
                        </tr>
                        <tr>
                            <td>BE</td>
                            <td>Cell 6</td>
                            <td>Cell 7</td>
                            <td>Cell 8</td>
                        </tr>
                        <tr>
                            <td>ZA</td>
                            <td>Cell 6</td>
                            <td>Cell 7</td>
                            <td>Cell 8</td>
                        </tr>
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
                        <tr>
                            <td>US</td>
                            <td>Cell 2</td>
                            <td>Cell 3</td>
                            <td>Cell 4</td>
                        </tr>
                        <tr>
                            <td>CA</td>
                            <td>Cell 6</td>
                            <td>Cell 7</td>
                            <td>Cell 8</td>
                        </tr>
                        <tr>
                            <td>UK</td>
                            <td>Cell 6</td>
                            <td>Cell 7</td>
                            <td>Cell 8</td>
                        </tr>
                        <tr>
                            <td>IN</td>
                            <td>Cell 6</td>
                            <td>Cell 7</td>
                            <td>Cell 8</td>
                        </tr>
                        <tr>
                            <td>DE</td>
                            <td>Cell 6</td>
                            <td>Cell 7</td>
                            <td>Cell 8</td>
                        </tr>
                        <tr>
                            <td>FR</td>
                            <td>Cell 6</td>
                            <td>Cell 7</td>
                            <td>Cell 8</td>
                        </tr>
                        <tr>
                            <td>IT</td>
                            <td>Cell 6</td>
                            <td>Cell 7</td>
                            <td>Cell 8</td>
                        </tr>
                        <tr>
                            <td>ES</td>
                            <td>Cell 6</td>
                            <td>Cell 7</td>
                            <td>Cell 8</td>
                        </tr>
                        <tr>
                            <td>MX</td>
                            <td>Cell 6</td>
                            <td>Cell 7</td>
                            <td>Cell 8</td>
                        </tr>
                        <tr>
                            <td>BR</td>
                            <td>Cell 6</td>
                            <td>Cell 7</td>
                            <td>Cell 8</td>
                        </tr>
                        <tr>
                            <td>AU</td>
                            <td>Cell 6</td>
                            <td>Cell 7</td>
                            <td>Cell 8</td>
                        </tr>
                        <tr>
                            <td>SG</td>
                            <td>Cell 6</td>
                            <td>Cell 7</td>
                            <td>Cell 8</td>
                        </tr>
                        <tr>
                            <td>JP</td>
                            <td>Cell 6</td>
                            <td>Cell 7</td>
                            <td>Cell 8</td>
                        </tr>
                        <tr>
                            <td>AE</td>
                            <td>Cell 6</td>
                            <td>Cell 7</td>
                            <td>Cell 8</td>
                        </tr>
                        <tr>
                            <td>SA</td>
                            <td>Cell 6</td>
                            <td>Cell 7</td>
                            <td>Cell 8</td>
                        </tr>
                        <tr>
                            <td>EG</td>
                            <td>Cell 6</td>
                            <td>Cell 7</td>
                            <td>Cell 8</td>
                        </tr>
                        <tr>
                            <td>NL</td>
                            <td>Cell 6</td>
                            <td>Cell 7</td>
                            <td>Cell 8</td>
                        </tr>
                        <tr>
                            <td>PL</td>
                            <td>Cell 6</td>
                            <td>Cell 7</td>
                            <td>Cell 8</td>
                        </tr>
                        <tr>
                            <td>SE</td>
                            <td>Cell 6</td>
                            <td>Cell 7</td>
                            <td>Cell 8</td>
                        </tr>
                        <tr>
                            <td>TR</td>
                            <td>Cell 6</td>
                            <td>Cell 7</td>
                            <td>Cell 8</td>
                        </tr>
                        <tr>
                            <td>BE</td>
                            <td>Cell 6</td>
                            <td>Cell 7</td>
                            <td>Cell 8</td>
                        </tr>
                        <tr>
                            <td>ZA</td>
                            <td>Cell 6</td>
                            <td>Cell 7</td>
                            <td>Cell 8</td>
                        </tr>
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
                        <tr>
                            <td>US</td>
                            <td>Cell 2</td>
                            <td>Cell 3</td>
                            <td>Cell 4</td>
                        </tr>
                        <tr>
                            <td>CA</td>
                            <td>Cell 6</td>
                            <td>Cell 7</td>
                            <td>Cell 8</td>
                        </tr>
                        <tr>
                            <td>UK</td>
                            <td>Cell 6</td>
                            <td>Cell 7</td>
                            <td>Cell 8</td>
                        </tr>
                        <tr>
                            <td>IN</td>
                            <td>Cell 6</td>
                            <td>Cell 7</td>
                            <td>Cell 8</td>
                        </tr>
                        <tr>
                            <td>DE</td>
                            <td>Cell 6</td>
                            <td>Cell 7</td>
                            <td>Cell 8</td>
                        </tr>
                        <tr>
                            <td>FR</td>
                            <td>Cell 6</td>
                            <td>Cell 7</td>
                            <td>Cell 8</td>
                        </tr>
                        <tr>
                            <td>IT</td>
                            <td>Cell 6</td>
                            <td>Cell 7</td>
                            <td>Cell 8</td>
                        </tr>
                        <tr>
                            <td>ES</td>
                            <td>Cell 6</td>
                            <td>Cell 7</td>
                            <td>Cell 8</td>
                        </tr>
                        <tr>
                            <td>MX</td>
                            <td>Cell 6</td>
                            <td>Cell 7</td>
                            <td>Cell 8</td>
                        </tr>
                        <tr>
                            <td>BR</td>
                            <td>Cell 6</td>
                            <td>Cell 7</td>
                            <td>Cell 8</td>
                        </tr>
                        <tr>
                            <td>AU</td>
                            <td>Cell 6</td>
                            <td>Cell 7</td>
                            <td>Cell 8</td>
                        </tr>
                        <tr>
                            <td>SG</td>
                            <td>Cell 6</td>
                            <td>Cell 7</td>
                            <td>Cell 8</td>
                        </tr>
                        <tr>
                            <td>JP</td>
                            <td>Cell 6</td>
                            <td>Cell 7</td>
                            <td>Cell 8</td>
                        </tr>
                        <tr>
                            <td>AE</td>
                            <td>Cell 6</td>
                            <td>Cell 7</td>
                            <td>Cell 8</td>
                        </tr>
                        <tr>
                            <td>SA</td>
                            <td>Cell 6</td>
                            <td>Cell 7</td>
                            <td>Cell 8</td>
                        </tr>
                        <tr>
                            <td>EG</td>
                            <td>Cell 6</td>
                            <td>Cell 7</td>
                            <td>Cell 8</td>
                        </tr>
                        <tr>
                            <td>NL</td>
                            <td>Cell 6</td>
                            <td>Cell 7</td>
                            <td>Cell 8</td>
                        </tr>
                        <tr>
                            <td>PL</td>
                            <td>Cell 6</td>
                            <td>Cell 7</td>
                            <td>Cell 8</td>
                        </tr>
                        <tr>
                            <td>SE</td>
                            <td>Cell 6</td>
                            <td>Cell 7</td>
                            <td>Cell 8</td>
                        </tr>
                        <tr>
                            <td>TR</td>
                            <td>Cell 6</td>
                            <td>Cell 7</td>
                            <td>Cell 8</td>
                        </tr>
                        <tr>
                            <td>BE</td>
                            <td>Cell 6</td>
                            <td>Cell 7</td>
                            <td>Cell 8</td>
                        </tr>
                        <tr>
                            <td>ZA</td>
                            <td>Cell 6</td>
                            <td>Cell 7</td>
                            <td>Cell 8</td>
                        </tr>
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
                        <tr>
                            <td>US</td>
                            <td>Cell 2</td>
                            <td>Cell 3</td>
                            <td>Cell 4</td>
                        </tr>
                        <tr>
                            <td>CA</td>
                            <td>Cell 6</td>
                            <td>Cell 7</td>
                            <td>Cell 8</td>
                        </tr>
                        <tr>
                            <td>UK</td>
                            <td>Cell 6</td>
                            <td>Cell 7</td>
                            <td>Cell 8</td>
                        </tr>
                        <tr>
                            <td>IN</td>
                            <td>Cell 6</td>
                            <td>Cell 7</td>
                            <td>Cell 8</td>
                        </tr>
                        <tr>
                            <td>DE</td>
                            <td>Cell 6</td>
                            <td>Cell 7</td>
                            <td>Cell 8</td>
                        </tr>
                        <tr>
                            <td>FR</td>
                            <td>Cell 6</td>
                            <td>Cell 7</td>
                            <td>Cell 8</td>
                        </tr>
                        <tr>
                            <td>IT</td>
                            <td>Cell 6</td>
                            <td>Cell 7</td>
                            <td>Cell 8</td>
                        </tr>
                        <tr>
                            <td>ES</td>
                            <td>Cell 6</td>
                            <td>Cell 7</td>
                            <td>Cell 8</td>
                        </tr>
                        <tr>
                            <td>MX</td>
                            <td>Cell 6</td>
                            <td>Cell 7</td>
                            <td>Cell 8</td>
                        </tr>
                        <tr>
                            <td>BR</td>
                            <td>Cell 6</td>
                            <td>Cell 7</td>
                            <td>Cell 8</td>
                        </tr>
                        <tr>
                            <td>AU</td>
                            <td>Cell 6</td>
                            <td>Cell 7</td>
                            <td>Cell 8</td>
                        </tr>
                        <tr>
                            <td>SG</td>
                            <td>Cell 6</td>
                            <td>Cell 7</td>
                            <td>Cell 8</td>
                        </tr>
                        <tr>
                            <td>JP</td>
                            <td>Cell 6</td>
                            <td>Cell 7</td>
                            <td>Cell 8</td>
                        </tr>
                        <tr>
                            <td>AE</td>
                            <td>Cell 6</td>
                            <td>Cell 7</td>
                            <td>Cell 8</td>
                        </tr>
                        <tr>
                            <td>SA</td>
                            <td>Cell 6</td>
                            <td>Cell 7</td>
                            <td>Cell 8</td>
                        </tr>
                        <tr>
                            <td>EG</td>
                            <td>Cell 6</td>
                            <td>Cell 7</td>
                            <td>Cell 8</td>
                        </tr>
                        <tr>
                            <td>NL</td>
                            <td>Cell 6</td>
                            <td>Cell 7</td>
                            <td>Cell 8</td>
                        </tr>
                        <tr>
                            <td>PL</td>
                            <td>Cell 6</td>
                            <td>Cell 7</td>
                            <td>Cell 8</td>
                        </tr>
                        <tr>
                            <td>SE</td>
                            <td>Cell 6</td>
                            <td>Cell 7</td>
                            <td>Cell 8</td>
                        </tr>
                        <tr>
                            <td>TR</td>
                            <td>Cell 6</td>
                            <td>Cell 7</td>
                            <td>Cell 8</td>
                        </tr>
                        <tr>
                            <td>BE</td>
                            <td>Cell 6</td>
                            <td>Cell 7</td>
                            <td>Cell 8</td>
                        </tr>
                        <tr>
                            <td>ZA</td>
                            <td>Cell 6</td>
                            <td>Cell 7</td>
                            <td>Cell 8</td>
                        </tr>
                    </table>
                </td>
                <td class="inner-table">
                    <table id="table15">
                        <tr>
                            <th colspan="4">Table 15</th>
                        </tr>
                         <tr>
                            <th>Org</th>
                            <th>In Queue</th>
                            <th>Age</th>
                            <th>Status</th>
                        </tr>
                        <tr>
                            <td>US</td>
                            <td>Cell 2</td>
                            <td>Cell 3</td>
                            <td>Cell 4</td>
                        </tr>
                        <tr>
                            <td>CA</td>
                            <td>Cell 6</td>
                            <td>Cell 7</td>
                            <td>Cell 8</td>
                        </tr>
                        <tr>
                            <td>UK</td>
                            <td>Cell 6</td>
                            <td>Cell 7</td>
                            <td>Cell 8</td>
                        </tr>
                        <tr>
                            <td>IN</td>
                            <td>Cell 6</td>
                            <td>Cell 7</td>
                            <td>Cell 8</td>
                        </tr>
                        <tr>
                            <td>DE</td>
                            <td>Cell 6</td>
                            <td>Cell 7</td>
                            <td>Cell 8</td>
                        </tr>
                        <tr>
                            <td>FR</td>
                            <td>Cell 6</td>
                            <td>Cell 7</td>
                            <td>Cell 8</td>
                        </tr>
                        <tr>
                            <td>IT</td>
                            <td>Cell 6</td>
                            <td>Cell 7</td>
                            <td>Cell 8</td>
                        </tr>
                        <tr>
                            <td>ES</td>
                            <td>Cell 6</td>
                            <td>Cell 7</td>
                            <td>Cell 8</td>
                        </tr>
                        <tr>
                            <td>MX</td>
                            <td>Cell 6</td>
                            <td>Cell 7</td>
                            <td>Cell 8</td>
                        </tr>
                        <tr>
                            <td>BR</td>
                            <td>Cell 6</td>
                            <td>Cell 7</td>
                            <td>Cell 8</td>
                        </tr>
                        <tr>
                            <td>AU</td>
                            <td>Cell 6</td>
                            <td>Cell 7</td>
                            <td>Cell 8</td>
                        </tr>
                        <tr>
                            <td>SG</td>
                            <td>Cell 6</td>
                            <td>Cell 7</td>
                            <td>Cell 8</td>
                        </tr>
                        <tr>
                            <td>JP</td>
                            <td>Cell 6</td>
                            <td>Cell 7</td>
                            <td>Cell 8</td>
                        </tr>
                        <tr>
                            <td>AE</td>
                            <td>Cell 6</td>
                            <td>Cell 7</td>
                            <td>Cell 8</td>
                        </tr>
                        <tr>
                            <td>SA</td>
                            <td>Cell 6</td>
                            <td>Cell 7</td>
                            <td>Cell 8</td>
                        </tr>
                        <tr>
                            <td>EG</td>
                            <td>Cell 6</td>
                            <td>Cell 7</td>
                            <td>Cell 8</td>
                        </tr>
                        <tr>
                            <td>NL</td>
                            <td>Cell 6</td>
                            <td>Cell 7</td>
                            <td>Cell 8</td>
                        </tr>
                        <tr>
                            <td>PL</td>
                            <td>Cell 6</td>
                            <td>Cell 7</td>
                            <td>Cell 8</td>
                        </tr>
                        <tr>
                            <td>SE</td>
                            <td>Cell 6</td>
                            <td>Cell 7</td>
                            <td>Cell 8</td>
                        </tr>
                        <tr>
                            <td>TR</td>
                            <td>Cell 6</td>
                            <td>Cell 7</td>
                            <td>Cell 8</td>
                        </tr>
                        <tr>
                            <td>BE</td>
                            <td>Cell 6</td>
                            <td>Cell 7</td>
                            <td>Cell 8</td>
                        </tr>
                        <tr>
                            <td>ZA</td>
                            <td>Cell 6</td>
                            <td>Cell 7</td>
                            <td>Cell 8</td>
                        </tr>
                    </table>
                </td>
            </tr>
        </table>
    </body>
    </html>
    """
