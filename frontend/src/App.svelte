<script>
  import { onMount } from 'svelte';
  let categories = [];
  let menus = [];
  let showCustomerInfo = false;
  let showCategories = false;
  let name = '';
  let phone = '';

  const orderButton = '주문';
  const inquiryButton = '문의';

  async function openCustomerInfoModal() {
    showCustomerInfo = true;
  }

  async function handleInquiry() {
    // 문의 버튼을 클릭하면 실행할 로직을 여기에 작성해주세요.
  }

  async function submitOrder() {
    const response = await fetch('http://127.0.0.1:8000/new_orderer', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        name: name,
        phone: phone
      })
    });
    if (response.ok) {
      showCustomerInfo = false;
      showCategories = true;
      loadCategories();
    }
  }

  async function loadCategories() {
    const response = await fetch('http://127.0.0.1:8000/categories');

    if (response.ok) {
      categories = await response.json();
    } else {
      console.error(`Error: ${response.statusText}`);
    }
  }

  async function loadMenus(category_pk) {
    const response = await fetch(`http://127.0.0.1:8000/menu/${category_pk}`);

    if (response.ok) {
      menus = await response.json();
      showCategories = false;
    } else {
      console.error(`Error: ${response.statusText}`);
    }
  }

  function backToCategories() {
    showCategories = true;
    menus = [];
  }
</script>

<div class="welcomeBox">
  <h2>영남 커피숍에 오신걸 환영합니다</h2>
  <div class="buttonGroup">
    <button on:click={openCustomerInfoModal} class="orderButton">{orderButton}</button>
    <button on:click={handleInquiry} class="inquiryButton">{inquiryButton}</button>
  </div>
</div>

{#if showCustomerInfo}
<div class="customerInfoModal">
  <div>
    <label for="name">이름:</label>
    <input type="text" id="name" bind:value={name} />
  </div>
  <div>
    <label for="phone">전화번호:</label>
    <input type="text" id="phone" bind:value={phone} />
  </div>
  <div>
    <button on:click={submitOrder} class="submitOrderButton">주문</button>
  </div>
</div>
{/if}

{#if showCategories}
<div class="categoryGroup">
  {#each categories as category}
  <button on:click={() => loadMenus(category.category_pk)} class="categoryButton">{category.category_name}</button>
  {/each}
</div>
{:else}
<div class="menuGroup">
  <button on:click={backToCategories} class="backButton">뒤로 가기</button>
  {#each menus as menu}
  <div class="menuItem">
    <h3>{menu.menu_name}</h3>
    <p>{menu.menu_price}원</p>
    <p>{menu.menu_description}</p>
  </div>
  {/each}
</div>
{/if}

<style>
  .welcomeBox {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    width: 600px;
    height: 400px;
    margin: auto;
    background-color: #2ECC71;
    color: white;
    font-size: 1.5em;
    box-shadow: 0px 0px 10px rgba(0,0,0,0.5);
  }

  .buttonGroup {
    margin-top: 20px;
  }

  .orderButton,
  .inquiryButton,
  .submitOrderButton,
  .categoryButton,
  .backButton {
    margin: 10px;
    padding: 10px 20px;
    font-size: 1em;
    border: none;
    border-radius: 5px;
    color: white;
    background-color: #27AE60;
    box-shadow: 0px 0px 10px rgba(0,0,0,0.3);
    cursor: pointer;
  }

  .orderButton:hover,
  .inquiryButton:hover,
  .submitOrderButton:hover,
  .categoryButton:hover,
  .backButton:hover {
    background-color: #229954;
  }

  .customerInfoModal {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    width: 600px;
    height: 400px;
    margin: auto;
    background-color: #2ECC71;
    color: white;
    font-size: 1.2em;
    box-shadow: 0px 0px 10px rgba(0,0,0,0.5);
  }

  .categoryGroup {
    display: flex;
    flex-direction: row;
    justify-content: center;
    flex-wrap: wrap;
    width: 600px;
    height: 400px;
    margin: auto;
    background-color: #2ECC71;
  }

  .menuGroup {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    width: 600px;
    height: 400px;
    margin: auto;
    background-color: #2ECC71;
  }

  .menuItem {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    margin: 20px;
    padding: 20px;
    width: 200px;
    background-color: #27AE60;
    color: white;
    border-radius: 5px;
    box-shadow: 0px 0px 10px rgba(0,0,0,0.5);
  }
</style>
