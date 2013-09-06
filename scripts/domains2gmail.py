#!/usr/bin/python

# Turn domains.txt into a set of gmail filter rules.

import os, sys

GMAIL_FILTER_CHAR_LIMIT = 1699

f = open(sys.argv[1])
doms = f.readlines()
doms = map( lambda s: s.strip(), doms )
doms = filter( lambda s: not s.startswith('#'), doms )
doms = filter( lambda s: len(s) > 0, doms )
doms.sort()


print 'Paste each string into a new gmail filter rule:'
print

current_filter = 0

filter_lists = [[]]


def create_filter_string(dom_list):
    return 'from:(%s)' % '|'.join(dom_list)


for dom in doms:
    if (len(create_filter_string(filter_lists[current_filter])) +
            len(dom) > GMAIL_FILTER_CHAR_LIMIT):
        filter_lists.append([])
        current_filter += 1
    filter_lists[current_filter].append(dom)

for i, filter_string in enumerate(filter_lists):
    print 'Filter %s: ' % (i + 1)
    filter_ = '|'.join(filter_string)
    print filter_

    print
    print "Filter has: %s chars" % len(filter_)
    print "Filter has: %s ORS" % len(filter_string)
    print





