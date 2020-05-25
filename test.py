from test_mongoDB import Testmongodb
import ini

if __name__ == "__main__":
    mongoDB = Testmongodb()

    mongoDB.measure_insert_one(ini.list_doc)

    print("insert_one 終了")

    mongoDB.measure_insert_one_with_index(ini.list_doc, ini.list_index_model)

    print("insert_one_with_index 終了")

    mongoDB.measure_insert_many(ini.list_doc)

    print("insert_many　終了")

    mongoDB.measure_insert_many_with_index(ini.list_doc, ini.list_index_model)

    print("insert_many_with_index 終了")
