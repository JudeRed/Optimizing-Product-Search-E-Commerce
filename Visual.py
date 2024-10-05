import matplotlib.pyplot as plt
import time

class ProductSearchBenchmark:
    def __init__(self, search_system):
        self.search_system = search_system

    def benchmark(self, skus, keywords):
        sku_times = []
        keyword_times = []

        for sku in skus:
            start_time = time.time()
            self.search_system.search_by_sku(sku)
            sku_times.append(time.time() - start_time)
        
        for keyword in keywords:
            start_time = time.time()
            self.search_system.search_by_keyword(keyword)
            keyword_times.append(time.time() - start_time)
        
        return sku_times, keyword_times

    def plot_performance(self, skus, sku_times, keywords, keyword_times):
        fig, ax = plt.subplots()
        ax.bar(skus, sku_times, label='SKU Search Time', color='blue')
        ax.bar(keywords, keyword_times, label='Keyword Search Time', color='green')
        ax.set_xlabel('Product Identifier')
        ax.set_ylabel('Search Time (s)')
        ax.set_title('SKU vs Keyword Search Performance')
        ax.legend()
        plt.show()

# Example Usage:
product_search = ProductSearch()
product_search.add_product('12345', 'Wireless Mouse')
product_search.add_product('12346', 'Gaming Mouse')

benchmark = ProductSearchBenchmark(product_search)
skus = ['12345', '12346']
keywords = ['Mouse', 'Gaming']

sku_times, keyword_times = benchmark.benchmark(skus, keywords)
benchmark.plot_performance(skus, sku_times, keywords, keyword_times)
