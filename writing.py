import random
import sys
import re

def split_into_chunks(text, chunk_size=3):
    words = text.split()
    chunks = [" ".join(words[i:i+chunk_size]) for i in range(0, len(words), chunk_size)]
    return chunks

def shuffle_chunks(chunks):
    random.shuffle(chunks)
    return chunks

def process_text(input_text):
    lines = input_text.strip().split("\n")
    
    english_sentences = {}
    korean_sentences = {}
    non_numbered_lines = []

    for line in lines:
        line = line.strip()
        if not line:
            continue

        # 번호가 있는 문장 찾기 (예: "1. 문장내용" 또는 "1.    문장내용")
        match = re.match(r"^(\d+)\.\s*(.+)$", line)
        if match:
            num = int(match.group(1))
            sentence = match.group(2).strip()

            # 영어인지 한글인지 판별
            if re.match(r"^[A-Za-z\"']", sentence):  # 영어 문장 (따옴표 포함)
                english_sentences[num] = sentence
            else:  # 한글 문장
                korean_sentences[num] = sentence
        else:
            non_numbered_lines.append(line)  # 번호 없는 문장은 그대로 저장

    # 번호 없는 문장 먼저 출력
    for line in non_numbered_lines:
        print(line)

    # 번호가 있는 문장을 순서대로 출력
    for num in sorted(korean_sentences.keys()):
        print(f"{num}. {korean_sentences[num]}")  # 한글 문장 출력
        
        if num in english_sentences:
            chunks = split_into_chunks(english_sentences[num])
            shuffled_chunks = shuffle_chunks(chunks)
            print(" | ".join(shuffled_chunks))  # 섞인 영어 문장 출력
        
        print("->")  # 공백 한 줄 출력

if __name__ == "__main__":
    print("문장을 입력하세요 (입력이 끝나면 Ctrl+D 또는 Ctrl+Z 후 Enter):")
    input_text = sys.stdin.read()  # 여러 줄 입력 받기
    process_text(input_text)
