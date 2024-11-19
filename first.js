function show(pageName, filterValue)

{

var newUrl = baseUrl + "&pageName=" + pageName;

if(null != filterValue && "" != filterValue)

{

newUrl += "&$filter=Industries/Industry eq '" + filterValue + "'";

}

//Assumes there's an iFrame on the page with id="iFrame"

// var report = document.getElementById("iFrame")

// report.src = "https://app.powerbi.com/view?r=eyJrIjoiODJkYjY5YmUtNzVkYi00MjRjLWFmZmMtZDk4MmM5ZmZkZTMxIiwidCI6ImY0YjI5ZTNmLTlmY2MtNDg4Yy1hMDFkLTRiNjAyZGNhMjVhYiJ9" frameborder="0" allowFullScreen="true"></iframe>";

// }/

var embedsittings={
    type:'report',
    id:
}