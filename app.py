def detect_device_type():
    """Определяет тип устройства на основе user agent с использованием st.context"""
    try:
        # Используем новую рекомендуемую функцию
        if hasattr(st, 'context') and hasattr(st.context, 'headers'):
            headers = st.context.headers
            if headers and 'User-Agent' in headers:
                user_agent = headers['User-Agent'].lower()
                # ... остальная логика
    except Exception as e:
        return 'desktop'  # Fallback













