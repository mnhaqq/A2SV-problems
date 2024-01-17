from math import ceil, floor

class Solution:
    def fullJustify(self, words: list[str], maxWidth: int) -> list[str]:
        #finding number of words and line length for each line of the output
        line_length = dict()
        curr_len = i = word_count = 0

        for word in words:
            curr_len += len(word) + 1
            word_count += 1
            if curr_len - 1 > maxWidth:
                line_length[i] = (word_count - 1, curr_len - len(word) - 2)
                word_count = 1
                curr_len = len(word) + 1
                i += 1
        last_line = i
        line_length[i] = (word_count, curr_len - 1)

        # arranging words
        ans = []
        line_num = 0
        i = 0
        while i < len(words):
            curr_line = ""
            if line_length[line_num][0] > 1:
                extra_spaces = (maxWidth - line_length[line_num][1]) / (line_length[line_num][0] - 1)
            else:
                extra_spaces = maxWidth - line_length[line_num][1]

            upper = ceil(extra_spaces)
            lower = floor(extra_spaces)

            if line_num == last_line:
                j = 0
                extra_spaces = maxWidth - line_length[line_num][1]
                while i < len(words) and j < line_length[line_num][0]:
                    curr_line += words[i]
                    if i != len(words) - 1:
                        curr_line += ' '
                    i += 1
                    j += 1
                curr_line += ' ' * extra_spaces
                ans.append(curr_line)
                break

            min_space_left = line_length[line_num][1] + (lower * (line_length[line_num][0]-1))
            j = 0
            while i < len(words) and j < line_length[line_num][0]:
                
                if j == line_length[line_num][0] - 1 and line_length[line_num][0] > 1:
                    curr_line += words[i]
                elif j == line_length[line_num][0] - 1:
                    curr_line += words[i] + ' ' * upper
                else:
                    if (len(curr_line) + upper + min_space_left - lower) > maxWidth:
                        curr_line += words[i] + ' ' + ' ' * lower
                        min_space_left -= (len(words[i]) + lower)

                    else:
                        curr_line += words[i] + ' ' + ' ' * upper
                        min_space_left -= (len(words[i]) + upper)
                j += 1
                i += 1
            line_num += 1
            ans.append(curr_line)
        return ans