class GradingSystem:

    def __init__(self, arr):
        self.arr = arr

    def run_grd(self):
        # created a list for symbols +, -, and white space
        sym = ['+', '', '-']

        # import string function to create a list of the letters in the alphabet in lower case
        import string
        alphabet = list(string.ascii_lowercase)
        # print(alphabet)

        # creating a num_list in descending order and convert each element into a string
        num_list = []
        for i in range(9, -1, -1):
            num_list.append(str(i))
        # print(num_list)

        # creating a list 'a' by concatenating the created lists: alphabet, num_list, and sym
        a = (alphabet + num_list + sym)
        # print(a)

        # creating a list of numbers as integers, to be added with the 'a' list as a dictionary
        num_value = []
        for i in range(37, -2, -1):
            num_value.append(i)
        # print(num_value)

        # the created dictionary using the functions dict and zip
        the_dict = dict(zip(a, num_value))
        # print(the_dict)

        # created a new list arr1 using a for loop and using the lower() function so that the strings are converted
        # the lower case for comparison purposes in the nested for loops below
        arr1 = []
        for i in self.arr:
            arr1.append(i.lower())
        # print(arr1)

        # created a sum_collection list with nested for loops for comparison of each character in each element then
        # obtaining the numerical value of each character from the the_dict dictionary, then adding each value as the
        # sum, then appending it to the sum_collection list
        sum_collection = []
        for i in arr1:
            sum = 0
            for j in i:
                for k in the_dict:
                    # print(j, k)
                    if j == k:
                        # print(j, the_dict[k])
                        sum += the_dict[k]
            # print(sum)
            sum_collection.append(sum)
        # print(sum_collection)

        # creating a dictionary 'result' from the self.arr and the sum_collection list
        result = dict(zip(self.arr, sum_collection))
        # print(result)

        # then assign a variable sort_by_value by using the sorted and lambda function passed in a dict function,
        # sorted ascending order
        sort_by_value = dict(sorted(result.items(), key=lambda item: item[1]))

        # another variable sorted_keys to output only the keys that are already sorted in ascending order from the
        # sort_by_value dictionary
        sorted_keys = sort_by_value.keys()
        # print(sorted_keys)

        # the final list arr2, then using a for loop to append the elements
        arr2 = []
        for i in sorted_keys:
            arr2.append(i)
        # printing the reverse of the arr2
        print(arr2[::-1])