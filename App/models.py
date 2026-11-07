from dataclasses import dataclass


@dataclass
class Record:
    id: int
    title: str
    completed: bool
    user_id: int


def convert_to_record(data):
    """Convert dictionary data into Record objects."""

    return Record(
        id=data["id"],
        title=data["title"],
        completed=data["completed"],
        user_id=data["userId"]
    )


if __name__ == "__main__":

    sample = {
        "userId": 1,
        "id": 1,
        "title": "Complete Python Training",
        "completed": False
    }

    task = convert_to_record(sample)

    print(task)
    print("Task ID:", task.id)
    print("Task Title:", task.title)
    print("Completed:", task.completed)