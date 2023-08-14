from lodepy.core.main import Main


class Script():
    def __init__(self,
                 store_file: str = None,
                ):
        '''
        :store_file: The file that is going to store all of the runs variables
        '''
        self.main = Main(store_file)

    def __enter__(self) -> Main:
        return self.main
        
    def __exit__(self) -> None:
        self.main.data_store.write_data()