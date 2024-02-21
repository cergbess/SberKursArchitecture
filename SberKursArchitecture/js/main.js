document.addEventListener("DOMContentLoaded", doit);

function doit() {
	var h1 = document.createElement("h1");
	h1.innerText = "Credit payments";

	var form = document.createElement("form");
	form.id = "form01";
	form.method = "get";
	form.action = "/cgi-bin/form.py";

	var deal_id_input = document.createElement("input");
	deal_id_input.id = "deal_id";
	deal_id_input.type = "number";
	deal_id_input.name = "deal_id";
	deal_id_input.required = true;

	var date = document.createElement("input");
	date.id = "date";
	date.type = "text";
	date.name = "date";
	date.pattern = "[0-9]{2}.[0-9]{4}";
	date.required = true;

	var submit = document.createElement("input");
	submit.className = "btn btn-success";
	submit.type = "submit";
	submit.id = "submit01";
	submit.value = "Submit";

	var br1 = document.createElement("br");
	var br2 = document.createElement("br");

	form.appendChild(deal_id_input);
	form.appendChild(br1);
	form.appendChild(date);
	form.appendChild(br2);
	form.appendChild(submit);

	root.appendChild(h1);
	root.appendChild(form);
}
