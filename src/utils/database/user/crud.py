# relative to 'main.py'
from utils.session import session_functions
from sqlalchemy import select, delete
from utils.database.user.models import User
from utils.database.engine import SessionLocal


class UserRepository:
    def write(self, username: str, chat_id: int) -> None:
        """
        Записывает данные пользователя в таблицу Users.
        Проверяет на дублирование перед записью.
        """
        with SessionLocal() as session:
            if self.search_by_name(username, chat_id):
                return None

            dates = session_functions.extract(username)
            day = dates[1][:-1]
            month = dates[2][:-1]
            birthday = f'{day}.{month}'

            # Создание и добавление нового пользователя
            new_user = User(
                username=username,
                birthday=birthday,
                chat_id=chat_id
            )
            session.add(new_user)
            session.commit()

    def remove(self, username, chat_id) -> None:
        """
        Удаляет пользователя из таблицы Users по имени и chat_id.
        """


        with SessionLocal() as session:
            session.execute(delete(User).where(User.username == username, User.chat_id == chat_id))
            session.commit()

    def search_by_name(self, target: str, chat_id: int) -> User | None:
        """
        Ищет пользователя по имени и chat_id в таблице Users.
        Возвращает объект User, если найден, или None.
        """
        with SessionLocal() as session:
            return session.execute(
                select(User).where(User.username == target, User.chat_id == chat_id)
            ).scalar_one_or_none()

    def search_by_date(self, target_date: str, chat_id: int) -> list[User]:
        """
        Ищет всех пользователей с указанной датой рождения (дд.мм) и chat_id.
        Возвращает список объектов User.
        """
        with SessionLocal() as session:
            result = session.execute(
                select(User).where(User.birthday == target_date, User.chat_id == chat_id)
            ).scalars().all()
        return result

user_repository = UserRepository()