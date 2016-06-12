#include <cstdint>

class Reader
{
public:
    virtual int open() = 0;
    virtual size_t read( uint8_t * buffer, const size_t BUFFER_SIZE ) = 0;
    virtual int close() = 0;
};

class NullReader : public Reader
{
public:
    virtual int open();
    virtual size_t read( uint8_t * buffer, const size_t BUFFER_SIZE );
    virtual int close();
};

