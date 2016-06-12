#include <iostream>
#include <cstdint>
#include <memory>
#include <array>

#include "type_example.h"


int NullReader::open(){ return 0; }
int NullReader::close(){ return 0; }

size_t NullReader::read( uint8_t * buffer, const size_t BUFFER_SIZE )
{
    for (size_t i = 0; i < BUFFER_SIZE; ++i)
    {
        buffer[i] = 0;
    }

    return BUFFER_SIZE;
}


static constexpr size_t BUFFER_SIZE = 1<<10;
int main(int argc, char const *argv[])
{
    std::unique_ptr<Reader> reader = std::make_unique<NullReader>();

    std::array<uint8_t, BUFFER_SIZE> buffer;
    buffer.fill( 0xc );
    reader->read( buffer.data(), BUFFER_SIZE );
    return 0;
}
