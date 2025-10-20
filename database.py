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

# ОПИСАНИЯ ТАРИФОВ И ФУНКЦИЙ - УСИЛЕННЫЕ ВОЗМОЖНОСТИ
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
            '📋 Планирование целей'
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
            '📈 Сравнение с бенчмарками'
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
            '🎯 Персональные стратегии'
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




