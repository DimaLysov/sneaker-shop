const BASE_URL = process.env.REACT_APP_PATH_URL_API;

export const AddItemOrder = async (requestBody) => {
    const response = await fetch(`${BASE_URL}/api/item_order/`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(requestBody),
    });
    if (!response.ok) {
      throw new Error(`Ошибка при добавлении содержимого заказа: ${response.statusText}`);
  }
    return await response.json();
  };