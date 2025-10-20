# app.py - полностью адаптивная версия С ГРАФИКАМИ И ВИЗУАЛИЗАЦИЯМИ

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
            'historical_data': self.generate_historical_data(),
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
    
    def generate_historical_data(self) -> pd.DataFrame:
        """Генерация исторических данных за 10 лет"""
        dates = pd.date_range(start='2014-01-01', end='2024-01-01', freq='M')
        np.random.seed(sum(ord(c) for c in self.client_name))
        
        # Генерируем реалистичные доходности в зависимости от типа портфеля
        portfolio_type_effects = {
            'агрессивный': {'mean': 0.012, 'std': 0.06, 'crisis_effect': -0.35},
            'сбалансированный': {'mean': 0.008, 'std': 0.035, 'crisis_effect': -0.20},
            'доходный': {'mean': 0.006, 'std': 0.025, 'crisis_effect': -0.15},
            'ультра-консервативный': {'mean': 0.004, 'std': 0.015, 'crisis_effect': -0.08}
        }
        
        # Базовые параметры (сбалансированный портфель по умолчанию)
        params = portfolio_type_effects.get('сбалансированный', portfolio_type_effects['сбалансированный'])
        
        monthly_returns = np.random.normal(params['mean'], params['std'], len(dates))
        
        # Добавляем реалистичные кризисы
        crisis_periods = [
            ('2015-07-01', '2016-02-01', -0.18),  # Кризис 2015-2016
            ('2018-09-01', '2018-12-01', -0.12),  # Коррекция 2018
            ('2020-02-01', '2020-04-01', -0.25),  # COVID-19
            ('2022-01-01', '2022-10-01', -0.20)   # Геополитический кризис
        ]
        
        for crisis_start, crisis_end, crisis_strength in crisis_periods:
            mask = (dates >= pd.to_datetime(crisis_start)) & (dates <= pd.to_datetime(crisis_end))
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
    
    def generate_performance_charts(self) -> Dict:
        """Генерация данных для графиков производительности"""
        historical_data = self.generate_historical_data()
        
        # Расчет скользящих средних
        historical_data['MA_6'] = historical_data['Portfolio_Value'].rolling(window=6).mean()
        historical_data['MA_12'] = historical_data['Portfolio_Value'].rolling(window=12).mean()
        
        # Расчет просадок
        historical_data['Peak'] = historical_data['Portfolio_Value'].expanding().max()
        historical_data['Drawdown'] = (historical_data['Portfolio_Value'] - historical_data['Peak']) / historical_data['Peak'] * 100
        
        return {
            'historical_data': historical_data,
            'annual_returns': self.calculate_annual_returns(historical_data),
            'volatility_data': self.calculate_rolling_volatility(historical_data)
        }
    
    def calculate_annual_returns(self, data: pd.DataFrame) -> pd.DataFrame:
        """Расчет годовой доходности"""
        data['Year'] = data['Date'].dt.year
        annual_data = data.groupby('Year').agg({
            'Portfolio_Value': ['first', 'last']
        }).reset_index()
        
        annual_data.columns = ['Year', 'Start_Value', 'End_Value']
        annual_data['Annual_Return'] = (annual_data['End_Value'] / annual_data['Start_Value'] - 1) * 100
        
        return annual_data
    
    def calculate_rolling_volatility(self, data: pd.DataFrame) -> pd.DataFrame:
        """Расчет скользящей волатильности"""
        data['Rolling_Volatility_1Y'] = data['Monthly_Return'].rolling(window=12).std() * np.sqrt(12) * 100
        return data[['Date', 'Rolling_Volatility_1Y']].dropna()
    
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

# ОБНОВЛЕННЫЕ TOOLTIP'Ы ДЛЯ ПОКАЗАТЕЛЕЙ - БЕЗ "ВАШ РЕЗУЛЬТАТ"
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
    """,
    
    'beta': """
    📈 **Бета-коэффициент** - Чувствительность к рынку
    
    **Что показывает:** Насколько ваш портфель реагирует на движения рынка
    
    **Уровни риска:**
    • < 0 - движется против рынка (редко)
    • 0-0.8 - защитный портфель
    • 0.8-1.2 - как рынок
    • > 1.2 - агрессивный рост
    """,
    
    'max_drawdown': """
    📉 **Максимальная просадка** - Самые большие потери
    
    **Что показывает:** Самое сильное падение стоимости от пика до минимума
    
    **О чем говорит:**
    • < 10% - отличная защита
    • 10-20% - умеренный риск  
    • 20-30% - высокий риск
    • > 30% - экстремальный риск
    """,
    
    'annual_return': """
    💰 **Годовая доходность** - Прирост капитала за год
    
    **Что показывает:** Насколько выросла стоимость портфеля за год
    
    **Сравнение с инфляцией:**
    • < 5% - ниже инфляции (реальные потери)
    • 5-10% - защита от инфляции
    • 10-15% - хороший рост
    • > 15% - высокая доходность
    """,
    
    'annual_volatility': """
    ⚡ **Волатильность** - Размах колебаний стоимости
    
    **Что показывает:** Насколько сильно "скачет" цена вашего портфеля
    
    **Уровни стабильности:**
    • < 10% - очень стабильно
    • 10-20% - умеренная волатильность
    • 20-30% - высокая волатильность  
    • > 30% - экстремальные колебания
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
    """,
    
    'treynor_ratio': """
    🏆 **Коэффициент Трейнора** - Доходность за системный риск
    
    **Что показывает:** Насколько вы превосходите безрисковые вложения
    
    **Особенность:** Учитывает только рыночный риск (бету)
    
    **Интерпретация:** Чем выше - тем лучше используете рыночные возможности
    """,
    
    'm_squared': """
    📊 **М-квадрат** - Сравнение с эталоном
    
    **Что показывает:** Какой была бы доходность при риске как у рынка
    
    **Проще говоря:** "Если бы мой портфель имел такую же волатильность как S&P 500"
    """,
    
    'jensen_alpha': """
    α **Альфа Дженсена** - Навык управления
    
    **Что показывает:** Насколько вы умнее рынка благодаря выбору акций
    
    **Ключевой показатель:** Положительная альфа = вы добавляете реальную ценность
    
    **Оценка:**
    • > 0 - превосходите рынок
    • = 0 - как рынок  
    • < 0 - отстаете от рынка
    """,
    
    'parametric_var_95': """
    🛡️ **Value at Risk (95%)** - Максимальные потери в нормальный день
    
    **Что означает:** "С вероятностью 95% за день я не потеряю больше X%"
    
    **Простой пример:** VaR -2.5% = в 95% дней потери не превысят 2.5%
    """,
    
    'cvar_95': """
    ⚡ **Conditional VaR** - Средние потери в плохие дни
    
    **Что означает:** "В худшие 5% дней я в среднем теряю X%"
    
    **Важнее VaR:** Показывает реальную боль в кризис
    """,
    
    # ПРЕМИУМ ПОКАЗАТЕЛИ
    'modigliani_ratio': """
    💎 **Коэффициент Модильяни** - Золотой стандарт оценки
    
    **Что показывает:** Насколько ваш портфель эффективнее рынка при том же риске
    
    **Лучшая метрика:** Для прямого сравнения разных портфелей
    
    **Интерпретация:** +2.8% = ваш портфель на 2.8% лучше рынка
    """,
    
    'information_ratio': """
    🎯 **Information Ratio** - Стабильность outperformance
    
    **Что показывает:** Насколько стабильно вы обгоняете бенчмарк
    
    **Для кого важно:** Активным управляющим
    
    **Оценка:**
    • 0.0-0.2 - нестабильное превосходство
    • 0.2-0.5 - хорошая стабильность
    • > 0.5 - выдающаяся стабильность
    """,
    
    'tracking_error': """
    📏 **Tracking Error** - Отклонение от эталона
    
    **Что показывает:** Насколько ваш портфель отличается от индекса
    
    **Что означает:**
    • Низкий TE (~2%) - пассивная стратегия
    • Высокий TE (~8%) - активная стратегия
    """,
    
    'calmar_ratio': """
    ⚖️ **Коэффициент Калмара** - Доходность vs Максимальная боль
    
    **Что показывает:** Сколько доходности вы получаете за максимальную просадку
    
    **Для кого важно:** Долгосрочным инвесторам
    
    **Оценка:**
    • < 0.5 - низкая компенсация за риск
    • 0.5-1.0 - хорошая компенсация
    • > 1.0 - отличная компенсация
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

def display_metric_with_tooltip(label: str, value: str, metric_name: str):
    """Отображает метрику с tooltip'ом - УПРОЩЕННАЯ ВЕРСИЯ БЕЗ ЛИШНИХ ОКОШЕК"""
    col1, col2 = st.columns([4, 1])
    
    with col1:
        st.metric(label, value)
    
    with col2:
        # Просто отображаем tooltip без лишних оберток
        st.markdown(create_tooltip(metric_name), unsafe_allow_html=True)

# НОВЫЕ ФУНКЦИИ ДЛЯ ГРАФИКОВ
def create_historical_performance_chart(historical_data: pd.DataFrame, client_name: str):
    """Создает график исторической производительности портфеля"""
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
    
    # Скользящие средние
    fig.add_trace(go.Scatter(
        x=historical_data['Date'],
        y=historical_data['MA_6'],
        mode='lines',
        name='Скользящая средняя 6 мес',
        line=dict(color='#A23B72', width=1, dash='dot'),
        opacity=0.7
    ))
    
    fig.add_trace(go.Scatter(
        x=historical_data['Date'],
        y=historical_data['MA_12'],
        mode='lines',
        name='Скользящая средняя 12 мес',
        line=dict(color='#F18F01', width=1, dash='dash'),
        opacity=0.7
    ))
    
    # Область просадок
    fig.add_trace(go.Scatter(
        x=historical_data['Date'],
        y=historical_data['Peak'],
        fill=None,
        mode='lines',
        line=dict(color='rgba(255,0,0,0.1)'),
        showlegend=False
    ))
    
    fig.add_trace(go.Scatter(
        x=historical_data['Date'],
        y=historical_data['Portfolio_Value'],
        fill='tonexty',
        mode='lines',
        line=dict(color='rgba(255,0,0,0.1)'),
        name='Просадки',
        fillcolor='rgba(255,0,0,0.1)'
    ))
    
    fig.update_layout(
        title=f'📈 Историческая производительность портфеля {client_name} (10 лет)',
        xaxis_title='Дата',
        yaxis_title='Стоимость портфеля (рубли)',
        hovermode='x unified',
        height=500,
        showlegend=True,
        template='plotly_white'
    )
    
    # Форматирование осей
    fig.update_yaxis(tickformat=",.0f")
    fig.update_xaxis(rangeslider_visible=False)
    
    return fig

def create_returns_volatility_chart(performance_data: Dict):
    """Создает комбинированный график доходности и волатильности"""
    historical_data = performance_data['historical_data']
    volatility_data = performance_data['volatility_data']
    
    fig = go.Figure()
    
    # График месячной доходности (столбцы)
    colors = ['red' if x < 0 else 'green' for x in historical_data['Monthly_Return'] * 100]
    
    fig.add_trace(go.Bar(
        x=historical_data['Date'],
        y=historical_data['Monthly_Return'] * 100,
        name='Месячная доходность %',
        marker_color=colors,
        opacity=0.6,
        yaxis='y1'
    ))
    
    # График волатильности (линия)
    fig.add_trace(go.Scatter(
        x=volatility_data['Date'],
        y=volatility_data['Rolling_Volatility_1Y'],
        mode='lines',
        name='Волатильность (12 мес) %',
        line=dict(color='purple', width=2),
        yaxis='y2'
    ))
    
    fig.update_layout(
        title='📊 Месячная доходность и волатильность портфеля',
        xaxis_title='Дата',
        yaxis=dict(
            title='Доходность (%)',
            titlefont=dict(color='green'),
            tickfont=dict(color='green')
        ),
        yaxis2=dict(
            title='Волатильность (%)',
            titlefont=dict(color='purple'),
            tickfont=dict(color='purple'),
            anchor='x',
            overlaying='y',
            side='right'
        ),
        hovermode='x unified',
        height=400,
        showlegend=True,
        template='plotly_white'
    )
    
    return fig

def create_drawdown_chart(historical_data: pd.DataFrame):
    """Создает график просадок портфеля"""
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
        hovermode='x unified',
        height=350,
        showlegend=False,
        template='plotly_white',
        yaxis=dict(autorange='reversed')  # Инвертируем ось Y для просадок
    )
    
    return fig

def create_annual_returns_chart(annual_data: pd.DataFrame):
    """Создает график годовой доходности"""
    colors = ['red' if x < 0 else 'green' for x in annual_data['Annual_Return']]
    
    fig = go.Figure()
    
    fig.add_trace(go.Bar(
        x=annual_data['Year'],
        y=annual_data['Annual_Return'],
        name='Годовая доходность',
        marker_color=colors,
        text=annual_data['Annual_Return'].round(1).astype(str) + '%',
        textposition='auto',
        hovertemplate='<b>%{x}</b><br>Доходность: %{y:.1f}%<extra></extra>'
    ))
    
    # Линия среднего значения
    mean_return = annual_data['Annual_Return'].mean()
    fig.add_hline(y=mean_return, line_dash="dash", line_color="blue", 
                  annotation_text=f"Среднее: {mean_return:.1f}%")
    
    fig.update_layout(
        title='📅 Годовая доходность портфеля',
        xaxis_title='Год',
        yaxis_title='Доходность (%)',
        height=400,
        showlegend=False,
        template='plotly_white'
    )
    
    return fig

def create_performance_summary_cards(historical_data: pd.DataFrame, annual_data: pd.DataFrame):
    """Создает карточки с ключевыми показателями производительности"""
    current_value = historical_data['Portfolio_Value'].iloc[-1]
    initial_value = historical_data['Portfolio_Value'].iloc[0]
    total_return = (current_value / initial_value - 1) * 100
    
    # Максимальная просадка
    max_drawdown = historical_data['Drawdown'].min()
    
    # Лучший и худший год
    best_year = annual_data.loc[annual_data['Annual_Return'].idxmax()]
    worst_year = annual_data.loc[annual_data['Annual_Return'].idxmin()]
    
    # Волатильность
    volatility = historical_data['Monthly_Return'].std() * np.sqrt(12) * 100
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric(
            "Общая доходность (10 лет)",
            f"{total_return:.1f}%",
            f"₽{current_value:,.0f}"
        )
    
    with col2:
        st.metric(
            "Максимальная просадка",
            f"{max_drawdown:.1f}%"
        )
    
    with col3:
        st.metric(
            "Лучший год",
            f"{best_year['Annual_Return']:.1f}%",
            f"{int(best_year['Year'])}"
        )
    
    with col4:
        st.metric(
            "Средняя волатильность",
            f"{volatility:.1f}%"
        )

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

# CSS ДЛЯ TOOLTIP'ОВ - УПРОЩЕННАЯ ВЕРСИЯ БЕЗ КВАДРАТИКОВ
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

/* Убираем все лишние отступы и обертки */
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
    """Создает метрики для портфеля с учетом уровня подписки И ПРОФИЛЯ КЛИЕНТА"""
    portfolio_type = client_data['portfolio_type']
    
    # Базовые метрики для всех - ТЕПЕРЬ СООТВЕТСТВУЮТ ПРОФИЛЮ
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
    
    # Добавляем продвинутые метрики для advanced и premium - ТЕПЕРЬ СООТВЕТСТВУЮТ ПРОФИЛЮ
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
    
    # Добавляем премиум метрики только для premium - ТЕПЕРЬ СООТВЕТСТВУЮТ ПРОФИЛЮ
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
        display_advanced_efficiency_metrics(results, subscription_level, client_data)
        
        # Продвинутые метрики рисков
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

def display_advanced_efficiency_metrics(results: Dict, subscription_level: str, client_data: Dict):
    """Отображение продвинутых метрик эффективности СООТВЕТСТВУЮЩИХ ПРОФИЛЮ"""
    if subscription_level not in ['advanced', 'premium']:
        return
    
    st.subheader("🎯 Продвинутые метрики эффективности")
    
    # Получаем метрики, соответствующие профилю клиента
    portfolio_metrics = create_portfolio_metrics(client_data, {}, subscription_level)
    
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

def display_historical_performance(results: Dict, client_name: str):
    """Отображение исторической производительности портфеля"""
    if not results.get('performance_charts'):
        return
    
    st.subheader("📈 Историческая производительность (10 лет)")
    
    performance_data = results['performance_charts']
    historical_data = performance_data['historical_data']
    annual_data = performance_data['annual_returns']
    
    # Карточки с ключевыми показателями
    create_performance_summary_cards(historical_data, annual_data)
    
    # Основной график производительности
    st.plotly_chart(
        create_historical_performance_chart(historical_data, client_name),
        use_container_width=True
    )
    
    # Дополнительные графики в колонках
    col1, col2 = st.columns(2)
    
    with col1:
        st.plotly_chart(
            create_returns_volatility_chart(performance_data),
            use_container_width=True
        )
    
    with col2:
        st.plotly_chart(
            create_drawdown_chart(historical_data),
            use_container_width=True
        )
    
    # Годовая доходность
    st.plotly_chart(
        create_annual_returns_chart(annual_data),
        use_container_width=True
    )

def dashboard_page():
    """Адаптивная панель управления С ОБНОВЛЕННЫМИ ТАРИФАМИ И ГРАФИКАМИ"""
    
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
    
    # 4. ИСТОРИЧЕСКАЯ ПРОИЗВОДИТЕЛЬНОСТЬ С ГРАФИКАМИ
    st.markdown("---")
    
    # Запускаем анализ для получения исторических данных
    with st.spinner("📊 Загружаем исторические данные..."):
        analyzer = AdvancedPortfolioAnalysis(portfolio_dict, current_client)
        results = analyzer.comprehensive_analysis()
    
    if results and results.get('performance_charts'):
        display_historical_performance(results, current_client)
    
    # 5. Рекомендации AI - РАЗНЫЕ ДЛЯ РАЗНЫХ ПОДПИСОК
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

# database.py остается без изменений (используем предыдущую версию)








