import re
import random

# 定义规则库：模式(正则表达式) -> 响应模板列表
rules = {
    r'我(?:需要|想要)(.*)': [
        "你为什么需要{0}？",
        "得到{0}真的能帮到你吗？",
        "你确定你需要{0}吗？"
    ],
    r'你为什么不(.*)[?？]?': [
        "你真的觉得我不{0}吗？",
        "也许有一天我会{0}的。",
        "你真的想让我{0}吗？"
    ],
    r'我(?:为什么|为何)不能(.*)[?？]?': [
        "你觉得你应该能够{0}吗？",
        "如果你能{0}，你会怎么做？",
        "我不知道——为什么你不能{0}呢？"
    ],
    r'我(?:是|觉得|感到)(.*)': [
        "你来找我是因为你{0}吗？",
        "你{0}这种情况多久了？",
        "对于{0}，你有什么感受？"
    ],
    r'.*(?:妈妈|母亲|妈).*': [
        "请多跟我说说你的母亲。",
        "你和母亲之间的关系怎么样？",
        "你对母亲有什么感受？"
    ],
    r'.*(?:爸爸|父亲|爸).*': [
        "请多跟我说说你的父亲。",
        "你父亲让你有什么感受？",
        "你父亲教会了你什么？"
    ],
    r'.*': [
        "请再多告诉我一些。",
        "我们换个话题吧……跟我说说你的家人。",
        "能详细说说吗？"
    ]
}

# 定义代词转换规则
pronoun_swap = {
    "我": "你", "你": "我", "我的": "你的", "你的": "我的",
    "我是": "你是", "你是": "我是", "我有": "你有", "你有": "我有",
    "我想": "你想", "你想": "我想",
}

def swap_pronouns(phrase):
    """
    对输入短语中的代词进行第一/第二人称转换
    """
    words = phrase.lower().split()
    swapped_words = [pronoun_swap.get(word, word) for word in words]
    return " ".join(swapped_words)

def respond(user_input):
    """
    根据规则库生成响应
    """
    for pattern, responses in rules.items():
        match = re.search(pattern, user_input, re.IGNORECASE)
        if match:
            # 捕获匹配到的部分
            captured_group = match.group(1) if match.groups() else ''
            # 进行代词转换
            swapped_group = swap_pronouns(captured_group)
            # 从模板中随机选择一个并格式化
            response = random.choice(responses).format(swapped_group)
            return response
    # 如果没有匹配任何特定规则，使用最后的通配符规则
    return random.choice(rules[r'.*'])

# 主聊天循环
if __name__ == '__main__':
    print("心理咨询师: 你好！今天有什么想聊的吗？")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["quit", "exit", "bye"]:
            print("Therapist: Goodbye. It was nice talking to you.")
            break
        response = respond(user_input)
        print(f"心理咨询师: {response}")