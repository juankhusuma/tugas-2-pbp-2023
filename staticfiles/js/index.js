const cards = document.querySelector('.cards');
const rupiah = (number) => {
    return new Intl.NumberFormat("id-ID", {
        style: "currency",
        currency: "IDR"
    }).format(number);
}

document.addEventListener('DOMContentLoaded', async () => {
    const res = await fetch('/json');
    const data = await res.json();
    data.map(model => {
        const cardHTML = `
            <div class="product" id=${"ZCZC" + model.pk}>
            <h1 class="product__name">${model.fields.name}</h1>
            <p class="">${rupiah(model.fields.price)}</p>
            <p class="">Stok: ${model.fields.amount}</p>
            <div>
                <form action="/increment/${model.pk}/" method="post">
                    <input type="submit" value="+">
                </form>
                <form action="/decrement/${model.pk}/" method="post">
                    <input type="submit" value="-">
                </form>
                <form action="/delete/${model.pk}/" method="post">
                    <input style="color: red; font-weight: bold;" type="submit" value="x">
                </form>
            </div>
        </div>
        `
        cards.innerHTML += cardHTML;
    });
});

const addBtn = document.querySelector('#button_add');

addBtn.addEventListener('click', async () => {
    const res = await fetch("/create-ajax", {
        method: "POST",
        body: new FormData(document.querySelector('#form'))
    })
    const pk = await res.text();

    const name = document.querySelector('#name').value;
    const price = document.querySelector('#price').value;
    const amount = document.querySelector('#amount').value;

    cards.innerHTML += `
        <div class="product" id=${pk}>
            <h1 class="product__name">${name}</h1>
            <p class="">${rupiah(price)}</p>
            <p class="">Stok: ${amount}</p>
            <div>
                <form action="/increment/${pk}/" method="post">
                    <input type="submit" value="+">
                </form>
                <form action="/decrement/${pk}/" method="post">
                    <input type="submit" value="-">
                </form>
                <form action="/delete/${pk}/" method="post">
                    <input style="color: red; font-weight: bold;" type="submit" value="x">
                </form>
            </div>
        </div>
    `;

});