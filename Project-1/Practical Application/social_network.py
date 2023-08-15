class SocialNetworkGraph:
    def __init__(self):
        self.graph = {}

    def add_user(self, user):
        if user not in self.graph:
            self.graph[user] = []

    def add_connection(self, user1, user2):
        if user1 in self.graph and user2 in self.graph:
            self.graph[user1].append(user2)
            self.graph[user2].append(user1)

    def suggest_friends(self, user):
        if user in self.graph:
            friends = set(self.graph[user])
            suggested_friends = set()

            for friend in friends:
                suggested_friends.update(self.graph[friend])

            suggested_friends.difference_update(friends)  # Remove existing friends
            suggested_friends.discard(user)  # Remove self

            return suggested_friends

    def find_communities(self):
        visited = set()
        communities = []

        for user in self.graph:
            if user not in visited:
                community = self._dfs(user, visited)
                communities.append(community)

        return communities

    def _dfs(self, user, visited):
        visited.add(user)
        community = [user]

        for friend in self.graph[user]:
            if friend not in visited:
                community.extend(self._dfs(friend, visited))

        return community

# Example usage
network = SocialNetworkGraph()
network.add_user("Alice")
network.add_user("Bob")
network.add_user("Charlie")
network.add_user("David")

network.add_connection("Alice", "Bob")
network.add_connection("Bob", "Charlie")
network.add_connection("Alice", "David")

print("Suggested friends for Alice:", network.suggest_friends("Alice"))

communities = network.find_communities()
print("Communities:", communities)
