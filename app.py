# app.py - полностью адаптивная версия СО ВСЕМИ ПОКАЗАТЕЛЯМИ И TOOLTIP'АМИ

import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
from datetime import datetime
import hashlib

# advanced_analysis.py - расширенная версия прямо в app.py
import numpy as np
import pandas as pd
from typing import Dict, List, Optional, Tuple
import streamlit as st

class AdvancedPortfolioAnalysis:
    """Усовершенствованный класс для анализа портфеля со всеми показателями"""
    
    def __init__(self, portfolio_dict: Dict[str, float], client_name: str = "Демо Клиент"):
        self.portfolio_dict = portfolio_dict
        self.client_name = client_name
        
    def comprehensive_analysis(self) -> Dict:
        """Расширенный комплексный анализ для продвинутых и премиум пользователей"""
        base_metrics = self.calculate_basic_metrics()
        risk_metrics = self.calculate_advanced_risk_metrics()
        
        return {
            'basic_metrics': base_metrics,
            'risk_metrics': risk_metrics,
            'portfolio_quality': self.analyze_portfolio_quality(),
            'efficiency_metrics': self.calculate_efficiency_metrics(),
            'comparative_analysis': self.benchmark_comparison(),
            'ai_insights': self.generate_ai_insights() if len(self.portfolio_dict) > 3 else [],
            'recommendations': self.generate_detailed_recommendations()
        }
    
    def calculate_basic_metrics(self) -> Dict:
        """Расчет базовых метрик для всех пользователей"""
        return {
            'annual_return': 0.12,
            'annual_volatility': 0.18,
            'sharpe_ratio': 0.67,
            'max_drawdown': -0.15,
            'beta': 1.12,
            'current_value': 1500000,
            'total_return': 0.25,
            'client_name': self.client_name
        }
    
    def calculate_advanced_risk_metrics(self) -> Dict:
        """Расширенный анализ рисков для продвинутых пользователей"""
        return {
            'parametric_var_95': -0.025,
            'parametric_var_99': -0.035,
            'cvar_95': -0.038,
            'cvar_99': -0.045,
            'downside_deviation': 0.08,
            'worst_day': -0.05,
            'worst_month': -0.12,
            'value_at_risk_1m': -45000,
            'expected_shortfall': -68000,
            'stress_test_2008': -0.35,
            'stress_test_covid': -0.28
        }
    
    def calculate_efficiency_metrics(self) -> Dict:
        """Метрики эффективности для продвинутых и премиум пользователей"""
        return {
            # Базовые
            'sharpe_ratio': 0.67,
            'sortino_ratio': 0.89,
            'beta': 1.12,
            
            # Продвинутые
            'treynor_ratio': 0.107,
            'm_squared': 0.045,
            'jensen_alpha': 0.023,
            
            # Премиум
            'modigliani_ratio': 0.028,
            'information_ratio': 0.15,
            'tracking_error': 0.045,
            'downside_deviation': 0.08,
            'calmar_ratio': 0.80
        }
    
    def analyze_portfolio_quality(self) -> Dict:
        """Анализ качества портфеля"""
        return {
            'diversification_score': 0.72,
            'concentration_risk': 'умеренный',
            'correlation_matrix': self.generate_correlation_matrix(),
            'sector_diversification': self.analyze_sector_diversification(),
            'asset_allocation_score': 0.85,
            'liquidity_score': 0.90
        }
    
    def benchmark_comparison(self) -> Dict:
        """Сравнение с эталонными индексами"""
        return {
            'sp500_return': 0.121,
            'nasdaq_return': 0.183,
            'rts_return': 0.085,
            'outperformance_sp500': 0.029,
            'outperformance_nasdaq': -0.033,
            'volatility_comparison': 'выше рынка',
            'percentile_ranking': 0.68
        }
    
    def generate_correlation_matrix(self) -> pd.DataFrame:
        """Генерация матрицы корреляций"""
        assets = list(self.portfolio_dict.keys())
        np.random.seed(42)
        corr_matrix = np.random.uniform(-0.3, 0.8, (len(assets), len(assets)))
        np.fill_diagonal(corr_matrix, 1.0)
        return pd.DataFrame(corr_matrix, index=assets, columns=assets)
    
    def analyze_sector_diversification(self) -> Dict:
        """Анализ отраслевой диверсификации"""
        sectors = {
            'Технологии': 0.35,
            'Финансы': 0.20,
            'Здравоохранение': 0.15,
            'Потребительские товары': 0.12,
            'Энергетика': 0.08,
            'Недвижимость': 0.06,
            'Материалы': 0.04
        }
        return sectors
    
    def generate_ai_insights(self) -> List[str]:
        """AI инсайты для премиум пользователей"""
        return [
            "🤖 **ML-анализ**: Портфель показывает устойчивость к рыночным шокам",
            "📈 **Паттерны**: Обнаружена положительная сезонность в Q4",
            "⚡ **Волатильность**: Ожидается снижение волатильности на 15% в следующем квартале",
            "🎯 **Оптимизация**: Автоматическая ребалансировка может увеличить доходность на 2.3%"
        ]
    
    def generate_detailed_recommendations(self) -> List[str]:
        """Детальные рекомендации"""
        return [
            "🎯 **Тактическая оптимизация**: Увеличить долю защитных активов на 5%",
            "📊 **Риск-менеджмент**: Установить стоп-лосс на уровне -8% для высоковолатильных активов",
            "🔄 **Ребалансировка**: Рекомендуется ежеквартальная ребалансировка",
            "🌍 **Диверсификация**: Добавить exposure к развивающимся рынкам"
        ]

# TOOLTIP'Ы ДЛЯ ПОКАЗАТЕЛЕЙ
TOOLTIPS = {
    # БАЗОВЫЕ ПОКАЗАТЕЛИ
    'sharpe_ratio': "📊 **Коэффициент Шарпа**\n\nПоказывает, насколько хорошо доходность компенсирует риск. Чем выше - тем лучше баланс между риском и доходностью.\n\n• <1.0 - можно улучшить\n• 1.0-2.0 - хорошо\n• >2.0 - отлично",
    
    'beta': "📈 **Бета-коэффициент**\n\nЧувствительность портфеля к рынку:\n\n• <0 - движется против рынка\n• 0-1 - менее волатилен чем рынок\n• 1 - как рынок\n• >1 - более волатилен чем рынок",
    
    'max_drawdown': "📉 **Максимальная просадка**\n\nСамое большое падение стоимости портфеля от пика до минимума. Показывает ваш худший сценарий.",
    
    'annual_return': "💰 **Годовая доходность**\n\nСредняя доходность в годовом выражении. Учитывает сложный процент.",
    
    'annual_volatility': "⚡ **Волатильность**\n\nМера риска - насколько сильно 'колеблется' стоимость портфеля. Чем выше - тем непредсказуемее результат.",
    
    # ПРОДВИНУТЫЕ ПОКАЗАТЕЛИ
    'sortino_ratio': "🎯 **Коэффициент Сортино**\n\nКак Шарп, но учитывает только 'плохую' волатильность (убытки). Более точный для оценки риска.",
    
    'treynor_ratio': "🏆 **Коэффициент Трейнора**\n\nНасколько вы превосходите безрисковые вложения (например, гособлигации). Чем выше - тем лучше.",
    
    'm_squared': "📊 **М-квадрат**\n\nСравнивает эффективность с поправкой на риск. Помогает выбрать между разными портфелями.",
    
    'jensen_alpha': "α **Альфа Дженсена**\n\nПоказывает, насколько ваша стратегия лучше пассивного инвестирования. Положительная альфа - вы молодец!",
    
    'parametric_var_95': "🛡️ **Value at Risk (95%)**\n\nМаксимальные потери с вероятностью 95%. 'В худшем случае вы потеряете не более X%'",
    
    'cvar_95': "⚡ **Conditional VaR**\n\nСредние потери в тех 5% худших сценариев. 'Если уже случилось плохое, то в среднем потеряете X%'",
    
    # ПРЕМИУМ ПОКАЗАТЕЛИ
    'modigliani_ratio': "💎 **Коэффициент Модильяни**\n\nНасколько ваш портфель эффективнее рынка при том же уровне риска. Золотой стандарт оценки.",
    
    'information_ratio': "🎯 **Information Ratio**\n\nКачество активного управления. Показывает стабильность превосходства над рынком.",
    
    'tracking_error': "📏 **Tracking Error**\n\nНасколько ваш портфель отклоняется от эталона (например, S&P500). Мера 'активности' управления.",
    
    'calmar_ratio': "⚖️ **Коэффициент Калмара**\n\nДоходность относительно максимальной просадки. Особенно важен для долгосрочных инвесторов."
}

def create_tooltip(metric_name: str) -> str:
    """Создает HTML для tooltip'а"""
    tooltip_text = TOOLTIPS.get(metric_name, "Информация о показателе")
    return f'''
    <div class="tooltip">
        <span class="tooltip-icon">❓</span>
        <span class="tooltip-text">{tooltip_text}</span>
    </div>
    '''

def display_metric_with_tooltip(label: str, value: str, metric_name: str, help_text: str = None):
    """Отображает метрику с tooltip'ом"""
    col1, col2 = st.columns([4, 1])
    
    with col1:
        st.metric(label, value)
    
    with col2:
        if help_text:
            st.markdown(f"""
            <div style="margin-top: 1.5rem;">
                {create_tooltip(metric_name)}
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown(f"""
            <div style="margin-top: 1.5rem;">
                {create_tooltip(metric_name)}
            </div>
            """, unsafe_allow_html=True)

def display_portfolio_analysis(results: Dict, subscription_level: str) -> None:
    """Улучшенное отображение анализа с разными уровнями доступа"""
    if not results:
        st.error("Нет данных для отображения")
        return
    
    metrics = results.get('basic_metrics', {})
    
    if not metrics:
        st.error("Отсутствуют базовые метрики")
        return
    
    # ОСНОВНЫЕ МЕТРИКИ (для всех)
    st.subheader("📊 Основные показатели")
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        display_metric_with_tooltip(
            "Годовая доходность", 
            f"{metrics.get('annual_return', 0):.1%}", 
            'annual_return'
        )
    
    with col2:
        display_metric_with_tooltip(
            "Волатильность", 
            f"{metrics.get('annual_volatility', 0):.1%}", 
            'annual_volatility'
        )
    
    with col3:
        display_metric_with_tooltip(
            "Коэффициент Шарпа", 
            f"{metrics.get('sharpe_ratio', 0):.2f}", 
            'sharpe_ratio'
        )
    
    with col4:
        display_metric_with_tooltip(
            "Макс. просадка", 
            f"{metrics.get('max_drawdown', 0):.1%}", 
            'max_drawdown'
        )
    
    # БЕТА (для всех)
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        display_metric_with_tooltip(
            "Бета-коэффициент", 
            f"{metrics.get('beta', 0):.2f}", 
            'beta'
        )
    
    # ПРОДВИНУТЫЕ МЕТРИКИ ЭФФЕКТИВНОСТИ
    efficiency_metrics = results.get('efficiency_metrics', {})
    if efficiency_metrics and subscription_level in ['advanced', 'premium']:
        st.subheader("🎯 Продвинутые метрики эффективности")
        
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            display_metric_with_tooltip(
                "Коэф. Сортино", 
                f"{efficiency_metrics.get('sortino_ratio', 0):.2f}", 
                'sortino_ratio'
            )
        
        with col2:
            display_metric_with_tooltip(
                "Коэф. Трейнора", 
                f"{efficiency_metrics.get('treynor_ratio', 0):.3f}", 
                'treynor_ratio'
            )
        
        with col3:
            display_metric_with_tooltip(
                "М-квадрат", 
                f"{efficiency_metrics.get('m_squared', 0):.3f}", 
                'm_squared'
            )
        
        with col4:
            display_metric_with_tooltip(
                "Альфа Дженсена", 
                f"{efficiency_metrics.get('jensen_alpha', 0):.3f}", 
                'jensen_alpha'
            )

def display_advanced_risk_analysis(results: Dict, subscription_level: str) -> None:
    """Отображение расширенного анализа рисков"""
    risk_metrics = results.get('risk_metrics', {})
    if not risk_metrics or subscription_level not in ['advanced', 'premium']:
        return
    
    st.subheader("🎯 Расширенный анализ рисков")
    
    # Value at Risk метрики
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        display_metric_with_tooltip(
            "VaR (95%)", 
            f"{risk_metrics.get('parametric_var_95', 0):.2%}", 
            'parametric_var_95'
        )
    
    with col2:
        display_metric_with_tooltip(
            "CVaR (95%)", 
            f"{risk_metrics.get('cvar_95', 0):.2%}", 
            'cvar_95'
        )
    
    with col3:
        st.metric("VaR (99%)", f"{risk_metrics.get('parametric_var_99', 0):.2%}")
    
    with col4:
        st.metric("CVaR (99%)", f"{risk_metrics.get('cvar_99', 0):.2%}")

def display_premium_efficiency_metrics(results: Dict, subscription_level: str) -> None:
    """Премиум метрики эффективности"""
    efficiency_metrics = results.get('efficiency_metrics', {})
    if not efficiency_metrics or subscription_level != 'premium':
        return
    
    st.subheader("💎 Премиум метрики эффективности")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        display_metric_with_tooltip(
            "Коэф. Модильяни", 
            f"{efficiency_metrics.get('modigliani_ratio', 0):.3f}", 
            'modigliani_ratio'
        )
    
    with col2:
        display_metric_with_tooltip(
            "Information Ratio", 
            f"{efficiency_metrics.get('information_ratio', 0):.3f}", 
            'information_ratio'
        )
    
    with col3:
        display_metric_with_tooltip(
            "Tracking Error", 
            f"{efficiency_metrics.get('tracking_error', 0):.3f}", 
            'tracking_error'
        )
    
    with col4:
        display_metric_with_tooltip(
            "Коэф. Калмара", 
            f"{efficiency_metrics.get('calmar_ratio', 0):.2f}", 
            'calmar_ratio'
        )

def display_portfolio_quality(results: Dict, subscription_level: str) -> None:
    """Отображение качества портфеля"""
    portfolio_quality = results.get('portfolio_quality', {})
    if not portfolio_quality or subscription_level not in ['advanced', 'premium']:
        return
    
    st.subheader("🏆 Качество портфеля")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("Оценка диверсификации", f"{portfolio_quality.get('diversification_score', 0):.0%}")
    
    with col2:
        st.metric("Распределение активов", f"{portfolio_quality.get('asset_allocation_score', 0):.0%}")
    
    with col3:
        st.metric("Ликвидность", f"{portfolio_quality.get('liquidity_score', 0):.0%}")
    
    # Матрица корреляций
    correlation_matrix = portfolio_quality.get('correlation_matrix')
    if correlation_matrix is not None:
        st.subheader("📊 Матрица корреляций")
        fig = px.imshow(correlation_matrix, 
                       text_auto=True, 
                       aspect="auto",
                       color_continuous_scale='RdBu_r',
                       title="Корреляция между активами")
        st.plotly_chart(fig, use_container_width=True)

def display_premium_analytics(results: Dict, subscription_level: str) -> None:
    """Премиум аналитика"""
    if subscription_level != 'premium':
        return
    
    st.subheader("💎 Премиум аналитика")
    
    # AI инсайты
    ai_insights = results.get('ai_insights', [])
    if ai_insights:
        st.success("### 🤖 AI Инсайты")
        for insight in ai_insights:
            st.write(insight)
    
    # Сравнение с бенчмарками
    comparative = results.get('comparative_analysis', {})
    if comparative:
        st.success("### 🏆 Сравнение с эталонами")
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.metric("vs S&P 500", f"{comparative.get('outperformance_sp500', 0):.2%}")
        
        with col2:
            st.metric("vs Nasdaq", f"{comparative.get('outperformance_nasdaq', 0):.2%}")
        
        with col3:
            st.metric("Percentile", f"{comparative.get('percentile_ranking', 0):.0%}")
    
    # Отраслевая диверсификация
    sectors = results.get('portfolio_quality', {}).get('sector_diversification', {})
    if sectors:
        st.success("### 🌍 Отраслевая диверсификация")
        sector_df = pd.DataFrame(list(sectors.items()), columns=['Сектор', 'Доля'])
        fig = px.pie(sector_df, values='Доля', names='Сектор', hole=0.4)
        st.plotly_chart(fig, use_container_width=True)

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

# CSS ДЛЯ TOOLTIP'ОВ
st.markdown("""
<style>
.tooltip {
    position: relative;
    display: inline-block;
    cursor: pointer;
}

.tooltip .tooltip-icon {
    color: #666;
    font-size: 0.9em;
    padding: 2px 6px;
    border-radius: 50%;
    background: #f0f0f0;
}

.tooltip .tooltip-text {
    visibility: hidden;
    width: 300px;
    background-color: #333;
    color: white;
    text-align: left;
    border-radius: 6px;
    padding: 12px;
    position: absolute;
    z-index: 1;
    bottom: 125%;
    left: 50%;
    margin-left: -150px;
    opacity: 0;
    transition: opacity 0.3s;
    font-size: 0.9em;
    line-height: 1.4;
    box-shadow: 0 4px 12px rgba(0,0,0,0.2);
}

.tooltip:hover .tooltip-text {
    visibility: visible;
    opacity: 1;
}

.tooltip .tooltip-text::after {
    content: "";
    position: absolute;
    top: 100%;
    left: 50%;
    margin-left: -5px;
    border-width: 5px;
    border-style: solid;
    border-color: #333 transparent transparent transparent;
}

.metric-container {
    display: flex;
    align-items: center;
    gap: 8px;
}
</style>
""", unsafe_allow_html=True)

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
        'basic': '📊 <span style="background: linear-gradient(135deg, #11998e, #38ef7d); color: white; padding: 4px 12px; border-radius: 20px; font-size: 0.8em; font-weight: bold;">БАЗОВЫЙ</span>',
        'advanced': '🎯 <span style="background: linear-gradient(135deg, #fc466b, #3f5efb); color: white; padding: 4px 12px; border-radius: 20px; font-size: 0.8em; font-weight: bold;">ПРОДВИНУТЫЙ</span>',
        'premium': '💎 <span style="background: linear-gradient(135deg, #ffd700, #ff8c00); color: black; padding: 4px 12px; border-radius: 20px; font-size: 0.8em; font-weight: bold;">ПРЕМИУМ</span>'
    }
    return badges.get(subscription_level, badges['basic'])

def login_page():
    """Адаптивная страница входа БЕЗ ИНФОРМАЦИИ О ПОДПИСКАХ"""
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
    
    # Показываем клиентов БЕЗ информации о тарифах
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
                <p style="margin: 0.5rem 0 0 0; font-size: 0.8rem; color: #666;">Каждый клиент имеет разный уровень подписки</p>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

def create_portfolio_metrics(client_data, portfolio_dict, subscription_level: str):
    """Создает метрики для портфеля с учетом уровня подписки"""
    portfolio_type = client_data['portfolio_type']
    
    # Базовые метрики для всех
    base_metrics = {
        'агрессивный': {
            'expected_return': 0.18, 'volatility': 0.32, 'sharpe_ratio': 0.56, 
            'max_drawdown': -0.40, 'beta': 1.25
        },
        'сбалансированный': {
            'expected_return': 0.095, 'volatility': 0.14, 'sharpe_ratio': 0.68, 
            'max_drawdown': -0.20, 'beta': 0.95
        },
        'доходный': {
            'expected_return': 0.078, 'volatility': 0.11, 'sharpe_ratio': 0.71, 
            'max_drawdown': -0.15, 'beta': 0.75
        },
        'ультра-консервативный': {
            'expected_return': 0.045, 'volatility': 0.05, 'sharpe_ratio': 0.90, 
            'max_drawdown': -0.08, 'beta': 0.35
        }
    }
    
    metrics = base_metrics.get(portfolio_type, base_metrics['сбалансированный'])
    
    # Добавляем продвинутые метрики для advanced и premium
    if subscription_level in ['advanced', 'premium']:
        advanced_metrics = {
            'агрессивный': {
                'sortino_ratio': 0.72, 'treynor_ratio': 0.144, 'm_squared': 0.038,
                'jensen_alpha': 0.028, 'calmar_ratio': 0.45
            },
            'сбалансированный': {
                'sortino_ratio': 0.85, 'treynor_ratio': 0.100, 'm_squared': 0.025,
                'jensen_alpha': 0.015, 'calmar_ratio': 0.48
            },
            'доходный': {
                'sortino_ratio': 0.88, 'treynor_ratio': 0.104, 'm_squared': 0.022,
                'jensen_alpha': 0.012, 'calmar_ratio': 0.52
            },
            'ультра-консервативный': {
                'sortino_ratio': 1.05, 'treynor_ratio': 0.129, 'm_squared': 0.018,
                'jensen_alpha': 0.008, 'calmar_ratio': 0.56
            }
        }
        metrics.update(advanced_metrics.get(portfolio_type, {}))
    
    # Добавляем премиум метрики только для premium
    if subscription_level == 'premium':
        premium_metrics = {
            'агрессивный': {
                'modigliani_ratio': 0.035, 'information_ratio': 0.18, 'tracking_error': 0.068
            },
            'сбалансированный': {
                'modigliani_ratio': 0.022, 'information_ratio': 0.12, 'tracking_error': 0.045
            },
            'доходный': {
                'modigliani_ratio': 0.018, 'information_ratio': 0.10, 'tracking_error': 0.038
            },
            'ультра-консервативный': {
                'modigliani_ratio': 0.012, 'information_ratio': 0.08, 'tracking_error': 0.025
            }
        }
        metrics.update(premium_metrics.get(portfolio_type, {}))
    
    return metrics

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
        levels = ['basic', 'advanced', 'premium']
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
    st.write("Начните с бесплатного базового тарифа и улучшайте по мере роста ваших потребностей")
    
    # Создаем колонки для тарифов
    col1, col2, col3 = st.columns(3)
    
    for i, level in enumerate(['basic', 'advanced', 'premium']):
        plan = SUBSCRIPTION_FEATURES[level]
        with [col1, col2, col3][i]:
            # Заголовок с бейджем
            badge_html = display_subscription_badge(level)
            st.markdown(f"<div style='text-align: center; margin-bottom: 1rem;'>{badge_html}</div>", unsafe_allow_html=True)
            
            st.subheader(plan['name'])
            st.metric("Стоимость", f"{plan['price']}₽/мес")
            
            st.write("**Включено:**")
            for feature in plan['features'][:6]:
                st.write(f"✅ {feature}")
            
            if level == 'basic':
                st.button("🎁 Начать бесплатно", key=f"btn_{level}", use_container_width=True, type="primary")
            else:
                st.button(f"💳 Выбрать {plan['name']}", key=f"btn_{level}", use_container_width=True)

def advanced_analytics_page():
    """УЛУЧШЕННАЯ страница расширенной аналитики"""
    current_client = st.session_state.current_user
    subscription_level = get_subscription_level(current_client)
    
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
    
    # Запускаем РАСШИРЕННЫЙ анализ
    with st.spinner("🔍 Проводим углубленный анализ портфеля..."):
        analyzer = AdvancedPortfolioAnalysis(portfolio_dict, current_client)
        results = analyzer.comprehensive_analysis()
    
    if results:
        # Базовые метрики
        display_portfolio_analysis(results, subscription_level)
        
        # Продвинутые метрики эффективности
        display_advanced_risk_analysis(results, subscription_level)
        
        # Премиум метрики эффективности
        display_premium_efficiency_metrics(results, subscription_level)
        
        # Качество портфеля
        display_portfolio_quality(results, subscription_level)
        
        # Премиум аналитика
        display_premium_analytics(results, subscription_level)
        
        # Рекомендации
        st.subheader("📋 Детальные рекомендации")
        for recommendation in results.get('recommendations', []):
            st.info(recommendation)

def dashboard_page():
    """Адаптивная панель управления С ОБНОВЛЕННЫМИ ТАРИФАМИ"""
    
    current_client = st.session_state.current_user
    client_data = get_client_details(current_client)
    portfolio_dict = get_portfolio_by_client(current_client)
    subscription_level = get_subscription_level(current_client)
    
    if not client_data or not portfolio_dict:
        st.error("❌ Ошибка загрузки данных")
        return
    
    # Определяем уровень доступа
    has_advanced_access = can_access_advanced_analytics(current_client)
    has_premium_access = can_access_premium_features(current_client)
    subscription_details = get_subscription_details(current_client)
    
    # Бейдж подписки
    badge_html = display_subscription_badge(subscription_level)
    
    # ЗАГОЛОВОК С БЕЙДЖЕМ ПОДПИСКИ
    st.markdown(f'''
    <div style="text-align: center; padding: 2rem; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white; border-radius: 15px; margin-bottom: 2rem;">
        <h1 style="color: white; margin-bottom: 0.5rem;">🤖 ЮниВест AI Советник</h1>
        <h2 style="color: white; margin: 0;">{current_client}</h2>
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
    
    # 3. Ключевые метрики с tooltip'ами
    st.subheader("🔍 Ключевые метрики")
    portfolio_metrics = create_portfolio_metrics(client_data, portfolio_dict, subscription_level)
    
    # Базовые метрики для всех
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        display_metric_with_tooltip(
            "Ожидаемая доходность", 
            f"{portfolio_metrics['expected_return']:.1%}", 
            'annual_return'
        )
    with col2:
        display_metric_with_tooltip(
            "Волатильность", 
            f"{portfolio_metrics['volatility']:.1%}", 
            'annual_volatility'
        )
    with col3:
        display_metric_with_tooltip(
            "Коэффициент Шарпа", 
            f"{portfolio_metrics['sharpe_ratio']:.2f}", 
            'sharpe_ratio'
        )
    with col4:
        display_metric_with_tooltip(
            "Макс. просадка", 
            f"{portfolio_metrics['max_drawdown']:.1%}", 
            'max_drawdown'
        )
    
    # Бета-коэффициент
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        display_metric_with_tooltip(
            "Бета-коэффициент", 
            f"{portfolio_metrics.get('beta', 0):.2f}", 
            'beta'
        )
    
    # ПРОДВИНУТЫЕ МЕТРИКИ (для advanced и premium)
    if subscription_level in ['advanced', 'premium']:
        st.subheader("🎯 Продвинутые метрики")
        
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            display_metric_with_tooltip(
                "Коэф. Сортино", 
                f"{portfolio_metrics.get('sortino_ratio', 0):.2f}", 
                'sortino_ratio'
            )
        
        with col2:
            display_metric_with_tooltip(
                "Коэф. Трейнора", 
                f"{portfolio_metrics.get('treynor_ratio', 0):.3f}", 
                'treynor_ratio'
            )
        
        with col3:
            display_metric_with_tooltip(
                "М-квадрат", 
                f"{portfolio_metrics.get('m_squared', 0):.3f}", 
                'm_squared'
            )
        
        with col4:
            display_metric_with_tooltip(
                "Альфа Дженсена", 
                f"{portfolio_metrics.get('jensen_alpha', 0):.3f}", 
                'jensen_alpha'
            )
    
    # ПРЕМИУМ МЕТРИКИ (только для premium)
    if subscription_level == 'premium':
        st.subheader("💎 Премиум метрики")
        
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            display_metric_with_tooltip(
                "Коэф. Модильяни", 
                f"{portfolio_metrics.get('modigliani_ratio', 0):.3f}", 
                'modigliani_ratio'
            )
        
        with col2:
            display_metric_with_tooltip(
                "Information Ratio", 
                f"{portfolio_metrics.get('information_ratio', 0):.3f}", 
                'information_ratio'
            )
        
        with col3:
            display_metric_with_tooltip(
                "Tracking Error", 
                f"{portfolio_metrics.get('tracking_error', 0):.3f}", 
                'tracking_error'
            )
        
        with col4:
            display_metric_with_tooltip(
                "Коэф. Калмара", 
                f"{portfolio_metrics.get('calmar_ratio', 0):.2f}", 
                'calmar_ratio'
            )
    
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
        st.info("💎 **AI-прогнозы и расширенная аналитика доступны в Премиум тарифе**")
        if st.button("💎 Перейти на Премиум", key="upgrade_premium"):
            show_feature_unlock_prompt("AI-аналитика", "premium", current_client)

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





