# app.py - УЛУЧШЕННАЯ ВЕРСИЯ С СОВРЕМЕННЫМ ДИЗАЙНОМ

import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
from datetime import datetime, timedelta
import hashlib
from typing import Dict, List, Optional, Tuple

# =============================================
# КОНФИГУРАЦИЯ СТРАНИЦЫ И СТИЛИ
# =============================================

def setup_page_config():
    """Настройка современного внешнего вида"""
    st.set_page_config(
        page_title="🤖 ЮниВест AI - Инвестиционный советник",
        page_icon="📊",
        layout="wide",
        initial_sidebar_state="expanded"
    )

def inject_modern_css():
    """Внедряет современный CSS с градиентами и анимациями"""
    st.markdown("""
    <style>
    /* Основные стили */
    .main-header {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 2rem;
        border-radius: 20px;
        color: white;
        margin-bottom: 2rem;
        text-align: center;
        box-shadow: 0 10px 30px rgba(0,0,0,0.1);
    }
    
    .metric-card {
        background: white;
        padding: 1.5rem;
        border-radius: 15px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
        border-left: 4px solid #667eea;
        transition: transform 0.3s ease;
    }
    
    .metric-card:hover {
        transform: translateY(-5px);
    }
    
    .section-header {
        background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
        color: white;
        padding: 1rem 1.5rem;
        border-radius: 12px;
        margin: 2rem 0 1rem 0;
        font-weight: 600;
    }
    
    .subscription-badge {
        padding: 8px 16px;
        border-radius: 25px;
        font-weight: bold;
        font-size: 0.8em;
        margin-left: 10px;
    }
    
    .badge-basic { background: linear-gradient(135deg, #11998e, #38ef7d); color: white; }
    .badge-advanced { background: linear-gradient(135deg, #fc466b, #3f5efb); color: white; }
    .badge-premium { background: linear-gradient(135deg, #ffd700, #ff8c00); color: black; }
    
    /* Анимации */
    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(20px); }
        to { opacity: 1; transform: translateY(0); }
    }
    
    .fade-in {
        animation: fadeIn 0.6s ease-in;
    }
    
    /* Кнопки */
    .stButton button {
        border-radius: 10px;
        font-weight: 600;
        transition: all 0.3s ease;
    }
    
    .stButton button:hover {
        transform: scale(1.05);
    }
    
    /* Сайдбар */
    .css-1d391kg {
        background: linear-gradient(180deg, #f8f9fa 0%, #e9ecef 100%);
    }
    </style>
    """, unsafe_allow_html=True)

# =============================================
# КЛАСС АНАЛИЗА ПОРТФЕЛЯ (УЛУЧШЕННЫЙ)
# =============================================

class ModernPortfolioAnalyzer:
    """Современный анализатор портфеля с улучшенной визуализацией"""
    
    def __init__(self, portfolio_dict: Dict[str, float], client_name: str = "Клиент"):
        self.portfolio_dict = portfolio_dict
        self.client_name = client_name
        self.portfolio_type = self._determine_portfolio_type()
    
    def _determine_portfolio_type(self) -> str:
        """Определяет тип портфеля с цветовым кодированием"""
        aggressive_keywords = ['TSLA', 'NVDA', 'AMD', 'ARKK', 'BTC', 'ETH']
        conservative_keywords = ['BND', 'GOVT', 'SHY', 'Cash']
        
        aggressive_score = sum(weight for asset, weight in self.portfolio_dict.items() 
                             if any(keyword in asset for keyword in aggressive_keywords))
        
        if aggressive_score > 0.4:
            return {'type': 'агрессивный', 'color': '#ff4757', 'icon': '🚀'}
        elif any(keyword in asset for asset in self.portfolio_dict for keyword in conservative_keywords):
            conservative_score = sum(weight for asset, weight in self.portfolio_dict.items() 
                                   if any(keyword in asset for keyword in conservative_keywords))
            if conservative_score > 0.5:
                return {'type': 'консервативный', 'color': '#2ed573', 'icon': '🛡️'}
            elif conservative_score > 0.3:
                return {'type': 'доходный', 'color': '#ffa502', 'icon': '💰'}
        return {'type': 'сбалансированный', 'color': '#3742fa', 'icon': '⚖️'}
    
    def get_portfolio_summary(self) -> Dict:
        """Возвращает сводку по портфелю"""
        total_value = 1_500_000  # Примерное значение
        assets_count = len(self.portfolio_dict)
        
        return {
            'total_value': total_value,
            'assets_count': assets_count,
            'portfolio_type': self.portfolio_type,
            'diversification_score': self._calculate_diversification_score()
        }
    
    def _calculate_diversification_score(self) -> float:
        """Рассчитывает оценку диверсификации"""
        weights = list(self.portfolio_dict.values())
        if not weights:
            return 0.0
        
        # Простая энтропия для оценки диверсификации
        entropy = -sum(w * np.log(w) for w in weights if w > 0)
        max_entropy = np.log(len(weights))
        
        return min(entropy / max_entropy if max_entropy > 0 else 0, 1.0)
    
    def generate_performance_data(self) -> pd.DataFrame:
        """Генерирует исторические данные производительности"""
        dates = pd.date_range(start='2020-01-01', end='2024-01-01', freq='M')
        np.random.seed(42)
        
        # Параметры в зависимости от типа портфеля
        params = {
            'агрессивный': {'mean': 0.015, 'std': 0.08},
            'сбалансированный': {'mean': 0.010, 'std': 0.05},
            'доходный': {'mean': 0.008, 'std': 0.04},
            'консервативный': {'mean': 0.005, 'std': 0.02}
        }
        
        portfolio_params = params.get(self.portfolio_type['type'], params['сбалансированный'])
        returns = np.random.normal(portfolio_params['mean'], portfolio_params['std'], len(dates))
        
        # Добавляем кризисные периоды
        crisis_periods = [
            ('2020-02-01', '2020-04-01', -0.25),
            ('2022-01-01', '2022-10-01', -0.15)
        ]
        
        for start, end, impact in crisis_periods:
            mask = (dates >= pd.to_datetime(start)) & (dates <= pd.to_datetime(end))
            if mask.any():
                returns[mask] += np.random.normal(impact, 0.05, mask.sum())
        
        # Рассчитываем стоимость портфеля
        initial_value = 1_000_000
        portfolio_values = [initial_value]
        for ret in returns:
            portfolio_values.append(portfolio_values[-1] * (1 + ret))
        
        df = pd.DataFrame({
            'Date': dates,
            'Value': portfolio_values[1:],
            'Return': returns,
            'Cumulative_Return': (np.array(portfolio_values[1:]) / initial_value - 1)
        })
        
        return df

# =============================================
# ВИЗУАЛЬНЫЕ КОМПОНЕНТЫ
# =============================================

def create_metric_card(title: str, value: str, delta: str = None, help_text: str = None):
    """Создает красивую карточку с метрикой"""
    col1, col2 = st.columns([3, 1])
    
    with col1:
        st.metric(title, value, delta)
    
    with col2:
        if help_text:
            with st.expander("ℹ️"):
                st.info(help_text)

def create_performance_chart(data: pd.DataFrame, title: str = "История портфеля"):
    """Создает интерактивный график производительности"""
    fig = go.Figure()
    
    fig.add_trace(go.Scatter(
        x=data['Date'],
        y=data['Value'],
        mode='lines',
        name='Стоимость портфеля',
        line=dict(color='#667eea', width=3),
        fill='tozeroy',
        fillcolor='rgba(102, 126, 234, 0.1)'
    ))
    
    fig.update_layout(
        title=title,
        xaxis_title="Дата",
        yaxis_title="Стоимость (рубли)",
        template="plotly_white",
        height=400,
        showlegend=True
    )
    
    return fig

def create_returns_chart(data: pd.DataFrame):
    """Создает график доходности"""
    colors = ['#ff4757' if x < 0 else '#2ed573' for x in data['Return'] * 100]
    
    fig = go.Figure()
    
    fig.add_trace(go.Bar(
        x=data['Date'],
        y=data['Return'] * 100,
        marker_color=colors,
        name='Месячная доходность',
        opacity=0.8
    ))
    
    fig.update_layout(
        title="📈 Месячная доходность",
        xaxis_title="Дата",
        yaxis_title="Доходность (%)",
        template="plotly_white",
        height=300
    )
    
    return fig

def create_asset_allocation_chart(portfolio_dict: Dict):
    """Создает круговую диаграмму распределения активов"""
    if not portfolio_dict:
        return None
    
    df = pd.DataFrame(list(portfolio_dict.items()), columns=['Актив', 'Доля'])
    
    fig = px.pie(
        df, 
        values='Доля', 
        names='Актив',
        title="📊 Распределение активов",
        hole=0.4,
        color_discrete_sequence=px.colors.qualitative.Set3
    )
    
    fig.update_traces(textposition='inside', textinfo='percent+label')
    fig.update_layout(height=400)
    
    return fig

# =============================================
# СТРАНИЦЫ ПРИЛОЖЕНИЯ
# =============================================

def login_page():
    """Современная страница входа"""
    st.markdown("""
    <div class="main-header">
        <h1 style="color: white; margin-bottom: 0.5rem;">🤖 ЮниВест AI</h1>
        <p style="color: white; opacity: 0.9; font-size: 1.2rem;">Интеллектуальный инвестиционный советник</p>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        with st.container():
            st.markdown("### 🔐 Вход в систему")
            
            clients = ['Иван Петров', 'Мария Сидорова', 'Алексей Козлов', 'Елена Волкова', 'Дмитрий Смирнов']
            selected_client = st.selectbox("Выберите клиента:", clients)
            
            password = st.text_input("Пароль:", type="password", placeholder="Введите демо-пароль")
            
            if st.button("🚀 Войти", use_container_width=True, type="primary"):
                if password == "demo123":
                    st.session_state.authenticated = True
                    st.session_state.current_user = selected_client
                    st.rerun()
                else:
                    st.error("❌ Неверный пароль. Используйте 'demo123'")
            
            st.markdown("---")
            st.info("""
            **💡 Демо-доступ:** 
            - Пароль: `demo123`
            - Каждый клиент имеет разные данные портфеля
            - Тестируйте различные сценарии анализа
            """)

def dashboard_page():
    """Главная панель управления"""
    current_user = st.session_state.current_user
    
    # Заголовок с информацией о клиенте
    col1, col2, col3 = st.columns([2, 1, 1])
    
    with col1:
        st.markdown(f"""
        <div class="main-header" style="text-align: left; padding: 1.5rem;">
            <h2 style="color: white; margin: 0;">👋 Добро пожаловать, {current_user}</h2>
            <p style="color: white; opacity: 0.9; margin: 0.5rem 0 0 0;">Панель управления инвестициями</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        subscription_level = get_subscription_level(current_user)
        badge_html = display_subscription_badge(subscription_level)
        st.markdown(f"<div style='text-align: center;'>{badge_html}</div>", unsafe_allow_html=True)
    
    with col3:
        if st.button("🚪 Выйти", use_container_width=True):
            st.session_state.authenticated = False
            st.session_state.current_user = None
            st.rerun()
    
    # Основные метрики
    st.markdown("### 📊 Обзор портфеля")
    
    portfolio_data = get_portfolio_by_client(current_user)
    analyzer = ModernPortfolioAnalyzer(portfolio_data, current_user)
    summary = analyzer.get_portfolio_summary()
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        create_metric_card(
            "Общая стоимость", 
            f"₽{summary['total_value']:,.0f}",
            help_text="Текущая рыночная стоимость вашего портфеля"
        )
    
    with col2:
        create_metric_card(
            "Количество активов", 
            str(summary['assets_count']),
            help_text="Диверсификация по количеству инструментов"
        )
    
    with col3:
        portfolio_type = summary['portfolio_type']
        create_metric_card(
            "Тип портфеля", 
            f"{portfolio_type['icon']} {portfolio_type['type'].title()}",
            help_text="Определяется на основе распределения активов и риска"
        )
    
    with col4:
        create_metric_card(
            "Оценка диверсификации", 
            f"{summary['diversification_score']:.0%}",
            help_text="Насколько хорошо диверсифицирован ваш портфель"
        )
    
    # Графики и визуализации
    col1, col2 = st.columns(2)
    
    with col1:
        # Распределение активов
        fig_pie = create_asset_allocation_chart(portfolio_data)
        if fig_pie:
            st.plotly_chart(fig_pie, use_container_width=True)
    
    with col2:
        # Историческая производительность
        performance_data = analyzer.generate_performance_data()
        fig_perf = create_performance_chart(performance_data)
        st.plotly_chart(fig_perf, use_container_width=True)
    
    # Детальная аналитика
    st.markdown("### 📈 Детальная аналитика")
    
    tab1, tab2, tab3 = st.tabs(["📊 Производительность", "⚡ Риски", "💡 Рекомендации"])
    
    with tab1:
        col1, col2 = st.columns(2)
        
        with col1:
            fig_returns = create_returns_chart(performance_data)
            st.plotly_chart(fig_returns, use_container_width=True)
        
        with col2:
            st.markdown("#### Ключевые показатели")
            
            metrics = {
                "Общая доходность": f"{(performance_data['Value'].iloc[-1] / performance_data['Value'].iloc[0] - 1) * 100:.1f}%",
                "Средняя месячная доходность": f"{performance_data['Return'].mean() * 100:.2f}%",
                "Волатильность": f"{performance_data['Return'].std() * 100:.2f}%",
                "Лучший месяц": f"{performance_data['Return'].max() * 100:.1f}%",
                "Худший месяц": f"{performance_data['Return'].min() * 100:.1f}%"
            }
            
            for metric, value in metrics.items():
                st.metric(metric, value)
    
    with tab2:
        st.markdown("#### Анализ рисков")
        
        risk_metrics = {
            "Максимальная просадка": "-15.2%",
            "Value at Risk (95%)": "-8.5%",
            "Бета-коэффициент": "1.2",
            "Коэффициент Шарпа": "0.8"
        }
        
        for i, (metric, value) in enumerate(risk_metrics.items()):
            col = st.columns(4)[i % 4]
            with col:
                st.metric(metric, value)
    
    with tab3:
        st.markdown("#### Персональные рекомендации")
        
        recommendations = [
            "🎯 **Ребалансировка**: Рекомендуется скорректировать долю технологических активов",
            "📈 **Диверсификация**: Добавьте exposure к сырьевым товарам",
            "🛡️ **Защита**: Рассмотрите хеджирование через опционы",
            "💰 **Дивиденды**: Увеличьте долю дивидендных аристократов"
        ]
        
        for rec in recommendations:
            st.info(rec)

def analytics_page():
    """Страница расширенной аналитики"""
    st.markdown("""
    <div class="main-header">
        <h2 style="color: white; margin: 0;">📈 Расширенная аналитика</h2>
        <p style="color: white; opacity: 0.9; margin: 0.5rem 0 0 0;">Глубокий анализ и AI инсайты</p>
    </div>
    """, unsafe_allow_html=True)
    
    current_user = st.session_state.current_user
    
    # Проверка доступа
    subscription_level = get_subscription_level(current_user)
    if subscription_level == 'basic':
        st.warning("""
        🔒 **Расширенная аналитика доступна на тарифах Продвинутый и Премиум**
        
        Обновите подписку для доступа к:
        - AI-прогнозам и инсайтам
        - Глубокому анализу рисков
        - Сравнению с эталонами
        - Премиум рекомендациям
        """)
        
        if st.button("💎 Посмотреть тарифы", use_container_width=True):
            st.session_state.current_page = "pricing"
            st.rerun()
        return
    
    st.success(f"🎉 У вас есть доступ к расширенной аналитике! (Тариф: {subscription_level.title()})")
    
    # Расширенная аналитика
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("#### 🤖 AI Инсайты")
        
        insights = [
            "📊 **Паттерны**: Обнаружена сезонность в технологическом секторе",
            "⚡ **Волатильность**: Ожидается снижение волатильности на 12% в следующем квартале",
            "🎯 **Оптимизация**: Ребалансировка может увеличить Sharpe ratio на 0.15",
            "🌍 **Корреляции**: Высокая корреляция с NASDAQ (0.85)"
        ]
        
        for insight in insights:
            st.markdown(f"""
            <div class="metric-card" style="margin-bottom: 1rem;">
                {insight}
            </div>
            """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("#### 📊 Сравнение с рынком")
        
        benchmarks = {
            "Ваш портфель": "+18.5%",
            "S&P 500": "+12.1%", 
            "NASDAQ": "+18.3%",
            "RTS Index": "+8.5%"
        }
        
        fig = go.Figure()
        
        colors = ['#667eea', '#764ba2', '#f093fb', '#f5576c']
        
        for i, (benchmark, return_) in enumerate(benchmarks.items()):
            fig.add_trace(go.Bar(
                name=benchmark,
                x=[return_],
                y=[benchmark],
                orientation='h',
                marker_color=colors[i],
                text=return_,
                textposition='auto'
            ))
        
        fig.update_layout(
            title="Доходность vs Эталоны",
            showlegend=False,
            height=300
        )
        
        st.plotly_chart(fig, use_container_width=True)

def pricing_page():
    """Страница с тарифами"""
    st.markdown("""
    <div class="main-header">
        <h2 style="color: white; margin: 0;">💎 Выберите свой тариф</h2>
        <p style="color: white; opacity: 0.9; margin: 0.5rem 0 0 0;">Инвестируйте в свое финансовое будущее</p>
    </div>
    """, unsafe_allow_html=True)
    
    current_user = st.session_state.current_user
    current_subscription = get_subscription_level(current_user)
    
    # Тарифные планы
    plans = {
        'basic': {
            'name': 'Базовый',
            'price': 0,
            'features': [
                'Базовые метрики портфеля',
                'Визуализация распределения', 
                'Историческая производительность',
                'Основные рекомендации',
                'Ограниченная аналитика'
            ],
            'color': '#11998e'
        },
        'advanced': {
            'name': 'Продвинутый', 
            'price': 450,
            'features': [
                'Все функции Базового',
                'Расширенная аналитика рисков',
                'Сравнение с эталонами',
                'AI инсайты',
                'Детальные отчеты'
            ],
            'color': '#3f5efb'
        },
        'premium': {
            'name': 'Премиум',
            'price': 800, 
            'features': [
                'Все функции Продвинутого',
                'Персональный AI советник',
                'Прогнозы и симуляции',
                'Премиум рекомендации',
                'Приоритетная поддержка'
            ],
            'color': '#ff8c00'
        }
    }
    
    col1, col2, col3 = st.columns(3)
    
    for i, (plan_id, plan) in enumerate(plans.items()):
        with [col1, col2, col3][i]:
            is_current = plan_id == current_subscription
            is_recommended = plan_id == 'advanced'
            
            st.markdown(f"""
            <div style="border: 2px solid {plan['color']}; border-radius: 20px; padding: 2rem; text-align: center; background: white; {'box-shadow: 0 10px 30px rgba(0,0,0,0.2); transform: scale(1.05);' if is_recommended else ''}">
                <h3 style="color: {plan['color']}; margin-bottom: 0.5rem;">{plan['name']}</h3>
                {'<div style="background: #ffd700; color: black; padding: 5px 15px; border-radius: 15px; margin-bottom: 1rem; font-weight: bold;">🚀 РЕКОМЕНДУЕМ</div>' if is_recommended else ''}
                {'<div style="background: #2ed573; color: white; padding: 5px 15px; border-radius: 15px; margin-bottom: 1rem; font-weight: bold;">✅ ВАШ ТАРИФ</div>' if is_current else ''}
                <h2 style="color: {plan['color']}; margin: 1rem 0;">{plan['price']}₽/мес</h2>
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown("<div style='margin: 1rem 0;'>", unsafe_allow_html=True)
            for feature in plan['features']:
                st.markdown(f"✅ {feature}")
            st.markdown("</div>", unsafe_allow_html=True)
            
            if is_current:
                st.button("✅ Текущий тариф", disabled=True, use_container_width=True)
            else:
                button_type = "primary" if is_recommended else "secondary"
                st.button(f"💳 Выбрать {plan['name']}", 
                         use_container_width=True, 
                         type=button_type,
                         key=f"btn_{plan_id}")

# =============================================
# ВСПОМОГАТЕЛЬНЫЕ ФУНКЦИИ
# =============================================

def get_all_clients():
    return ['Иван Петров', 'Мария Сидорова', 'Алексей Козлов', 'Елена Волкова', 'Дмитрий Смирнов']

def get_portfolio_by_client(client_name):
    portfolios = {
        'Иван Петров': {'TSLA': 0.25, 'NVDA': 0.20, 'AMD': 0.15, 'ARKK': 0.15, 'BTC-USD': 0.10, 'ETH-USD': 0.05, 'Cash': 0.10},
        'Мария Сидорова': {'TSLA': 0.30, 'NVDA': 0.25, 'AMD': 0.20, 'ARKK': 0.15, 'Cash': 0.10},
        'Алексей Козлов': {'VTI': 0.25, 'VXUS': 0.15, 'BND': 0.20, 'VNQ': 0.10, 'AAPL': 0.07, 'MSFT': 0.07, 'Cash': 0.06},
        'Елена Волкова': {'VYM': 0.20, 'SCHD': 0.18, 'T': 0.10, 'VZ': 0.09, 'XOM': 0.08, 'JNJ': 0.07, 'Cash': 0.08},
        'Дмитрий Смирнов': {'BND': 0.40, 'GOVT': 0.25, 'SHY': 0.15, 'JNJ': 0.08, 'Cash': 0.12}
    }
    return portfolios.get(client_name, portfolios['Алексей Козлов'])

def get_subscription_level(client_name):
    subscriptions = {
        'Иван Петров': 'premium',
        'Мария Сидорова': 'advanced', 
        'Алексей Козлов': 'basic',
        'Елена Волкова': 'basic',
        'Дмитрий Смирнов': 'basic'
    }
    return subscriptions.get(client_name, 'basic')

def display_subscription_badge(subscription_level: str) -> str:
    """Создает красивый бейдж подписки"""
    badges = {
        'basic': '<span class="subscription-badge badge-basic">БАЗОВЫЙ</span>',
        'advanced': '<span class="subscription-badge badge-advanced">ПРОДВИНУТЫЙ</span>',
        'premium': '<span class="subscription-badge badge-premium">ПРЕМИУМ</span>'
    }
    return badges.get(subscription_level, badges['basic'])

def init_session_state():
    """Инициализация состояния сессии"""
    if 'authenticated' not in st.session_state:
        st.session_state.authenticated = False
    if 'current_user' not in st.session_state:
        st.session_state.current_user = None
    if 'current_page' not in st.session_state:
        st.session_state.current_page = "dashboard"

def sidebar_navigation():
    """Навигация в сайдбаре"""
    st.sidebar.markdown("""
    <div style="text-align: center; margin-bottom: 2rem;">
        <h2>🤖 ЮниВест</h2>
        <p style="opacity: 0.7;">AI Советник</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Выбор клиента
    clients = get_all_clients()
    current_user = st.session_state.current_user
    
    new_user = st.sidebar.selectbox(
        "👤 Текущий клиент:",
        clients,
        index=clients.index(current_user) if current_user in clients else 0
    )
    
    if new_user != current_user:
        st.session_state.current_user = new_user
        st.rerun()
    
    st.sidebar.markdown("---")
    
    # Навигация
    page_options = {
        "📊 Дашборд": "dashboard",
        "📈 Аналитика": "analytics", 
        "💎 Тарифы": "pricing"
    }
    
    selected_page = st.sidebar.radio("Навигация", list(page_options.keys()))
    st.session_state.current_page = page_options[selected_page]
    
    st.sidebar.markdown("---")
    
    # Информация о подписке
    subscription_level = get_subscription_level(current_user)
    st.sidebar.markdown(f"**💎 Ваша подписка:** {subscription_level.title()}")
    
    if subscription_level != 'premium':
        st.sidebar.info("Обновите подписку для доступа ко всем функциям!")
    
    st.sidebar.markdown("---")
    
    # Быстрые действия
    st.sidebar.markdown("### 🚀 Быстрые действия")
    
    if st.sidebar.button("📥 Скачать отчет", use_container_width=True):
        st.sidebar.success("Отчет будет готов через несколько секунд...")
    
    if st.sidebar.button("🔄 Ребалансировка", use_container_width=True):
        st.sidebar.info("Анализируем оптимальное распределение...")

# =============================================
# ГЛАВНАЯ ФУНКЦИЯ
# =============================================

def main():
    """Основная функция приложения"""
    # Инициализация
    setup_page_config()
    inject_modern_css()
    init_session_state()
    
    # Проверка аутентификации
    if not st.session_state.authenticated:
        login_page()
        return
    
    # Основной интерфейс
    sidebar_navigation()
    
    # Отображение текущей страницы
    current_page = st.session_state.current_page
    
    if current_page == "dashboard":
        dashboard_page()
    elif current_page == "analytics":
        analytics_page()
    elif current_page == "pricing":
        pricing_page()

if __name__ == "__main__":
    main()













