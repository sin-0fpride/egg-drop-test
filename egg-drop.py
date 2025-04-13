# Function to find the highest safe floor with max 7 eggs (Empire State Building)
def find_safe_floor(total_floors, break_floor):
    eggs = 7  # Max eggs allowed
    steps = 0  # Track steps
    low = 1
    high = total_floors
    
    # Simulate egg breaking (for testing)
    def does_break(floor):
        return floor > break_floor
    
    # Binary search to find the safe floor
    while low <= high and eggs > 0:
        steps += 1
        mid = (low + high) // 2  # Test middle floor
        if does_break(mid):  # Egg breaks
            eggs -= 1  # Lose an egg
            high = mid - 1  # Search lower half
        else:  # Egg doesn’t break
            low = mid + 1  # Search upper half
    
    # Return highest safe floor, steps, and eggs used
    return low - 1, steps, 7 - eggs

# Function to find first buggy software version (alternative use case)
def find_buggy_version(total_versions, bug_version):
    tests = 0  # Track test runs
    low = 1
    high = total_versions
    
    # Simulate bug presence (for testing)
    def has_bug(version):
        return version >= bug_version
    
    # Binary search to find first buggy version
    while low <= high:
        tests += 1
        mid = (low + high) // 2
        if has_bug(mid):  # Bug exists
            high = mid - 1  # Check earlier versions
        else:  # No bug
            low = mid + 1  # Check later versions
    
    # Return first buggy version and number of tests
    return low, tests

# Test both scenarios
def test_egg_scenarios():
    # Scenario 1: Empire State Building (102 floors, egg breaks at floor 50)
    total_floors = 102
    break_floor = 50
    safe_floor, steps, eggs_used = find_safe_floor(total_floors, break_floor)
    print(f"Highest safe floor: {safe_floor}, Steps: {steps}, Eggs used: {eggs_used}")
    
    # Scenario 2: Buggy software version (102 versions, bug at version 50)
    total_versions = 102
    bug_version = 50
    buggy_version, tests = find_buggy_version(total_versions, bug_version)
    print(f"First buggy version: {buggy_version}, Tests: {tests}")

# Run the tests
test_egg_scenarios()