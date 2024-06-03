import pytest
from fastapi import HTTPException
from jwt import decode

from fast_zero.security import create_access_token, get_current_user, settings


def test_jwt():
    data = {'test': 'test'}
    token = create_access_token(data)

    decoded = decode(
        token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM]
    )

    assert decoded['test'] == data['test']
    assert decoded['exp']  # Testa se o valor de exp foi adicionado ao token


async def test_get_current_user(session):
    with pytest.raises(HTTPException) as excinfo:
        await get_current_user(
            session,
            'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJ0ZXN0ZUB0ZXN0LmNvbSIsImV4cCI6MTcxNzAxMTk2Mn0.niBs8UoCtI-ihQhuUKC45ooTOk86j9mY1H_L0Q9kaaa',
        )
    assert str(excinfo.value) == '401: Could not validate credentials'
