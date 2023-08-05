<script>
  import { onMount } from "svelte";

  let name = '';
  let phone = '';
  let ordering = false;
  let categories = [];
  let menus = [];
  let selectedMenu = null;
  let options = [];
  let selectedOptions = [];
  let ordererId = null;
  let orderDetail = null;
  let cart = [];

  onMount(async () => {
    const res = await fetch('http://127.0.0.1:8000/categories');
    categories = await res.json();
  });

  async function startOrder() {
    const res = await fetch('http://127.0.0.1:8000/new_orderer', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({ name, phone })
    });
    const data = await res.json();
    ordererId = data.orderer_id;
    ordering = true;
  }

  async function selectCategory(category_pk) {
    const res = await fetch(`http://127.0.0.1:8000/menu/${category_pk}`);
    menus = await res.json();
  }

  function selectMenu(menu) {
    selectedMenu = menu;
  }

  function selectOption(option) {
    selectedOptions.push(option);
  }

  function addToCart() {
    cart.push({ menu: selectedMenu, options: selectedOptions });
    selectedMenu = null;
    selectedOptions = [];
  }

  async function completeOrder() {
    for (const item of cart) {
      const res = await fetch(`http://127.0.0.1:8000/order/${ordererId}`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({
          menu_pk: item.menu.menu_pk,
          options: item.options.map(option => option.option_pk)
        })
      });
      orderDetail = await res.json();
    }
    cart = [];
    ordering = false;
  }

  async function getOrderDetail() {
    const res = await fetch(`http://127.0.0.1:8000/order_check/${ordererId}`);
    orderDetail = await res.json();
  }
</script>

<main>
  {#if ordering}
    <div>
      <h2>Categories</h2>
      <ul>
        {#each categories as category (category.category_pk)}
          <li>
            <button on:click={() => selectCategory(category.category_pk)}>{category.category_name}</button>
          </li>
        {/each}
      </ul>

      <h2>Menus</h2>
      <ul>
        {#each menus as menu (menu.menu_pk)}
          <li>
            <button on:click={() => selectMenu(menu)}>{menu.menu_name}</button>
          </li>
        {/each}
      </ul>

      {#if selectedMenu}
        <h2>Options for {selectedMenu.menu_name}</h2>
        <ul>
          {#each options as option (option.option_pk)}
            <li>
              <button on:click={() => selectOption(option)}>{option.option_name}</button>
            </li>
          {/each}
        </ul>
        <button on:click={addToCart}>Add to Cart</button>
      {/if}

      <h2>Cart</h2>
      <ul>
        {#each cart as item (item.menu.menu_pk)}
          <li>
            {item.menu.menu_name} - {item.options.map(option => option.option_name).join(', ')}
          </li>
        {/each}
      </ul>

      <button on:click={completeOrder}>Complete Order</button>
    </div>
  {:else}
    <h1>Welcome to our FastFood Order System!</h1>
    <input bind:value={name} placeholder="Your Name" />
    <input bind:value={phone} placeholder="Your Phone Number" />
    <button on:click={startOrder}>Start Order</button>

    <!-- Show order detail after completing an order... -->
    {#if orderDetail}
      <button on:click={getOrderDetail}>Show Order Detail</button>

      <!-- Display order detail here... -->
      <div>
        <h2>Order Details:</h2>
        {#each orderDetail.orders as order (order.menu_name)}
          <div>
            <h3>{order.menu_name}</h3>
            <p>Price: {order.total_price}</p>
            <h4>Options:</h4>
            {#each order.options as option (option.option_name)}
              <div>
                <span>{option.option_name}: </span>
                <span>{option.option_price}</span>
              </div>
            {/each}
          </div>
        {/each}
      </div>
    {/if}
  {/if}
</main>
<style>
  main {
    font-family: Arial, sans-serif;
    margin: 0 auto;
    max-width: 800px;
    padding: 20px;
  }
  
  h1, h2, h3, h4 {
    color: #333;
  }
  
  button {
    background-color: #4CAF50;
    border: none;
    color: white;
    padding: 15px 32px;
    text-align: center;
    text-decoration: none;
    display: inline-block;
    font-size: 16px;
    margin: 4px 2px;
    cursor: pointer;
  }
  
  input {
    width: 100%;
    padding: 12px 20px;
    margin: 8px 0;
    box-sizing: border-box;
  }
  
  ul {
    list-style-type: none;
    padding: 0;
  }
  
  ul li {
    padding: 10px;
    border-bottom: 1px solid #ddd;
  }
  
  ul li:last-child {
    border-bottom: none;
  }
  </style>
  


