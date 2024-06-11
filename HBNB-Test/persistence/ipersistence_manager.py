from abc import ABC, abstractmethod            # Import the ABC (Abstract Base Class) and abstractmethod decorators from the abc module

class IPersistenceManager(ABC):                # Define a new abstract base class named IPersistenceManager that inherits from ABC
    @abstractmethod                            # Decorator to define an abstract method
    def save(self, entity):                    # Abstract method to save an entity
        pass                                   # Placeholder for the method body, as it's abstract and must be implemented by subclasses

    @abstractmethod
    def get(self, entity_id, entity_type):     # Abstract method to get an entity by its ID and type
        pass

    @abstractmethod
    def update(self, entity):                  # Abstract method to update an entity
        pass

    @abstractmethod
    def delete(self, entity_id, entity_type):  # Abstract method to delete an entity by its ID and type
        pass
