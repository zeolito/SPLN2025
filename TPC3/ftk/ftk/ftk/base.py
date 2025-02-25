import re
import jjcli
import collections

def lexer(txt):
    # FIXME patterns, stopwords, lems
    return re.findall(r'(\w+(?:-\w+)*)|[^\w\s]+', txt)

def counter(tokens):
    return collections.Counter(tokens)

def token_occurrences(counter, token):
    return counter.get(token, 0)

def token_frequencies(counter, relative=True):
    total_tokens = sum(counter.values())
    
    if relative:
        # Return both absolute and relative frequencies
        return {token: (count, count/total_tokens) 
                for token, count in counter.items()}
    else:
        # Return only absolute frequencies
        return {token: (count, None) for token, count in counter.items()}

def modify_occurrences(counter, token, amount):
    new_counter = counter.copy()
    new_counter[token] += amount
    
    # Remove token if count becomes zero or negative
    if new_counter[token] <= 0:
        del new_counter[token]
        
    return new_counter

def print_token_stats(counter, sort_by='count', top_n=None):
    frequencies = token_frequencies(counter)
    total_tokens = sum(counter.values())
    
    # Sort items
    if sort_by == 'alpha':
        items = sorted(frequencies.items())
    else:  # Default to sorting by count
        items = sorted(frequencies.items(), key=lambda x: x[1][0], reverse=True)
    
    # Limit to top N if specified
    if top_n is not None:
        items = items[:top_n]
    
    print(f"{'Token':<20} {'Count':<10} {'Frequency':<10}")
    print("-" * 40)
    
    for token, (count, freq) in items:
        print(f"{token:<20} {count:<10} {freq:.6f}")
    
    print("-" * 40)
    print(f"Total tokens: {total_tokens}")

def main():
    cl = jjcli.clfilter()
    
    all_tokens = []
    for txt in cl.text():
        tokens = lexer(txt)
        all_tokens.extend(tokens)
        
    token_counter = counter(all_tokens)
    
    # Example usage of the new functions
    print("\nToken statistics:")
    print_token_stats(token_counter, top_n=10)
    
    # Example of finding occurrences of a specific token
    example_token = next(iter(token_counter)) if token_counter else "example"
    print(f"\nOccurrences of '{example_token}': {token_occurrences(token_counter, example_token)}")
    
    # Example of modifying occurrences
    print(f"\nAfter adding 5 occurrences of '{example_token}':")
    modified_counter = modify_occurrences(token_counter, example_token, 5)
    print(f"New count: {token_occurrences(modified_counter, example_token)}")
