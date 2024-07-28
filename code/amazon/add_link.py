#
# OA June - 2 leetcode medium Questions. Dont remember the questions. Completed the first question and most of test cases passed for the second question
#
# After a month
#
# Screening Round - Focus was on writing clean and structured code
# Design a data structure for browser history
# 1. add a link
# 2. remove a link
# 3. each link has many keywords, search by keyword
# 4. print all links in a inserted link order
# 4. example - '/google/search' , it has google and search as keywords
# 5. link could be duplicate
# Suggested doubly linkedlist for links and hashmap for each keyword , Hashmap value is list of links
# Although solution may not be optimal, Interviewer asked me to implement the approach
# Some Java questions - Runnable vs Thread, Stream API, Deadlock, Notify vs Wait, concurrency and oops concepts mostly
#
# After a week
# In House Interviews
# Round 1 ( 1 hour) . Java grilling , Most of the concepts were touched, from running hello program to concurrency, JRE vs JVM
# singleton design pattern, volatile, method hiding vs method overriding, threadpoolexecutor ( 40 minutes)
# coding question (20 minutes): https://leetcode.com/problems/kth-smallest-number-in-multiplication-table/ suggested all 3 approaches- sorting, priority queue and binary search
#
# Round2 (1 hour) . Resume based Questions, Singleton Design Pattern, Design Flight booking System - Focus was on finding multiple stops flight schedules, Design LRU, Design Java annotation
#
# After 2 weeks
# HR scheduled 3rd Techical round, but informed me last moment that it will be rescheduled.
# Till now I have not heard back from the HR


class ListNode:
    def __init__(self, link):
        self.link = link
        self.prev = None
        self.next = None


class BrowserHistory:
    def __init__(self):
        self.head = None
        self.tail = None
        self.keywords_map = {}

    def add_link(self, link, keywords):
        new_node = ListNode(link)
        if not self.head:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

        for keyword in keywords:
            if keyword not in self.keywords_map:
                self.keywords_map[keyword] = []
            self.keywords_map[keyword].append(new_node)

    def remove_link(self, link):
        current = self.head
        while current:
            if current.link == link:
                if current.prev:
                    current.prev.next = current.next
                else:
                    self.head = current.next
                if current.next:
                    current.next.prev = current.prev
                else:
                    self.tail = current.prev

                # Collect keywords to update
                keywords_to_update = []
                for keyword, nodes in self.keywords_map.items():
                    if current in nodes:
                        nodes.remove(current)
                        if not nodes:
                            keywords_to_update.append(keyword)

                # Remove empty keywords
                for keyword in keywords_to_update:
                    del self.keywords_map[keyword]

                return True
            current = current.next
        return False

    def search_by_keyword(self, keyword):
        if keyword in self.keywords_map:
            return [node.link for node in self.keywords_map[keyword]]
        return []

    def print_all_links(self):
        current = self.head
        links = []
        while current:
            links.append(current.link)
            current = current.next
        print(links)


# Example usage:
bh = BrowserHistory()
bh.add_link('/google/search', ['google', 'search'])
bh.add_link('/youtube/watch', ['youtube', 'video'])
bh.add_link('/google/maps', ['google', 'maps'])

print(bh.search_by_keyword('google'))  # ['/google/search', '/google/maps']
print(bh.search_by_keyword('video'))  # ['/youtube/watch']

bh.print_all_links()  # ['/google/search', '/youtube/watch', '/google/maps']

bh.remove_link('/google/search')
bh.print_all_links()  # ['/youtube/watch', '/google/maps']
