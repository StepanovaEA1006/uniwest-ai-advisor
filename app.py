# app.py - обновленная версия с системой пользователей и портфелями

import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
from datetime import datetime
import hashlib

# ИМПОРТИРУЕМ ФУНКЦИИ ИЗ database.py
from database import (
    get_all_clients, 
    get_client_details, 
    get_portfolio_by_client, 
    generate_client_recommendations,
    get_complete_client_data,
    CLIENTS_DETAILED_DATA
)

# Настраиваем страницу Streamlit
st.set_page_config(
    page_title="ЮниВест - AI Советник по Инвестициям",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

def hash_password(password):
    """Хеширование пароля"""
    return hashlib.sha256(password.encode()).hexdigest()

def init_session_state():
    """Инициализация состояния сессии"""
    if 'authenticated' not in st.session_state:
        st.session_state.authenticated = False
    if 'current_user' not in st.session_state:
        st.session_state.current_user = None
    if 'page' not in st.session_state:
        st.session_state.page = "login"
    if 'client_data' not in st.session_state:
        st.session_state.client_data = None
    if 'portfolio_data' not in st.session_state:
        st.session_state.portfolio_data = None

def login_page():
    """Упрощенная страница входа - только форма входа"""
    st.markdown("""
    <style>
        .login-container {
            max-width: 400px;
            margin: 150px auto;
            padding: 3rem;
            background: white;
            border-radius: 20px;
            box-shadow: 0 20px 40px rgba(0,0,0,0.1);
            text-align: center;
        }
        .main-title {
            font-size: 2.8rem;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin-bottom: 0.5rem;
            font-weight: bold;
        }
        .subtitle {
            color: #666;
            margin-bottom: 2rem;
            font-size: 1.2rem;
        }
    </style>
    """, unsafe_allow_html=True)
    
    # Используем центрирование через HTML вместо колонок
    st.markdown("""
    <div style='display: flex; justify-content: center; align-items: center; min-height: 80vh;'>
        <div class="login-container">
            <h1 class="main-title">🤖 ЮниВест</h1>
            <div class="subtitle">AI Советник по Инвестициям</div>
    """, unsafe_allow_html=True)
    
    # Простая форма входа
    clients = get_all_clients()
    selected_client = st.selectbox(
        "👤 Выберите клиента:",
        clients,
        index=0
    )
    
    password = st.text_input("🔒 Пароль:", type="password", value="demo123")
    
    if st.button("🚀 Войти в систему", use_container_width=True, type="primary"):
        if password == "demo123":
            st.session_state.authenticated = True
            st.session_state.current_user = selected_client
            st.session_state.page = "dashboard"
            st.rerun()
        else:
            st.error("❌ Неверный пароль. Используйте 'demo123'")
    
    st.markdown("""
            <div style="margin-top: 2rem; padding: 1rem; background: #f8f9fa; border-radius: 10px;">
                <p style="margin: 0; font-size: 0.9rem;"><strong>💡 Демо-доступ:</strong> Пароль: <code>demo123</code></p>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# ОСТАЛЬНЫЕ ФУНКЦИИ ОСТАЮТСЯ БЕЗ ИЗМЕНЕНИЙ
def create_portfolio_metrics(client_data, portfolio_dict):
    """Создает метрики для портфеля"""
    portfolio_type = client_data['portfolio_type']
    
    # Более детальные метрики для разных типов портфелей
    metrics_map = {
        'агрессивный': {
            'expected_return': 0.18, 
            'volatility': 0.32, 
            'sharpe_ratio': 0.56, 
            'max_drawdown': -0.40,
            'diversification_score': 65
        },
        'сбалансированный': {
            'expected_return': 0.095, 
            'volatility': 0.14, 
            'sharpe_ratio': 0.68, 
            'max_drawdown': -0.20,
            'diversification_score': 85
        },
        'доходный': {
            'expected_return': 0.078, 
            'volatility': 0.11, 
            'sharpe_ratio': 0.71, 
            'max_drawdown': -0.15,
            'diversification_score': 80
        },
        'ультра-консервативный': {
            'expected_return': 0.045, 
            'volatility': 0.05, 
            'sharpe_ratio': 0.90, 
            'max_drawdown': -0.08,
            'diversification_score': 70
        }
    }
    
    return metrics_map.get(portfolio_type, metrics_map['сбалансированный'])

def create_growth_chart(client_data, portfolio_type, current_client):
    """Создает график роста портфеля"""
    dates = pd.date_range(start='2021-01-01', end='2024-01-01', freq='M')
    
    # Разные профили доходности для разных типов портфелей
    returns_map = {
        'агрессивный': {'mean': 0.015, 'std': 0.08},
        'сбалансированный': {'mean': 0.008, 'std': 0.04},
        'доходный': {'mean': 0.006, 'std': 0.03},
        'ультра-консервативный': {'mean': 0.004, 'std': 0.02}
    }
    
    return_profile = returns_map.get(portfolio_type, returns_map['сбалансированный'])
    
    # Уникальное зерно для каждого клиента
    seed = sum(ord(c) for c in current_client)
    np.random.seed(seed)
    
    monthly_returns = np.random.normal(
        return_profile['mean'], 
        return_profile['std'], 
        len(dates)
    )
    
    initial = client_data['initial_investment']
    values = [initial]
    
    for ret in monthly_returns:
        values.append(values[-1] * (1 + ret))
    
    return dates, values[1:], initial

def dashboard_page():
    """Основная панель управления"""
    
    # Заголовок приложения - ОБНОВЛЕННЫЕ СТИЛИ ДЛЯ ЛУЧШЕЙ ЧИТАЕМОСТИ
    st.markdown("""
    <style>
        /* Белый фон для всего приложения */
        .stApp {
            background-color: #ffffff !important;
        }
        
        /* Черный текст везде для лучшей читаемости */
        body, p, div, h1, h2, h3, h4, h5, h6, span, li, strong, em {
            color: #000000 !important;
        }
        
        .main-header {
            font-size: 2.5rem;
            color: #1f77b4 !important;
            text-align: center;
            margin-bottom: 1rem;
            font-weight: bold;
        }
        
        /* Карточки с белым фоном и черным текстом */
        .client-card {
            background: #ffffff !important;
            color: #000000 !important;
            padding: 2rem;
            border-radius: 15px;
            margin: 1rem 0;
            border: 2px solid #1f77b4;
            box-shadow: 0 4px 15px rgba(0,0,0,0.1);
        }
        
        .metric-card {
            background: #f8f9fa !important;
            color: #000000 !important;
            padding: 1rem;
            border-radius: 10px;
            border-left: 4px solid #1f77b4;
            margin: 0.5rem 0;
            box-shadow: 0 2px 8px rgba(0,0,0,0.1);
        }
        
        .user-info {
            background: #f8f9fa !important;
            color: #000000 !important;
            padding: 1rem;
            border-radius: 10px;
            margin: 0.5rem 0;
            border: 1px solid #dee2e6;
        }
        
        .recommendation-card {
            background: #f8f9fa !important;
            color: #000000 !important;
            padding: 1rem;
            border-radius: 10px;
            margin: 0.5rem 0;
            border-left: 4px solid #28a745;
            box-shadow: 0 2px 8px rgba(0,0,0,0.1);
        }
        
        /* Улучшаем читаемость sidebar */
        .css-1d391kg {
            background-color: #f8f9fa !important;
        }
        
        /* Убираем градиентные фоны */
        [style*="gradient"] {
            background: #ffffff !important;
        }
    </style>
    """, unsafe_allow_html=True)
    
    # Текущий клиент
    current_client = st.session_state.current_user
    
    # Получаем данные клиента
    client_data = get_client_details(current_client)
    if not client_data:
        st.error(f"❌ Нет данных для клиента: {current_client}")
        st.stop()
    
    # Получаем портфель
    portfolio_dict = get_portfolio_by_client(current_client)
    if not portfolio_dict:
        st.error(f"❌ Не удалось загрузить портфель для клиента: {current_client}")
        st.stop()
    
    # Хедер с информацией о пользователе и навигацией
    col1, col2, col3 = st.columns([3, 1, 1])
    
    with col1:
        st.markdown(f'<div class="main-header">🤖 ЮниВест - AI Советник по Инвестициям</div>', unsafe_allow_html=True)
    
    with col2:
        st.markdown(f'<div class="user-info">👤 <strong>{current_client}</strong></div>', unsafe_allow_html=True)
    
    with col3:
        if st.button("🚪 Выйти", use_container_width=True):
            st.session_state.authenticated = False
            st.session_state.current_user = None
            st.session_state.page = "login"
            st.rerun()
    
    st.markdown("---")
    
    # Боковая панель с навигацией
    st.sidebar.title("🎯 Навигация")
    
    # Переключение между пользователями
    st.sidebar.subheader("👥 Быстрое переключение")
    all_clients = get_all_clients()
    current_index = all_clients.index(current_client) if current_client in all_clients else 0
    
    new_user = st.sidebar.selectbox(
        "Выберите пользователя:",
        all_clients,
        index=current_index,
        key="user_switch"
    )
    
    if new_user != current_client:
        st.session_state.current_user = new_user
        st.rerun()
    
    # Информация в сайдбаре
    st.sidebar.markdown("---")
    st.sidebar.subheader(f"📊 Портфель {current_client}")
    st.sidebar.write(f"**💼 Тип:** {client_data['portfolio_type']}")
    st.sidebar.write(f"**⚡ Риск:** {client_data['risk_profile']}")
    st.sidebar.write(f"**🎯 Цель:** {client_data['financial_goals']}")
    st.sidebar.write(f"**💰 Инвестиции:** {client_data['initial_investment']:,.0f} ₽")
    st.sidebar.write(f"**📊 Активов:** {len(portfolio_dict)}")
    st.sidebar.write(f"**📅 Горизонт:** {client_data['investment_horizon']}")
    
    # Рекомендации AI
    st.sidebar.markdown("---")
    st.sidebar.subheader("🤖 AI Рекомендации")
    recommendations = generate_client_recommendations(current_client)
    for rec in recommendations[:3]:  # Показываем только 3 основные рекомендации
        st.sidebar.info(rec)
    
    # ОСНОВНОЕ СОДЕРЖИМОЕ СТРАНИЦЫ
    
    # 1. Профиль клиента
    st.markdown(f"""
    <div class="client-card">
        <h2>👤 {current_client}</h2>
        <p><em>{client_data['description']}</em></p>
        <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 1rem; margin-top: 1rem;">
            <div>
                <p><strong>💼 Тип портфеля:</strong> {client_data['portfolio_type']}</p>
                <p><strong>🎯 Финансовая цель:</strong> {client_data['financial_goals']}</p>
                <p><strong>💰 Целевая сумма:</strong> {client_data['target_amount']:,.0f} ₽</p>
            </div>
            <div>
                <p><strong>⚡ Уровень риска:</strong> {client_data['risk_profile']}</p>
                <p><strong>💪 Опыт инвестирования:</strong> {client_data['experience']}</p>
                <p><strong>📅 Инвестиционный горизонт:</strong> {client_data['investment_horizon']}</p>
            </div>
            <div>
                <p><strong>🌐 Диверсификация:</strong> {client_data['diversification_level']}</p>
                <p><strong>💼 Начальные инвестиции:</strong> {client_data['initial_investment']:,.0f} ₽</p>
                <p><strong>🎯 Толерантность к риску:</strong> {client_data['risk_tolerance']:.0%}</p>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # 2. Обзор портфеля
    st.header("📊 Детальный обзор портфеля")
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.subheader("🍕 Состав портфеля")
        weights_df = pd.DataFrame(list(portfolio_dict.items()), columns=['Актив', 'Доля'])
        
        fig_pie = px.pie(
            weights_df, 
            values='Доля', 
            names='Актив', 
            color_discrete_sequence=px.colors.sequential.RdBu,
            hole=0.3
        )
        fig_pie.update_traces(
            textposition='inside', 
            textinfo='percent+label',
            pull=[0.1 if i == 0 else 0 for i in range(len(portfolio_dict))]  # Выделяем первый актив
        )
        fig_pie.update_layout(showlegend=False)
        st.plotly_chart(fig_pie, use_container_width=True)
    
    with col2:
        st.subheader("📈 Детали активов")
        
        # Сортируем активы по доле
        sorted_assets = sorted(portfolio_dict.items(), key=lambda x: x[1], reverse=True)
        
        # Создаем DataFrame для лучшего отображения
        assets_df = pd.DataFrame(sorted_assets, columns=['Актив', 'Доля'])
        assets_df['Доля'] = assets_df['Доля'].apply(lambda x: f'{x:.1%}')
        assets_df['Инвестиции'] = assets_df['Доля'].apply(
            lambda x: f"{client_data['initial_investment'] * float(x.strip('%'))/100:,.0f} ₽"
        )
        
        # Отображаем в виде таблицы
        st.dataframe(
            assets_df,
            use_container_width=True,
            hide_index=True
        )
        
        # Метрики портфеля
        col1, col2, col3 = st.columns(3)
        total_weight = sum(portfolio_dict.values())
        
        with col1:
            st.metric("Общая доля активов", f"{total_weight:.1%}")
        with col2:
            st.metric("Количество активов", len(portfolio_dict))
        with col3:
            diversification_score = len(portfolio_dict) * 10 + 30  # Простая оценка
            st.metric("Оценка диверсификации", f"{diversification_score}/100")
        
        # Оценка диверсификации
        if len(portfolio_dict) < 4:
            st.error("⚠️ Недостаточно активов для хорошей диверсификации")
        elif len(portfolio_dict) < 6:
            st.warning("⚠️ Хорошая диверсификация, можно улучшить")
        else:
            st.success("✅ Отличная диверсификация портфеля")
    
    # 3. Ключевые метрики портфеля
    st.header("🔍 Ключевые метрики и анализ")
    
    portfolio_metrics = create_portfolio_metrics(client_data, portfolio_dict)
    key_metrics = client_data.get('key_metrics', {})
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Ожидаемая доходность", 
                 f"{key_metrics.get('expected_return', portfolio_metrics['expected_return']):.2%}",
                 help="Среднегодовая ожидаемая доходность")
    with col2:
        st.metric("Волатильность", 
                 f"{key_metrics.get('volatility', portfolio_metrics['volatility']):.2%}",
                 help="Стандартное отклонение доходности")
    with col3:
        st.metric("Коэффициент Шарпа", 
                 f"{key_metrics.get('sharpe_ratio', portfolio_metrics['sharpe_ratio']):.2f}",
                 help="Доходность на единицу риска")
    with col4:
        st.metric("Макс. просадка", 
                 f"{portfolio_metrics['max_drawdown']:.1%}",
                 help="Максимальная историческая просадка")
    
    # 4. График роста портфеля
    st.header("📈 Динамика портфеля за 3 года")
    
    try:
        dates, values, initial = create_growth_chart(
            client_data, 
            client_data['portfolio_type'], 
            current_client
        )
        
        df = pd.DataFrame({'Дата': dates, 'Стоимость портфеля': values})
        fig = px.line(
            df, 
            x='Дата', 
            y='Стоимость портфеля', 
            title=f'Историческая динамика портфеля {current_client}',
            color_discrete_sequence=['#1f77b4']
        )
        fig.update_layout(
            xaxis_title="Дата",
            yaxis_title="Стоимость портфеля (₽)",
            hovermode='x unified',
            showlegend=False
        )
        
        # Добавляем начальную инвестицию как горизонтальную линию
        fig.add_hline(
            y=initial, 
            line_dash="dash", 
            line_color="red",
            annotation_text=f"Начальные инвестиции: {initial:,.0f} ₽"
        )
        
        st.plotly_chart(fig, use_container_width=True)
        
        # Расчет итоговых показателей
        final_value = values[-1]
        total_growth = final_value - initial
        annualized_return = (final_value / initial) ** (1/3) - 1
        
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.metric("Начальная сумма", f"{initial:,.0f} ₽")
        with col2:
            st.metric("Текущая сумма", f"{final_value:,.0f} ₽")
        with col3:
            st.metric("Общий рост", f"{total_growth:,.0f} ₽")
        with col4:
            st.metric("Годовая доходность", f"{annualized_return:.2%}")
            
    except Exception as e:
        st.error(f"Ошибка при построении графика: {e}")
    
    # 5. Сравнение с другими пользователями
    st.header("👥 Сравнение с другими портфелями")
    
    try:
        comparison_data = []
        for client in get_all_clients():
            if client != current_client:
                client_info = get_client_details(client)
                if client_info:
                    comparison_data.append({
                        'Клиент': client,
                        'Тип портфеля': client_info['portfolio_type'],
                        'Уровень риска': client_info['risk_profile'],
                        'Инвестиции (млн ₽)': client_info['initial_investment'] / 1000000,
                        'Количество активов': len(get_portfolio_by_client(client) or {}),
                        'Опыт': client_info['experience']
                    })
        
        if comparison_data:
            comparison_df = pd.DataFrame(comparison_data)
            
            # Стилизуем таблицу
            st.dataframe(
                comparison_df.style.format({
                    'Инвестиции (млн ₽)': '{:.1f}'
                }),
                use_container_width=True
            )
        else:
            st.info("📊 Это единственный пользователь в системе")
            
    except Exception as e:
        st.warning(f"Не удалось загрузить данные для сравнения: {e}")
    
    # 6. Детальные рекомендации AI
    st.header("🤖 Персонализированные рекомендации AI")
    
    recommendations = generate_client_recommendations(current_client)
    for i, rec in enumerate(recommendations):
        st.markdown(f"""
        <div class="recommendation-card">
            <strong>📌 Рекомендация {i+1}:</strong> {rec}
        </div>
        """, unsafe_allow_html=True)
    
    # Футер
    st.markdown("---")
    st.markdown("""
    <div style='text-align: center; color: #666;'>
        <p>🤖 ЮниВест AI Советник | Мульти-пользовательская инвестиционная платформа</p>
        <p>💼 Инвестиционные рекомендации не являются гарантией доходности</p>
        <p>📊 Данные обновлены: {}</p>
    </div>
    """.format(datetime.now().strftime("%d.%m.%Y %H:%M")), unsafe_allow_html=True)

def main():
    """Главная функция приложения"""
    init_session_state()
    
    if not st.session_state.authenticated:
        login_page()
    else:
        dashboard_page()

# Запуск приложения
if __name__ == "__main__":
    main()
