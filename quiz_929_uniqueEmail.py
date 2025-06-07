class Solution(object):
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        unique_email = set()

        for email in emails :
            local , domain = email.split("@")
            local = local.split("+")[0].replace(".", "")

            unique_email.add(local + "@" + domain)

        return len(unique_email)
