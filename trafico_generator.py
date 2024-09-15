import csv
import grpc
import cache_pb2
import cache_pb2_grpc

# Limita el archivo 3rd_lev_domains.csv a 10,000 filas y lo guarda como data.csv
def limit_csv(input_file, output_file, limit=10000):
    with open(input_file, 'r') as infile, open(output_file, 'w', newline='') as outfile:
        reader = csv.reader(infile)
        writer = csv.writer(outfile)
        for i, row in enumerate(reader):
            if i >= limit:
                break
            writer.writerow(row)
    print(f"Limited {input_file} to {limit} rows and saved as {output_file}")

# Función para generar tráfico desde el archivo CSV
def generate_traffic(api_stub, dataset):
    with open(dataset, 'r') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            key = row[0]
            value = row[1] if len(row) > 1 else '0.0.0.0'
            api_stub.Set(cache_pb2.SetRequest(key=key, value=value))
            print(f"Set {key} -> {value}")

if __name__ == '__main__':
    # Limitar el archivo original a 10,000 filas
    limit_csv('3rd_lev_domains.csv', 'data.csv', limit=10000)

    # Usar el archivo limitado data.csv para generar tráfico
    channel = grpc.insecure_channel('localhost:50051')
    stub = cache_pb2_grpc.CacheStub(channel)
    generate_traffic(stub, 'data.csv')
