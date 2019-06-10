object Solution {

  def findMedianSortedArrays(nums1: Array[Int], nums2: Array[Int]): Double = {
    var numsTwo = nums2
    var numsOne = nums1
    var m: Int = numsOne.length
    var n: Int = numsTwo.length
    if (m > n) {
      val temp: Array[Int] = numsOne
      numsOne = numsTwo
      numsTwo = temp
      val tmp: Int = m
      m = n
      n = tmp
    }
    var iMin: Int = 0
    var iMax: Int = m
    var halfLen: Int = (m + n + 1) / 2
    while (iMin <= iMax) {
      val i: Int = (iMin + iMax) / 2
      val j: Int = halfLen - i
      if (i < iMax && numsTwo(j - 1) > numsOne(i)) {
        iMin = i + 1
      } else if (i > iMin && numsOne(i - 1) > numsTwo(j)) {
        iMax = i - 1
      } else {
        var maxLeft: Int = 0
        maxLeft =
          if (i == 0) numsTwo(j - 1)
          else if (j == 0) numsOne(i - 1)
          else Math.max(numsOne(i - 1), numsTwo(j - 1))
        if ((m + n) % 2 == 1) {
          maxLeft
        }
        var minRight: Int = 0
        minRight =
          if (i == m) numsTwo(j)
          else if (j == n) numsOne(i)
          else Math.min(numsTwo(j), numsOne(i))
        (maxLeft + minRight) / 2.0
      }
    }
    0.0
  }

}

// needs improvement possibly need to import Java library.
