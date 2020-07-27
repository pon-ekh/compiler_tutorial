rm -rf coverage
lcov --base-directory . --directory . --zerocounters -q
