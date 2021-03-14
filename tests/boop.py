from craigslist_meta import Site, Country

print(Site("eugene").url)
# print(Country('japan').url)
print(next(iter(Site("sfbay"))).url)

print(all(item == 200 for item in [200, 200, 2]))
