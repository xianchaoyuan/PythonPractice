# 这是一个示例 Python 脚本。

# 按 Shift+F10 执行或将其替换为您的代码。
# 按 双击 Shift 在所有地方搜索类、文件、工具窗口、操作和设置。


def print_hi(name):
    # 在下面的代码行中使用断点来调试脚本。
    print(f'Hi, {name}')  # 按 Ctrl+F8 切换断点。


# 按间距中的绿色按钮以运行脚本。
if __name__ == '__main__':
    print_hi('PyCharm')


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# class Solution {
# public:
#     ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
#         ListNode *head = nullptr, *tail = nullptr;
#         int carry = 0;
#         while (l1 || l2) {
#             int n1 = l1 ? l1->val: 0;
#             int n2 = l2 ? l2->val: 0;
#             int sum = n1 + n2 + carry;
#             if (!head) {
#                 head = tail = new ListNode(sum % 10);
#             } else {
#                 tail->next = new ListNode(sum % 10);
#                 tail = tail->next;
#             }
#             carry = sum / 10;
#             if (l1) {
#                 l1 = l1->next;
#             }
#             if (l2) {
#                 l2 = l2->next;
#             }
#         }
#         if (carry > 0) {
#             tail->next = new ListNode(carry);
#         }
#         return head;
#     }
# };

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head, tail = None, None
        carry = 0

        while True:
            n1 = l1.val
            n2 = l2.val

            new_n = (n1 + n2 + carry) % 10
            carry = (n1 + n2) // 10

            if not head:
                head = tail = ListNode(new_n)
            else:
                tail.next = ListNode(new_n)
                tail = tail.next

            if not l1.next and not l2.next:
                break

            if l1.next:
                l1 = l1.next
            if l2.next:
                l2 = l2.next

        if carry != 0:
            tail.next = ListNode(new_n);

        return head


node1 = ListNode(1)
node2 = ListNode(2, node1)
node3 = ListNode(3, node2)

node4 = ListNode(4)
node5 = ListNode(5, node4)
node6 = ListNode(6, node5)

solution = Solution()
ret = solution.addTwoNumbers(node3, node6)
while ret.next:
    print(ret.val)
    ret = ret.next
