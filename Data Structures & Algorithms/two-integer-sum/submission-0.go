func twoSum(nums []int, target int) []int {
	hm := make(map[int]int)

	for i, num := range nums {
		compl := target - num

		if j, ok := hm[compl]; ok {
			return []int{j, i}
		}
		hm[num] = i
	}

	return nil
}