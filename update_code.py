import sys
import re

def update_file(file_path):
    try:
        with open(file_path, 'r') as f:
            content = f.read()
        
        original_content = content
        
        # Helper to multiply by 1.5
        def repl_tokens(match):
            prefix = match.group(1)
            val = int(match.group(2))
            new_val = int(val * 1.5)
            return f"{prefix}{new_val}"
            
        # Patterns for Max Tokens
        # 1. max_tokens=100 or max_tokens: 100
        content = re.sub(r'(max_tokens\s*[:=]\s*)(\d+)', repl_tokens, content)
        # 2. "max_tokens": 100
        content = re.sub(r'(["\']max_tokens["\']\s*[:]\s*)(\d+)', repl_tokens, content)
        # 3. MaxTokens = 100
        content = re.sub(r'(MaxTokens\s*=\s*)(\d+)', repl_tokens, content)
        # 4. maxTokens: 100
        content = re.sub(r'(maxTokens\s*[:]\s*)(\d+)', repl_tokens, content)
        
        # Helper for temperature -> 0.75
        # We need to preserve the suffix (like 'f' in C# if present, though usually implicit or explicitly float)
        # But regex matching [\d\.]+ matches 0.5. 
        # If C# has 0.5f, [\d\.]+ matches 0.5. 'f' remains.
        # So replacing with 0.75 is fine, 'f' will stay if it was after the match? 
        # No, if I match [\d\.]+, it consumes 0.5. The 'f' is after.
        # But if I replace 0 with 0.75, I get 0.75f. Correct.
        
        # Patterns for Temperature
        # 1. temperature=0.5 or temperature: 0.5
        content = re.sub(r'(temperature\s*[:=]\s*)[\d\.]+', r'\g<1>0.75', content)
        # 2. "temperature": 0.5
        content = re.sub(r'(["\']temperature["\']\s*[:]\s*)[\d\.]+', r'\g<1>0.75', content)
        # 3. Temperature = 0.5
        content = re.sub(r'(Temperature\s*=\s*)[\d\.]+', r'\g<1>0.75', content)
        
        if content != original_content:
            with open(file_path, 'w') as f:
                f.write(content)
            print(f"Updated {file_path}")
            
    except (IOError, UnicodeDecodeError) as e:
        print(f"Error processing {file_path}: {e}")

def main():
    for line in sys.stdin:
        file_path = line.strip()
        if file_path:
            update_file(file_path)

if __name__ == "__main__":
    main()
