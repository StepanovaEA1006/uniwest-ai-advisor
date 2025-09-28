# app.py - полностью адаптивная версия

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
    generate_client_recommendations
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

def login_page():
    """Адаптивная страница входа"""
    st.markdown("""
    <style>
        .login-container {
            max-width: 90%;
            width: 400px;
            margin: 10vh auto;
            padding: 2rem;
            background: white;
            border-radius: 20px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.1);
            text-align: center;
        }
        .main-title {
            font-size: clamp(2rem, 5vw, 2.8rem);
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin-bottom: 0.5rem;
            font-weight: bold;
        }
        .subtitle {
            color: #666;
            margin-bottom: 2rem;
            font-size: clamp(1rem, 3vw, 1.2rem);
        }
        
        /* Адаптивность для мобильных */
        @media (max-width: 768px) {
            .login-container {
                margin: 5vh auto;
                padding: 1.5rem;
                width: 85%;
            }
        }
    </style>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div style='display: flex; justify-content: center; align-items: center; min-height: 80vh; padding: 1rem;'>
        <div class="login-container">
            <h1 class="main-title">🤖 ЮниВест</h1>
            <div class="subtitle">AI Советник по Инвестициям</div>
    """, unsafe_allow_html=True)
    
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

def create_portfolio_metrics(client_data, portfolio_dict):
    """Создает метрики для портфеля"""
    portfolio_type = client_data['portfolio_type']
    
    metrics_map = {
        'агрессивный': {'expected_return': 0.18, 'volatility': 0.32, 'sharpe_ratio': 0.56, 'max_drawdown': -0.40},
        'сбалансированный': {'expected_return': 0.095, 'volatility': 0.14, 'sharpe_ratio': 0.68, 'max_drawdown': -0.20},
        'доходный': {'expected_return': 0.078, 'volatility': 0.11, 'sharpe_ratio': 0.71, 'max_drawdown': -0.15},
        'ультра-консервативный': {'expected_return': 0.045, 'volatility': 0.05, 'sharpe_ratio': 0.90, 'max_drawdown': -0.08}
    }
    
    return metrics_map.get(portfolio_type, metrics_map['сбалансированный'])

def create_growth_chart(client_data, portfolio_type, current_client):
    """Создает адаптивный график роста"""
    dates = pd.date_range(start='2021-01-01', end='2024-01-01', freq='M')
    
    returns_map = {
        'агрессивный': {'mean': 0.015, 'std': 0.08},
        'сбалансированный': {'mean': 0.008, 'std': 0.04},
        'доходный': {'mean': 0.006, 'std': 0.03},
        'ультра-консервативный': {'mean': 0.004, 'std': 0.02}
    }
    
    return_profile = returns_map.get(portfolio_type, returns_map['сбалансированный'])
    seed = sum(ord(c) for c in current_client)
    np.random.seed(seed)
    
    monthly_returns = np.random.normal(return_profile['mean'], return_profile['std'], len(dates))
    initial = client_data['initial_investment']
    values = [initial]
    
    for ret in monthly_returns:
        values.append(values[-1] * (1 + ret))
    
    return dates, values[1:], initial

def dashboard_page():
    """Адаптивная панель управления"""
    
    # АДАПТИВНЫЕ СТИЛИ ДЛЯ ВСЕХ УСТРОЙСТВ
    st.markdown("""
    <style>
        /* Базовые стили для всех устройств */
        .stApp {
            background-color: #ffffff !important;
        }
        
        body, p, div, h1, h2, h3, h4, h5, h6, span, li, strong, em {
            color: #000000 !important;
        }
        
        /* Адаптивные заголовки */
        .main-header {
            font-size: clamp(1.8rem, 4vw, 2.5rem) !important;
            color: #1f77b4 !important;
            text-align: center;
            margin-bottom: 1rem;
            font-weight: bold;
        }
        
        .section-header {
            font-size: clamp(1.3rem, 3vw, 1.8rem) !important;
            margin: 1.5rem 0 1rem 0 !important;
        }
        
        /* Адаптивные карточки */
        .client-card {
            background: #ffffff !important;
            color: #000000 !important;
            padding: clamp(1rem, 3vw, 2rem) !important;
            border-radius: 15px;
            margin: 1rem 0;
            border: 2px solid #1f77b4;
            box-shadow: 0 4px 15px rgba(0,0,0,0.1);
        }
        
        .metric-card {
            background: #f8f9fa !important;
            color: #000000 !important;
            padding: clamp(0.8rem, 2vw, 1rem) !important;
            border-radius: 10px;
            border-left: 4px solid #1f77b4;
            margin: 0.5rem 0;
            box-shadow: 0 2px 8px rgba(0,0,0,0.1);
        }
        
        /* Адаптивная кнопка выхода */
        div.stButton > button[kind="secondary"] {
            background-color: #f8f9fa !important;
            color: #000000 !important;
            border: 1px solid #dee2e6 !important;
            font-weight: 500;
            font-size: clamp(0.8rem, 2vw, 1rem) !important;
        }
        
        /* Мобильная навигация */
        @media (max-width: 768px) {
            /* Упрощаем хедер на мобильных */
            .mobile-header {
                flex-direction: column !important;
                gap: 0.5rem !important;
            }
            
            /* Уменьшаем отступы */
            .client-card {
                margin: 0.5rem 0 !important;
            }
            
            /* Адаптируем sidebar */
            .sidebar-content {
                font-size: 0.9rem !important;
            }
            
            /* Улучшаем таблицы */
            .dataframe {
                font-size: 0.8rem !important;
            }
        }
        
        /* Планшеты */
        @media (min-width: 769px) and (max-width: 1024px) {
            .client-card {
                padding: 1.5rem !important;
            }
        }
        
        /* Скрываем сложные элементы на мобильных */
        @media (max-width: 480px) {
            .hide-on-mobile {
                display: none !important;
            }
        }
    </style>
    """, unsafe_allow_html=True)
    
    current_client = st.session_state.current_user
    client_data = get_client_details(current_client)
    portfolio_dict = get_portfolio_by_client(current_client)
    
    if not client_data or not portfolio_dict:
        st.error("❌ Ошибка загрузки данных")
        return
    
    # АДАПТИВНЫЙ ХЕДЕР
    st.markdown(f'<div class="main-header">🤖 ЮниВест - AI Советник</div>', unsafe_allow_html=True)
    
    # Используем разные раскладки для разных устройств
    col1, col2, col3 = st.columns([2, 1, 1])
    
    with col1:
        st.markdown(f'<div class="user-info">👤 <strong>{current_client}</strong></div>', unsafe_allow_html=True)
    
    with col2:
        st.metric("Инвестиции", f"{client_data['initial_investment']:,.0f} ₽")
    
    with col3:
        if st.button("🚪 Выйти", use_container_width=True, type="secondary"):
            st.session_state.authenticated = False
            st.session_state.current_user = None
            st.rerun()
    
    st.markdown("---")
    
    # АДАПТИВНЫЙ SIDEBAR
    with st.sidebar:
        st.title("🎯 Навигация")
        
        # Переключение пользователей
        clients = get_all_clients()
        new_user = st.selectbox("👥 Выберите клиента:", clients, 
                              index=clients.index(current_client))
        
        if new_user != current_client:
            st.session_state.current_user = new_user
            st.rerun()
        
        st.markdown("---")
        
        # Быстрая статистика - адаптивная
        st.subheader("📊 Статистика")
        col1, col2 = st.columns(2)
        with col1:
            st.metric("Активы", len(portfolio_dict))
        with col2:
            st.metric("Риск", client_data['risk_profile'])
        
        st.markdown("---")
        
        # Рекомендации AI
        st.subheader("🤖 Советы")
        recommendations = generate_client_recommendations(current_client)
        for rec in recommendations[:2]:  # Меньше рекомендаций на мобильных
            st.info(rec)
    
    # ОСНОВНОЙ КОНТЕНТ - АДАПТИВНЫЙ
    
    # 1. Профиль клиента - адаптивная сетка
    st.markdown(f"""
    <div class="client-card">
        <h2>👤 {current_client}</h2>
        <p><em>{client_data['description']}</em></p>
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 1rem; margin-top: 1rem;">
            <div>
                <p><strong>💼 Тип портфеля:</strong> {client_data['portfolio_type']}</p>
                <p><strong>🎯 Цель:</strong> {client_data['financial_goals']}</p>
                <p><strong>💰 Цель:</strong> {client_data['target_amount']:,.0f} ₽</p>
            </div>
            <div>
                <p><strong>⚡ Уровень риска:</strong> {client_data['risk_profile']}</p>
                <p><strong>💪 Опыт:</strong> {client_data['experience']}</p>
                <p><strong>📅 Горизонт:</strong> {client_data['investment_horizon']}</p>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # 2. Обзор портфеля - адаптивные колонки
    st.markdown('<div class="section-header">📊 Обзор портфеля</div>', unsafe_allow_html=True)
    
    # На мобильных - вертикальная раскладка, на десктопе - горизонтальная
    if st.checkbox("📱 Компактный вид", value=False, help="Оптимизировать для мобильных устройств"):
        # Вертикальная раскладка для мобильных
        st.subheader("🍕 Состав портфеля")
        weights_df = pd.DataFrame(list(portfolio_dict.items()), columns=['Актив', 'Доля'])
        
        fig_pie = px.pie(weights_df, values='Доля', names='Актив', 
                        color_discrete_sequence=px.colors.sequential.RdBu, hole=0.3)
        fig_pie.update_traces(textposition='inside', textinfo='percent+label')
        fig_pie.update_layout(showlegend=False, height=300)
        st.plotly_chart(fig_pie, use_container_width=True)
        
        # Детали активов в компактном виде
        st.subheader("📈 Детали активов")
        sorted_assets = sorted(portfolio_dict.items(), key=lambda x: x[1], reverse=True)
        
        for asset, weight in sorted_assets:
            investment = client_data['initial_investment'] * weight
            st.markdown(f"""
            <div class="metric-card">
                <div style="display: flex; justify-content: space-between; align-items: center;">
                    <strong>{asset}</strong>
                    <span>{weight:.1%} • {investment:,.0f} ₽</span>
                </div>
            </div>
            """, unsafe_allow_html=True)
    else:
        # Горизонтальная раскладка для десктопа
        col1, col2 = st.columns([1, 2])
        
        with col1:
            st.subheader("🍕 Состав портфеля")
            weights_df = pd.DataFrame(list(portfolio_dict.items()), columns=['Актив', 'Доля'])
            
            fig_pie = px.pie(weights_df, values='Доля', names='Актив', 
                            color_discrete_sequence=px.colors.sequential.RdBu, hole=0.3)
            fig_pie.update_traces(textposition='inside', textinfo='percent+label')
            fig_pie.update_layout(showlegend=False, height=400)
            st.plotly_chart(fig_pie, use_container_width=True)
        
        with col2:
            st.subheader("📈 Детали активов")
            sorted_assets = sorted(portfolio_dict.items(), key=lambda x: x[1], reverse=True)
            
            assets_df = pd.DataFrame(sorted_assets, columns=['Актив', 'Доля'])
            assets_df['Доля'] = assets_df['Доля'].apply(lambda x: f'{x:.1%}')
            assets_df['Инвестиции'] = assets_df['Доля'].apply(
                lambda x: f"{client_data['initial_investment'] * float(x.strip('%'))/100:,.0f} ₽"
            )
            
            st.dataframe(assets_df, use_container_width=True, hide_index=True)
    
    # 3. Ключевые метрики - адаптивная сетка
    st.markdown('<div class="section-header">🔍 Ключевые метрики</div>', unsafe_allow_html=True)
    
    portfolio_metrics = create_portfolio_metrics(client_data, portfolio_dict)
    key_metrics = client_data.get('key_metrics', {})
    
    # На мобильных - 2 колонки, на десктопе - 4 колонки
    cols = st.columns(2)  # Всегда 2 колонки для лучшей адаптивности
    
    with cols[0]:
        st.metric("Ожидаемая доходность", f"{key_metrics.get('expected_return', portfolio_metrics['expected_return']):.2%}")
        st.metric("Волатильность", f"{key_metrics.get('volatility', portfolio_metrics['volatility']):.2%}")
    
    with cols[1]:
        st.metric("Коэффициент Шарпа", f"{key_metrics.get('sharpe_ratio', portfolio_metrics['sharpe_ratio']):.2f}")
        st.metric("Макс. просадка", f"{portfolio_metrics['max_drawdown']:.1%}")
    
    # 4. График роста - адаптивный
    st.markdown('<div class="section-header">📈 Динамика портфеля</div>', unsafe_allow_html=True)
    
    try:
        dates, values, initial = create_growth_chart(client_data, client_data['portfolio_type'], current_client)
        
        df = pd.DataFrame({'Дата': dates, 'Стоимость портфеля': values})
        fig = px.line(df, x='Дата', y='Стоимость портфеля', 
                     title='', color_discrete_sequence=['#1f77b4'])
        fig.update_layout(
            xaxis_title="",
            yaxis_title="Стоимость (₽)",
            hovermode='x unified',
            showlegend=False,
            height=300  # Фиксированная высота для мобильных
        )
        
        st.plotly_chart(fig, use_container_width=True)
        
    except Exception as e:
        st.error(f"Ошибка при построении графика: {e}")
    
    # 5. Рекомендации AI - всегда вертикальные
    st.markdown('<div class="section-header">🤖 Рекомендации AI</div>', unsafe_allow_html=True)
    
    recommendations = generate_client_recommendations(current_client)
    for i, rec in enumerate(recommendations):
        st.markdown(f"""
        <div class="metric-card">
            <strong>📌 {rec}</strong>
        </div>
        """, unsafe_allow_html=True)
    
    # Футер
    st.markdown("---")
    st.markdown("""
    <div style='text-align: center; color: #666; font-size: 0.9rem;'>
        <p>🤖 ЮниВест AI Советник | Адаптивная инвестиционная платформа</p>
    </div>
    """, unsafe_allow_html=True)

def main():
    """Главная функция приложения"""
    init_session_state()
    
    if not st.session_state.authenticated:
        login_page()
    else:
        dashboard_page()

if __name__ == "__main__":
    main()
