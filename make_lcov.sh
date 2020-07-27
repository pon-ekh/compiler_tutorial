coverage_dir=lcov_coverage
coverage_file=$coverage_dir/coverage.info

rm -rf $coverage_dir
mkdir -p $coverage_dir
lcov --base-directory . --directory . -c -o $coverage_file --rc lcov_branch_coverage=1
lcov --remove $coverage_file "/usr*" -o $coverage_file --rc lcov_branch_coverage=1
genhtml --rc genhtml_branch_coverage=1 -o $coverage_dir $coverage_file 
