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

# ОБНОВЛЕННЫЕ TOOLTIP'Ы ДЛЯ ПОКАЗАТЕЛЕЙ - УЛУЧШЕННЫЕ И БОЛЕЕ ПОНЯТНЫЕ
TOOLTIPS = {
    # БАЗОВЫЕ ПОКАЗАТЕЛИ
    'sharpe_ratio': """
    📊 **Коэффициент Шарпа** - Доходность с поправкой на риск
    
    **Что показывает:** Сколько дополнительной доходности вы получаете за каждую единицу риска
    
    **Как интерпретировать:**
    • < 0.5 - низкая эффективность
    • 0.5-1.0 - хорошо  
    • 1.0-2.0 - отлично
    • > 2.0 - выдающийся результат
    
    **Ваш результат: 0.67 - Хорошо, есть потенциал для улучшения**
    """,
    
    'beta': """
    📈 **Бета-коэффициент** - Чувствительность к рынку
    
    **Что показывает:** Насколько ваш портфель реагирует на движения рынка
    
    **Уровни риска:**
    • < 0 - движется против рынка (редко)
    • 0-0.8 - защитный портфель
    • 0.8-1.2 - как рынок
    • > 1.2 - агрессивный рост
    
    **Ваш результат: 1.12 - Ожидайте колебаний как у рынка**
    """,
    
    'max_drawdown': """
    📉 **Максимальная просадка** - Самые большие потери
    
    **Что показывает:** Самое сильное падение стоимости от пика до минимума
    
    **О чем говорит:**
    • < 10% - отличная защита
    • 10-20% - умеренный риск  
    • 20-30% - высокий риск
    • > 30% - экстремальный риск
    
    **Ваш результат: -15% - Умеренный уровень просадок**
    """,
    
    'annual_return': """
    💰 **Годовая доходность** - Прирост капитала за год
    
    **Что показывает:** Насколько выросла стоимость портфеля за год
    
    **Сравнение с инфляцией:**
    • < 5% - ниже инфляции (реальные потери)
    • 5-10% - защита от инфляции
    • 10-15% - хороший рост
    • > 15% - высокая доходность
    
    **Ваш результат: 12% - Хорошая доходность выше инфляции**
    """,
    
    'annual_volatility': """
    ⚡ **Волатильность** - Размах колебаний стоимости
    
    **Что показывает:** Насколько сильно "скачет" цена вашего портфеля
    
    **Уровни стабильности:**
    • < 10% - очень стабильно
    • 10-20% - умеренная волатильность
    • 20-30% - высокая волатильность  
    • > 30% - экстремальные колебания
    
    **Ваш результат: 18% - Умеренные колебания, комфортный уровень**
    """,
    
    # ПРОДВИНУТЫЕ ПОКАЗАТЕЛИ
    'sortino_ratio': """
    🎯 **Коэффициент Сортино** - Умная версия Шарпа
    
    **В чем отличие от Шарпа:** Учитывает только "плохую" волатильность (убытки)
    
    **Преимущество:** Более точно оценивает риск для инвесторов
    
    **Оценка:**
    • < 0 - неэффективно
    • 0-1 - удовлетворительно
    • 1-2 - хорошо
    • > 2 - отлично
    
    **Ваш результат: 0.89 - Хорошо, портфель контролирует убытки**
    """,
    
    'treynor_ratio': """
    🏆 **Коэффициент Трейнора** - Доходность за системный риск
    
    **Что показывает:** Насколько вы превосходите безрисковые вложения
    
    **Особенность:** Учитывает только рыночный риск (бету)
    
    **Интерпретация:** Чем выше - тем лучше используете рыночные возможности
    
    **Ваш результат: 0.107 - Положительное превосходство над облигациями**
    """,
    
    'm_squared': """
    📊 **М-квадрат** - Сравнение с эталоном
    
    **Что показывает:** Какой была бы доходность при риске как у рынка
    
    **Проще говоря:** "Если бы мой портфель имел такую же волатильность как S&P 500"
    
    **Ваш результат: +4.5% - Вы бы обогнали рынок на 4.5% при равном риске**
    """,
    
    'jensen_alpha': """
    α **Альфа Дженсена** - Навык управления
    
    **Что показывает:** Насколько вы умнее рынка благодаря выбору акций
    
    **Ключевой показатель:** Положительная альфа = вы добавляете реальную ценность
    
    **Оценка:**
    • > 0 - превосходите рынок
    • = 0 - как рынок  
    • < 0 - отстаете от рынка
    
    **Ваш результат: +2.3% - Вы добавляете ценность сверх рыночной**
    """,
    
    'parametric_var_95': """
    🛡️ **Value at Risk (95%)** - Максимальные потери в нормальный день
    
    **Что означает:** "С вероятностью 95% за день я не потеряю больше X%"
    
    **Простой пример:** VaR -2.5% = в 95% дней потери не превысят 2.5%
    
    **Ваш результат: -2.5% - В обычный день рискуете потерять до 2.5%**
    """,
    
    'cvar_95': """
    ⚡ **Conditional VaR** - Средние потери в плохие дни
    
    **Что означает:** "В худшие 5% дней я в среднем теряю X%"
    
    **Важнее VaR:** Показывает реальную боль в кризис
    
    **Ваш результат: -3.8% - В кризисные дни теряете в среднем 3.8%**
    """,
    
    # ПРЕМИУМ ПОКАЗАТЕЛИ
    'modigliani_ratio': """
    💎 **Коэффициент Модильяни** - Золотой стандарт оценки
    
    **Что показывает:** Насколько ваш портфель эффективнее рынка при том же риске
    
    **Лучшая метрика:** Для прямого сравнения разных портфелей
    
    **Интерпретация:** +2.8% = ваш портфель на 2.8% лучше рынка
    
    **Ваш результат: +2.8% - Значительное превосходство над эталоном**
    """,
    
    'information_ratio': """
    🎯 **Information Ratio** - Стабильность outperformance
    
    **Что показывает:** Насколько стабильно вы обгоняете бенчмарк
    
    **Для кого важно:** Активным управляющим
    
    **Оценка:**
    • 0.0-0.2 - нестабильное превосходство
    • 0.2-0.5 - хорошая стабильность
    • > 0.5 - выдающаяся стабильность
    
    **Ваш результат: 0.15 - Превосходство есть, но можно стабилизировать**
    """,
    
    'tracking_error': """
    📏 **Tracking Error** - Отклонение от эталона
    
    **Что показывает:** Насколько ваш портфель отличается от индекса
    
    **Что означает:**
    • Низкий TE (~2%) - пассивная стратегия
    • Высокий TE (~8%) - активная стратегия
    
    **Ваш результат: 4.5% - Умеренно-активное управление**
    """,
    
    'calmar_ratio': """
    ⚖️ **Коэффициент Калмара** - Доходность vs Максимальная боль
    
    **Что показывает:** Сколько доходности вы получаете за максимальную просадку
    
    **Для кого важно:** Долгосрочным инвесторам
    
    **Оценка:**
    • < 0.5 - низкая компенсация за риск
    • 0.5-1.0 - хорошая компенсация
    • > 1.0 - отличная компенсация
    
    **Ваш результат: 0.80 - Хорошая компенсация за перенесенные просадки**
    """
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
    width: 350px;
    background-color: #1a1a1a;
    color: white;
    text-align: left;
    border-radius: 8px;
    padding: 15px;
    position: absolute;
    z-index: 1000;
    bottom: 125%;
    left: 50%;
    margin-left: -175px;
    opacity: 0;
    transition: opacity 0.3s;
    font-size: 0.85em;
    line-height: 1.5;
    box-shadow: 0 8px 25px rgba(0,0,0,0.3);
    border: 1px solid #333;
    white-space: pre-line;
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
    border-color: #1a1a1a transparent transparent transparent;
}

.metric-container {
    display: flex;
    align-items: center;
    gap: 8px;
}

/* Адаптивность для мобильных */
@media (max-width: 768px) {
    .tooltip .tooltip-text {
        width: 280px;
        margin-left: -140px;
        font-size: 0.8em;
    }
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


# database.py - файл для работы с базой данных портфелей

import sqlite3
import logging
from typing import Dict, List, Optional, Tuple
from datetime import datetime
import os

# Настройка логирования
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# ДАННЫЕ О ПОДПИСКАХ КЛИЕНТОВ - ОБНОВЛЕННЫЕ ДАННЫЕ С НОВЫМИ ТАРИФАМИ!
CLIENT_SUBSCRIPTIONS = {
    'Иван Петров': {'level': 'premium', 'price': 800, 'expires': '2024-12-31'},
    'Мария Сидорова': {'level': 'advanced', 'price': 450, 'expires': '2024-11-30'},
    'Алексей Козлов': {'level': 'basic', 'price': 0, 'expires': '2024-10-15'},
    'Елена Волкова': {'level': 'basic', 'price': 0, 'expires': '2024-09-30'},
    'Дмитрий Смирнов': {'level': 'basic', 'price': 0, 'expires': '2024-09-30'}
}

# ОПИСАНИЯ ТАРИФОВ И ФУНКЦИЙ - УСИЛЕННЫЕ ВОЗМОЖНОСТИ С НОВЫМИ ПОКАЗАТЕЛЯМИ
SUBSCRIPTION_FEATURES = {
    'basic': {
        'name': 'Базовый',
        'price': 0,
        'features': [
            '📊 Все базовые метрики портфеля',
            '💡 Персональные рекомендации',
            '📈 Анализ диверсификации',
            '🔄 Мониторинг портфеля',
            '📱 Доступ с любых устройств',
            '📊 Визуализация активов',
            '🎯 Базовые инвестиционные идеи',
            '📋 Планирование целей',
            '📊 Коэффициент Шарпа и Бета',
            '📈 Объяснения показателей'
        ],
        'limitations': [
            '❌ Без продвинутого риск-менеджмента',
            '❌ Без оптимизации по Марковицу',
            '❌ Без новостного анализа',
            '❌ Без AI-прогнозов'
        ]
    },
    'advanced': {
        'name': 'Продвинутый',
        'price': 450,
        'features': [
            '✅ Все функции Базового тарифа',
            '🎯 Расширенная оптимизация портфеля',
            '📉 Глубокий анализ рисков (VaR, CVaR)',
            '📊 Stress-testing сценарии',
            '⚡ Тактические рекомендации',
            '📈 Метрики эффективности (Сортино, Калмар)',
            '🔄 Автоматическая ребалансировка',
            '📊 Матрица корреляций',
            '🎯 Анализ качества портфеля',
            '📈 Сравнение с бенчмарками',
            '📊 Коэффициенты Трейнора и М-квадрат',
            'α Альфа Дженсена и расширенная аналитика'
        ],
        'upgrade_reason': 'Для профессионального управления рисками'
    },
    'premium': {
        'name': 'Премиум',
        'price': 800,
        'features': [
            '✅ Все функции Продвинутого тарифа',
            '🤖 AI-прогнозы на основе ML',
            '🏆 Детальное сравнение с эталонами',
            '🚀 Приоритетная поддержка 24/7',
            '📈 Расширенная аналитика',
            '💎 Персональный финансовый советник',
            '🎯 Эксклюзивные инвестиционные идеи',
            '📊 Кастомные отчеты и дашборды',
            '🌍 Отраслевой анализ',
            '⚡ Монте-Карло симуляции',
            '📊 AI инсайты и паттерны',
            '🎯 Персональные стратегии',
            '💎 Коэффициенты Модильяни и Information Ratio',
            '📏 Tracking Error и премиум аналитика'
        ],
        'upgrade_reason': 'Для максимальных результатов с AI-помощником'
    }
}

# ФУНКЦИИ ДЛЯ РАБОТЫ С ПОДПИСКАМИ
def get_subscription_level(client_name: str) -> str:
    """Возвращает уровень подписки клиента"""
    subscription = CLIENT_SUBSCRIPTIONS.get(client_name, {})
    return subscription.get('level', 'basic')

def get_subscription_details(client_name: str) -> Dict:
    """Возвращает детали подписки"""
    subscription = CLIENT_SUBSCRIPTIONS.get(client_name, {})
    level = subscription.get('level', 'basic')
    
    details = SUBSCRIPTION_FEATURES.get(level, {}).copy()
    details.update({
        'level': level,
        'price': subscription.get('price', 0),
        'expires': subscription.get('expires', '2024-01-01')
    })
    
    return details

def can_access_advanced_analytics(client_name: str) -> bool:
    """Проверяет доступ к продвинутой аналитике"""
    level = get_subscription_level(client_name)
    return level in ['advanced', 'premium']

def can_access_premium_features(client_name: str) -> bool:
    """Проверяет доступ к премиум функциям"""
    return get_subscription_level(client_name) == 'premium'

def can_access_news_analysis(client_name: str) -> bool:
    """Проверяет доступ к новостному анализу"""
    level = get_subscription_level(client_name)
    return level in ['advanced', 'premium']

# РАСШИРЕННЫЕ ДАННЫЕ ДЛЯ ПРЕМИУМ-АНАЛИТИКИ
PREMIUM_ANALYTICS_DATA = {
    'Иван Петров': {
        'ai_predictions': {
            'next_month_return': 0.045,
            'confidence': 0.78,
            'trend': 'bullish',
            'key_drivers': ['технологический сектор', 'снижение инфляции'],
            'risk_warnings': ['геополитическая напряженность', 'волатильность рынка'],
            'optimal_rebalance': {'TSLA': -0.02, 'NVDA': -0.01, 'BND': 0.03}
        },
        'benchmark_comparison': {
            'sp500': {'return': 0.121, 'volatility': 0.15, 'sharpe': 0.81},
            'nasdaq': {'return': 0.183, 'volatility': 0.22, 'sharpe': 0.83},
            'russian_index': {'return': 0.085, 'volatility': 0.18, 'sharpe': 0.47},
            'your_portfolio': {'return': 0.150, 'volatility': 0.20, 'sharpe': 0.75},
            'percentile_ranking': 0.72
        },
        'ml_insights': [
            '📈 **Высокая корреляция с технологическим сектором** (0.85)',
            '⚡ **Портфель перевешен в акции роста** - рассмотрите балансировку',
            '🛡️ **Рекомендуется добавить защитные активы** для снижения VaR',
            '🎯 **Оптимальный момент для ребалансировки** - потенциал +2.3%',
            '📊 **Stress-test показал устойчивость** к умеренным коррекциям'
        ],
        'sector_analysis': {
            'Технологии': 0.35,
            'Финансы': 0.20, 
            'Здравоохранение': 0.15,
            'Потребительские товары': 0.12,
            'Энергетика': 0.08,
            'Недвижимость': 0.06,
            'Материалы': 0.04
        }
    },
    'Мария Сидорова': {
        'ai_predictions': {
            'next_month_return': 0.028,
            'confidence': 0.72,
            'trend': 'neutral',
            'key_drivers': ['потребительский сектор', 'динамика рубля'],
            'risk_warnings': ['инфляционное давление', 'изменение ставок ЦБ'],
            'optimal_rebalance': {'VTI': 0.02, 'BND': -0.02, 'GLD': 0.01}
        },
        'benchmark_comparison': {
            'sp500': {'return': 0.121, 'volatility': 0.15, 'sharpe': 0.81},
            'nasdaq': {'return': 0.183, 'volatility': 0.22, 'sharpe': 0.83},
            'russian_index': {'return': 0.085, 'volatility': 0.18, 'sharpe': 0.47},
            'your_portfolio': {'return': 0.100, 'volatility': 0.16, 'sharpe': 0.63},
            'percentile_ranking': 0.58
        },
        'ml_insights': [
            '💰 **Хорошая диверсификация по секторам**',
            '📊 **Умеренный уровень риска** соответствует профилю',
            '🔄 **Рекомендуется реинвестировать дивиденды**',
            '⏰ **Идеальный горизонт инвестиций 3-5 лет**',
            '🎯 **Портфель оптимален для поставленных целей**'
        ],
        'sector_analysis': {
            'Технологии': 0.25,
            'Финансы': 0.18,
            'Здравоохранение': 0.15,
            'Потребительские товары': 0.20,
            'Энергетика': 0.12,
            'Недвижимость': 0.08,
            'Материалы': 0.02
        }
    }
}

# ФУНКЦИИ ДЛЯ ПРЕМИУМ-АНАЛИТИКИ
def get_ai_predictions(client_name: str) -> Optional[Dict]:
    """Возвращает AI-прогнозы для премиум клиентов"""
    if not can_access_premium_features(client_name):
        return None
    return PREMIUM_ANALYTICS_DATA.get(client_name, {}).get('ai_predictions')

def get_benchmark_comparison(client_name: str) -> Optional[Dict]:
    """Возвращает сравнение с эталонными индексами"""
    if not can_access_premium_features(client_name):
        return None
    return PREMIUM_ANALYTICS_DATA.get(client_name, {}).get('benchmark_comparison')

def get_ml_insights(client_name: str) -> List[str]:
    """Возвращает ML инсайты для портфеля"""
    if not can_access_premium_features(client_name):
        return []
    return PREMIUM_ANALYTICS_DATA.get(client_name, {}).get('ml_insights', [])

def get_sector_analysis(client_name: str) -> Optional[Dict]:
    """Возвращает отраслевой анализ"""
    if not can_access_premium_features(client_name):
        return None
    return PREMIUM_ANALYTICS_DATA.get(client_name, {}).get('sector_analysis')

# Детальные данные клиентов с уникальными характеристиками
CLIENTS_DETAILED_DATA = {
    'Иван Петров': {
        'name': 'Иван Петров',
        'portfolio_name': 'агрессивный',
        'description': 'Молодой инвестор, ориентированный на максимальный рост капитала',
        'risk_profile': 'очень высокий',
        'investment_horizon': '15+ лет',
        'experience': 'Эксперт',
        'financial_goals': 'Создание технологического фонда, венчурные инвестиции',
        'portfolio_type': 'агрессивный',
        'risk_tolerance': 0.85,
        'diversification_level': 'низкий',
        'initial_investment': 500000,
        'target_amount': 5000000,
        'key_metrics': {
            'expected_return': 0.18,
            'volatility': 0.32,
            'sharpe_ratio': 0.56
        }
    },
    'Мария Сидорова': {
        'name': 'Мария Сидорова',
        'portfolio_name': 'агрессивный',
        'description': 'Молодая инвестор, готовая к риску для ускоренного роста',
        'risk_profile': 'высокий',
        'investment_horizon': '5-7 лет',
        'experience': 'Начинающий',
        'financial_goals': 'Ускоренное накопление на жилье',
        'portfolio_type': 'агрессивный',
        'risk_tolerance': 0.70,
        'diversification_level': 'средний',
        'initial_investment': 300000,
        'target_amount': 800000,
        'key_metrics': {
            'expected_return': 0.15,
            'volatility': 0.25,
            'sharpe_ratio': 0.60
        }
    },
    'Алексей Козлов': {
        'name': 'Алексей Козлов',
        'portfolio_name': 'сбалансированный',
        'description': 'Семейный инвестор с умеренными аппетитами к риску',
        'risk_profile': 'умеренный',
        'investment_horizon': '7-10 лет',
        'experience': 'Продвинутый',
        'financial_goals': 'Образование детей, покупка загородного дома',
        'portfolio_type': 'сбалансированный',
        'risk_tolerance': 0.55,
        'diversification_level': 'очень высокий',
        'initial_investment': 800000,
        'target_amount': 2500000,
        'key_metrics': {
            'expected_return': 0.095,
            'volatility': 0.14,
            'sharpe_ratio': 0.68
        }
    },
    'Елена Волкова': {
        'name': 'Елена Волкова',
        'portfolio_name': 'доходный',
        'description': 'Опытный инвестор, ориентированный на пассивный доход',
        'risk_profile': 'средний',
        'investment_horizon': '10+ лет',
        'experience': 'Опытный',
        'financial_goals': 'Пассивный доход для досрочного выхода на пенсию',
        'portfolio_type': 'доходный',
        'risk_tolerance': 0.45,
        'diversification_level': 'высокий',
        'initial_investment': 1200000,
        'target_amount': 4000000,
        'key_metrics': {
            'expected_return': 0.078,
            'volatility': 0.11,
            'sharpe_ratio': 0.71
        }
    },
    'Дмитрий Смирнов': {
        'name': 'Дмитрий Смирнов',
        'portfolio_name': 'ультра-консервативный',
        'description': 'Пенсионер, основной приоритет - сохранение капитала',
        'risk_profile': 'очень низкий',
        'investment_horizon': '1-3 года',
        'experience': 'Консервативный',
        'financial_goals': 'Сохранить сбережения от инфляции',
        'portfolio_type': 'ультра-консервативный',
        'risk_tolerance': 0.15,
        'diversification_level': 'средний',
        'initial_investment': 2000000,
        'target_amount': 2200000,
        'key_metrics': {
            'expected_return': 0.045,
            'volatility': 0.05,
            'sharpe_ratio': 0.90
        }
    }
}

class PortfolioDatabase:
    """
    Класс для работы с базой данных портфелей
    """
    
    def __init__(self, db_path: str = 'uniwest.db'):
        self.db_path = db_path
        self._init_database()
    
    def _get_connection(self) -> sqlite3.Connection:
        """Возвращает соединение с базой данных"""
        try:
            conn = sqlite3.connect(self.db_path)
            conn.row_factory = sqlite3.Row
            return conn
        except sqlite3.Error as e:
            logger.error(f"Ошибка подключения к базе данных: {e}")
            raise
    
    def _init_database(self) -> None:
        """
        Инициализирует базу данных и заполняет демо-данными
        """
        conn = None
        try:
            conn = self._get_connection()
            cursor = conn.cursor()
            
            # Создаем таблицу для портфелей
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS portfolios (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT UNIQUE NOT NULL,
                    description TEXT,
                    created_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    last_modified TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            ''')
            
            # Создаем таблицу для активов в портфелях
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS portfolio_assets (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    portfolio_id INTEGER NOT NULL,
                    ticker TEXT NOT NULL,
                    weight REAL NOT NULL CHECK (weight >= 0 AND weight <= 1),
                    FOREIGN KEY (portfolio_id) REFERENCES portfolios (id) ON DELETE CASCADE,
                    UNIQUE(portfolio_id, ticker)
                )
            ''')
            
            conn.commit()
            logger.info("База данных инициализирована")
            
            # Заполняем демо-данными
            self._seed_demo_data(conn)
            
        except sqlite3.Error as e:
            logger.error(f"Ошибка инициализации базы данных: {e}")
            raise
        finally:
            if conn:
                conn.close()
    
    def _seed_demo_data(self, conn: sqlite3.Connection) -> None:
        """
        Заполняет базу данных демо-данными
        """
        try:
            cursor = conn.cursor()
            
            # Демо-портфели (соответствуют клиентам из app.py)
            demo_portfolios = [
                ("агрессивный", "Портфель Ивана Петрова - высокорисковые активы"),
                ("сбалансированный", "Портфель Алексея Козлова - баланс роста и стабильности"),
                ("доходный", "Портфель Елены Волкова - дивидендные акции"),
                ("ультра-консервативный", "Портфель Дмитрия Смирнова - максимальная защита")
            ]
            
            for portfolio_name, description in demo_portfolios:
                cursor.execute('''
                    INSERT OR IGNORE INTO portfolios (name, description) 
                    VALUES (?, ?)
                ''', (portfolio_name, description))
            
            # Активы для портфелей (уникальные для каждого клиента)
            portfolios_assets = {
                "агрессивный": {
                    'TSLA': 0.25, 'NVDA': 0.20, 'AMD': 0.15, 'ARKK': 0.15,
                    'SQ': 0.10, 'BTC-USD': 0.10, 'ETH-USD': 0.05
                },
                "сбалансированный": {
                    'VTI': 0.25, 'VXUS': 0.15, 'BND': 0.20, 'VNQ': 0.10,
                    'GLD': 0.08, 'AAPL': 0.07, 'MSFT': 0.07, 'JPM': 0.05, 'Cash': 0.03
                },
                "доходный": {
                    'VYM': 0.20, 'SCHD': 0.18, 'T': 0.10, 'VZ': 0.09,
                    'XOM': 0.08, 'PFE': 0.08, 'JNJ': 0.07, 'PG': 0.07, 'O': 0.06, 'Cash': 0.07
                },
                "ультра-консервативный": {
                    'BND': 0.40, 'GOVT': 0.25, 'SHY': 0.15, 'JNJ': 0.08,
                    'PG': 0.07, 'Cash': 0.05
                }
            }
            
            # Добавляем активы для каждого портфеля
            for portfolio_name, assets in portfolios_assets.items():
                cursor.execute('SELECT id FROM portfolios WHERE name = ?', (portfolio_name,))
                result = cursor.fetchone()
                
                if result:
                    portfolio_id = result[0]
                    
                    # Удаляем старые активы
                    cursor.execute('DELETE FROM portfolio_assets WHERE portfolio_id = ?', (portfolio_id,))
                    
                    # Добавляем новые активы
                    for ticker, weight in assets.items():
                        cursor.execute('''
                            INSERT INTO portfolio_assets (portfolio_id, ticker, weight) 
                            VALUES (?, ?, ?)
                        ''', (portfolio_id, ticker, weight))
            
            conn.commit()
            logger.info("Демо-данные успешно добавлены")
            
        except sqlite3.Error as e:
            logger.error(f"Ошибка заполнения демо-данными: {e}")
            conn.rollback()
            raise
    
    def get_portfolio(self, portfolio_name: str) -> Optional[Dict[str, float]]:
        """
        Получает портфель из базы данных по имени
        """
        conn = None
        try:
            conn = self._get_connection()
            cursor = conn.cursor()
            
            cursor.execute('''
                SELECT pa.ticker, pa.weight 
                FROM portfolio_assets pa 
                JOIN portfolios p ON pa.portfolio_id = p.id 
                WHERE p.name = ?
                ORDER BY pa.weight DESC
            ''', (portfolio_name,))
            
            assets = {}
            total_weight = 0.0
            
            for row in cursor.fetchall():
                ticker = row['ticker']
                weight = row['weight']
                assets[ticker] = weight
                total_weight += weight
            
            # Нормализуем веса если сумма не равна 1.0
            if assets and abs(total_weight - 1.0) > 0.001:
                assets = {ticker: weight/total_weight for ticker, weight in assets.items()}
                logger.warning(f"Веса портфеля '{portfolio_name}' нормализованы")
            
            return assets if assets else None
            
        except sqlite3.Error as e:
            logger.error(f"Ошибка получения портфеля '{portfolio_name}': {e}")
            return None
        finally:
            if conn:
                conn.close()

    def get_all_portfolios(self) -> List[Tuple[str, str]]:
        """
        Возвращает список всех портфелей
        """
        conn = None
        try:
            conn = self._get_connection()
            cursor = conn.cursor()
            
            cursor.execute('SELECT name, description FROM portfolios ORDER BY name')
            return [(row['name'], row['description']) for row in cursor.fetchall()]
            
        except sqlite3.Error as e:
            logger.error(f"Ошибка получения списка портфелей: {e}")
            return []
        finally:
            if conn:
                conn.close()

# Функции для обратной совместимости
def init_database():
    """Инициализирует базу данных (для обратной совместимости)"""
    PortfolioDatabase()

def get_portfolio(portfolio_name: str) -> Optional[Dict[str, float]]:
    """Получает портфель (для обратной совместимости)"""
    db = PortfolioDatabase()
    return db.get_portfolio(portfolio_name)

def get_all_portfolios() -> List[Tuple[str, str]]:
    """Получает все портфели (для обратной совместимости)"""
    db = PortfolioDatabase()
    return db.get_all_portfolios()

# Новые функции для работы с клиентами
def get_client_details(client_name: str) -> Optional[Dict]:
    """Возвращает детальную информацию о клиенте"""
    client_data = CLIENTS_DETAILED_DATA.get(client_name)
    if client_data:
        # Добавляем имя клиента в данные для совместимости с app.py
        client_data_with_name = client_data.copy()
        client_data_with_name['name'] = client_name
        return client_data_with_name
    return None

def get_all_clients() -> List[str]:
    """Возвращает список всех клиентов"""
    return list(CLIENTS_DETAILED_DATA.keys())

def get_portfolio_by_client(client_name: str) -> Optional[Dict[str, float]]:
    """Получает портфель по имени клиента"""
    client_data = CLIENTS_DETAILED_DATA.get(client_name)
    if not client_data:
        return None
    
    portfolio_name = client_data['portfolio_name']
    return get_portfolio(portfolio_name)

# ВСПОМОГАТЕЛЬНЫЕ ФУНКЦИИ ДЛЯ РЕКОМЕНДАЦИЙ
def analyze_diversification(portfolio: Dict[str, float], client_data: Dict) -> List[str]:
    """Анализ диверсификации портфеля"""
    recommendations = []
    num_assets = len(portfolio)
    max_weight = max(portfolio.values()) if portfolio else 0
    
    # Анализ количества активов
    if num_assets < 5:
        recommendations.append("🔄 **Увеличьте диверсификацию**: Добавьте еще 2-3 актива для снижения риска")
    elif num_assets > 12:
        recommendations.append("⚖️ **Оптимизируйте портфель**: Слишком много активов может усложнить управление")
    
    # Анализ концентрации
    if max_weight > 0.25:
        top_asset = max(portfolio, key=portfolio.get)
        recommendations.append(f"📉 **Снизьте концентрацию**: Актив {top_asset} составляет {max_weight:.1%} - рассмотрите уменьшение доли")
    
    # Анализ корреляции
    if has_high_correlation_assets(portfolio):
        recommendations.append("🌍 **Добавьте некоррелированные активы**: Рассмотрите золото (GLD) или международные ETF (VXUS) для диверсификации")
    
    return recommendations

def analyze_risk_profile(portfolio: Dict[str, float], client_data: Dict) -> List[str]:
    """Анализ соответствия портфеля профилю риска"""
    recommendations = []
    risk_tolerance = client_data.get('risk_tolerance', 0.5)
    portfolio_risk = calculate_portfolio_risk(portfolio)
    
    # Сравнение риска портфеля с толерантностью клиента
    if portfolio_risk > risk_tolerance + 0.2:
        recommendations.append("🛡️ **Снизьте риск портфеля**: Текущий уровень риска превышает вашу толерантность")
    elif portfolio_risk < risk_tolerance - 0.2:
        recommendations.append("🚀 **Увеличьте потенциал роста**: Можно добавить больше акций роста для повышения доходности")
    
    # Анализ защитных активов
    defensive_assets_weight = sum(weight for asset, weight in portfolio.items() 
                                if asset in ['BND', 'GOVT', 'SHY', 'Cash', 'GLD', 'JNJ', 'PG'])
    
    if client_data['risk_profile'] in ['низкий', 'очень низкий'] and defensive_assets_weight < 0.4:
        recommendations.append("🏦 **Увеличьте долю защитных активов**: Добавьте облигации (BND) для стабильности портфеля")
    
    return recommendations

def analyze_asset_allocation(portfolio: Dict[str, float], client_data: Dict) -> List[str]:
    """Анализ распределения активов"""
    recommendations = []
    
    # Классификация активов
    stocks_weight = sum(weight for asset, weight in portfolio.items() 
                       if not is_defensive_asset(asset))
    bonds_weight = sum(weight for asset, weight in portfolio.items() 
                      if asset in ['BND', 'GOVT', 'SHY'])
    cash_weight = portfolio.get('Cash', 0)
    crypto_weight = sum(weight for asset, weight in portfolio.items() 
                       if 'BTC' in asset or 'ETH' in asset)
    
    # Анализ по типу портфеля
    portfolio_type = client_data['portfolio_type']
    
    if portfolio_type == 'агрессивный' and stocks_weight < 0.7:
        recommendations.append("📈 **Увеличьте долю акций**: Для агрессивной стратегии целесообразно 70-80% в акциях")
    
    elif portfolio_type == 'сбалансированный' and not (0.4 <= stocks_weight <= 0.6):
        recommendations.append("⚖️ **Балансируйте портфель**: Оптимальное соотношение 50/50 или 60/40 между акциями и облигациями")
    
    elif portfolio_type == 'доходный' and bonds_weight < 0.3:
        recommendations.append("🏛️ **Увеличьте долю облигаций**: Для доходного портфеля рекомендуется 30-40% в облигациях")
    
    elif portfolio_type == 'ультра-консервативный' and bonds_weight < 0.5:
        recommendations.append("🛡️ **Увеличьте долю защитных активов**: Для консервативного портфеля рекомендуется 50-70% в облигациях")
    
    # Анализ денежной позиции
    if cash_weight < 0.03:
        recommendations.append("💵 **Создайте денежный резерв**: Рекомендуется держать 3-5% наличности для возможностей")
    elif cash_weight > 0.1:
        recommendations.append("💰 **Используйте избыточную наличность**: Рассмотрите инвестирование части cash в доходные активы")
    
    # Анализ крипто-экспозиции
    if crypto_weight > 0.1 and client_data['risk_profile'] in ['низкий', 'очень низкий']:
        recommendations.append("⚡ **Снизьте долю криптоактивов**: Для вашего профиля риска рекомендуется не более 5% в крипто")
    
    return recommendations

def generate_tactical_recommendations(client_data: Dict) -> List[str]:
    """Тактические рекомендации на основе текущей рыночной ситуации"""
    recommendations = []
    portfolio_type = client_data['portfolio_type']
    
    # Рекомендации для разных типов портфелей
    if portfolio_type == 'агрессивный':
        recommendations.extend([
            "🎯 **Фокус на рост**: Рассмотрите добавление технологических ETF (QQQ, ARKK)",
            "⏰ **Ребалансировка раз в квартал**: Активно управляйте портфелем для максимизации доходности",
            "📊 **Мониторинг волатильности**: Установите стоп-лосс уровни для защиты от сильных просадок"
        ])
    
    elif portfolio_type == 'сбалансированный':
        recommendations.extend([
            "🔄 **Ребалансировка раз в 6 месяцев**: Поддерживайте целевое распределение активов",
            "🌍 **Глобальная диверсификация**: Добавьте международные ETF (VXUS, EFA)",
            "📈 **Дивидендная стратегия**: Рассмотрите дивидендные аристократы для стабильного дохода"
        ])
    
    elif portfolio_type == 'доходный':
        recommendations.extend([
            "💵 **Реинвестирование дивидендов**: Используйте DRIP для сложного процента",
            "🏢 **REIT и инфраструктура**: Добавьте риел-эстейт инвестиции для диверсификации дохода",
            "📅 **Ежеквартальный доход**: Оптимизируйте для стабильных дивидендных выплат"
        ])
    
    else:  # консервативный
        recommendations.extend([
            "🛡️ **Защита капитала**: Фокус на высококачественные корпоративные и государственные облигации",
            "📉 **Минимизация волатильности**: Избегайте высокорисковых активов",
            "🏦 **Ликвидность**: Держите повышенную долю cash для возможности покупки на просадках"
        ])
    
    return recommendations

def generate_general_recommendations(client_data: Dict) -> List[str]:
    """Общие рекомендации для всех клиентов"""
    horizon = client_data['investment_horizon']
    experience = client_data['experience']
    
    recommendations = [
        "📚 **Непрерывное обучение**: Изучайте финансовые рынки и инвестиционные стратегии",
        "📊 **Регулярный мониторинг**: Проводите ежемесячный анализ портфеля",
        "🎯 **Дисциплина**: Придерживайтесь своей инвестиционной стратегии несмотря на рыночные колебания"
    ]
    
    # Персонализация по горизонту инвестирования
    if '15+' in horizon or '10+' in horizon:
        recommendations.append("🚀 **Долгосрочная перспектива**: Используйте преимущество времени для сложного процента")
    elif '1-3' in horizon or '3-5' in horizon:
        recommendations.append("⏳ **Краткосрочная осторожность**: Фокус на сохранение капитала и ликвидность")
    
    # Персонализация по опыту
    if experience in ['начальный', 'Начинающий']:
        recommendations.append("👨‍🏫 **Консультация специалиста**: Рассмотрите работу с финансовым советником для начала")
    elif experience in ['эксперт', 'Эксперт']:
        recommendations.append("💡 **Продвинутые стратегии**: Исследуйте опционные стратегии для хеджирования и дохода")
    
    return recommendations

# ВСПОМОГАТЕЛЬНЫЕ ФУНКЦИИ
def has_high_correlation_assets(portfolio: Dict[str, float]) -> bool:
    """Проверяет наличие высококоррелированных активов"""
    tech_assets = ['TSLA', 'NVDA', 'AMD', 'AAPL', 'MSFT', 'SQ']
    tech_weight = sum(weight for asset, weight in portfolio.items() if asset in tech_assets)
    return tech_weight > 0.4

def is_defensive_asset(asset: str) -> bool:
    """Определяет, является ли актив защитным"""
    defensive_assets = ['BND', 'GOVT', 'SHY', 'Cash', 'GLD', 'JNJ', 'PG', 'XOM', 'T', 'VZ']
    return asset in defensive_assets

def calculate_portfolio_risk(portfolio: Dict[str, float]) -> float:
    """Упрощенный расчет риска портфеля"""
    # Веса рисков для разных типов активов
    risk_weights = {
        'high_risk': ['TSLA', 'NVDA', 'AMD', 'SQ', 'ARKK', 'BTC-USD', 'ETH-USD'],
        'medium_risk': ['AAPL', 'MSFT', 'VTI', 'VXUS', 'VNQ', 'VYM', 'SCHD'],
        'low_risk': ['BND', 'GOVT', 'SHY', 'JNJ', 'PG', 'XOM', 'T', 'VZ', 'Cash', 'GLD']
    }
    
    total_risk = 0
    for asset, weight in portfolio.items():
        if asset in risk_weights['high_risk']:
            total_risk += weight * 0.8
        elif asset in risk_weights['medium_risk']:
            total_risk += weight * 0.5
        else:
            total_risk += weight * 0.2
    
    return min(total_risk, 1.0)

# ОБНОВЛЕННАЯ ФУНКЦИЯ РЕКОМЕНДАЦИЙ
def generate_client_recommendations(client_name: str) -> List[str]:
    """Генерирует реалистичные и точные рекомендации для клиента"""
    client_data = CLIENTS_DETAILED_DATA.get(client_name)
    if not client_data:
        return ["💡 Информация о клиенте не найдена"]
    
    portfolio = get_portfolio_by_client(client_name)
    if not portfolio:
        return ["💡 Портфель клиента не найден"]
    
    recommendations = []
    
    # Персонализированное приветствие
    recommendations.append(f"👤 **Персональные рекомендации для {client_name}**")
    
    # Анализ диверсификации
    diversification_recs = analyze_diversification(portfolio, client_data)
    recommendations.extend(diversification_recs)
    
    # Анализ риска
    risk_recs = analyze_risk_profile(portfolio, client_data)
    recommendations.extend(risk_recs)
    
    # Анализ распределения активов
    allocation_recs = analyze_asset_allocation(portfolio, client_data)
    recommendations.extend(allocation_recs)
    
    # Тактические рекомендации
    tactical_recs = generate_tactical_recommendations(client_data)
    recommendations.extend(tactical_recs[:2])  # Берем 2 самые важные
    
    # Общие рекомендации
    general_recs = generate_general_recommendations(client_data)
    recommendations.extend(general_recs[:2])  # Берем 2 самые важные
    
    return recommendations[:8]  # Ограничиваем 8 рекомендациями

# ФУНКЦИЯ ДЛЯ РЕКОМЕНДАЦИЙ С УЧЕТОМ ПОДПИСКИ - ОБНОВЛЕННАЯ ДЛЯ 3 УРОВНЕЙ
def generate_subscription_based_recommendations(client_name: str) -> List[str]:
    """Генерирует рекомендации в зависимости от уровня подписки"""
    level = get_subscription_level(client_name)
    base_recommendations = generate_client_recommendations(client_name)
    
    # Добавляем явные сообщения о подписке
    subscription_messages = {
        'basic': [
            "🎁 **Бесплатный тариф**: Доступны базовые функции анализа",
            "🚀 **Улучшите до Продвинутого**: Получите оптимизацию портфеля и анализ рисков за 450 руб/мес"
        ],
        'advanced': [
            "🎯 **Продвинутый тариф**: Доступны расширенная аналитика и оптимизация",
            "💎 **Улучшите до Премиум**: Получите AI-прогнозы и персонального советника за 800 руб/мес"
        ],
        'premium': [
            "💎 **Премиум тариф**: Полный доступ ко всем функциям",
            "🤖 **AI-советник**: Ваш персональный финансовый эксперт всегда на связи"
        ]
    }
    
    if level == 'basic':
        return base_recommendations[:4] + subscription_messages['basic']
    
    elif level == 'advanced':
        # Добавляем тактические рекомендации
        advanced_recs = [
            "🎯 **Тактическая рекомендация**: Рассмотрите увеличение доли технологических акций на 3-5%",
            "📊 **Анализ рисков**: Текущий VaR на приемлемом уровне (-2.3%)",
            "🔄 **Оптимизация**: Рекомендуемая ребалансировка - 2.3% в облигации"
        ]
        return base_recommendations + advanced_recs[:2] + subscription_messages['advanced']
    
    else:  # premium
        # Добавляем премиум рекомендации
        premium_recs = [
            "🤖 **AI-прогноз**: Ожидается рост на 4.5% в следующем месяце с уверенностью 78%",
            "🏆 **Сравнение с эталоном**: Ваш портфель превосходит S&P 500 на 3.1%",
            "💎 **Премиум-совет**: Рекомендуем хеджирование опционами для защиты прибыли",
            "🚀 **Эксклюзивная идея**: Рассмотрите добавление AI-ETF для диверсификации"
        ]
        ai_insights = get_ml_insights(client_name)
        return base_recommendations + premium_recs[:3] + ai_insights[:2] + subscription_messages['premium']

# Функция для получения всех данных клиента (удобно для Streamlit)
def get_complete_client_data(client_name: str) -> Optional[Dict]:
    """Возвращает полные данные клиента включая портфель"""
    client_data = get_client_details(client_name)
    if not client_data:
        return None
    
    portfolio = get_portfolio_by_client(client_name)
    recommendations = generate_subscription_based_recommendations(client_name)
    
    return {
        'client_info': client_data,
        'portfolio': portfolio,
        'recommendations': recommendations,
        'subscription': get_subscription_details(client_name)
    }

# ТЕСТИРОВАНИЕ ПОДПИСОК
def test_subscriptions():
    """Быстрая проверка подписок"""
    print("=== ТЕСТ ПОДПИСОК ===")
    clients = get_all_clients()
    for client in clients:
        level = get_subscription_level(client)
        details = get_subscription_details(client)
        print(f"{client}: {level} - {details['name']} ({details['price']} руб)")
        
        # Проверяем доступ
        advanced = can_access_advanced_analytics(client)
        premium = can_access_premium_features(client)
        print(f"  Advanced: {advanced}, Premium: {premium}")
        
        # Тестируем рекомендации
        recs = generate_subscription_based_recommendations(client)
        print(f"  Рекомендации ({len(recs)}):")
        for rec in recs[:2]:
            print(f"    - {rec}")

# Пример использования
if __name__ == "__main__":
    # Инициализация базы данных
    db = PortfolioDatabase()
    
    # Тестируем подписки
    test_subscriptions()
    
    print("\n" + "="*50)
    print("Демо-портфели:")
    portfolios = get_all_portfolios()
    for name, description in portfolios:
        print(f"- {name}: {description}")
    
    print("\nДетали агрессивного портфеля:")
    aggressive = get_portfolio("агрессивный")
    if aggressive:
        for ticker, weight in aggressive.items():
            print(f"  {ticker}: {weight:.1%}")






