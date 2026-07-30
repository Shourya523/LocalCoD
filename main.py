from core.inference_manager import InferenceManager
from models.completion_request import CompletionRequest

manager = InferenceManager()

# The C++ code provided by user
cpp_code = """#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    int maxElement(vector<int>& nums) {

        int maxi = INT_MIN;

        for(int i = 0; i < nums.size(); i++) {

            
        }

        return maxi;
    }
};

int main() {

    vector<int> nums = {4, 1, 9, 2, 7};

    Solution s;

    cout << s.maxElement(nums);

    return 0;
}"""

# Calculate cursor position right inside the for loop
target_prefix = """#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    int maxElement(vector<int>& nums) {

        int maxi = INT_MIN;

        for(int i = 0; i < nums.size(); i++) {

"""

cursor_position = len(target_prefix)

request = CompletionRequest(
    model="Qwen2.5-Coder:latest",
    file_content=cpp_code,
    cursor_position=cursor_position,
    language="cpp"
)

print("=== Running C++ Code Completion ===")
response = manager.complete(request)

print("\n=== Completion Result ===")
print(response.text)


