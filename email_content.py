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
                    <table id="table1">
                        <tr>
                            <th colspan="4">Table 1</th>
                        </tr>
                        <tr>
                            <th>Header 1</th>
                            <th>Header 2</th>
                            <th>Header 3</th>
                            <th>Header 4</th>
                        </tr>
                        <tr>
                            <td>Cell 1</td>
                            <td>Cell 2</td>
                            <td>Cell 3</td>
                            <td>Cell 4</td>
                        </tr>
                        <tr>
                            <td>Cell 5</td>
                            <td>Cell 6</td>
                            <td>Cell 7</td>
                            <td>Cell 8</td>
                        </tr>
                    </table>
                </td>
                <td class="inner-table">
                    <table id="table2">
                        <tr>
                            <th colspan="4">Table 2</th>
                        </tr>
                        <tr>
                            <th>Header 1</th>
                            <th>Header 2</th>
                            <th>Header 3</th>
                            <th>Header 4</th>
                        </tr>
                        <tr>
                            <td>Cell 1</td>
                            <td>Cell 2</td>
                            <td>Cell 3</td>
                            <td>Cell 4</td>
                        </tr>
                        <tr>
                            <td>Cell 5</td>
                            <td>Cell 6</td>
                            <td>Cell 7</td>
                            <td>Cell 8</td>
                        </tr>
                    </table>
                </td>
                <td class="inner-table">
                    <table id="table3">
                        <tr>
                            <th colspan="4">Table 3</th>
                        </tr>
                        <tr>
                            <th>Header 1</th>
                            <th>Header 2</th>
                            <th>Header 3</th>
                            <th>Header 4</th>
                        </tr>
                        <tr>
                            <td>Cell 1</td>
                            <td>Cell 2</td>
                            <td>Cell 3</td>
                            <td>Cell 4</td>
                        </tr>
                        <tr>
                            <td>Cell 5</td>
                            <td>Cell 6</td>
                            <td>Cell 7</td>
                            <td>Cell 8</td>
                        </tr>
                    </table>
                </td>
                <td class="inner-table">
                    <table id="table4">
                        <tr>
                            <th colspan="4">Table 4</th>
                        </tr>
                        <tr>
                            <th>Header 1</th>
                            <th>Header 2</th>
                            <th>Header 3</th>
                            <th>Header 4</th>
                        </tr>
                        <tr>
                            <td>Cell 1</td>
                            <td>Cell 2</td>
                            <td>Cell 3</td>
                            <td>Cell 4</td>
                        </tr>
                        <tr>
                            <td>Cell 5</td>
                            <td>Cell 6</td>
                            <td>Cell 7</td>
                            <td>Cell 8</td>
                        </tr>
                    </table>
                </td>
                <td class="inner-table">
                    <table id="table5">
                        <tr>
                            <th colspan="4">Table 5</th>
                        </tr>
                        <tr>
                            <th>Header 1</th>
                            <th>Header 2</th>
                            <th>Header 3</th>
                            <th>Header 4</th>
                        </tr>
                        <tr>
                            <td>Cell 1</td>
                            <td>Cell 2</td>
                            <td>Cell 3</td>
                            <td>Cell 4</td>
                        </tr>
                        <tr>
                            <td>Cell 5</td>
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
                    <table id="table6">
                        <tr>
                            <th colspan="4">Table 6</th>
                        </tr>
                        <tr>
                            <th>Header 1</th>
                            <th>Header 2</th>
                            <th>Header 3</th>
                            <th>Header 4</th>
                        </tr>
                        <tr>
                            <td>Cell 1</td>
                            <td>Cell 2</td>
                            <td>Cell 3</td>
                            <td>Cell 4</td>
                        </tr>
                        <tr>
                            <td>Cell 5</td>
                            <td>Cell 6</td>
                            <td>Cell 7</td>
                            <td>Cell 8</td>
                        </tr>
                    </table>
                </td>
                <td class="inner-table">
                    <table id="table7">
                        <tr>
                            <th colspan="4">Table 7</th>
                        </tr>
                        <tr>
                            <th>Header 1</th>
                            <th>Header 2</th>
                            <th>Header 3</th>
                            <th>Header 4</th>
                        </tr>
                        <tr>
                            <td>Cell 1</td>
                            <td>Cell 2</td>
                            <td>Cell 3</td>
                            <td>Cell 4</td>
                        </tr>
                        <tr>
                            <td>Cell 5</td>
                            <td>Cell 6</td>
                            <td>Cell 7</td>
                            <td>Cell 8</td>
                        </tr>
                    </table>
                </td>
                <td class="inner-table">
                    <table id="table8">
                        <tr>
                            <th colspan="4">Table 8</th>
                        </tr>
                        <tr>
                            <th>Header 1</th>
                            <th>Header 2</th>
                            <th>Header 3</th>
                            <th>Header 4</th>
                        </tr>
                        <tr>
                            <td>Cell 1</td>
                            <td>Cell 2</td>
                            <td>Cell 3</td>
                            <td>Cell 4</td>
                        </tr>
                        <tr>
                            <td>Cell 5</td>
                            <td>Cell 6</td>
                            <td>Cell 7</td>
                            <td>Cell 8</td>
                        </tr>
                    </table>
                </td>
                <td class="inner-table">
                    <table id="table9">
                        <tr>
                            <th colspan="4">Table 9</th>
                        </tr>
                        <tr>
                            <th>Header 1</th>
                            <th>Header 2</th>
                            <th>Header 3</th>
                            <th>Header 4</th>
                        </tr>
                        <tr>
                            <td>Cell 1</td>
                            <td>Cell 2</td>
                            <td>Cell 3</td>
                            <td>Cell 4</td>
                        </tr>
                        <tr>
                            <td>Cell 5</td>
                            <td>Cell 6</td>
                            <td>Cell 7</td>
                            <td>Cell 8</td>
                        </tr>
                    </table>
                </td>
                <td class="inner-table">
                    <table id="table10">
                        <tr>
                            <th colspan="4">Table 10</th>
                        </tr>
                        <tr>
                            <th>Header 1</th>
                            <th>Header 2</th>
                            <th>Header 3</th>
                            <th>Header 4</th>
                        </tr>
                        <tr>
                            <td>Cell 1</td>
                            <td>Cell 2</td>
                            <td>Cell 3</td>
                            <td>Cell 4</td>
                        </tr>
                        <tr>
                            <td>Cell 5</td>
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
                    <table id="table11">
                        <tr>
                            <th colspan="4">Table 11</th>
                        </tr>
                        <tr>
                            <th>Header 1</th>
                            <th>Header 2</th>
                            <th>Header 3</th>
                            <th>Header 4</th>
                        </tr>
                        <tr>
                            <td>Cell 1</td>
                            <td>Cell 2</td>
                            <td>Cell 3</td>
                            <td>Cell 4</td>
                        </tr>
                        <tr>
                            <td>Cell 5</td>
                            <td>Cell 6</td>
                            <td>Cell 7</td>
                            <td>Cell 8</td>
                        </tr>
                    </table>
                </td>
                <td class="inner-table">
                    <table id="table12">
                        <tr>
                            <th colspan="4">Table 12</th>
                        </tr>
                        <tr>
                            <th>Header 1</th>
                            <th>Header 2</th>
                            <th>Header 3</th>
                            <th>Header 4</th>
                        </tr>
                        <tr>
                            <td>Cell 1</td>
                            <td>Cell 2</td>
                            <td>Cell 3</td>
                            <td>Cell 4</td>
                        </tr>
                        <tr>
                            <td>Cell 5</td>
                            <td>Cell 6</td>
                            <td>Cell 7</td>
                            <td>Cell 8</td>
                        </tr>
                    </table>
                </td>
                <td class="inner-table">
                    <table id="table13">
                        <tr>
                            <th colspan="4">Table 13</th>
                        </tr>
                        <tr>
                            <th>Header 1</th>
                            <th>Header 2</th>
                            <th>Header 3</th>
                            <th>Header 4</th>
                        </tr>
                        <tr>
                            <td>Cell 1</td>
                            <td>Cell 2</td>
                            <td>Cell 3</td>
                            <td>Cell 4</td>
                        </tr>
                        <tr>
                            <td>Cell 5</td>
                            <td>Cell 6</td>
                            <td>Cell 7</td>
                            <td>Cell 8</td>
                        </tr>
                    </table>
                </td>
                <td class="inner-table">
                    <table id="table14">
                        <tr>
                            <th colspan="4">Table 14</th>
                        </tr>
                        <tr>
                            <th>Header 1</th>
                            <th>Header 2</th>
                            <th>Header 3</th>
                            <th>Header 4</th>
                        </tr>
                        <tr>
                            <td>Cell 1</td>
                            <td>Cell 2</td>
                            <td>Cell 3</td>
                            <td>Cell 4</td>
                        </tr>
                        <tr>
                            <td>Cell 5</td>
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
                            <th>Header 1</th>
                            <th>Header 2</th>
                            <th>Header 3</th>
                            <th>Header 4</th>
                        </tr>
                        <tr>
                            <td>Cell 1</td>
                            <td>Cell 2</td>
                            <td>Cell 3</td>
                            <td>Cell 4</td>
                        </tr>
                        <tr>
                            <td>Cell 5</td>
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
