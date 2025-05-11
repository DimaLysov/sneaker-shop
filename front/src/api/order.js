const BASE_URL = process.env.REACT_APP_PATH_URL_API;

export const AddOrder = async (requestBody) => {
    const response = await fetch(`${BASE_URL}/api/orders/`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(requestBody),
    });
    if (!response.ok) {
      throw new Error(`Ошибка при добавлении заказа: ${response.statusText}`);
  }
    return await response.json();
  };