import argparse
import fuzzing

def main():
    parser = argparse.ArgumentParser()

    url_helper_text = "The URL to fuzz, add 'FUZZ' to the place in the url you want to fuzz, f.ex: 'http://example.com/user/FUZZ'"

    parser.add_argument("--url", required=True, help=url_helper_text)
    parser.add_argument("--list", required=True, help="Filename of the wordlist to use to fuzz")
    parser.add_argument("-m", "--method", help="The HTTP method to use in the fuzzing (get/post/put)")
    parser.add_argument("-c", "--cookie", action="append", help="HTTP cookie to add to the request, format: <cookie-name>:<cookie-value>, can also be fuzzed")
    parser.add_argument("-o", "--output", help="Output file for the fuzzing attempts")

    args = parser.parse_args()

    if args.method == None:
        args.method = "get"

    optional_arguments = {
        "cookies": args.cookie,
    }

    fuzz_output = args.output if args.output is not None else "fuzz_output.csv"
    fuzzing.fuzz_url(args.url, args.method, args.list, fuzz_output, optional_arguments)


if __name__ == "__main__":
    main()