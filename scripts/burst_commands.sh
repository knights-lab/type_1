#!/usr/bin/env bash
/usr/bin/time -v burst15 /
  -t 72 /
  -q {path_to_query_files} /
  -a {path_to_acx} /
  -r {path_to_edx} /
  -o {path_to_output} /
  -m ALLPATHS /
  -fr /
  -i 0.98 /
  -- noprogress /
  > {path_to_output_file} 2>&1

