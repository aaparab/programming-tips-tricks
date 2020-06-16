/*
Read CSV files in C++, convert string to float. 
*/

class CSVRow
{
    private:
        std::vector<std::string>    m_data;
    public:
        std::string const& operator[](std::size_t index) const
        {
            return m_data[index];
        }
        std::size_t size() const
        {
            return m_data.size();
        }
        void readNextRow(std::istream& str)
        {
            std::string         line;
            std::getline(str, line);

            std::stringstream   lineStream(line);
            std::string         cell;

            m_data.clear();
            while(std::getline(lineStream, cell, ','))
            {
                m_data.push_back(cell);
            }
            // This checks for a trailing comma with no data after it.
            if (!lineStream && cell.empty())
            {
                // If there was a trailing comma then add an empty element.
                m_data.push_back("");
            }
        }
};

std::istream& operator>>(std::istream& str, CSVRow& data)
{
    data.readNextRow(str);
    return str;
}

long double my_stof(std::string text)
{
    /*
    Convert string to double (str to float) when reading the csv file
    */
    long double number = 0.0;
    std::istringstream iss (text);
    iss >> number;
    return number;
}
