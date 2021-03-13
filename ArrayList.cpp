#include <iostream>
#include <string>

template <typename T>
class ArrayList {
public:
    //type aliases
    using pointer_type = T*;
    using size_type = size_t;

    //members
    std::allocator<T> m_allocator;
    size_type m_capacity;
    size_type m_size;
    pointer_type m_st_ptr;

    //constants
    const size_type INITIAL_ALLOCATION_SIZE = 16;
    const double LOAD_FACTOR = 0.75;

    //constructor
    ArrayList() {
        m_st_ptr = m_allocator.allocate(INITIAL_ALLOCATION_SIZE);
        m_capacity = INITIAL_ALLOCATION_SIZE;
        m_size = 0;
    }

    //destructor
    ~ArrayList() {
        for(int i = 0; i < m_size; ++i) {
            m_allocator.destroy(m_st_ptr + i);
        }
        m_allocator.deallocate(m_st_ptr, m_capacity);
    }

    //class methods
    size_type getSize() {
        return m_size;
    }

    size_type getCapacity() {
        return m_capacity;
    }

    void push_back(const T& x) {
        if(m_size >= LOAD_FACTOR * m_capacity) {
            pointer_type old_ptr = m_st_ptr;
            m_capacity *= 2;
            m_st_ptr = m_allocator.allocate(m_capacity);
            for(int i = 0; i < m_size; ++i) {
                m_allocator.construct(m_st_ptr + i, old_ptr[i]);
                m_allocator.destroy(old_ptr + i);
            }
            m_allocator.deallocate(old_ptr, m_capacity/2);
        }
        m_allocator.construct(m_st_ptr + m_size, x);
        ++m_size;
    }

    T set(const T& x, size_type idx) {
        if(idx >= m_size || idx < 0) {
            std::cout << "Index Out of Bounds Error!\n";
        } else {
            m_allocator.destroy(m_st_ptr + idx);
            m_allocator.construct(m_st_ptr + idx, x);
        }
    }

    std::string print_list() {
        for(int i = 0; i < m_size; ++i) {
            std::cout << m_st_ptr[i] << " ";
        }
        std::cout << "\n";
    }


private:

};


int main() {
    ArrayList<int> x;
    x.push_back(2);
    x.print_list();
    x.print_list();

    return 0;
}
