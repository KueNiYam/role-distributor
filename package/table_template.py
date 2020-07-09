TABLE = """
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>역할 분배 결과</title>
    <link rel="stylesheet" type="text/css" href="style.css">
</head>
<body>
    <div>
        <h2>역할 분배 결과</h2>
    </div>
    <table>
        <tr>
            <th class="th_role">역할</th>
            <th class="th_person">이름</th>
        </tr>
            {rows}
    </table>
</body>
</html>
"""

ROW = """
    <tr>
        <td>{role}</td>
        <td class="td_person">{person}</td>
    </tr>"""