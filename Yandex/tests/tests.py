import pytest
from main import BooksCollector


@pytest.fixture
def collector():
    return BooksCollector()


class TestBooksCollector:
    @pytest.mark.parametrize("name", ["Book1", "Another Book", "Short"])
    def test_add_new_book(self, collector, name):
        collector.add_new_book(name)
        assert name in collector.books_genre

    @pytest.mark.parametrize("genre", BooksCollector().genre)
    def test_set_book_genre_valid(self, collector, genre):
        book_name = "Test Book"
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, genre)
        assert collector.get_book_genre(book_name) == genre

    def test_get_books_with_specific_genre(self, collector):
        collector.add_new_book("Book1")
        collector.add_new_book("Book2")
        collector.set_book_genre("Book1", "Фантастика")
        collector.set_book_genre("Book2", "Ужасы")

        result = collector.get_books_with_specific_genre("Фантастика")
        assert result == ["Book1"]

    def test_get_books_for_children(self, collector):
        collector.add_new_book("ChildBook")
        collector.add_new_book("HorrorBook")
        collector.set_book_genre("ChildBook", "Комедии")
        collector.set_book_genre("HorrorBook", "Ужасы")

        result = collector.get_books_for_children()
        assert result == ["ChildBook"]

    @pytest.mark.parametrize("book_name", ["ExistingBook", "NonExistingBook"])
    def test_add_book_in_favorites(self, collector, book_name):
        collector.add_new_book(book_name)
        collector.add_book_in_favorites(book_name)
        assert book_name in collector.get_list_of_favorites_books()

    def test_delete_book_from_favorites(self, collector):
        book_name = "FavoriteBook"
        collector.add_new_book(book_name)
        collector.add_book_in_favorites(book_name)

        collector.delete_book_from_favorites(book_name)
        assert book_name not in collector.get_list_of_favorites_books()

    @pytest.mark.parametrize("name", ["ExistingBook", "NonExistingBook"])
    def test_get_book_genre(self, collector, name):
        collector.add_new_book(name)
        collector.set_book_genre(name, "Фантастика")

        result = collector.get_book_genre(name)
        assert result == "Фантастика"

    def test_get_books_genre(self, collector):
        collector.add_new_book("Book1")
        collector.add_new_book("Book2")
        collector.set_book_genre("Book1", "Фантастика")

        result = collector.get_books_genre()
        assert isinstance(result, dict)
        assert len(result) == 2
        assert "Book1" in result and "Book2" in result


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
