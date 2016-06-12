#include <iostream>
#include <cstdint>
#include <memory>

class Something
{
    std::unique_ptr<float> _fvalue
public:
    Something();
    void set_value( int32_t x );
};

void Something::set_value( double x )
{

}

static float some_function(  )
{
    float f = 3.0f;
    auto x = 2;
    return f;
}


int main(int argc, char const *argv[])
{
    std::cout << "hello world" << std::endl
    return 0;
}