
 <script>
  let page = '';
  let menuType = '';
  let menuItems = [];

  async function get_menu_list(menuType) {
    const response = await fetch(`http://127.0.0.1:8000/meun/list/${menuType}`);
    const data = await response.json();
    menuItems = data;
  }

  function setMenuType(type) {
    menuType = type;
    get_menu_list(type);
  }

  function goToPage(newPage) {
    page = newPage;
    if (newPage !== 'order') {
      menuType = '';
      menuItems = [];
    }
  }
</script>

<style>
  .main-button {
    background-color: #4CAF50; /* Green */
    border: none;
    color: white;
    padding: 15px 32px;
    text-align: center;
    text-decoration: none;
    display: inline-block;
    font-size: 16px;
    margin: 4px 2px;
    cursor: pointer;
    border-radius: 12px;
  }

  ul {
    list-style: none;
    padding: 0;
  }

  li {
    border: 1px solid #ccc;
    margin-bottom: 1em;
    padding: 1em;
    border-radius: 0.5em;
  }

  h2 {
    margin: 0 0 0.5em 0;
    color: #333;
  }

  p {
    margin: 0.5em 0;
  }

  .price {
    font-weight: bold;
  }
</style>

{#if page === ''}
  <button class="main-button" on:click={() => goToPage('order')}>주문</button>
  <button class="main-button" on:click={() => goToPage('inquiry')}>문의</button>
{:else if page === 'order'}
  <button class="main-button" on:click={() => setMenuType('coffee')}>커피</button>
  <button class="main-button" on:click={() => setMenuType('smoothie')}>스무디</button>
  <button class="main-button" on:click={() => setMenuType('tea')}>티</button>
  <button class="main-button" on:click={() => setMenuType('cake')}>케이크</button>
  {#if menuType !== ''}
    <ul>
      {#each menuItems as item}
        <li>
          <h2>{item.name}</h2>
          <p class="price">가격: {item.price}</p>
          <p>설명: {item.description}</p>
        </li>
      {/each}
    </ul>
    <button class="main-button" on:click={() => goToPage('')}>뒤로 가기</button>
  {/if}
{:else if page === 'inquiry'}
  <!-- 문의 페이지 내용을 여기에 넣으세요 -->
  <button class="main-button" on:click={() => goToPage('')}>뒤로 가기</button>
{/if}
