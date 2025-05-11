import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';

import { AddOrder } from '../api/order';

const Checkout = () => {
  const [formData, setFormData] = useState({
    fullName: '',
    phone: '',
    address: '',
  });
  const navigate = useNavigate();

  // Обработчик изменения полей ввода
  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData((prev) => ({ ...prev, [name]: value }));
  };

  // Обработчик отправки формы
  const handleSubmit = async (e) => {
    e.preventDefault();
    const user_tg_id = window.Telegram.WebApp.initDataUnsafe?.user?.id;
    if (!user_tg_id) {
      throw new Error('Telegram ID пользователя не найден');
    }
    // Сохранение данных о заказе 
    const infoOrder = {
      tg_id: user_tg_id,
      fullname: formData.fullName,
      phone_number: Number(formData.phone),
      delivery_address: formData.address,
    };
    console.log('Данные заказа:', infoOrder);
    const order = await AddOrder(infoOrder)
    console.log('Заказ успешно добавлен', order);
    
    alert('Заказ успешно оформлен!');
    navigate('/'); // Перенаправление на главную страницу
  };

  return (
    <div className="checkout">
      <h1>Оформление заказа</h1>
      <form onSubmit={handleSubmit}>
        <div className="form-group">
          <label htmlFor="fullName">ФИО</label>
          <input
            type="text"
            id="fullName"
            name="fullName"
            value={formData.fullName}
            onChange={handleChange}
            required
          />
        </div>
        <div className="form-group">
          <label htmlFor="phone">Номер телефона</label>
          <input
            type="tel"
            id="phone"
            name="phone"
            value={formData.phone}
            onChange={handleChange}
            required
            pattern="[0-9]+"
          />
        </div>
        <div className="form-group">
          <label htmlFor="address">Адрес доставки</label>
          <textarea
            id="address"
            name="address"
            value={formData.address}
            onChange={handleChange}
            required
          />
        </div>
        <button type="submit" className="submit-btn">
          Оформить заказ
        </button>
      </form>
    </div>
  );
};

export default Checkout;