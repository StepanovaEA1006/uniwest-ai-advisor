# app.py - полностью адаптивная версия С ИСПРАВЛЕННЫМИ ГРАФИКАМИ

import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
from datetime import datetime, timedelta
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
            'recommendations': self.generate_detailed_recommendations(),
            'performance_charts': self.generate_performance_charts()
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
        if len(assets) == 0:
            return pd.DataFrame()
        
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
    
    def generate_performance_charts(self) -> Dict:
        """Генерация данных для графиков производительности"""
        historical_data = self.generate_historical_data()
        
        if historical_data.empty:
            return {}
        
        # Расчет скользящих средних
        historical_data['MA_6'] = historical_data['Portfolio_Value'].rolling(window=6, min_periods=1).mean()
        historical_data['MA_12'] = historical_data['Portfolio_Value'].rolling(window=12, min_periods=1).mean()
        
        # Расчет просадок
        historical_data['Peak'] = historical_data['Portfolio_Value'].expanding().max()
        historical_data['Drawdown'] = (historical_data['Portfolio_Value'] - historical_data['Peak']) / historical_data['Peak'] * 100
        
        return {
            'historical_data': historical_data,
            'annual_returns': self.calculate_annual_returns(historical_data),
            'volatility_data': self.calculate_rolling_volatility(historical_data)
        }
    
    def generate_historical_data(self) -> pd.DataFrame:
        """Генерация исторических данных за 10 лет"""
        try:
            dates = pd.date_range(start='2014-01-01', end='2024-01-01', freq='M')
            np.random.seed(sum(ord(c) for c in self.client_name))
            
            # Базовые параметры
            mean_return = 0.008  # 0.8% в месяц
            std_return = 0.035   # 3.5% волатильность
            
            monthly_returns = np.random.normal(mean_return, std_return, len(dates))
            
            # Добавляем реалистичные кризисы
            crisis_periods = [
                ('2015-07-01', '2016-02-01', -0.18),  # Кризис 2015-2016
                ('2018-09-01', '2018-12-01', -0.12),  # Коррекция 2018
                ('2020-02-01', '2020-04-01', -0.25),  # COVID-19
                ('2022-01-01', '2022-10-01', -0.20)   # Геополитический кризис
            ]
            
            for crisis_start, crisis_end, crisis_strength in crisis_periods:
                mask = (dates >= pd.to_datetime(crisis_start)) & (dates <= pd.to_datetime(crisis_end))
                if mask.any():
                    monthly_returns[mask] += np.random.normal(crisis_strength, 0.02, mask.sum())
            
            # Расчет накопленной стоимости
            initial_investment = 1000000  # 1 млн рублей
            portfolio_value = [initial_investment]
            
            for ret in monthly_returns:
                portfolio_value.append(portfolio_value[-1] * (1 + ret))
            
            df = pd.DataFrame({
                'Date': dates,
                'Portfolio_Value': portfolio_value[1:],
                'Monthly_Return': monthly_returns,
                'Cumulative_Return': (np.array(portfolio_value[1:]) / initial_investment - 1) * 100
            })
            
            return df
            
        except Exception as e:
            st.error(f"Ошибка генерации исторических данных: {e}")
            return pd.DataFrame()
    
    def calculate_annual_returns(self, data: pd.DataFrame) -> pd.DataFrame:
        """Расчет годовой доходности"""
        if data.empty:
            return pd.DataFrame(columns=['Year', 'Start_Value', 'End_Value', 'Annual_Return'])
        
        try:
            data = data.copy()
            data['Year'] = data['Date'].dt.year
            
            annual_data = data.groupby('Year').agg({
                'Portfolio_Value': ['first', 'last']
            }).reset_index()
            
            annual_data.columns = ['Year', 'Start_Value', 'End_Value']
            annual_data['Annual_Return'] = (annual_data['End_Value'] / annual_data['Start_Value'] - 1) * 100
            
            return annual_data
            
        except Exception as e:
            st.error(f"Ошибка расчета годовой доходности: {e}")
            return pd.DataFrame(columns=['Year', 'Start_Value', 'End_Value', 'Annual_Return'])
    
    def calculate_rolling_volatility(self, data: pd.DataFrame) -> pd.DataFrame:
        """Расчет скользящей волатильности"""
        if data.empty:
            return pd.DataFrame(columns=['Date', 'Rolling_Volatility_1Y'])
        
        try:
            data = data.copy()
            data['Rolling_Volatility_1Y'] = data['Monthly_Return'].rolling(window=12, min_periods=1).std() * np.sqrt(12) * 100
            return data[['Date', 'Rolling_Volatility_1Y']].dropna()
            
        except Exception as e:
            st.error(f"Ошибка расчета волатильности: {e}")
            return pd.DataFrame(columns=['Date', 'Rolling_Volatility_1Y'])
    
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

# ОБНОВЛЕННЫЕ TOOLTIP'Ы ДЛЯ ПОКАЗАТЕЛЕЙ
TOOLTIPS = {
    'sharpe_ratio': "📊 **Коэффициент Шарпа** - Показывает доходность с поправкой на риск",
    'beta': "📈 **Бета-коэффициент** - Чувствительность портфеля к рынку",
    'max_drawdown': "📉 **Максимальная просадка** - Самое большое падение стоимости",
    'annual_return': "💰 **Годовая доходность** - Прирост капитала за год",
    'annual_volatility': "⚡ **Волатильность** - Размах колебаний стоимости",
    'sortino_ratio': "🎯 **Коэффициент Сортино** - Учитывает только 'плохую' волатильность",
    'treynor_ratio': "🏆 **Коэффициент Трейнора** - Доходность за системный риск",
    'm_squared': "📊 **М-квадрат** - Сравнение с эталоном при равном риске",
    'jensen_alpha': "α **Альфа Дженсена** - Навык управления портфелем",
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

def display_metric_with_tooltip(label: str, value: str, metric_name: str):
    """Отображает метрику с tooltip'ом"""
    col1, col2 = st.columns([4, 1])
    
    with col1:
        st.metric(label, value)
    
    with col2:
        st.markdown(create_tooltip(metric_name), unsafe_allow_html=True)

# ПРОСТЫЕ И НАДЕЖНЫЕ ФУНКЦИИ ДЛЯ ГРАФИКОВ
def create_historical_performance_chart(historical_data: pd.DataFrame, client_name: str):
    """Создает простой и надежный график исторической производительности"""
    try:
        if historical_data.empty:
            return go.Figure()
        
        fig = go.Figure()
        
        # Основная линия портфеля
        fig.add_trace(go.Scatter(
            x=historical_data['Date'],
            y=historical_data['Portfolio_Value'],
            mode='lines',
            name='Стоимость портфеля',
            line=dict(color='#2E86AB', width=3),
            hovertemplate='<b>%{x|%b %Y}</b><br>₽%{y:,.0f}<extra></extra>'
        ))
        
        fig.update_layout(
            title=f'📈 Историческая производительность портфеля {client_name}',
            xaxis_title='Дата',
            yaxis_title='Стоимость портфеля (рубли)',
            hovermode='x unified',
            height=400,
            showlegend=True,
            template='plotly_white'
        )
        
        return fig
        
    except Exception as e:
        st.error(f"Ошибка создания графика: {e}")
        return go.Figure()

def create_returns_chart(historical_data: pd.DataFrame):
    """Создает график месячной доходности"""
    try:
        if historical_data.empty:
            return go.Figure()
        
        colors = ['red' if x < 0 else 'green' for x in historical_data['Monthly_Return'] * 100]
        
        fig = go.Figure()
        
        fig.add_trace(go.Bar(
            x=historical_data['Date'],
            y=historical_data['Monthly_Return'] * 100,
            name='Месячная доходность %',
            marker_color=colors,
            opacity=0.7
        ))
        
        fig.update_layout(
            title='📊 Месячная доходность портфеля',
            xaxis_title='Дата',
            yaxis_title='Доходность (%)',
            height=300,
            showlegend=False,
            template='plotly_white'
        )
        
        return fig
        
    except Exception as e:
        st.error(f"Ошибка создания графика доходности: {e}")
        return go.Figure()

def create_drawdown_chart(historical_data: pd.DataFrame):
    """Создает простой график просадок"""
    try:
        if historical_data.empty:
            return go.Figure()
        
        fig = go.Figure()
        
        fig.add_trace(go.Scatter(
            x=historical_data['Date'],
            y=historical_data['Drawdown'],
            fill='tozeroy',
            mode='lines',
            name='Просадка',
            line=dict(color='red', width=2),
            fillcolor='rgba(255,0,0,0.2)',
            hovertemplate='<b>%{x|%b %Y}</b><br>Просадка: %{y:.1f}%<extra></extra>'
        ))
        
        fig.update_layout(
            title='📉 Исторические просадки портфеля',
            xaxis_title='Дата',
            yaxis_title='Просадка (%)',
            height=300,
            showlegend=False,
            template='plotly_white'
        )
        
        return fig
        
    except Exception as e:
        st.error(f"Ошибка создания графика просадок: {e}")
        return go.Figure()

def create_annual_returns_chart(annual_data: pd.DataFrame):
    """Создает график годовой доходности"""
    try:
        if annual_data.empty:
            return go.Figure()
        
        colors = ['red' if x < 0 else 'green' for x in annual_data['Annual_Return']]
        
        fig = go.Figure()
        
        fig.add_trace(go.Bar(
            x=annual_data['Year'],
            y=annual_data['Annual_Return'],
            name='Годовая доходность',
            marker_color=colors,
            text=annual_data['Annual_Return'].round(1).astype(str) + '%',
            textposition='auto'
        ))
        
        fig.update_layout(
            title='📅 Годовая доходность портфеля',
            xaxis_title='Год',
            yaxis_title='Доходность (%)',
            height=300,
            showlegend=False,
            template='plotly_white'
        )
        
        return fig
        
    except Exception as e:
        st.error(f"Ошибка создания графика годовой доходности: {e}")
        return go.Figure()

def create_performance_summary_cards(historical_data: pd.DataFrame):
    """Создает карточки с ключевыми показателями производительности"""
    try:
        if historical_data.empty:
            st.warning("Нет данных для отображения")
            return
        
        current_value = historical_data['Portfolio_Value'].iloc[-1]
        initial_value = historical_data['Portfolio_Value'].iloc[0]
        total_return = (current_value / initial_value - 1) * 100
        
        # Максимальная просадка
        max_drawdown = historical_data['Drawdown'].min()
        
        # Волатильность
        volatility = historical_data['Monthly_Return'].std() * np.sqrt(12) * 100
        
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.metric(
                "Общая доходность",
                f"{total_return:.1f}%"
            )
        
        with col2:
            st.metric(
                "Текущая стоимость",
                f"₽{current_value:,.0f}"
            )
        
        with col3:
            st.metric(
                "Макс. просадка",
                f"{max_drawdown:.1f}%"
            )
        
        with col4:
            st.metric(
                "Волатильность",
                f"{volatility:.1f}%"
            )
            
    except Exception as e:
        st.error(f"Ошибка создания карточек: {e}")

def display_historical_performance(results: Dict, client_name: str):
    """Отображение исторической производительности портфеля"""
    try:
        if not results.get('performance_charts'):
            st.warning("Исторические данные недоступны")
            return
        
        performance_data = results['performance_charts']
        historical_data = performance_data['historical_data']
        annual_data = performance_data['annual_returns']
        
        if historical_data.empty:
            st.warning("Нет исторических данных для отображения")
            return
        
        st.subheader("📈 Историческая производительность (10 лет)")
        
        # Карточки с ключевыми показателями
        create_performance_summary_cards(historical_data)
        
        # Основной график производительности
        st.plotly_chart(
            create_historical_performance_chart(historical_data, client_name),
            use_container_width=True
        )
        
        # Дополнительные графики в колонках
        col1, col2 = st.columns(2)
        
        with col1:
            st.plotly_chart(
                create_returns_chart(historical_data),
                use_container_width=True
            )
        
        with col2:
            st.plotly_chart(
                create_drawdown_chart(historical_data),
                use_container_width=True
            )
        
        # Годовая доходность
        if not annual_data.empty:
            st.plotly_chart(
                create_annual_returns_chart(annual_data),
                use_container_width=True
            )
            
    except Exception as e:
        st.error(f"Ошибка отображения исторических данных: {e}")

# ОСТАЛЬНЫЕ ФУНКЦИИ ОСТАЮТСЯ БЕЗ ИЗМЕНЕНИЙ
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

def display_advanced_efficiency_metrics(results: Dict, subscription_level: str, client_data: Dict):
    """Отображение продвинутых метрик эффективности"""
    if subscription_level not in ['advanced', 'premium']:
        return
    
    st.subheader("🎯 Продвинутые метрики эффективности")
    
    # Упрощенные метрики для демонстрации
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        display_metric_with_tooltip(
            "Коэф. Сортино", 
            "0.85", 
            'sortino_ratio'
        )
    
    with col2:
        display_metric_with_tooltip(
            "Коэф. Трейнора", 
            "0.107", 
            'treynor_ratio'
        )
    
    with col3:
        display_metric_with_tooltip(
            "М-квадрат", 
            "0.045", 
            'm_squared'
        )
    
    with col4:
        display_metric_with_tooltip(
            "Альфа Дженсена", 
            "0.023", 
            'jensen_alpha'
        )

# ИМПОРТИРУЕМ ФУНКЦИИ ИЗ database.py
try:
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
except ImportError:
    # Заглушки для случая, если database.py не доступен
    def get_all_clients():
        return ['Иван Петров', 'Мария Сидорова', 'Алексей Козлов', 'Елена Волкова', 'Дмитрий Смирнов']
    
    def get_client_details(client_name):
        return {
            'portfolio_type': 'сбалансированный',
            'risk_profile': 'умеренный',
            'investment_horizon': '7-10 лет',
            'experience': 'Продвинутый',
            'financial_goals': 'Образование детей',
            'target_amount': 2500000,
            'initial_investment': 800000
        }
    
    def get_portfolio_by_client(client_name):
        return {'AAPL': 0.25, 'MSFT': 0.20, 'GOOGL': 0.15, 'AMZN': 0.10, 'TSLA': 0.08, 'Cash': 0.22}
    
    def generate_subscription_based_recommendations(client_name):
        return ["Рекомендация 1", "Рекомендация 2"]
    
    def get_subscription_level(client_name):
        return 'basic'
    
    def get_subscription_details(client_name):
        return {'name': 'Базовый', 'price': 0, 'expires': '2024-12-31'}
    
    def can_access_advanced_analytics(client_name):
        return False
    
    def can_access_premium_features(client_name):
        return False
    
    SUBSCRIPTION_FEATURES = {}

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
    background-color: #1a1a1a;
    color: white;
    text-align: left;
    border-radius: 8px;
    padding: 10px;
    position: absolute;
    z-index: 1000;
    bottom: 125%;
    left: 50%;
    margin-left: -150px;
    opacity: 0;
    transition: opacity 0.3s;
    font-size: 0.8em;
    line-height: 1.4;
}

.tooltip:hover .tooltip-text {
    visibility: visible;
    opacity: 1;
}
</style>
""", unsafe_allow_html=True)

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
        'basic': '📊 БАЗОВЫЙ',
        'advanced': '🎯 ПРОДВИНУТЫЙ', 
        'premium': '💎 ПРЕМИУМ'
    }
    return badges.get(subscription_level, badges['basic'])

def login_page():
    """Адаптивная страница входа"""
    st.title("🤖 ЮниВест - AI Советник по Инвестициям")
    
    clients = get_all_clients()
    
    selected_client = st.selectbox("👤 Выберите клиента:", clients)
    password = st.text_input("🔒 Пароль:", type="password", value="demo123")
    
    if st.button("🚀 Войти в систему", type="primary"):
        if password == "demo123":
            st.session_state.authenticated = True
            st.session_state.current_user = selected_client
            st.rerun()
        else:
            st.error("❌ Неверный пароль. Используйте 'demo123'")

def dashboard_page():
    """Адаптивная панель управления"""
    
    current_client = st.session_state.current_user
    client_data = get_client_details(current_client)
    portfolio_dict = get_portfolio_by_client(current_client)
    subscription_level = get_subscription_level(current_client)
    
    if not client_data or not portfolio_dict:
        st.error("❌ Ошибка загрузки данных")
        return
    
    st.title(f"🤖 ЮниВест AI Советник - {current_client}")
    st.write(f"Уровень подписки: {display_subscription_badge(subscription_level)}")
    
    # Боковая панель
    with st.sidebar:
        st.title("🎯 Навигация")
        
        page = st.radio("Выберите раздел:", 
                       ["📊 Дашборд", "📈 Расширенная аналитика", "💎 Тарифы"])
        
        if page != st.session_state.current_page:
            st.session_state.current_page = page
            st.rerun()
        
        st.markdown("---")
        if st.button("🚪 Выйти"):
            st.session_state.authenticated = False
            st.session_state.current_user = None
            st.rerun()
    
    # Основной контент
    st.subheader("👤 Профиль клиента")
    col1, col2 = st.columns(2)
    
    with col1:
        st.write(f"**Тип портфеля:** {client_data['portfolio_type']}")
        st.write(f"**Уровень риска:** {client_data['risk_profile']}")
    
    with col2:
        st.write(f"**Инвестиции:** ₽{client_data['initial_investment']:,.0f}")
        st.write(f"**Цель:** ₽{client_data['target_amount']:,.0f}")
    
    # Обзор портфеля
    st.subheader("📊 Обзор портфеля")
    weights_df = pd.DataFrame(list(portfolio_dict.items()), columns=['Актив', 'Доля'])
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        fig_pie = px.pie(weights_df, values='Доля', names='Актив', hole=0.3)
        st.plotly_chart(fig_pie, use_container_width=True)
    
    with col2:
        st.dataframe(weights_df, use_container_width=True, hide_index=True)
    
    # Ключевые метрики
    st.subheader("🔍 Ключевые метрики")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        display_metric_with_tooltip("Годовая доходность", "12.5%", 'annual_return')
    
    with col2:
        display_metric_with_tooltip("Волатильность", "18.2%", 'annual_volatility')
    
    with col3:
        display_metric_with_tooltip("Коэффициент Шарпа", "0.69", 'sharpe_ratio')
    
    with col4:
        display_metric_with_tooltip("Макс. просадка", "-15.3%", 'max_drawdown')
    
    # ИСТОРИЧЕСКАЯ ПРОИЗВОДИТЕЛЬНОСТЬ
    st.markdown("---")
    st.subheader("📈 Историческая производительность")
    
    # Запускаем анализ для получения исторических данных
    with st.spinner("📊 Генерируем исторические данные..."):
        analyzer = AdvancedPortfolioAnalysis(portfolio_dict, current_client)
        results = analyzer.comprehensive_analysis()
    
    if results and results.get('performance_charts'):
        display_historical_performance(results, current_client)
    else:
        st.warning("Не удалось загрузить исторические данные")
    
    # Рекомендации AI
    st.subheader("🤖 Рекомендации AI")
    
    recommendations = generate_subscription_based_recommendations(current_client)
    
    for rec in recommendations:
        st.info(rec)

def advanced_analytics_page():
    """Страница расширенной аналитики"""
    st.title("📈 Расширенная аналитика")
    st.info("Эта функция доступна на продвинутом и премиум тарифах")
    
    if st.button("💎 Перейти к тарифам"):
        st.session_state.current_page = "💎 Тарифы"
        st.rerun()

def display_pricing_page():
    """Страница с сравнением тарифов"""
    st.title("💎 Выберите свой тариф")
    
    col1, col2, col3 = st.columns(3)
    
    for i, level in enumerate(['basic', 'advanced', 'premium']):
        with [col1, col2, col3][i]:
            if level == 'basic':
                st.subheader("📊 Базовый")
                st.metric("Стоимость", "0₽/мес")
                st.write("✅ Базовые метрики")
                st.write("✅ Рекомендации AI")
                st.write("✅ Визуализация портфеля")
                st.button("🎁 Начать бесплатно", key=level)
            elif level == 'advanced':
                st.subheader("🎯 Продвинутый") 
                st.metric("Стоимость", "450₽/мес")
                st.write("✅ Все функции Базового")
                st.write("✅ Расширенная аналитика")
                st.write("✅ Глубокий анализ рисков")
                st.button("💳 Выбрать", key=level)
            else:
                st.subheader("💎 Премиум")
                st.metric("Стоимость", "800₽/мес")
                st.write("✅ Все функции Продвинутого")
                st.write("✅ AI-прогнозы и инсайты")
                st.write("✅ Персональный советник")
                st.button("💎 Выбрать", key=level)

def main():
    """Главная функция приложения"""
    init_session_state()
    
    if not st.session_state.authenticated:
        login_page()
    else:
        if st.session_state.current_page == "📊 Дашборд":
            dashboard_page()
        elif st.session_state.current_page == "📈 Расширенная аналитика":
            advanced_analytics_page()
        elif st.session_state.current_page == "💎 Тарифы":
            display_pricing_page()

if __name__ == "__main__":
    main()









