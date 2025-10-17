# app.py - полностью адаптивная версия С УЛУЧШЕННЫМ ОТОБРАЖЕНИЕМ ПОДПИСОК

import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
from datetime import datetime
import hashlib

# advanced_analysis.py - упрощенная версия прямо в app.py
import numpy as np
import pandas as pd
from typing import Dict, List, Optional, Tuple
import streamlit as st

class AdvancedPortfolioAnalysis:
    """Упрощенный класс для анализа портфеля"""
    
    def __init__(self, portfolio_dict: Dict[str, float], client_name: str = "Демо Клиент"):
        self.portfolio_dict = portfolio_dict
        self.client_name = client_name
        
    def comprehensive_analysis(self) -> Dict:
        """Упрощенный комплексный анализ"""
        return {
            'basic_metrics': {
                'annual_return': 0.12,
                'annual_volatility': 0.18,
                'sharpe_ratio': 0.67,
                'max_drawdown': -0.15,
                'client_name': self.client_name,
                'subscription_level': 'basic'
            },
            'risk_metrics': {
                'parametric_var': -0.025,
                'cvar': -0.035,
                'downside_deviation': 0.08,
                'worst_day': -0.05,
                'access_restricted': False
            },
            'recommendations': [
                f"📊 Базовый анализ для {self.client_name}",
                "💡 Рекомендуется диверсификация портфеля",
                "📈 Рассмотрите добавление защитных активов"
            ]
        }
    
    def calculate_basic_metrics(self) -> Dict:
        """Упрощенный расчет метрик"""
        return {
            'annual_return': 0.12,
            'annual_volatility': 0.18,
            'sharpe_ratio': 0.67,
            'max_drawdown': -0.15,
            'sortino_ratio': 0.75,
            'calmar_ratio': 0.80,
            'client_name': self.client_name
        }
    
    def calculate_risk_metrics(self, confidence_level: float = 0.95) -> Dict:
        """Упрощенный расчет рисков"""
        return {
            'parametric_var': -0.025,
            'historical_var': -0.020,
            'cvar': -0.035,
            'downside_deviation': 0.08,
            'worst_day': -0.05,
            'confidence_level': confidence_level,
            'access_restricted': False
        }

def display_portfolio_analysis(results: Dict) -> None:
    """Упрощенное отображение анализа"""
    if not results:
        st.error("Нет данных для отображения")
        return
    
    metrics = results.get('basic_metrics', {})
    
    if not metrics:
        st.error("Отсутствуют базовые метрики")
        return
    
    # Основные метрики
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Годовая доходность", f"{metrics.get('annual_return', 0):.1%}")
    
    with col2:
        st.metric("Волатильность", f"{metrics.get('annual_volatility', 0):.1%}")
    
    with col3:
        st.metric("Коэффициент Шарпа", f"{metrics.get('sharpe_ratio', 0):.2f}")
    
    with col4:
        st.metric("Макс. просадка", f"{metrics.get('max_drawdown', 0):.1%}")
    
    # Метрики риска
    risk_metrics = results.get('risk_metrics', {})
    if risk_metrics and not risk_metrics.get('access_restricted', True):
        st.subheader("📉 Метрики риска")
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.metric("VaR (95%)", f"{risk_metrics.get('parametric_var', 0):.2%}")
        
        with col2:
            st.metric("CVaR", f"{risk_metrics.get('cvar', 0):.2%}")
        
        with col3:
            st.metric("Downside Dev", f"{risk_metrics.get('downside_deviation', 0):.2%}")
        
        with col4:
            st.metric("Worst Day", f"{risk_metrics.get('worst_day', 0):.2%}")
    
    # Рекомендации
    st.subheader("📋 Рекомендации")
    for recommendation in results.get('recommendations', []):
        st.write(recommendation)

# ИМПОРТИРУЕМ ФУНКЦИИ ИЗ database.py
from database import (
    get_all_clients, 
    get_client_details, 
    get_portfolio_by_client, 
    generate_subscription_based_recommendations,
    get_subscription_level,
    get_subscription_details,
    can_access_advanced_analytics,
    can_access_premium_features,
    SUBSCRIPTION_FEATURES
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
    if 'current_page' not in st.session_state:
        st.session_state.current_page = "📊 Дашборд"

def display_subscription_badge(subscription_level: str) -> str:
    """Создает красивый бейдж подписки"""
    badges = {
        'trial': '🎁 <span style="background: linear-gradient(135deg, #667eea, #764ba2); color: white; padding: 4px 12px; border-radius: 20px; font-size: 0.8em; font-weight: bold;">ПРОБНЫЙ</span>',
        'basic': '📊 <span style="background: linear-gradient(135deg, #11998e, #38ef7d); color: white; padding: 4px 12px; border-radius: 20px; font-size: 0.8em; font-weight: bold;">БАЗОВЫЙ</span>',
        'advanced': '🎯 <span style="background: linear-gradient(135deg, #fc466b, #3f5efb); color: white; padding: 4px 12px; border-radius: 20px; font-size: 0.8em; font-weight: bold;">ПРОДВИНУТЫЙ</span>',
        'premium': '💎 <span style="background: linear-gradient(135deg, #ffd700, #ff8c00); color: black; padding: 4px 12px; border-radius: 20px; font-size: 0.8em; font-weight: bold;">ПРЕМИУМ</span>'
    }
    return badges.get(subscription_level, badges['trial'])

def login_page():
    """Адаптивная страница входа С ИНФОРМАЦИЕЙ О ПОДПИСКАХ"""
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
    </style>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div style='display: flex; justify-content: center; align-items: center; min-height: 80vh; padding: 1rem;'>
        <div class="login-container">
            <h1 class="main-title">🤖 ЮниВест</h1>
            <div class="subtitle">AI Советник по Инвестициям</div>
    """, unsafe_allow_html=True)
    
    clients = get_all_clients()
    
    # Показываем клиентов с их подписками
    selected_client = st.selectbox(
        "👤 Выберите клиента:",
        clients,
        format_func=lambda x: f"{x} - {get_subscription_details(x)['name']} ({get_subscription_details(x)['price']} руб/мес)",
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
                <p style="margin: 0.5rem 0 0 0; font-size: 0.8rem; color: #666;">Каждый клиент имеет разный уровень подписки</p>
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

def display_subscription_status(client_name: str):
    """Отображает статус подписки клиента"""
    subscription_level = get_subscription_level(client_name)
    subscription_details = get_subscription_details(client_name)
    
    st.sidebar.markdown("---")
    st.sidebar.subheader("💎 Ваша подписка")
    
    # Бейдж подписки
    badge_html = display_subscription_badge(subscription_level)
    st.sidebar.markdown(f"<div style='text-align: center; margin-bottom: 1rem;'>{badge_html}</div>", unsafe_allow_html=True)
    
    # Информация о текущем тарифе
    st.sidebar.write(f"**Тариф:** {subscription_details['name']}")
    st.sidebar.write(f"**Стоимость:** {subscription_details['price']} руб/мес")
    st.sidebar.write(f"**Действует до:** {subscription_details['expires']}")
    
    # Доступные функции
    st.sidebar.markdown("**Доступные функции:**")
    features = SUBSCRIPTION_FEATURES[subscription_level]['features']
    for feature in features[:3]:
        st.sidebar.write(f"• {feature}")
    
    # Кнопка улучшения, если не премиум
    if subscription_level != 'premium':
        st.sidebar.markdown("---")
        levels = ['trial', 'basic', 'advanced', 'premium']
        current_index = levels.index(subscription_level) if subscription_level in levels else 0
        next_level = levels[current_index + 1] if current_index < len(levels) - 1 else 'premium'
        next_sub_info = SUBSCRIPTION_FEATURES.get(next_level, {})
        
        if st.sidebar.button(f"🚀 Улучшить до {next_sub_info.get('name', 'Премиум')}", use_container_width=True):
            st.session_state.current_page = "💎 Тарифы"
            st.rerun()

def show_feature_unlock_prompt(feature_name: str, required_level: str, client_name: str):
    """Показывает промт для разблокировки функции"""
    current_level = get_subscription_level(client_name)
    required_plan = SUBSCRIPTION_FEATURES[required_level]
    
    st.warning(f"🔒 **{feature_name} доступна на тарифе {required_plan['name']}**")
    
    col1, col2 = st.columns([3, 1])
    
    with col1:
        st.write(f"**Что вы получите:**")
        for feature in required_plan['features'][:3]:
            st.write(f"• {feature}")
    
    with col2:
        if st.button(f"💳 {required_plan['price']}₽/мес", key=f"unlock_{feature_name}"):
            st.session_state.current_page = "💎 Тарифы"
            st.rerun()

def display_pricing_page():
    """Страница с сравнением тарифов"""
    st.title("💎 Выберите свой тариф")
    st.write("Начните с бесплатного пробного периода и улучшайте по мере роста ваших потребностей")
    
    # Создаем колонки для тарифов
    col1, col2, col3, col4 = st.columns(4)
    
    for i, level in enumerate(['trial', 'basic', 'advanced', 'premium']):
        plan = SUBSCRIPTION_FEATURES[level]
        with [col1, col2, col3, col4][i]:
            st.subheader(plan['name'])
            st.metric("Стоимость", f"{plan['price']}₽/мес")
            
            st.write("**Включено:**")
            for feature in plan['features'][:4]:
                st.write(f"✅ {feature}")
            
            if level == 'trial':
                st.button("🎁 Начать пробный период", key=f"btn_{level}", use_container_width=True)
            else:
                st.button(f"💳 Выбрать {plan['name']}", key=f"btn_{level}", use_container_width=True)

def advanced_analytics_page():
    """Страница расширенной аналитики"""
    current_client = st.session_state.current_user
    
    st.title("📈 Расширенная аналитика")
    
    # Проверяем доступ
    if not can_access_advanced_analytics(current_client):
        show_feature_unlock_prompt("Расширенная аналитика", "advanced", current_client)
        return
    
    st.success(f"🎯 У вас есть доступ к расширенной аналитике!")
    
    # Загружаем данные клиента
    client_data = get_client_details(current_client)
    portfolio_dict = get_portfolio_by_client(current_client)
    
    if not portfolio_dict:
        st.error("❌ Не удалось загрузить портфель")
        return
    
    # Запускаем расширенный анализ
    with st.spinner("🔍 Проводим углубленный анализ портфеля..."):
        analyzer = AdvancedPortfolioAnalysis(portfolio_dict, current_client)
        results = analyzer.comprehensive_analysis()
    
    if results:
        display_portfolio_analysis(results)

def dashboard_page():
    """Адаптивная панель управления С УЛУЧШЕННЫМ ОТОБРАЖЕНИЕМ ПОДПИСОК"""
    
    current_client = st.session_state.current_user
    client_data = get_client_details(current_client)
    portfolio_dict = get_portfolio_by_client(current_client)
    
    if not client_data or not portfolio_dict:
        st.error("❌ Ошибка загрузки данных")
        return
    
    # ОТЛАДОЧНАЯ ИНФОРМАЦИЯ
    st.sidebar.markdown("---")
    st.sidebar.subheader("🔧 Отладка подписок")
    subscription_level = get_subscription_level(current_client)
    subscription_details = get_subscription_details(current_client)
    st.sidebar.write(f"**Клиент:** {current_client}")
    st.sidebar.write(f"**Уровень:** {subscription_level}")
    st.sidebar.write(f"**Название:** {subscription_details['name']}")
    st.sidebar.write(f"**Цена:** {subscription_details['price']} руб")
    st.sidebar.write(f"**Advanced доступ:** {can_access_advanced_analytics(current_client)}")
    st.sidebar.write(f"**Premium доступ:** {can_access_premium_features(current_client)}")
    
    # Определяем уровень доступа
    has_advanced_access = can_access_advanced_analytics(current_client)
    has_premium_access = can_access_premium_features(current_client)
    subscription_level = get_subscription_level(current_client)
    subscription_details = get_subscription_details(current_client)
    
    # Бейдж подписки
    badge_html = display_subscription_badge(subscription_level)
    
    # ЗАГОЛОВОК С БЕЙДЖЕМ ПОДПИСКИ
    st.markdown(f'''
    <div style="text-align: center; padding: 2rem; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white; border-radius: 15px; margin-bottom: 2rem;">
        <h1 style="color: white; margin-bottom: 0.5rem;">🤖 ЮниВест AI Советник</h1>
        <h2 style="color: white; margin: 0;">{current_client} - {subscription_details['name']}</h2>
        <div style="margin-top: 0.5rem;">
            {badge_html}
        </div>
    </div>
    ''', unsafe_allow_html=True)
    
    # Используем разные раскладки для разных устройств
    col1, col2, col3 = st.columns([2, 1, 1])
    
    with col1:
        st.markdown(f'<div style="font-size: 1.2rem;">👤 <strong>{current_client}</strong></div>', unsafe_allow_html=True)
    
    with col2:
        st.metric("Инвестиции", f"{client_data['initial_investment']:,.0f} ₽")
    
    with col3:
        if st.button("🚪 Выйти", use_container_width=True, type="secondary"):
            st.session_state.authenticated = False
            st.session_state.current_user = None
            st.rerun()
    
    st.markdown("---")
    
    # SIDEBAR
    with st.sidebar:
        st.title("🎯 Навигация")
        
        # Навигация по страницам
        page = st.radio("Выберите раздел:", 
                       ["📊 Дашборд", "📈 Расширенная аналитика", "💎 Тарифы"],
                       index=0)
        
        if page != st.session_state.current_page:
            st.session_state.current_page = page
            st.rerun()
        
        # Переключение пользователей
        st.markdown("---")
        clients = get_all_clients()
        new_user = st.selectbox("👥 Выберите клиента:", clients, 
                              index=clients.index(current_client))
        
        if new_user != current_client:
            st.session_state.current_user = new_user
            st.rerun()
        
        st.markdown("---")
        
        # Быстрая статистика
        st.subheader("📊 Статистика")
        col1, col2 = st.columns(2)
        with col1:
            st.metric("Активы", len(portfolio_dict))
        with col2:
            st.metric("Риск", client_data['risk_profile'])
        
        # Статус подписки
        display_subscription_status(current_client)
        
        st.markdown("---")
        
        # Рекомендации AI
        st.subheader("🤖 Советы")
        recommendations = generate_subscription_based_recommendations(current_client)
        for rec in recommendations[:2]:
            st.info(rec)
    
    # ОСНОВНОЙ КОНТЕНТ
    
    # 1. Профиль клиента
    st.subheader("👤 Профиль клиента")
    col1, col2 = st.columns(2)
    
    with col1:
        st.write(f"**Тип портфеля:** {client_data['portfolio_type']}")
        st.write(f"**Уровень риска:** {client_data['risk_profile']}")
        st.write(f"**Инвестиционный горизонт:** {client_data['investment_horizon']}")
    
    with col2:
        st.write(f"**Опыт:** {client_data['experience']}")
        st.write(f"**Цель:** {client_data['financial_goals']}")
        st.write(f"**Целевая сумма:** {client_data['target_amount']:,.0f} ₽")
    
    # 2. Обзор портфеля
    st.subheader("📊 Обзор портфеля")
    weights_df = pd.DataFrame(list(portfolio_dict.items()), columns=['Актив', 'Доля'])
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        fig_pie = px.pie(weights_df, values='Доля', names='Актив', hole=0.3)
        st.plotly_chart(fig_pie, use_container_width=True)
    
    with col2:
        st.dataframe(weights_df, use_container_width=True, hide_index=True)
    
    # 3. Ключевые метрики
    st.subheader("🔍 Ключевые метрики")
    portfolio_metrics = create_portfolio_metrics(client_data, portfolio_dict)
    
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Ожидаемая доходность", f"{portfolio_metrics['expected_return']:.1%}")
    with col2:
        st.metric("Волатильность", f"{portfolio_metrics['volatility']:.1%}")
    with col3:
        st.metric("Коэффициент Шарпа", f"{portfolio_metrics['sharpe_ratio']:.2f}")
    with col4:
        st.metric("Макс. просадка", f"{portfolio_metrics['max_drawdown']:.1%}")
    
    # 4. Рекомендации AI - РАЗНЫЕ ДЛЯ РАЗНЫХ ПОДПИСОК
    st.subheader("🤖 Рекомендации AI")
    
    recommendations = generate_subscription_based_recommendations(current_client)
    
    for rec in recommendations:
        st.info(rec)
    
    # Премиум секция (только для премиум подписчиков)
    if has_premium_access:
        st.subheader("💎 Премиум аналитика")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.success("""
            **🤖 AI Прогноз на месяц**
            - Ожидаемый рост: +4.5%
            - Уверенность: 78%
            - Рекомендация: Держать позиции
            """)
        
        with col2:
            st.success("""
            **🏆 Сравнение с эталонами**
            - Ваш портфель: +15.2%
            - S&P 500: +12.1%
            - Nasdaq: +18.3%
            """)
    elif has_advanced_access:
        # Предложение улучшить до премиум
        st.info("💎 **AI-прогнозы и сравнение с эталонами доступны в Премиум тарифе**")
        if st.button("💎 Перейти на Премиум", key="upgrade_premium"):
            show_feature_unlock_prompt("AI-прогнозы", "premium", current_client)

def main():
    """Главная функция приложения"""
    init_session_state()
    
    if not st.session_state.authenticated:
        login_page()
    else:
        # Роутинг по страницам
        if st.session_state.current_page == "📊 Дашборд":
            dashboard_page()
        elif st.session_state.current_page == "📈 Расширенная аналитика":
            advanced_analytics_page()
        elif st.session_state.current_page == "💎 Тарифы":
            display_pricing_page()

if __name__ == "__main__":
    main()


