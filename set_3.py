'''Programming Set 3

This assignment will develop your ability to manipulate data.
'''

def relationship_status(from_member, to_member, social_graph):
    '''Relationship Status.

    Let us pretend that you are building a new app.
    Your app supports social media functionality, which means that users can have
    relationships with other users.

    There are two guidelines for describing relationships on this social media app:
    1. Any user can follow any other user.
    2. If two users follow each other, they are considered friends.

    This function describes the relationship that two users have with each other.

    Please see "set_3_sample_data.py" for sample data. The social graph
    will adhere to the same pattern.

    Parameters
    ----------
    from_member: str
        the subject member
    to_member: str
        the object member
    social_graph: dict
        the relationship data

    Returns
    -------
    str
        "follower" if from_member follows to_member,
        "followed by" if from_member is followed by to_member,
        "friends" if from_member and to_member follow each other,
        "no relationship" if neither from_member nor to_member follow each other.
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    pass


def tic_tac_toe(board):
    '''Tic Tac Toe.

    Tic Tac Toe is a common paper-and-pencil game.
    Players must attempt to successfully draw a straight line of their symbol across a grid.
    The player that does this first is considered the winner.

    This function evaluates a tic tac toe board and returns the winner.

    Please see "set_3_sample_data.py" for sample data. The board will adhere
    to the same pattern. The board may by 3x3, 4x4, 5x5, or 6x6. The board will never
    have more than one winner. The board will only ever have 2 unique symbols at the same time.

    Parameters
    ----------
    board: list
        the representation of the tic-tac-toe board as a square list of lists

    Returns
    -------
    str
        the symbol of the winner or "NO WINNER" if there is no winner
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    pass

def eta(first_stop, second_stop, route_map):
    '''ETA.

    A shuttle van service is tasked to travel along a predefined circlar route.
    This route is divided into several legs between stops.
    The route is one-way only, and it is fully connected to itself.

    This function returns how long it will take the shuttle to arrive at a stop
    after leaving another stop.

    Please see "set_3_sample_data.py" for sample data. The route map will
    adhere to the same pattern. The route map may contain more legs and more stops,
    but it will always be one-way and fully enclosed.

    Parameters
    ----------
    first_stop: str
        the stop that the shuttle will leave
    second_stop: str
        the stop that the shuttle will arrive at
    route_map: dict
        the data describing the routes

    Returns
    -------
    int
        the time it will take the shuttle to travel from first_stop to second_stop
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    def relationship_status(user_a, user_b, network):
    is_following = user_b in network[user_a]["following"]
    is_followed_by = user_a in network[user_b]["following"]
    if is_following and is_followed_by:
        return "friends"
    elif is_following:
        return "follower"
    elif is_followed_by:
        return "followed by"
    else:
        return "no relationship"

def tic_tac_toe(grid):
    match_count = 0
    size = len(grid)

    for row in range(size):
        match_count = 0
        for col in range(size - 1):
            if grid[row][col] == grid[row][col + 1] and grid[row][col] != "":
                match_count += 1
            else:
                break
        if match_count == size - 1:
            return grid[row][0]

    for col in range(size):
        match_count = 0
        for row in range(size - 1):
            if grid[row][col] == grid[row + 1][col] and grid[row][col] != "":
                match_count += 1
            else:
                break
        if match_count == size - 1:
            return grid[0][col]

    match_count = 0
    for idx in range(size - 1):
        if grid[idx][idx] == grid[idx + 1][idx + 1] and grid[idx][idx] != "":
            match_count += 1
        else:
            break
    if match_count == size - 1:
        return grid[0][0]

    match_count = 0
    for idx in range(size - 1):
        if grid[idx][size - 1 - idx] == grid[idx + 1][size - 2 - idx] and grid[idx][size - 1 - idx] != "":
            match_count += 1
        else:
            break
    if match_count == size - 1:
        return grid[0][size - 1]

    return "NO WINNER"

def eta(start, end, route_map):
    duration = 0
    current = start

    while current != end:
        for segment in route_map:
            if segment[0] == current:
                duration += route_map[segment]['travel_time_mins']
                current = segment[1]
                break

    return duration
