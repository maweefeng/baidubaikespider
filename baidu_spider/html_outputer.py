class HtmlOutputer(object):
    def __init__(self):
        self.datas = []

    def collect_data(self, data):
        if data is None:
            return
        print(data)
        self.datas.append(data)

        pass

    def output_html(self):
        fout = open("formatter.html", "w")
        fout.write("""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <meta http-equiv="X-UA-Compatible" content="ie=edge">
            <title>Document</title>
            <!-- 最新版本的 Bootstrap 核心 CSS 文件 -->
            <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@3.3.7/dist/css/bootstrap.min.css"
            integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u" crossorigin="anonymous">
            <!-- 最新的 Bootstrap 核心 JavaScript 文件 -->
            <script src="https://cdn.jsdelivr.net/npm/bootstrap@3.3.7/dist/js/bootstrap.min.js"
            integrity="sha384-Tc5IQib027qvyjSMfHjOMaLkfuWVxZxUPnCJA7l2mCWNIpG9mGCD8wGNIcPD7Txa" crossorigin="anonymous">
            </script>
        </head>
        """
        )
        fout.write("<body>")
        fout.write('<table class="table table-bordered">')
        fout.write('<thead>')
        fout.write('<tr>')
        fout.write('<th>标题</th>')
        fout.write('<th>摘要</th>')
        fout.write("</tr>")
        fout.write('</thead>')
        for data in self.datas:
            fout.write('<tr class="active">')
            # fout.write('<td>%s</td>'% data['url'])
            fout.write('<td class="active">%s</td>' % data["title"])
            fout.write('<td class="active">%s</td>' % data["summary"])
            fout.write("</tr>")
        fout.write("</table>")
        fout.write("</body>")
        fout.write("</html>")

        pass
