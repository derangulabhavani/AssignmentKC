# Sample student details data
student_data = [
    {"id": "1", "name": "Roi", "total_marks": "85"},
    {"id": "2", "name": "Jane ", "total_marks": "92"},
    {"id": "3", "name": "David", "total_marks": "78"},
    {"id": "4", "name": "Kina", "total_marks": "90"},
    {"id": "5", "name": "Sam", "total_marks": "87"},
    {"id": "6", "name": "Sarah", "total_marks": "95"},
    {"id": "7", "name": "Honey", "total_marks": "82"},
    {"id": "8", "name": "mira", "total_marks": "88"},
    {"id": "9", "name": "Smith", "total_marks": "75"},
    {"id": "10", "name": "Sophia", "total_marks": "93"}
]

# Load Student Details API
def load_student_details(page_number, page_size):
    start_index = (page_number - 1) * page_size
    end_index = start_index + page_size
    page_data = student_data[start_index:end_index]

    return page_data

# Server-side Filtering API
def filter_student_details(filters):
    filtered_data = student_data

    for filter_key, filter_value in filters.items():
        filtered_data = [data for data in filtered_data if data[filter_key] == filter_value]

    return filtered_data

# API endpoint for Load Student Details
def load_student_details_api(page_number, page_size):
    paginated_data = load_student_details(page_number, page_size)
    return paginated_data

# API endpoint for Server-side Filtering
def filter_student_details_api(filters):
    filtered_data = filter_student_details(filters)
    return filtered_data

# Example usage
page_number = 1
page_size = 10
filtered_criteria = {"total_marks": "82"}

# Load Student Details API
result = load_student_details_api(page_number, page_size)
print("Load Student Details API:")
print(result)

# Server-side Filtering API
result = filter_student_details_api(filtered_criteria)
print("\nServer-side Filtering API:")
print(result)