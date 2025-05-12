var str = $response.body;

var json = JSON.parse(str);

var url = $request.url;

var myDate = new Date();
var year = myDate.getFullYear();
var month = myDate.getMonth() + 1;
var date = myDate.getDate();
if (month < 10) {
    month = "0" + month;
}
if (date < 10) {
    date = "0" + date;
}
var dateStr = year + "-" + month + "-" + date;
var dateSugStr = year + " " + month + " " + (date - 1);
if (url.endsWith('%E5%AE%A1%E6%A0%B8%E9%80%9A%E8%BF%87') || url.endsWith('all')) {
    json.rows[0].outtimetext = dateStr + ' 08:35:59';
    json.rows[0].backtimetext = dateStr + ' 23:35:59';
    json.rows[0].verifier1text = '审批通过';
    json.rows[0].verifier2suggestiontext = ' 审批人：李欢欢，审批时间：' + dateSugStr + ' 16:04:18';
} else if (url.indexOf('zhaji=') != -1) {
    json.rows[0].verifier1text = '审批通过';
    json.rows[0].verifier2suggestiontext = ' 审批人：李欢欢，审批时间：' + dateSugStr + ' 16:04:18';
}

$done({ body: JSON.stringify(json) });