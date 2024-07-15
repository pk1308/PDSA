* **Author+** :

  * Author → Publisher, Pages (from FD 1)
  * Publisher → Ratings (from FD 2)
  * Pages, Ratings → Type (from FD 3)
  * Type → Author (from FD 4)
  * Therefore, Author+ = {Author, Publisher, Pages, Ratings, Type}
* **{Ratings, pages}+** :

  * Pages, Ratings → Type (from FD 3)
  * Type → Author (from FD 4)
  * Author → Publisher, Pages (from FD 1)
  * Therefore, Pages+ = {Pages, Ratings, Type, Author, Publisher}
* **Type+** :

  * Type → Author (from FD 4)
  * Author → Publisher, Pages (from FD 1)
  * Publisher → Ratings (from FD 2)
  * Pages, Ratings → Type (from FD 3)
  * Therefore, Type+ = {Type, Author, Publisher, Pages, Ratings
* **{Publisher, pages} +**:

  * Publisher → Ratings (from FD 2)
  * Ratings, combined with Pages , can determine Type
  * Type → Author
  * From Author, we can determine everything else

From the closures, we can see that the following sets of attributes can determine all other attributes in the relation:

* **{Author}**
* **{Publisher, pages}**
* **{Type}**
* **{Ratings ,pages}**
