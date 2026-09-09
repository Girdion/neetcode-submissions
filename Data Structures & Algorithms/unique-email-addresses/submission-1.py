class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        res = set()

        for email in emails:
            local, domain = email.split('@')

            normalizedLocal = ""

            for char in local:
                if char == '+':
                    break

                if char == '.':
                    continue

                normalizedLocal += char

            normalizedMail = normalizedLocal + '@' + domain
            res.add(normalizedMail)

        return len(res)