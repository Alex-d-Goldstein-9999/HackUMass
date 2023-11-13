#!

cd ../python\ scripts

#delete old data
python3 delete_documents.py worcester 0
python3 delete_documents.py hampshire 0
python3 delete_documents.py berkshire 0
python3 delete_documents.py franklin 0

#refresh documents
python3 insert_documents.py worcester
python3 insert_documents.py hampshire
python3 insert_documents.py berkshire
python3 insert_documents.py franklin


#delete old_scores
python3 delete_documents.py worcester-scores 1
python3 delete_documents.py hampshire-scores 1
python3 delete_documents.py berkshire-scores 1
python3 delete_documents.py franklin-scores 1


#refresh scores
python3 assignScoresForMeals.py breakfast worcester 75
python3 assignScoresForMeals.py lunch worcester 75
python3 assignScoresForMeals.py dinner worcester 75
python3 assignScoresForMeals.py grabngo worcester 75
python3 assignScoresForMeals.py latenight worcester 75

python3 assignScoresForMeals.py breakfast franklin 75
python3 assignScoresForMeals.py lunch franklin 75
python3 assignScoresForMeals.py dinner franklin 75
python3 assignScoresForMeals.py grabngo franklin 75


python3 assignScoresForMeals.py breakfast berkshire 75
python3 assignScoresForMeals.py lunch berkshire 75
python3 assignScoresForMeals.py dinner berkshire 75
python3 assignScoresForMeals.py grabngo berkshire 75
python3 assignScoresForMeals.py latenight berkshire 75

python3 assignScoresForMeals.py breakfast hampshire 75
python3 assignScoresForMeals.py lunch hampshire 75
python3 assignScoresForMeals.py dinner hampshire 75
python3 assignScoresForMeals.py grabngo hampshire 75
