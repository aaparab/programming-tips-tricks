//marks.csv

/*
ID,Name,Math,English,Science
1,Alice,90,70,80
2,Bob,75,75,75
3,Chuck,80,65,85
*/

#include "csv.h"

int main()
{
    std::string file_path = "marks.csv";
    std::ifstream file(file_path);
    CSVRow row;
    
    // Fetch Bob's scores
    unsigned int id = 2; // bob's id
    std::pair<float, float, float> score;
    while (file >> row)
    {
        if (my_stof(row[0]) == id)
        {
            std::get<0>(score) = my_stof(row[2]); // math
            std::get<1>(score) = my_stof(row[3]); // english
            std::get<2>(score) = my_stof(row[4]); // science
        }
    }
    
    // Fetch everyone's Math scores
    std::vector<float> math_scores;
    while (file >> row)
    {
        math_scores.push_back(my_stof(row[2]));
    }
    
    // Print those Math scores
    for(int i=0; i < math_scores.size(); i++)
        std::cout << math_scores[i] << ' ';
    
    return 0;
}
