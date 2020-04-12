#include <iostream>
#include <vector>
#include <string>

std::vector<std::vector<std::string> > per_set;

void permutation_(std::vector<std::string> set, std::vector<bool> bool_vec, std::vector<std::string> permutation)
{
	bool is_last = true;
	for(int i = 0; i < set.size(); i++)
	{
		if(bool_vec[i] == true)
		{
			std::vector<bool> new_bool_vec = bool_vec;
			new_bool_vec[i] = false;
			std::vector<std::string> new_permutation = permutation;
			new_permutation.push_back(set[i]);
			permutation_(set, new_bool_vec, new_permutation);
			is_last = false;
		}
	}

	if(is_last)
	{
		per_set.push_back(permutation);
	}
}

void list_power_set(std::vector<std::string> input_set)
{
	std::vector<std::vector<std::string> > power_set;
	std::vector<std::string> empty_set;
	empty_set.push_back("empty set");
	power_set.push_back(empty_set);
	for(auto itr = input_set.begin(); itr != input_set.end(); itr++)
	{
		std::vector<std::string>::size_type end = power_set.size();
		for(int i = 0; i < end; i++)
		{
			if(power_set[i] == empty_set)
			{
				std::vector<std::string> temp;
				temp.push_back(*itr);
				power_set.push_back(temp);
			}else{
				std::vector<std::string> temp = power_set[i];
				temp.push_back(*itr);
				power_set.push_back(temp);
			}
		}
	}

	for(auto vec : power_set)
	{
		std::vector<bool> bool_vec(vec.size(), true);
		std::vector<std::string> per;
		permutation_(vec, bool_vec, per);
	}
	/*
	for(auto vec : power_set)
	{
		for(auto str : vec)
		{
			std::cout << str << ", ";
		}
		std::cout << std::endl;
	}
	*/

}


int main()
{
	std::cout << "hello cpp" << std::endl;
	std::vector<std::string> input_set = {"Eiyad", "Abdulrahman", "Osamah"};
	list_power_set(input_set);

	std::cout << "--------" << std::endl << std::endl;

	for(auto vec : per_set)
	{
		for(auto str1 : vec)
		{
			std::cout << str1 << " ";
		}
		std::cout << std::endl;
	}

}











