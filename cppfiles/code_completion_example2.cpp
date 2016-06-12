#include <iostream>
#include <cstdint>
#include <memory>

class Reader
{
public:
    virtual int open() = 0;
    virtual size_t read( uint8_t * buffer, const size_t BUFFER_SIZE ) = 0;
    virtual int close() = 0;
};



int main(int argc, char const *argv[])
{
    std::unique_ptr<Reader> reader;
    reader.
    return 0;
}