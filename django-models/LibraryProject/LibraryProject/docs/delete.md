book.delete()
print(Book.objects.all())  # Should return an empty QuerySet


<!-- output  -->
<QuerySet []>
