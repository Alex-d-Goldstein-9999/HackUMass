#!

cd ../python\ scripts

#delete old data
python3 delete_documents.py worcester
python3 delete_documents.py hampshire
python3 delete_documents.py berkshire
python3 delete_documents.py franklin

#refresh documents
python3 insert_documents.py worcester
python3 insert_documents.py hampshire
python3 insert_documents.py berkshire
python3 insert_documents.py franklin


