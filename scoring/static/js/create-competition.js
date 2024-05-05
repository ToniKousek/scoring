// ! to do: NEVER WRITE JAVASCRIPT ANYMORE
// I hate this
competitors_num = 0;
fields_num = 0;

function add_competitor() {
  ++competitors_num;
  const inputElement = document.createElement("input");
  inputElement.setAttribute("id", `competitor${competitors_num}`);
  inputElement.setAttribute("name", `competitor${competitors_num}`);
  const labelElement = document.createElement("label");
  labelElement.setAttribute("for", `competitor${competitors_num}`);

  const text = document.createTextNode(`Competitor ${competitors_num} name:`);
  labelElement.appendChild(text);

  const div = document.createElement("div");
  inputElement.setAttribute("class", `competitor${competitors_num} competitor`);
  div.appendChild(labelElement);
  div.appendChild(inputElement);

  const form = document.getElementById("competitors-form");
  form.appendChild(div);
}

function add_field() {
  ++fields_num;
  const inputElement = document.createElement("input");
  inputElement.setAttribute("id", `field-name${fields_num}`);
  inputElement.setAttribute("name", `field-name${fields_num}`);
  inputElement.setAttribute("type", "name");
  const labelElement = document.createElement("label");
  labelElement.setAttribute("for", `field-name${fields_num}`);

  const text = document.createTextNode(`Field ${competitors_num} name:`);
  labelElement.appendChild(text);

  const rangeElement = document.createElement("input");
  rangeElement.setAttribute("id", `field-max${fields_num}`);
  rangeElement.setAttribute("name", `field-max${fields_num}`);
  rangeElement.setAttribute("type", "number");
  const rLabelElement = document.createElement("label");
  rLabelElement.setAttribute("for", `field-max${fields_num}`);

  const textRange = document.createTextNode(
    `Field ${competitors_num} max-range:`
  );
  rLabelElement.appendChild(textRange);

  const form = document.getElementById("fields-form");
  const div = document.createElement("div");
  inputElement.setAttribute("class", `competitor${competitors_num} competitor`);
  div.appendChild(labelElement);
  div.appendChild(inputElement);
  div.appendChild(rLabelElement);
  div.appendChild(rangeElement);

  form.appendChild(div);
}

add_competitor();
add_field();
