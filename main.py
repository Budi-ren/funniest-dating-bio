import os

BIO = "I only date people who pass CAPTCHAs. You've failed four times. That's a record."

def main():
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="") as f:
        f.write(BIO)

if __name__ == "__main__":
    main()
