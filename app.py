# app.py - АДАПТИВНАЯ ВЕРСИЯ С УЛУЧШЕННЫМ ВИЗУАЛОМ
# СОХРАНЕНА ВСЯ ИСХОДНАЯ ЛОГИКА И ФУНКЦИОНАЛ

import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
from datetime import datetime, timedelta
import hashlib
from typing import Dict, List, Optional, Tuple

# =============================================
# ВИЗУАЛЬНЫЕ УЛУЧШЕНИЯ - ТОЛЬКО CSS
# =============================================

def setup_modern_design():
    """Настройка современного дизайна без изменения логики"""
    st.set_page_config(
        page_title="ЮниВест - AI Советник",
        page_icon="📊",
        layout="wide",
        initial_sidebar_state="expanded"
    )
    
    # ИНЪЕКТИМ КРАСИВЫЕ СТИЛИ
    st.markdown("""
    <style>
    /* СОВРЕМЕННЫЙ ДИЗАЙН БЕЗ ИЗМЕНЕНИЯ ЛОГИКИ */
    
    /* Градиентные заголовки */
    .modern-main-header {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 2.5rem 2rem;
        border-radius: 20px;
        color: white;
        margin-bottom: 2rem;
        text-align: center;
        box-shadow: 0 10px 30px rgba(0,0,0,0.15);
    }
    
    .modern-section-header {
        background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
        color: white;
        padding: 1.2rem 1.5rem;
        border-radius: 15px;
        margin: 2.5rem 0 1.5rem 0;
        font-weight: 700;
        font-size: 1.3em;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
    }
    
    /* Карточки метрик с анимацией */
    .modern-metric-card {
        background: white;
        padding: 1.5rem;
        border-radius: 15px;
        box-shadow: 0 4px 20px rgba(0,0,0,0.08);
        border-left: 5px solid #667eea;
        transition: all 0.3s ease;
        margin-bottom: 1rem;
        height: 100%;
    }
    
    .modern-metric-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 8px 30px rgba(0,0,0,0.15);
    }
    
    /* Улучшенные бейджи подписок */
    .modern-subscription-badge {
        padding: 10px 20px;
        border-radius: 25px;
        font-weight: bold;
        font-size: 0.85em;
        text-align: center;
        display: inline-block;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
    }
    
    .modern-badge-basic { 
        background: linear-gradient(135deg, #11998e, #38ef7d); 
        color: white; 
    }
    
    .modern-badge-advanced { 
        background: linear-gradient(135deg, #fc466b, #3f5efb); 
        color: white; 
    }
    
    .modern-badge-premium { 
        background: linear-gradient(135deg, #ffd700, #ff8c00); 
        color: black; 
    }
    
    /* Анимированные кнопки */
    .stButton button {
        border-radius: 12px;
        font-weight: 600;
        transition: all 0.3s ease;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
    }
    
    .stButton button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(0,0,0,0.15);
    }
    
    /* Улучшенные тултипы */
    .tooltip-modern {
        background: #2d3748 !important;
        border-radius: 12px !important;
        border: 2px solid #4a5568 !important;
        box-shadow: 0 10px 30px rgba(0,0,0,0.25) !important;
        font-size: 0.9em !important;
    }
    
    /* Красивые графики */
    .plotly-graph-div {
        border-radius: 15px;
        box-shadow: 0 4px 20px rgba(0,0,0,0.1);
    }
    
    /* Улучшенные секции */
    .modern-collapsible {
        background: white;
        border-radius: 15px;
        padding: 1.5rem;
        margin: 1.5rem 0;
        box-shadow: 0 4px 20px rgba(0,0,0,0.08);
        border: 1px solid #e0e0e0;
    }
    
    /* Адаптивность сохраняется */
    @media (max-width: 768px) {
        .modern-main-header {
            padding: 2rem 1.5rem;
            border-radius: 15px;
        }
        .modern-metric-card {
            padding: 1.2rem;
        }
    }
    
    /* Улучшенный сайдбар */
    .css-1d391kg {
        background: linear-gradient(180deg, #f8f9fa 0%, #e9ecef 100%);
    }
    
    /* Красивые уведомления */
    .stAlert {
        border-radius: 12px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
    }
    </style>
    """, unsafe_allow_html=True)

# =============================================
# ВАШ ИСХОДНЫЙ КЛАСС АНАЛИЗА ПОРТФЕЛЯ - ПОЛНОСТЬЮ СОХРАНЕН
# =============================================

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
        portfolio_type = self._get_portfolio_type()
        
        metrics_map = {
            'агрессивный': {
                'annual_return': 0.18, 'annual_volatility': 0.32, 'sharpe_ratio': 0.56,
                'max_drawdown': -0.40, 'beta': 1.25, 'current_value': 1500000, 'total_return': 0.85
            },
            'сбалансированный': {
                'annual_return': 0.095, 'annual_volatility': 0.14, 'sharpe_ratio': 0.68,
                'max_drawdown': -0.20, 'beta': 0.95, 'current_value': 1200000, 'total_return': 0.45
            },
            'доходный': {
                'annual_return': 0.078, 'annual_volatility': 0.11, 'sharpe_ratio': 0.71,
                'max_drawdown': -0.15, 'beta': 0.75, 'current_value': 1800000, 'total_return': 0.32
            },
            'ультра-консервативный': {
                'annual_return': 0.045, 'annual_volatility': 0.05, 'sharpe_ratio': 0.90,
                'max_drawdown': -0.08, 'beta': 0.35, 'current_value': 2200000, 'total_return': 0.18
            }
        }
        
        return metrics_map.get(portfolio_type, metrics_map['сбалансированный'])
    
    def _get_portfolio_type(self) -> str:
        """Определяет тип портфеля на основе активов"""
        aggressive_keywords = ['TSLA', 'NVDA', 'AMD', 'ARKK', 'BTC', 'ETH']
        conservative_keywords = ['BND', 'GOVT', 'SHY', 'Cash']
        
        aggressive_score = sum(weight for asset, weight in self.portfolio_dict.items() 
                             if any(keyword in asset for keyword in aggressive_keywords))
        conservative_score = sum(weight for asset, weight in self.portfolio_dict.items() 
                               if any(keyword in asset for keyword in conservative_keywords))
        
        if aggressive_score > 0.4:
            return 'агрессивный'
        elif conservative_score > 0.5:
            return 'ультра-консервативный'
        elif conservative_score > 0.3:
            return 'доходный'
        else:
            return 'сбалансированный'
    
    def calculate_advanced_risk_metrics(self) -> Dict:
        """Расширенный анализ рисков для продвинутых пользователей"""
        portfolio_type = self._get_portfolio_type()
        
        risk_metrics_map = {
            'агрессивный': {
                'parametric_var_95': -0.085, 'parametric_var_99': -0.125,
                'cvar_95': -0.118, 'cvar_99': -0.155,
                'downside_deviation': 0.15, 'worst_day': -0.08, 'worst_month': -0.22,
                'value_at_risk_1m': -127500, 'expected_shortfall': -187000,
                'stress_test_2008': -0.55, 'stress_test_covid': -0.48
            },
            'сбалансированный': {
                'parametric_var_95': -0.045, 'parametric_var_99': -0.065,
                'cvar_95': -0.058, 'cvar_99': -0.075,
                'downside_deviation': 0.08, 'worst_day': -0.05, 'worst_month': -0.12,
                'value_at_risk_1m': -54000, 'expected_shortfall': -78000,
                'stress_test_2008': -0.35, 'stress_test_covid': -0.28
            },
            'доходный': {
                'parametric_var_95': -0.035, 'parametric_var_99': -0.048,
                'cvar_95': -0.042, 'cvar_99': -0.055,
                'downside_deviation': 0.06, 'worst_day': -0.04, 'worst_month': -0.09,
                'value_at_risk_1m': -63000, 'expected_shortfall': -89000,
                'stress_test_2008': -0.25, 'stress_test_covid': -0.20
            },
            'ультра-консервативный': {
                'parametric_var_95': -0.015, 'parametric_var_99': -0.022,
                'cvar_95': -0.018, 'cvar_99': -0.025,
                'downside_deviation': 0.03, 'worst_day': -0.02, 'worst_month': -0.05,
                'value_at_risk_1m': -33000, 'expected_shortfall': -44000,
                'stress_test_2008': -0.12, 'stress_test_covid': -0.10
            }
        }
        
        return risk_metrics_map.get(portfolio_type, risk_metrics_map['сбалансированный'])
    
    def calculate_efficiency_metrics(self) -> Dict:
        """Метрики эффективности для продвинутых и премиум пользователей"""
        portfolio_type = self._get_portfolio_type()
        
        efficiency_map = {
            'агрессивный': {
                'sharpe_ratio': 0.56, 'sortino_ratio': 0.72, 'beta': 1.25,
                'treynor_ratio': 0.144, 'm_squared': 0.038, 'jensen_alpha': 0.028,
                'modigliani_ratio': 0.035, 'information_ratio': 0.18, 'tracking_error': 0.068,
                'downside_deviation': 0.15, 'calmar_ratio': 0.45
            },
            'сбалансированный': {
                'sharpe_ratio': 0.68, 'sortino_ratio': 0.85, 'beta': 0.95,
                'treynor_ratio': 0.100, 'm_squared': 0.025, 'jensen_alpha': 0.015,
                'modigliani_ratio': 0.022, 'information_ratio': 0.12, 'tracking_error': 0.045,
                'downside_deviation': 0.08, 'calmar_ratio': 0.48
            },
            'доходный': {
                'sharpe_ratio': 0.71, 'sortino_ratio': 0.88, 'beta': 0.75,
                'treynor_ratio': 0.104, 'm_squared': 0.022, 'jensen_alpha': 0.012,
                'modigliani_ratio': 0.018, 'information_ratio': 0.10, 'tracking_error': 0.038,
                'downside_deviation': 0.06, 'calmar_ratio': 0.52
            },
            'ультра-консервативный': {
                'sharpe_ratio': 0.90, 'sortino_ratio': 1.05, 'beta': 0.35,
                'treynor_ratio': 0.129, 'm_squared': 0.018, 'jensen_alpha': 0.008,
                'modigliani_ratio': 0.012, 'information_ratio': 0.08, 'tracking_error': 0.025,
                'downside_deviation': 0.03, 'calmar_ratio': 0.56
            }
        }
        
        return efficiency_map.get(portfolio_type, efficiency_map['сбалансированный'])
    
    def analyze_portfolio_quality(self) -> Dict:
        """Анализ качества портфеля"""
        portfolio_type = self._get_portfolio_type()
        
        quality_map = {
            'агрессивный': {
                'diversification_score': 0.65, 'concentration_risk': 'высокий',
                'asset_allocation_score': 0.75, 'liquidity_score': 0.85
            },
            'сбалансированный': {
                'diversification_score': 0.82, 'concentration_risk': 'умеренный', 
                'asset_allocation_score': 0.88, 'liquidity_score': 0.92
            },
            'доходный': {
                'diversification_score': 0.78, 'concentration_risk': 'низкий',
                'asset_allocation_score': 0.85, 'liquidity_score': 0.90
            },
            'ультра-консервативный': {
                'diversification_score': 0.70, 'concentration_risk': 'очень низкий',
                'asset_allocation_score': 0.92, 'liquidity_score': 0.95
            }
        }
        
        base_quality = quality_map.get(portfolio_type, quality_map['сбалансированный'])
        base_quality.update({
            'correlation_matrix': self.generate_correlation_matrix(),
            'sector_diversification': self.analyze_sector_diversification()
        })
        
        return base_quality
    
    def benchmark_comparison(self) -> Dict:
        """Сравнение с эталонными индексами"""
        portfolio_type = self._get_portfolio_type()
        
        benchmark_map = {
            'агрессивный': {
                'sp500_return': 0.121, 'nasdaq_return': 0.183, 'rts_return': 0.085,
                'outperformance_sp500': 0.059, 'outperformance_nasdaq': -0.003,
                'volatility_comparison': 'выше рынка', 'percentile_ranking': 0.72
            },
            'сбалансированный': {
                'sp500_return': 0.121, 'nasdaq_return': 0.183, 'rts_return': 0.085,
                'outperformance_sp500': -0.026, 'outperformance_nasdaq': -0.088,
                'volatility_comparison': 'ниже рынка', 'percentile_ranking': 0.58
            },
            'доходный': {
                'sp500_return': 0.121, 'nasdaq_return': 0.183, 'rts_return': 0.085,
                'outperformance_sp500': -0.043, 'outperformance_nasdaq': -0.105,
                'volatility_comparison': 'значительно ниже', 'percentile_ranking': 0.45
            },
            'ультра-консервативный': {
                'sp500_return': 0.121, 'nasdaq_return': 0.183, 'rts_return': 0.085,
                'outperformance_sp500': -0.076, 'outperformance_nasdaq': -0.138,
                'volatility_comparison': 'минимальная', 'percentile_ranking': 0.35
            }
        }
        
        return benchmark_map.get(portfolio_type, benchmark_map['сбалансированный'])
    
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
        portfolio_type = self._get_portfolio_type()
        
        sector_map = {
            'агрессивный': {
                'Технологии': 0.45, 'Финансы': 0.15, 'Здравоохранение': 0.12,
                'Потребительские товары': 0.08, 'Энергетика': 0.06,
                'Недвижимость': 0.04, 'Материалы': 0.03, 'Крипто': 0.07
            },
            'сбалансированный': {
                'Технологии': 0.25, 'Финансы': 0.18, 'Здравоохранение': 0.15,
                'Потребительские товары': 0.12, 'Энергетика': 0.08,
                'Недвижимость': 0.10, 'Материалы': 0.06, 'Облигации': 0.06
            },
            'доходный': {
                'Технологии': 0.15, 'Финансы': 0.20, 'Здравоохранение': 0.18,
                'Потребительские товары': 0.16, 'Энергетика': 0.12,
                'Недвижимость': 0.10, 'Коммунальные услуги': 0.09
            },
            'ультра-консервативный': {
                'Облигации': 0.65, 'Денежные средства': 0.15, 'Защитные акции': 0.12,
                'Золото': 0.08
            }
        }
        
        return sector_map.get(portfolio_type, sector_map['сбалансированный'])
    
    def generate_performance_charts(self) -> Dict:
        """Генерация данных для графиков производительности"""
        historical_data = self.generate_historical_data()
        
        if historical_data.empty:
            return {}
        
        historical_data['MA_6'] = historical_data['Portfolio_Value'].rolling(window=6, min_periods=1).mean()
        historical_data['MA_12'] = historical_data['Portfolio_Value'].rolling(window=12, min_periods=1).mean()
        
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
            
            portfolio_type = self._get_portfolio_type()
            params_map = {
                'агрессивный': {'mean': 0.012, 'std': 0.055},
                'сбалансированный': {'mean': 0.008, 'std': 0.035},
                'доходный': {'mean': 0.006, 'std': 0.028},
                'ультра-консервативный': {'mean': 0.004, 'std': 0.015}
            }
            
            params = params_map.get(portfolio_type, params_map['сбалансированный'])
            monthly_returns = np.random.normal(params['mean'], params['std'], len(dates))
            
            crisis_periods = [
                ('2015-07-01', '2016-02-01', -0.18),
                ('2018-09-01', '2018-12-01', -0.12),
                ('2020-02-01', '2020-04-01', -0.25),
                ('2022-01-01', '2022-10-01', -0.20)
            ]
            
            for crisis_start, crisis_end, crisis_strength in crisis_periods:
                mask = (dates >= pd.to_datetime(crisis_start)) & (dates <= pd.to_datetime(crisis_end))
                if mask.any():
                    monthly_returns[mask] += np.random.normal(crisis_strength, 0.02, mask.sum())
            
            initial_investment = 1000000
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
            return pd.DataFrame()
        
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
            return pd.DataFrame()
    
    def calculate_rolling_volatility(self, data: pd.DataFrame) -> pd.DataFrame:
        """Расчет скользящей волатильности"""
        if data.empty:
            return pd.DataFrame()
        
        try:
            data = data.copy()
            data['Rolling_Volatility_1Y'] = data['Monthly_Return'].rolling(window=12, min_periods=1).std() * np.sqrt(12) * 100
            return data[['Date', 'Rolling_Volatility_1Y']].dropna()
            
        except Exception as e:
            st.error(f"Ошибка расчета волатильности: {e}")
            return pd.DataFrame()
    
    def generate_ai_insights(self) -> List[str]:
        """AI инсайты для премиум пользователей"""
        portfolio_type = self._get_portfolio_type()
        
        insights_map = {
            'агрессивный': [
                "🤖 **ML-анализ**: Высокая чувствительность к технологическому сектору",
                "📈 **Паттерны**: Сильная волатильность в периоды новостей ФРС",
                "⚡ **Волатильность**: Ожидается снижение на 12% после выборов",
                "🎯 **Оптимизация**: Ребалансировка может увеличить Sharpe на 0.15"
            ],
            'сбалансированный': [
                "🤖 **ML-анализ**: Портфель показывает устойчивость к рыночным шокам",
                "📈 **Паттерны**: Обнаружена положительная сезонность в Q4",
                "⚡ **Волатильность**: Ожидается снижение волатильности на 8%",
                "🎯 **Оптимизация**: Добавление REIT может увеличить доходность на 1.2%"
            ],
            'доходный': [
                "🤖 **ML-анализ**: Стабильный дивидендный поток",
                "📈 **Паттерны**: Низкая корреляция с технологическим сектором",
                "⚡ **Волатильность**: Минимальные колебания в кризисные периоды",
                "🎯 **Оптимизация**: Реинвестирование дивидендов увеличит CAGR на 0.8%"
            ],
            'ультра-консервативный': [
                "🤖 **ML-анализ**: Идеальная защита капитала в кризисы",
                "📈 **Паттерны**: Предсказуемая доходность в любых условиях",
                "⚡ **Волатильность**: Почти нулевая чувствительность к рынку",
                "🎯 **Оптимизация**: Текущая структура оптимальна для целей"
            ]
        }
        
        return insights_map.get(portfolio_type, insights_map['сбалансированный'])
    
    def generate_detailed_recommendations(self) -> List[str]:
        """Детальные рекомендации"""
        portfolio_type = self._get_portfolio_type()
        
        recommendations_map = {
            'агрессивный': [
                "🎯 **Тактическая оптимизация**: Увеличить долю защитных активов на 5%",
                "📊 **Риск-менеджмент**: Установить стоп-лосс на уровне -12% для высоковолатильных активов",
                "🔄 **Ребалансировка**: Рекомендуется ежемесячный мониторинг",
                "🌍 **Диверсификация**: Добавить exposure к сырьевым активам"
            ],
            'сбалансированный': [
                "🎯 **Тактическая оптимизация**: Балансировать между growth и value",
                "📊 **Риск-менеджмент**: Диверсифицировать по географическим регионам",
                "🔄 **Ребалансировка**: Рекомендуется ежеквартальная ребалансировка",
                "🌍 **Диверсификация**: Добавить exposure к развивающимся рынкам"
            ],
            'доходный': [
                "🎯 **Тактическая оптимизация**: Фокус на дивидендных аристократах",
                "📊 **Риск-менеджмент**: Мониторинг дивидендной устойчивости",
                "🔄 **Ребалансировка**: Полугодовая проверка дивидендных выплат",
                "🌍 **Диверсификация**: Добавить инфраструктурные активы"
            ],
            'ультра-консервативный': [
                "🎯 **Тактическая оптимизация**: Поддержание ликвидности",
                "📊 **Риск-менеджмент**: Фокус на кредитное качество облигаций",
                "🔄 **Ребалансировка**: Годовая проверка достаточности",
                "🌍 **Диверсификация**: Рассмотреть индексированные облигации"
            ]
        }
        
        return recommendations_map.get(portfolio_type, recommendations_map['сбалансированный'])

# =============================================
# ВАШИ ИСХОДНЫЕ TOOLTIP'Ы - ПОЛНОСТЬЮ СОХРАНЕНЫ
# =============================================

TOOLTIPS = {
    'sharpe_ratio': "📊 **Коэффициент Шарпа**\n\nПоказывает, насколько хорошо доходность компенсирует риск. Чем выше - тем лучше баланс между риском и доходностью.\n\n• <1.0 - можно улучшить\n• 1.0-2.0 - хорошо\n• >2.0 - отлично",
    
    'beta': "📈 **Бета-коэффициент**\n\nЧувствительность портфеля к рынку:\n\n• <0 - движется против рынка\n• 0-1 - менее волатилен чем рынок\n• 1 - как рынок\n• >1 - более волатилен чем рынок",
    
    'max_drawdown': "📉 **Максимальная просадка**\n\nСамое большое падение стоимости портфеля от пика до минимума. Показывает ваш худший сценарий.",
    
    'annual_return': "💰 **Годовая доходность**\n\nСредняя доходность в годовом выражении. Учитывает сложный процент.",
    
    'annual_volatility': "⚡ **Волатильность**\n\nМера риска - насколько сильно 'колеблется' стоимость портфеля. Чем выше - тем непредсказуемее результат.",
    
    'sortino_ratio': "🎯 **Коэффициент Сортино**\n\nКак Шарп, но учитывает только 'плохую' волатильность (убытки). Более точный для оценки риска.",
    
    'treynor_ratio': "🏆 **Коэффициент Трейнора**\n\nНасколько вы превосходите безрисковые вложения (например, гособлигации). Чем выше - тем лучше.",
    
    'm_squared': "📊 **М-квадрат**\n\nСравнивает эффективность с поправкой на риск. Помогает выбрать между разными портфелями.",
    
    'jensen_alpha': "α **Альфа Дженсена**\n\nПоказывает, насколько ваша стратегия лучше пассивного инвестирования. Положительная альфа - вы молодец!",
    
    'parametric_var_95': "🛡️ **Value at Risk (95%)**\n\nМаксимальные потери с вероятностью 95%. 'В худшем случае вы потеряете не более X%'",
    
    'cvar_95': "⚡ **Conditional VaR**\n\nСредние потери в тех 5% худших сценариев. 'Если уже случилось плохое, то в среднем потеряете X%'",
    
    'modigliani_ratio': "💎 **Коэффициент Модильяни**\n\nНасколько ваш портфель эффективнее рынка при том же уровне риска. Золотой стандарт оценки.",
    
    'information_ratio': "🎯 **Information Ratio**\n\nКачество активного управления. Показывает стабильность превосходства над рынком.",
    
    'tracking_error': "📏 **Tracking Error**\n\nНасколько ваш портфель отклоняется от эталона (например, S&P500). Мера 'активности' управления.",
    
    'calmar_ratio': "⚖️ **Коэффициент Калмара**\n\nДоходность относительно максимальной просадка. Особенно важен для долгосрочных инвесторов."
}

# =============================================
# ВАШИ ИСХОДНЫЕ ФУНКЦИИ ОТОБРАЖЕНИЯ - ПОЛНОСТЬЮ СОХРАНЕНЫ
# =============================================

def display_metric_with_tooltip(label: str, value: str, metric_name: str):
    """Отображает метрику с tooltip'ом который работает при наведении"""
    col1, col2 = st.columns([4, 1])
    
    with col1:
        st.metric(label, value)
    
    with col2:
        tooltip_text = TOOLTIPS.get(metric_name, "Информация о показателе")
        st.markdown(f"""
        <div style="display: flex; align-items: center; justify-content: center; height: 100%;">
            <div class="tooltip">
                <span class="tooltip-icon">❓</span>
                <div class="tooltip-content tooltip-modern">
                    {tooltip_text}
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

# ВАШИ ФУНКЦИИ ДЛЯ ГРАФИКОВ (полностью сохранены)
def create_historical_performance_chart(historical_data: pd.DataFrame, client_name: str):
    """Создает график исторической производительности"""
    try:
        if historical_data.empty:
            return go.Figure()
        
        fig = go.Figure()
        
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
    """Создает график просадок"""
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
        
        max_drawdown = historical_data['Drawdown'].min()
        volatility = historical_data['Monthly_Return'].std() * np.sqrt(12) * 100
        
        # Адаптивная верстка для разных устройств
        if st.session_state.is_mobile:
            col1, col2 = st.columns(2)
            with col1:
                st.metric("Общая доходность", f"{total_return:.1f}%")
            with col2:
                st.metric("Текущая стоимость", f"₽{current_value:,.0f}")
            
            col3, col4 = st.columns(2)
            with col3:
                st.metric("Макс. просадка", f"{max_drawdown:.1f}%")
            with col4:
                st.metric("Волатильность", f"{volatility:.1f}%")
        else:
            col1, col2, col3, col4 = st.columns(4)
            with col1:
                st.metric("Общая доходность", f"{total_return:.1f}%")
            with col2:
                st.metric("Текущая стоимость", f"₽{current_value:,.0f}")
            with col3:
                st.metric("Макс. просадка", f"{max_drawdown:.1f}%")
            with col4:
                st.metric("Волатильность", f"{volatility:.1f}%")
            
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
        
        st.markdown('<div class="modern-section-header">📈 Историческая производительность (10 лет)</div>', unsafe_allow_html=True)
        
        create_performance_summary_cards(historical_data)
        
        st.plotly_chart(
            create_historical_performance_chart(historical_data, client_name),
            use_container_width=True
        )
        
        # Адаптивная верстка графиков
        if st.session_state.is_mobile:
            st.plotly_chart(
                create_returns_chart(historical_data),
                use_container_width=True
            )
            st.plotly_chart(
                create_drawdown_chart(historical_data),
                use_container_width=True
            )
        else:
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
        
        if not annual_data.empty:
            st.plotly_chart(
                create_annual_returns_chart(annual_data),
                use_container_width=True
            )
            
    except Exception as e:
        st.error(f"Ошибка отображения исторических данных: {e}")

# АДАПТИВНЫЕ ФУНКЦИИ ОТОБРАЖЕНИЯ (ваши функции полностью сохранены)
def display_collapsible_section(title: str, expanded: bool = True):
    """Создает адаптивную сворачиваемую секцию"""
    key = f"collapsible_{hash(title)}"
    
    if key not in st.session_state:
        st.session_state[key] = expanded
    
    # Адаптивный заголовок для мобильных устройств
    if st.session_state.is_mobile:
        col1, col2 = st.columns([5, 1])
    else:
        col1, col2 = st.columns([6, 1])
    
    with col1:
        st.markdown(f'<div class="modern-section-header">{title}</div>', unsafe_allow_html=True)
    
    with col2:
        button_label = "⬆️" if st.session_state[key] else "⬇️"
        if st.button(button_label, key=f"btn_{key}", use_container_width=True):
            st.session_state[key] = not st.session_state[key]
    
    return st.session_state[key]

def display_portfolio_analysis(results: Dict, subscription_level: str) -> None:
    """Адаптивное отображение анализа с разными уровнями доступа"""
    if not results:
        st.error("Нет данных для отображения")
        return
    
    metrics = results.get('basic_metrics', {})
    
    if not metrics:
        st.error("Отсутствуют базовые метрики")
        return
    
    # ОСНОВНЫЕ ПОКАЗАТЕЛИ
    if display_collapsible_section("📊 Основные показатели", expanded=True):
        if st.session_state.is_mobile:
            # Мобильная версия - 2 колонки
            col1, col2 = st.columns(2)
            with col1:
                display_metric_with_tooltip("Годовая доходность", f"{metrics.get('annual_return', 0):.1%}", 'annual_return')
                display_metric_with_tooltip("Коэффициент Шарпа", f"{metrics.get('sharpe_ratio', 0):.2f}", 'sharpe_ratio')
            with col2:
                display_metric_with_tooltip("Волатильность", f"{metrics.get('annual_volatility', 0):.1%}", 'annual_volatility')
                display_metric_with_tooltip("Макс. просадка", f"{metrics.get('max_drawdown', 0):.1%}", 'max_drawdown')
            
            col3, col4 = st.columns(2)
            with col3:
                display_metric_with_tooltip("Бета-коэффициент", f"{metrics.get('beta', 0):.2f}", 'beta')
                st.metric("Текущая стоимость", f"₽{metrics.get('current_value', 0):,}")
            with col4:
                st.metric("Общая доходность", f"{metrics.get('total_return', 0):.1%}")
                st.metric("Тип портфеля", results.get('portfolio_quality', {}).get('concentration_risk', 'Н/Д'))
        else:
            # Десктопная версия - 4 колонки
            col1, col2, col3, col4 = st.columns(4)
            with col1:
                display_metric_with_tooltip("Годовая доходность", f"{metrics.get('annual_return', 0):.1%}", 'annual_return')
            with col2:
                display_metric_with_tooltip("Волатильность", f"{metrics.get('annual_volatility', 0):.1%}", 'annual_volatility')
            with col3:
                display_metric_with_tooltip("Коэффициент Шарпа", f"{metrics.get('sharpe_ratio', 0):.2f}", 'sharpe_ratio')
            with col4:
                display_metric_with_tooltip("Макс. просадка", f"{metrics.get('max_drawdown', 0):.1%}", 'max_drawdown')
            
            col1, col2, col3, col4 = st.columns(4)
            with col1:
                display_metric_with_tooltip("Бета-коэффициент", f"{metrics.get('beta', 0):.2f}", 'beta')
            with col2:
                st.metric("Текущая стоимость", f"₽{metrics.get('current_value', 0):,}")
            with col3:
                st.metric("Общая доходность", f"{metrics.get('total_return', 0):.1%}")
            with col4:
                st.metric("Тип портфеля", results.get('portfolio_quality', {}).get('concentration_risk', 'Н/Д'))

def display_efficiency_metrics(results: Dict, subscription_level: str) -> None:
    """Адаптивное отображение метрик эффективности"""
    efficiency_metrics = results.get('efficiency_metrics', {})
    if not efficiency_metrics:
        return
    
    if display_collapsible_section("📈 Метрики эффективности", expanded=True):
        if st.session_state.is_mobile:
            col1, col2 = st.columns(2)
            with col1:
                display_metric_with_tooltip("Коэф. Шарпа", f"{efficiency_metrics.get('sharpe_ratio', 0):.2f}", 'sharpe_ratio')
                display_metric_with_tooltip("Бета", f"{efficiency_metrics.get('beta', 0):.2f}", 'beta')
            with col2:
                display_metric_with_tooltip("Коэф. Сортино", f"{efficiency_metrics.get('sortino_ratio', 0):.2f}", 'sortino_ratio')
                st.metric("Downside Dev", f"{efficiency_metrics.get('downside_deviation', 0):.2%}")
        else:
            col1, col2, col3, col4 = st.columns(4)
            with col1:
                display_metric_with_tooltip("Коэф. Шарпа", f"{efficiency_metrics.get('sharpe_ratio', 0):.2f}", 'sharpe_ratio')
            with col2:
                display_metric_with_tooltip("Коэф. Сортино", f"{efficiency_metrics.get('sortino_ratio', 0):.2f}", 'sortino_ratio')
            with col3:
                display_metric_with_tooltip("Бета", f"{efficiency_metrics.get('beta', 0):.2f}", 'beta')
            with col4:
                st.metric("Downside Dev", f"{efficiency_metrics.get('downside_deviation', 0):.2%}")
        
        # Продвинутые метрики
        if subscription_level in ['advanced', 'premium']:
            if st.session_state.is_mobile:
                col1, col2 = st.columns(2)
                with col1:
                    display_metric_with_tooltip("Коэф. Трейнора", f"{efficiency_metrics.get('treynor_ratio', 0):.3f}", 'treynor_ratio')
                    display_metric_with_tooltip("Альфа Дженсена", f"{efficiency_metrics.get('jensen_alpha', 0):.3f}", 'jensen_alpha')
                with col2:
                    display_metric_with_tooltip("М-квадрат", f"{efficiency_metrics.get('m_squared', 0):.3f}", 'm_squared')
                    display_metric_with_tooltip("Коэф. Калмара", f"{efficiency_metrics.get('calmar_ratio', 0):.2f}", 'calmar_ratio')
            else:
                col1, col2, col3, col4 = st.columns(4)
                with col1:
                    display_metric_with_tooltip("Коэф. Трейнора", f"{efficiency_metrics.get('treynor_ratio', 0):.3f}", 'treynor_ratio')
                with col2:
                    display_metric_with_tooltip("М-квадрат", f"{efficiency_metrics.get('m_squared', 0):.3f}", 'm_squared')
                with col3:
                    display_metric_with_tooltip("Альфа Дженсена", f"{efficiency_metrics.get('jensen_alpha', 0):.3f}", 'jensen_alpha')
                with col4:
                    display_metric_with_tooltip("Коэф. Калмара", f"{efficiency_metrics.get('calmar_ratio', 0):.2f}", 'calmar_ratio')

def display_advanced_risk_analysis(results: Dict, subscription_level: str) -> None:
    """Адаптивное отображение расширенного анализа рисков"""
    risk_metrics = results.get('risk_metrics', {})
    if not risk_metrics or subscription_level not in ['advanced', 'premium']:
        return
    
    if display_collapsible_section("🎯 Расширенный анализ рисков", expanded=True):
        if st.session_state.is_mobile:
            col1, col2 = st.columns(2)
            with col1:
                display_metric_with_tooltip("VaR (95%)", f"{risk_metrics.get('parametric_var_95', 0):.2%}", 'parametric_var_95')
                st.metric("VaR (99%)", f"{risk_metrics.get('parametric_var_99', 0):.2%}")
                st.metric("Downside Deviation", f"{risk_metrics.get('downside_deviation', 0):.2%}")
            with col2:
                display_metric_with_tooltip("CVaR (95%)", f"{risk_metrics.get('cvar_95', 0):.2%}", 'cvar_95')
                st.metric("CVaR (99%)", f"{risk_metrics.get('cvar_99', 0):.2%}")
                st.metric("Worst Day", f"{risk_metrics.get('worst_day', 0):.2%}")
        else:
            col1, col2, col3, col4 = st.columns(4)
            with col1:
                display_metric_with_tooltip("VaR (95%)", f"{risk_metrics.get('parametric_var_95', 0):.2%}", 'parametric_var_95')
            with col2:
                display_metric_with_tooltip("CVaR (95%)", f"{risk_metrics.get('cvar_95', 0):.2%}", 'cvar_95')
            with col3:
                st.metric("VaR (99%)", f"{risk_metrics.get('parametric_var_99', 0):.2%}")
            with col4:
                st.metric("CVaR (99%)", f"{risk_metrics.get('cvar_99', 0):.2%}")
            
            col1, col2, col3, col4 = st.columns(4)
            with col1:
                st.metric("Downside Deviation", f"{risk_metrics.get('downside_deviation', 0):.2%}")
            with col2:
                st.metric("Worst Day", f"{risk_metrics.get('worst_day', 0):.2%}")
            with col3:
                st.metric("Worst Month", f"{risk_metrics.get('worst_month', 0):.2%}")
            with col4:
                st.metric("Stress Test 2008", f"{risk_metrics.get('stress_test_2008', 0):.1%}")

def display_portfolio_quality(results: Dict, subscription_level: str) -> None:
    """Адаптивное отображение качества портфеля"""
    portfolio_quality = results.get('portfolio_quality', {})
    if not portfolio_quality or subscription_level not in ['advanced', 'premium']:
        return
    
    if display_collapsible_section("🏆 Качество портфеля", expanded=True):
        if st.session_state.is_mobile:
            col1, col2 = st.columns(2)
            with col1:
                st.metric("Оценка диверсификации", f"{portfolio_quality.get('diversification_score', 0):.0%}")
                st.metric("Ликвидность", f"{portfolio_quality.get('liquidity_score', 0):.0%}")
            with col2:
                st.metric("Распределение активов", f"{portfolio_quality.get('asset_allocation_score', 0):.0%}")
        else:
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("Оценка диверсификации", f"{portfolio_quality.get('diversification_score', 0):.0%}")
            with col2:
                st.metric("Распределение активов", f"{portfolio_quality.get('asset_allocation_score', 0):.0%}")
            with col3:
                st.metric("Ликвидность", f"{portfolio_quality.get('liquidity_score', 0):.0%}")
        
        correlation_matrix = portfolio_quality.get('correlation_matrix')
        if correlation_matrix is not None and not correlation_matrix.empty:
            st.subheader("📊 Матрица корреляций")
            fig = px.imshow(correlation_matrix, 
                           text_auto=True, 
                           aspect="auto",
                           color_continuous_scale='RdBu_r',
                           title="Корреляция между активами")
            st.plotly_chart(fig, use_container_width=True)

def display_premium_analytics(results: Dict, subscription_level: str) -> None:
    """Адаптивная премиум аналитика"""
    if subscription_level != 'premium':
        return
    
    if display_collapsible_section("💎 Премиум аналитика", expanded=True):
        ai_insights = results.get('ai_insights', [])
        if ai_insights:
            st.success("### 🤖 AI Инсайты")
            for insight in ai_insights:
                st.write(insight)
        
        comparative = results.get('comparative_analysis', {})
        if comparative:
            st.success("### 🏆 Сравнение с эталонами")
            if st.session_state.is_mobile:
                col1, col2 = st.columns(2)
                with col1:
                    st.metric("vs S&P 500", f"{comparative.get('outperformance_sp500', 0):.2%}")
                    st.metric("Percentile", f"{comparative.get('percentile_ranking', 0):.0%}")
                with col2:
                    st.metric("vs Nasdaq", f"{comparative.get('outperformance_nasdaq', 0):.2%}")
            else:
                col1, col2, col3 = st.columns(3)
                with col1:
                    st.metric("vs S&P 500", f"{comparative.get('outperformance_sp500', 0):.2%}")
                with col2:
                    st.metric("vs Nasdaq", f"{comparative.get('outperformance_nasdaq', 0):.2%}")
                with col3:
                    st.metric("Percentile", f"{comparative.get('percentile_ranking', 0):.0%}")
        
        sectors = results.get('portfolio_quality', {}).get('sector_diversification', {})
        if sectors:
            st.success("### 🌍 Отраслевая диверсификация")
            sector_df = pd.DataFrame(list(sectors.items()), columns=['Сектор', 'Доля'])
            fig = px.pie(sector_df, values='Доля', names='Сектор', hole=0.4)
            st.plotly_chart(fig, use_container_width=True)

# БАЗОВЫЕ ФУНКЦИИ ДЛЯ РАБОТЫ С ДАННЫМИ (ваши функции полностью сохранены)
def get_all_clients():
    return ['Иван Петров', 'Мария Сидорова', 'Алексей Козлов', 'Елена Волкова', 'Дмитрий Смирнов']

def get_client_details(client_name):
    clients_data = {
        'Иван Петров': {
            'portfolio_type': 'агрессивный', 'risk_profile': 'очень высокий', 'investment_horizon': '15+ лет',
            'experience': 'Эксперт', 'financial_goals': 'Создание технологического фонда', 'target_amount': 5000000,
            'initial_investment': 500000
        },
        'Мария Сидорова': {
            'portfolio_type': 'агрессивный', 'risk_profile': 'высокий', 'investment_horizon': '5-7 лет',
            'experience': 'Начинающий', 'financial_goals': 'Накопление на жилье', 'target_amount': 800000,
            'initial_investment': 300000
        },
        'Алексей Козлов': {
            'portfolio_type': 'сбалансированный', 'risk_profile': 'умеренный', 'investment_horizon': '7-10 лет',
            'experience': 'Продвинутый', 'financial_goals': 'Образование детей', 'target_amount': 2500000,
            'initial_investment': 800000
        },
        'Елена Волкова': {
            'portfolio_type': 'доходный', 'risk_profile': 'средний', 'investment_horizon': '10+ лет',
            'experience': 'Опытный', 'financial_goals': 'Пассивный доход', 'target_amount': 4000000,
            'initial_investment': 1200000
        },
        'Дмитрий Смирнов': {
            'portfolio_type': 'ультра-консервативный', 'risk_profile': 'очень низкий', 'investment_horizon': '1-3 года',
            'experience': 'Консервативный', 'financial_goals': 'Сохранение капитала', 'target_amount': 2200000,
            'initial_investment': 2000000
        }
    }
    return clients_data.get(client_name, clients_data['Алексей Козлов'])

def get_portfolio_by_client(client_name):
    portfolios = {
        'Иван Петров': {'TSLA': 0.25, 'NVDA': 0.20, 'AMD': 0.15, 'ARKK': 0.15, 'SQ': 0.10, 'BTC-USD': 0.10, 'ETH-USD': 0.05},
        'Мария Сидорова': {'TSLA': 0.30, 'NVDA': 0.25, 'AMD': 0.20, 'ARKK': 0.15, 'BTC-USD': 0.10},
        'Алексей Козлов': {'VTI': 0.25, 'VXUS': 0.15, 'BND': 0.20, 'VNQ': 0.10, 'GLD': 0.08, 'AAPL': 0.07, 'MSFT': 0.07, 'JPM': 0.05, 'Cash': 0.03},
        'Елена Волкова': {'VYM': 0.20, 'SCHD': 0.18, 'T': 0.10, 'VZ': 0.09, 'XOM': 0.08, 'PFE': 0.08, 'JNJ': 0.07, 'PG': 0.07, 'O': 0.06, 'Cash': 0.07},
        'Дмитрий Смирнов': {'BND': 0.40, 'GOVT': 0.25, 'SHY': 0.15, 'JNJ': 0.08, 'PG': 0.07, 'Cash': 0.05}
    }
    return portfolios.get(client_name, portfolios['Алексей Козлов'])

def generate_subscription_based_recommendations(client_name):
    return [
        "🎯 **Оптимизация портфеля**: Рекомендуется ребалансировка раз в квартал",
        "📊 **Диверсификация**: Добавьте международные активы для снижения риска",
        "💡 **Обучение**: Изучайте финансовые рынки для лучших решений"
    ]

def get_subscription_level(client_name):
    subscriptions = {
        'Иван Петров': 'premium',
        'Мария Сидорова': 'advanced', 
        'Алексей Козлов': 'basic',
        'Елена Волкова': 'basic',
        'Дмитрий Смирнов': 'basic'
    }
    return subscriptions.get(client_name, 'basic')

def get_subscription_details(client_name):
    level = get_subscription_level(client_name)
    details = {
        'basic': {'name': 'Базовый', 'price': 0, 'expires': '2024-12-31'},
        'advanced': {'name': 'Продвинутый', 'price': 450, 'expires': '2024-11-30'},
        'premium': {'name': 'Премиум', 'price': 800, 'expires': '2024-12-31'}
    }
    return details.get(level, details['basic'])

def can_access_advanced_analytics(client_name):
    return get_subscription_level(client_name) in ['advanced', 'premium']

def can_access_premium_features(client_name):
    return get_subscription_level(client_name) == 'premium'

SUBSCRIPTION_FEATURES = {
    'basic': {
        'name': 'Базовый', 'price': 0,
        'features': ['Базовые метрики', 'Рекомендации AI', 'Визуализация портфеля']
    },
    'advanced': {
        'name': 'Продвинутый', 'price': 450,
        'features': ['Все функции Базового', 'Расширенная аналитика', 'Глубокий анализ рисков']
    },
    'premium': {
        'name': 'Премиум', 'price': 800,
        'features': ['Все функции Продвинутого', 'AI-прогнозы', 'Персональный советник']
    }
}

# ФУНКЦИЯ ДЕТЕКЦИИ УСТРОЙСТВ (ваша функция полностью сохранена)
def detect_device_type():
    """Определяет тип устройства на основе user agent"""
    try:
        # Используем новую рекомендуемую функцию
        if hasattr(st, 'context') and hasattr(st.context, 'headers'):
            headers = st.context.headers
            if headers and 'User-Agent' in headers:
                user_agent = headers['User-Agent'].lower()
                
                # Детекция мобильных устройств
                mobile_keywords = ['mobile', 'android', 'iphone', 'ipad', 'tablet']
                if any(keyword in user_agent for keyword in mobile_keywords):
                    return 'mobile'
                
                # Детекция планшетов
                tablet_keywords = ['tablet', 'ipad']
                if any(keyword in user_agent for keyword in tablet_keywords):
                    return 'tablet'
                    
        return 'desktop'
    except Exception as e:
        # Fallback на десктоп, если что-то пошло не так
        return 'desktop'

# НАСТРОЙКА СТРАНИЦЫ STREAMLIT (ваша функция полностью сохранена)
def setup_page_config():
    """Настройка конфигурации страницы в зависимости от устройства"""
    device_type = detect_device_type()
    
    if device_type == 'mobile':
        st.set_page_config(
            page_title="ЮниВест - AI Советник",
            page_icon="📊",
            layout="centered",
            initial_sidebar_state="collapsed"
        )
        st.session_state.is_mobile = True
        st.session_state.is_tablet = False
    elif device_type == 'tablet':
        st.set_page_config(
            page_title="ЮниВест - AI Советник",
            page_icon="📊",
            layout="wide",
            initial_sidebar_state="expanded"
        )
        st.session_state.is_mobile = False
        st.session_state.is_tablet = True
    else:
        st.set_page_config(
            page_title="ЮниВест - AI Советник по Инвестициям",
            page_icon="📊",
            layout="wide",
            initial_sidebar_state="expanded"
        )
        st.session_state.is_mobile = False
        st.session_state.is_tablet = False

# АДАПТИВНЫЙ CSS ДЛЯ РАЗНЫХ УСТРОЙСТВ (ваш CSS полностью сохранен)
def inject_adaptive_css():
    """Внедряет адаптивный CSS для разных устройств"""
    st.markdown("""
    <style>
    /* Базовые стили для всех устройств */
    .tooltip {
        position: relative;
        display: inline-block;
        cursor: pointer;
    }

    .tooltip-icon {
        color: #666;
        font-size: 1.1em;
        padding: 4px 8px;
        border-radius: 50%;
        background: #f0f0f0;
        transition: all 0.3s ease;
    }

    .tooltip-icon:hover {
        background: #e0e0e0;
        transform: scale(1.1);
    }

    .tooltip-content {
        visibility: hidden;
        width: 280px;
        background-color: #2d3748;
        color: white;
        text-align: left;
        border-radius: 8px;
        padding: 12px;
        position: absolute;
        z-index: 1000;
        bottom: 125%;
        left: 50%;
        transform: translateX(-50%);
        opacity: 0;
        transition: opacity 0.3s;
        font-size: 0.85em;
        line-height: 1.5;
        box-shadow: 0 4px 12px rgba(0,0,0,0.2);
        border: 1px solid #4a5568;
        white-space: pre-line;
    }

    .tooltip-content::after {
        content: "";
        position: absolute;
        top: 100%;
        left: 50%;
        margin-left: -5px;
        border-width: 5px;
        border-style: solid;
        border-color: #2d3748 transparent transparent transparent;
    }

    .tooltip:hover .tooltip-content {
        visibility: visible;
        opacity: 1;
    }

    .subscription-badge {
        padding: 4px 12px;
        border-radius: 20px;
        font-size: 0.8em;
        font-weight: bold;
        text-align: center;
    }

    .badge-basic {
        background: linear-gradient(135deg, #11998e, #38ef7d);
        color: white;
    }

    .badge-advanced {
        background: linear-gradient(135deg, #fc466b, #3f5efb);
        color: white;
    }

    .badge-premium {
        background: linear-gradient(135deg, #ffd700, #ff8c00);
        color: black;
    }

    /* Адаптивные стили для мобильных устройств */
    @media (max-width: 768px) {
        .main-title {
            font-size: 1.5rem !important;
        }
        
        .metric-row {
            flex-direction: column;
        }
        
        .metric-card {
            margin-bottom: 0.5rem;
            width: 100% !important;
        }
        
        /* Улучшаем отображение графиков на мобильных */
        .js-plotly-plot .plotly .modebar {
            display: none !important;
        }
        
        /* Увеличиваем кнопки для touch */
        .stButton button {
            min-height: 44px;
            font-size: 16px;
        }
        
        /* Улучшаем читаемость текста */
        .stMarkdown {
            font-size: 14px;
        }
        
        /* Адаптивные колонки */
        .block-container {
            padding: 1rem;
        }
    }

    /* Стили для планшетов */
    @media (min-width: 769px) and (max-width: 1024px) {
        .main-title {
            font-size: 2rem !important;
        }
        
        .metric-card {
            min-width: 45% !important;
        }
    }

    /* Стили для десктопов */
    @media (min-width: 1025px) {
        .main-title {
            font-size: 2.5rem !important;
        }
        
        .metric-card {
            min-width: 22% !important;
        }
    }

    /* Улучшенные стили для сворачиваемых секций */
    .collapsible-section {
        border: 1px solid #e0e0e0;
        border-radius: 10px;
        padding: 1rem;
        margin: 1rem 0;
        background: white;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }

    .collapsible-header {
        display: flex;
        justify-content: space-between;
        align-items: center;
        cursor: pointer;
        padding: 0.5rem 0;
    }

    .collapsible-content {
        margin-top: 1rem;
    }

    /* Стили для страницы входа */
    .login-container {
        max-width: 90%;
        width: 400px;
        margin: 5vh auto;
        padding: 2rem;
        background: white;
        border-radius: 20px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.1);
        text-align: center;
    }
    .main-title {
        font-size: clamp(1.8rem, 5vw, 2.8rem);
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0.5rem;
        font-weight: bold;
    }
    .subtitle {
        color: #666;
        margin-bottom: 2rem;
        font-size: clamp(0.9rem, 3vw, 1.2rem);
    }
    
    @media (max-width: 768px) {
        .login-container {
            margin: 2vh auto;
            padding: 1.5rem;
        }
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
    if 'is_mobile' not in st.session_state:
        st.session_state.is_mobile = False
    if 'is_tablet' not in st.session_state:
        st.session_state.is_tablet = False

def display_subscription_badge(subscription_level: str) -> str:
    """Отображение бейджа подписки"""
    badges = {
        'basic': '📊 <span class="subscription-badge badge-basic">БАЗОВЫЙ</span>',
        'advanced': '🎯 <span class="subscription-badge badge-advanced">ПРОДВИНУТЫЙ</span>',
        'premium': '💎 <span class="subscription-badge badge-premium">ПРЕМИУМ</span>'
    }
    return badges.get(subscription_level, badges['basic'])

def login_page():
    """Страница входа с выбором клиента и паролем"""
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
                <p style="margin: 0.5rem 0 0 0; font-size: 0.8rem; color: #666;">Каждый клиент имеет разный уровень подписки</p>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

def display_adaptive_sidebar(current_client: str):
    """Адаптивная боковая панель"""
    if st.session_state.is_mobile:
        # На мобильных устройствах используем expander для боковой панели
        with st.expander("🎯 Меню", expanded=False):
            display_sidebar_content(current_client)
    else:
        # На планшетах и десктопах обычная боковая панель
        display_sidebar_content(current_client)

def display_sidebar_content(current_client: str):
    """Содержимое боковой панели"""
    st.title("🎯 Навигация")
    
    page = st.radio("Выберите раздел:", 
                   ["📊 Дашборд", "📈 Расширенная аналитика", "💎 Тарифы"],
                   index=0)
    
    if page != st.session_state.current_page:
        st.session_state.current_page = page
        st.rerun()
    
    st.markdown("---")
    clients = get_all_clients()
    new_user = st.selectbox("👥 Выберите клиента:", clients, 
                          index=clients.index(current_client))
    
    if new_user != current_client:
        st.session_state.current_user = new_user
        st.rerun()
    
    st.markdown("---")
    
    st.subheader("📊 Статистика")
    portfolio_dict = get_portfolio_by_client(current_client)
    
    if st.session_state.is_mobile:
        col1, col2 = st.columns(2)
        with col1:
            st.metric("Активы", len(portfolio_dict))
        with col2:
            client_data = get_client_details(current_client)
            st.metric("Риск", client_data['risk_profile'])
    else:
        col1, col2 = st.columns(2)
        with col1:
            st.metric("Активы", len(portfolio_dict))
        with col2:
            client_data = get_client_details(current_client)
            st.metric("Риск", client_data['risk_profile'])
    
    display_subscription_status(current_client)
    
    st.markdown("---")
    
    st.subheader("🤖 Советы")
    recommendations = generate_subscription_based_recommendations(current_client)
    for rec in recommendations[:2]:
        st.info(rec)

def display_subscription_status(client_name: str):
    """Отображение статуса подписки"""
    subscription_level = get_subscription_level(client_name)
    subscription_details = get_subscription_details(client_name)
    
    st.sidebar.markdown("---")
    st.sidebar.subheader("💎 Ваша подписка")
    
    badge_html = display_subscription_badge(subscription_level)
    st.sidebar.markdown(f"<div style='text-align: center; margin-bottom: 1rem;'>{badge_html}</div>", unsafe_allow_html=True)
    
    st.sidebar.write(f"**Тариф:** {subscription_details['name']}")
    st.sidebar.write(f"**Стоимость:** {subscription_details['price']} руб/мес")
    st.sidebar.write(f"**Действует до:** {subscription_details['expires']}")
    
    st.sidebar.markdown("**Доступные функции:**")
    features = SUBSCRIPTION_FEATURES[subscription_level]['features']
    for feature in features[:3]:
        st.sidebar.write(f"• {feature}")
    
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
    """Показ промпта разблокировки функции"""
    current_level = get_subscription_level(client_name)
    required_plan = SUBSCRIPTION_FEATURES[required_level]
    
    st.warning(f"🔒 **{feature_name} доступна на тарифе {required_plan['name']}**")
    
    if st.session_state.is_mobile:
        st.write(f"**Что вы получите:**")
        for feature in required_plan['features'][:2]:
            st.write(f"• {feature}")
        
        if st.button(f"💳 {required_plan['price']}₽/мес", key=f"unlock_{feature_name}", use_container_width=True):
            st.session_state.current_page = "💎 Тарифы"
            st.rerun()
    else:
        col1, col2 = st.columns([3, 1])
        with col1:
            st.write(f"**Что вы получите:**")
            for feature in required_plan['features'][:3]:
                st.write(f"• {feature}")
        with col2:
            if st.button(f"💳 {required_plan['price']}₽/мес", key=f"unlock_{feature_name}"):
                st.session_state.current_page = "💎 Тарифы"
                st.rerun()

def adaptive_dashboard_page():
    """Адаптивная главная страница дашборда"""
    current_client = st.session_state.current_user
    client_data = get_client_details(current_client)
    portfolio_dict = get_portfolio_by_client(current_client)
    subscription_level = get_subscription_level(current_client)
    
    if not client_data or not portfolio_dict:
        st.error("❌ Ошибка загрузки данных")
        return
    
    has_advanced_access = can_access_advanced_analytics(current_client)
    has_premium_access = can_access_premium_features(current_client)
    
    badge_html = display_subscription_badge(subscription_level)
    
    # Адаптивный заголовок с современным дизайном
    if st.session_state.is_mobile:
        st.markdown(f'''
        <div class="modern-main-header">
            <h1 style="color: white; margin-bottom: 0.5rem; font-size: 1.5rem;">🤖 ЮниВест AI</h1>
            <h2 style="color: white; margin: 0; font-size: 1.2rem;">{current_client}</h2>
            <div style="margin-top: 0.5rem;">
                {badge_html}
            </div>
        </div>
        ''', unsafe_allow_html=True)
    else:
        st.markdown(f'''
        <div class="modern-main-header">
            <h1 style="color: white; margin-bottom: 0.5rem;">🤖 ЮниВест AI Советник</h1>
            <h2 style="color: white; margin: 0;">{current_client}</h2>
            <div style="margin-top: 0.5rem;">
                {badge_html}
            </div>
        </div>
        ''', unsafe_allow_html=True)
    
    # Адаптивная верхняя панель
    if st.session_state.is_mobile:
        col1, col2 = st.columns([3, 1])
        with col1:
            st.markdown(f'<div style="font-size: 1.1rem;">👤 <strong>{current_client}</strong></div>', unsafe_allow_html=True)
        with col2:
            if st.button("🚪 Выйти", use_container_width=True, type="secondary"):
                st.session_state.authenticated = False
                st.session_state.current_user = None
                st.rerun()
    else:
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
    
    # Адаптивный профиль клиента
    st.markdown('<div class="modern-section-header">👤 Профиль клиента</div>', unsafe_allow_html=True)
    
    if st.session_state.is_mobile:
        st.write(f"**Тип портфеля:** {client_data['portfolio_type']}")
        st.write(f"**Уровень риска:** {client_data['risk_profile']}")
        st.write(f"**Инвестиционный горизонт:** {client_data['investment_horizon']}")
        st.write(f"**Опыт:** {client_data['experience']}")
        st.write(f"**Цель:** {client_data['financial_goals']}")
        st.write(f"**Целевая сумма:** {client_data['target_amount']:,.0f} ₽")
    else:
        col1, col2 = st.columns(2)
        with col1:
            st.write(f"**Тип портфеля:** {client_data['portfolio_type']}")
            st.write(f"**Уровень риска:** {client_data['risk_profile']}")
            st.write(f"**Инвестиционный горизонт:** {client_data['investment_horizon']}")
        with col2:
            st.write(f"**Опыт:** {client_data['experience']}")
            st.write(f"**Цель:** {client_data['financial_goals']}")
            st.write(f"**Целевая сумма:** {client_data['target_amount']:,.0f} ₽")
    
    # Адаптивный обзор портфеля
    st.markdown('<div class="modern-section-header">📊 Обзор портфеля</div>', unsafe_allow_html=True)
    
    weights_df = pd.DataFrame(list(portfolio_dict.items()), columns=['Актив', 'Доля'])
    
    if st.session_state.is_mobile:
        st.dataframe(weights_df, use_container_width=True, hide_index=True)
        fig_pie = px.pie(weights_df, values='Доля', names='Актив', hole=0.3)
        st.plotly_chart(fig_pie, use_container_width=True)
    else:
        col1, col2 = st.columns([1, 2])
        with col1:
            fig_pie = px.pie(weights_df, values='Доля', names='Актив', hole=0.3)
            st.plotly_chart(fig_pie, use_container_width=True)
        with col2:
            st.dataframe(weights_df, use_container_width=True, hide_index=True)
    
    # Анализ портфеля
    with st.spinner("🔍 Проводим комплексный анализ портфеля..."):
        analyzer = AdvancedPortfolioAnalysis(portfolio_dict, current_client)
        results = analyzer.comprehensive_analysis()
    
    if results:
        display_portfolio_analysis(results, subscription_level)
        display_efficiency_metrics(results, subscription_level)
        display_advanced_risk_analysis(results, subscription_level)
        display_portfolio_quality(results, subscription_level)
        
        st.markdown("---")
        display_historical_performance(results, current_client)
        
        display_premium_analytics(results, subscription_level)
        
        st.markdown('<div class="modern-section-header">📋 Детальные рекомендации</div>', unsafe_allow_html=True)
        for recommendation in results.get('recommendations', []):
            st.info(recommendation)
    else:
        st.error("❌ Не удалось провести анализ портфеля")

def adaptive_advanced_analytics_page():
    """Адаптивная страница расширенной аналитики"""
    current_client = st.session_state.current_user
    subscription_level = get_subscription_level(current_client)
    
    st.markdown('<div class="modern-section-header">📈 Расширенная аналитика</div>', unsafe_allow_html=True)
    
    if not can_access_advanced_analytics(current_client):
        show_feature_unlock_prompt("Расширенная аналитика", "advanced", current_client)
        return
    
    st.success(f"🎯 У вас есть доступ к расширенной аналитике!")
    
    client_data = get_client_details(current_client)
    portfolio_dict = get_portfolio_by_client(current_client)
    
    if not portfolio_dict:
        st.error("❌ Не удалось загрузить портфель")
        return
    
    with st.spinner("🔍 Проводим углубленный анализ портфеля..."):
        analyzer = AdvancedPortfolioAnalysis(portfolio_dict, current_client)
        results = analyzer.comprehensive_analysis()
    
    if results:
        display_portfolio_analysis(results, subscription_level)
        display_efficiency_metrics(results, subscription_level)
        display_advanced_risk_analysis(results, subscription_level)
        display_portfolio_quality(results, subscription_level)
        
        st.markdown("---")
        display_historical_performance(results, current_client)
        
        display_premium_analytics(results, subscription_level)
        
        st.markdown('<div class="modern-section-header">📋 Детальные рекомендации</div>', unsafe_allow_html=True)
        for recommendation in results.get('recommendations', []):
            st.info(recommendation)

def adaptive_pricing_page():
    """Адаптивная страница тарифов"""
    st.markdown('<div class="modern-section-header">💎 Выберите свой тариф</div>', unsafe_allow_html=True)
    
    st.write("Начните с бесплатного базового тарифа и улучшайте по мере роста ваших потребностей")
    
    if st.session_state.is_mobile:
        # Мобильная версия - вертикальное расположение
        for level in ['basic', 'advanced', 'premium']:
            plan = SUBSCRIPTION_FEATURES[level]
            badge_html = display_subscription_badge(level)
            st.markdown(f"<div style='text-align: center; margin-bottom: 1rem;'>{badge_html}</div>", unsafe_allow_html=True)
            
            st.subheader(plan['name'])
            st.metric("Стоимость", f"{plan['price']}₽/мес")
            
            st.write("**Включено:**")
            for feature in plan['features'][:4]:
                st.write(f"✅ {feature}")
            
            if level == 'basic':
                st.button("🎁 Начать бесплатно", key=f"btn_{level}", use_container_width=True, type="primary")
            else:
                st.button(f"💳 Выбрать {plan['name']}", key=f"btn_{level}", use_container_width=True)
            
            st.markdown("---")
    else:
        # Десктопная версия - горизонтальное расположение
        col1, col2, col3 = st.columns(3)
        
        for i, level in enumerate(['basic', 'advanced', 'premium']):
            plan = SUBSCRIPTION_FEATURES[level]
            with [col1, col2, col3][i]:
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

def main():
    """Главная функция приложения"""
    # Инициализация и настройка
    setup_page_config()
    setup_modern_design()  # Добавляем современный дизайн
    init_session_state()
    inject_adaptive_css()
    
    if not st.session_state.authenticated:
        login_page()
    else:
        # Адаптивный layout
        if st.session_state.is_mobile:
            # Мобильная версия - без боковой панели
            adaptive_dashboard_page()
        else:
            # Версия для планшетов и десктопов - с боковой панелью
            with st.sidebar:
                display_adaptive_sidebar(st.session_state.current_user)
            
            # Основной контент
            if st.session_state.current_page == "📊 Дашборд":
                adaptive_dashboard_page()
            elif st.session_state.current_page == "📈 Расширенная аналитика":
                adaptive_advanced_analytics_page()
            elif st.session_state.current_page == "💎 Тарифы":
                adaptive_pricing_page()

if __name__ == "__main__":
    main()












