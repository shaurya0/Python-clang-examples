#include <iostream>
#include <cstdint>

class A
{
private:
    float _fvalue;
    double _dvalue;
    int _ivalue;
public:
    A(  );
    A( uint8_t a, uint8_t b );
    A( int32_t *data );
    void method1();
    void method2( double v );
    uint64_t method3(  );
};


int main(int argc, char const *argv[])
{
    A my_class;
    my_class.
    return 0;
}