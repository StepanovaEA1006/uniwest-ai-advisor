# app.py - полностью адаптивная версия С УЛУЧШЕННЫМ ОТОБРАЖЕНИЕМ ПОДПИСОК

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
    generate_subscription_based_recommendations,  # ИСПОЛЬЗУЕМ ОБНОВЛЕННУЮ ФУНКЦИЮ
    get_subscription_level,
    get_subscription_details,  # ДОБАВИЛИ ЭТУ ФУНКЦИЮ
    can_access_advanced_analytics,
    can_access_premium_features,
    SUBSCRIPTION_FEATURES
)

# Импорт анализа портфеля
from advanced_analysis import AdvancedPortfolioAnalysis, display_portfolio_analysis

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
        .client-option {
            padding: 0.5rem;
            margin: 0.5rem 0;
            border-radius: 10px;
            border: 1px solid #e0e0e0;
        }
        .client-option:hover {
            background: #f8f9fa;
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
    
    # Создаем опции с информацией о подписке
    client_options = []
    for client in clients:
        subscription = get_subscription_level(client)
        subscription_details = get_subscription_details(client)
        badge = display_subscription_badge(subscription)
        client_options.append({
            'name': client,
            'subscription': subscription,
            'badge': badge,
            'price': subscription_details['price']
        })
    
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
    
    # Индикатор уровня подписки
    levels = ['trial', 'basic', 'advanced', 'premium']
    current_index = levels.index(subscription_level) if subscription_level in levels else 0
    
    progress = (current_index + 1) / len(levels)
    st.sidebar.progress(progress)
    
    # Информация о текущем тарифе
    st.sidebar.write(f"**Тариф:** {subscription_details['name']}")
    st.sidebar.write(f"**Стоимость:** {subscription_details['price']} руб/мес")
    st.sidebar.write(f"**Действует до:** {subscription_details['expires']}")
    
    # Доступные функции
    st.sidebar.markdown("**Доступные функции:**")
    features = SUBSCRIPTION_FEATURES[subscription_level]['features']
    for feature in features[:3]:  # Показываем первые 3 функции
        st.sidebar.write(f"• {feature}")
    
    # Кнопка улучшения, если не премиум
    if subscription_level != 'premium':
        st.sidebar.markdown("---")
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
        
        if 'upgrade_reason' in required_plan:
            st.info(f"💡 {required_plan['upgrade_reason']}")
    
    with col2:
        if st.button(f"💳 {required_plan['price']}₽/мес", key=f"unlock_{feature_name}"):
            st.session_state.current_page = "💎 Тарифы"
            st.rerun()

def display_pricing_page():
    """Страница с сравнением тарифов"""
    st.markdown("""
    <style>
    .pricing-card {
        background: white;
        border-radius: 15px;
        padding: 2rem;
        margin: 1rem 0;
        border: 2px solid #e0e0e0;
        transition: all 0.3s ease;
        height: 100%;
    }
    .pricing-card:hover {
        border-color: #1f77b4;
        transform: translateY(-5px);
        box-shadow: 0 10px 30px rgba(0,0,0,0.1);
    }
    .pricing-card.premium {
        border-color: #ffd700;
        background: linear-gradient(135deg, #fffaf0, #fffde7);
    }
    .feature-list {
        margin: 1rem 0;
    }
    .feature-item {
        margin: 0.5rem 0;
        display: flex;
        align-items: center;
    }
    .price-tag {
        font-size: 2rem;
        font-weight: bold;
        color: #1f77b4;
        margin: 1rem 0;
    }
    </style>
    """, unsafe_allow_html=True)
    
    st.title("💎 Выберите свой тариф")
    st.write("Начните с бесплатного пробного периода и улучшайте по мере роста ваших потребностей")
    
    # Создаем колонки для тарифов
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        display_pricing_card('trial')
    with col2:
        display_pricing_card('basic')
    with col3:
        display_pricing_card('advanced')
    with col4:
        display_pricing_card('premium')

def display_pricing_card(level: str):
    """Отображает карточку тарифа"""
    plan = SUBSCRIPTION_FEATURES[level]
    
    st.markdown(f"""
    <div class="pricing-card {'premium' if level == 'premium' else ''}">
        <h3>{plan['name']}</h3>
        <div class="price-tag">{plan['price']}₽</div>
        <p>/месяц</p>
    """, unsafe_allow_html=True)
    
    # Кнопка выбора тарифа
    if level == 'trial':
        st.button("🎁 Начать пробный период", key=f"btn_{level}", use_container_width=True)
    else:
        st.button(f"💳 Выбрать {plan['name']}", key=f"btn_{level}", use_container_width=True,
                type="primary" if level == 'premium' else "secondary")
    
    # Список функций
    st.markdown("<div class='feature-list'>", unsafe_allow_html=True)
    for feature in plan['features'][:5]:  # Показываем первые 5 функций
        st.markdown(f"<div class='feature-item'>✅ {feature}</div>", unsafe_allow_html=True)
    
    # Ограничения для trial и basic
    if 'limitations' in plan:
        st.markdown("---")
        for limitation in plan['limitations'][:2]:  # Показываем первые 2 ограничения
            st.markdown(f"<div class='feature-item'>{limitation}</div>", unsafe_allow_html=True)
    
    st.markdown("</div></div>", unsafe_allow_html=True)

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
        
        # Дополнительные премиум-функции
        if can_access_premium_features(current_client):
            st.markdown("---")
            st.subheader("💎 Премиум аналитика")
            
            col1, col2 = st.columns(2)
            
            with col1:
                st.info("""
                **🤖 AI Прогнозы:**
                - Ожидаемый рост: +4.5% в следующем месяце
                - Уверенность: 78%
                - Рекомендация: Держать позиции
                """)
            
            with col2:
                st.info("""
                **🏆 Сравнение с эталонами:**
                - Ваш портфель: +15.2%
                - S&P 500: +12.1% 
                - Nasdaq: +18.3%
                - Превышение эталона: ✅
                """)

def dashboard_page():
    """Адаптивная панель управления С УЛУЧШЕННЫМ ОТОБРАЖЕНИЕМ ПОДПИСОК"""
    
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
        
        .premium-feature {
            background: linear-gradient(135deg, #fffaf0, #fffde7) !important;
            border-left: 4px solid #ffd700 !important;
        }
        
        .restricted-feature {
            background: linear-gradient(135deg, #f8f9fa, #e9ecef) !important;
            border-left: 4px solid #6c757d !important;
            opacity: 0.7;
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
    
    # ОТЛАДОЧНАЯ ИНФОРМАЦИЯ - ДОБАВИЛИ ЭТОТ БЛОК
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
    
    # АДАПТИВНЫЙ ХЕДЕР С БЕЙДЖЕМ ПОДПИСКИ
    st.markdown(f'''
    <div class="main-header">
        🤖 ЮниВест - AI Советник 
        <div style="display: inline-block; margin-left: 10px;">
            {badge_html}
        </div>
    </div>
    ''', unsafe_allow_html=True)
    
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
        
        # Навигация по страницам
        page = st.radio("Выберите раздел:", 
                       ["📊 Дашборд", "📈 Расширенная аналитики", "💎 Тарифы"],
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
        
        # Быстрая статистика - адаптивная
        st.subheader("📊 Статистика")
        col1, col2 = st.columns(2)
        with col1:
            st.metric("Активы", len(portfolio_dict))
        with col2:
            st.metric("Риск", client_data['risk_profile'])
        
        # Статус подписки
        display_subscription_status(current_client)
        
        st.markdown("---")
        
        # Рекомендации AI - ИСПРАВИЛИ ЗДЕСЬ: используем новую функцию
        st.subheader("🤖 Советы")
        recommendations = generate_subscription_based_recommendations(current_client)
        for rec in recommendations[:2]:  # Меньше рекомендаций на мобильных
            st.info(rec)
    
    # ОСНОВНОЙ КОНТЕНТ - АДАПТИВНЫЙ
    
    # 1. Профиль клиента - адаптивная сетка С ДЕТАЛЬНОЙ ИНФОРМАЦИЕЙ О ПОДПИСКЕ
    st.markdown(f"""
    <div class="client-card">
        <h2>👤 {current_client} {badge_html}</h2>
        <p><em>{client_data['description']}</em></p>
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 1rem; margin-top: 1rem;">
            <div>
                <p><strong>💼 Тип портфеля:</strong> {client_data['portfolio_type']}</p>
                <p><strong>🎯 Цель:</strong> {client_data['financial_goals']}</p>
                <p><strong>💰 Цель:</strong> {client_data['target_amount']:,.0f} ₽</p>
                <p><strong>💎 Подписка:</strong> {subscription_details['name']}</p>
            </div>
            <div>
                <p><strong>⚡ Уровень риска:</strong> {client_data['risk_profile']}</p>
                <p><strong>💪 Опыт:</strong> {client_data['experience']}</p>
                <p><strong>📅 Горизонт:</strong> {client_data['investment_horizon']}</p>
                <p><strong>💰 Стоимость:</strong> {subscription_details['price']} руб/мес</p>
            </div>
        </div>
        <div style="margin-top: 1rem; padding: 1rem; background: #f8f9fa; border-radius: 10px;">
            <p><strong>🚀 Доступные возможности:</strong></p>
            <p>{'💎 AI-прогнозы и премиум аналитика' if has_premium_access else '🎯 Расширенная аналитика и оптимизация' if has_advanced_access else '📊 Базовые метрики и рекомендации'}</p>
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
    
    # 3. Ключевые метрики - адаптивная сетка С УЧЕТОМ ПОДПИСКИ
    st.markdown('<div class="section-header">🔍 Ключевые метрики</div>', unsafe_allow_html=True)
    
    portfolio_metrics = create_portfolio_metrics(client_data, portfolio_dict)
    key_metrics = client_data.get('key_metrics', {})
    
    # Базовые метрики (всегда видны)
    cols = st.columns(2)
    with cols[0]:
        st.metric("Ожидаемая доходность", f"{key_metrics.get('expected_return', portfolio_metrics['expected_return']):.2%}")
        st.metric("Волатильность", f"{key_metrics.get('volatility', portfolio_metrics['volatility']):.2%}")
    
    with cols[1]:
        st.metric("Коэффициент Шарпа", f"{key_metrics.get('sharpe_ratio', portfolio_metrics['sharpe_ratio']):.2f}")
        st.metric("Макс. просадка", f"{portfolio_metrics['max_drawdown']:.1%}")
    
    # Продвинутые метрики (только для advanced+)
    if has_advanced_access:
        st.markdown('<div class="section-header">🎯 Продвинутые метрики</div>', unsafe_allow_html=True)
        
        # Запускаем расширенный анализ
        with st.spinner("🔍 Анализируем риски..."):
            analyzer = AdvancedPortfolioAnalysis(portfolio_dict, current_client)
            basic_results = analyzer.calculate_basic_metrics()
            risk_metrics = analyzer.calculate_risk_metrics()
        
        if basic_results and 'sortino_ratio' in basic_results:
            cols = st.columns(2)
            with cols[0]:
                st.metric("Коэффициент Сортино", f"{basic_results.get('sortino_ratio', 0):.2f}",
                         help="Доходность на единицу downside риска")
            with cols[1]:
                st.metric("Коэффициент Калмара", f"{basic_results.get('calmar_ratio', 0):.2f}",
                         help="Доходность к максимальной просадке")
        
        if risk_metrics and not risk_metrics.get('access_restricted', True):
            st.markdown('<div class="section-header">📉 Метрики риска</div>', unsafe_allow_html=True)
            cols = st.columns(4)
            
            with cols[0]:
                st.metric("VaR (95%)", f"{risk_metrics.get('parametric_var', 0):.2%}")
            with cols[1]:
                st.metric("CVaR", f"{risk_metrics.get('cvar', 0):.2%}")
            with cols[2]:
                st.metric("Downside Dev", f"{risk_metrics.get('downside_deviation', 0):.2%}")
            with cols[3]:
                st.metric("Worst Day", f"{risk_metrics.get('worst_day', 0):.2%}")
    else:
        # Предложение улучшить подписку
        st.info("🔒 **Расширенные метрики риска доступны на тарифе Продвинутый**")
        if st.button("🎯 Разблокировать метрики риска", key="unlock_metrics"):
            show_feature_unlock_prompt("Расширенные метрики", "advanced", current_client)
    
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
    
    # 5. Рекомендации AI - РАЗНЫЕ ДЛЯ РАЗНЫХ ПОДПИСОК - ИСПРАВИЛИ ЗДЕСЬ: используем новую функцию
    st.markdown('<div class="section-header">🤖 Рекомендации AI</div>', unsafe_allow_html=True)
    
    recommendations = generate_subscription_based_recommendations(current_client)
    
    for i, rec in enumerate(recommendations):
        # Разные стили карточек в зависимости от типа рекомендации
        if "🔒" in rec or "🚀" in rec:
            card_class = "metric-card restricted-feature"
        elif "💎" in rec:
            card_class = "metric-card premium-feature"
        elif "🎯" in rec:
            card_class = "metric-card"
        else:
            card_class = "metric-card"
            
        st.markdown(f"""
        <div class="{card_class}">
            <strong>{rec}</strong>
        </div>
        """, unsafe_allow_html=True)
    
    # Премиум секция (только для премиум подписчиков)
    if has_premium_access:
        st.markdown('<div class="section-header">💎 Премиум аналитика</div>', unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            <div class="metric-card premium-feature">
                <strong>🤖 AI Прогноз на месяц</strong>
                <p>📈 Ожидаемый рост: +4.5%</p>
                <p>🎯 Уверенность: 78%</p>
                <p>💡 Рекомендация: Держать позиции</p>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown("""
            <div class="metric-card premium-feature">
                <strong>🏆 Сравнение с эталонами</strong>
                <p>✅ Ваш портфель: +15.2%</p>
                <p>📊 S&P 500: +12.1%</p>
                <p>🚀 Nasdaq: +18.3%</p>
            </div>
            """, unsafe_allow_html=True)
    elif has_advanced_access:
        # Предложение улучшить до премиум
        st.info("💎 **AI-прогнозы и сравнение с эталонами доступны в Премиум тарифе**")
        if st.button("💎 Перейти на Премиум", key="upgrade_premium"):
            show_feature_unlock_prompt("AI-прогнозы", "premium", current_client)
    
    # Футер
    st.markdown("---")
    st.markdown("""
    <div style='text-align: center; color: #666; font-size: 0.9rem;'>
        <p>🤖 ЮниВест AI Советник | Адаптивная инвестиционная платформа</p>
        <p>Ваш тариф: <strong>{subscription_details['name']}</strong> | Следующий уровень: <strong>{'Максимальный' if subscription_level == 'premium' else 'Премиум' if subscription_level == 'advanced' else 'Продвинутый'}</strong></p>
    </div>
    """.format(subscription_details=subscription_details, subscription_level=subscription_level), unsafe_allow_html=True)

def main():
    """Главная функция приложения"""
    init_session_state()
    
    # ТЕСТИРОВАНИЕ ПОДПИСОК - ДОБАВИЛИ ЭТОТ БЛОК
    if st.session_state.authenticated and not hasattr(st.session_state, 'subscription_tested'):
        current_client = st.session_state.current_user
        subscription_level = get_subscription_level(current_client)
        subscription_details = get_subscription_details(current_client)
        st.sidebar.success(f"✅ Подписка: {subscription_details['name']} ({subscription_level})")
        st.session_state.subscription_tested = True
    
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

