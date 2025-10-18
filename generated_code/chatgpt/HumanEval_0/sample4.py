    if threshold <= 0:
        return False
    bucket_map = {}
    bucket_size = threshold
    for num in numbers:
        bucket = int(num // bucket_size)
        if bucket in bucket_map:
            return True
        if (bucket - 1 in bucket_map and abs(num - bucket_map[bucket - 1]) < threshold):
            return True
        if (bucket + 1 in bucket_map and abs(num - bucket_map[bucket + 1]) < threshold):
            return True
        bucket_map[bucket] = num
    return False