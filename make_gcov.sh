coverage_dir=gcov_coverage

rm -rf $coverage_dir
mkdir -p $coverage_dir
cd $coverage_dir

gcov `find .. -name "*.gcno*"`
