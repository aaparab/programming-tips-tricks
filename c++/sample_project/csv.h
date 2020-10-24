// csv.h

#include "csv.cpp"

class CSVRow;
std::istream& operator>>(std::istream& str, CSVRow& data);
long double my_stof(std::string text);
