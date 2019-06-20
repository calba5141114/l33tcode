# @param {Integer} x
# @return {Boolean}
def is_palindrome(x)
    xRev = x.to_s.reverse.to_i 
    if x == xRev
        return true
    elsif x != xRev
        return false
    end
end
