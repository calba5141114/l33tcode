class Solution {

    /**
     * @param Integer $x
     * @return Boolean
     */
    function isPalindrome($x) {
        $xRev = intval(strrev((string)$x));
        if($xRev != $x){
            return false;
        }
        elseif($xRev == $x){
            return true;
        }
    }
}

// Runtime: 24 ms, faster than 90.91% of PHP online submissions for Palindrome Number.
// Memory Usage: 14.8 MB, less than 43.33% of PHP online submissions for Palindrome Number.
