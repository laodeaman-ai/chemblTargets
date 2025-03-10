import os
import pandas as pd
from chembl_webresource_client.new_client import new_client

def search_targets(query_list, job_dir):
    for search_term in query_list:
        # Load target data
        target = new_client.target

        # Perform target search
        try:
            target_query = target.search(search_term)
            
            # Pastikan ada data yang ditemukan
            if target_query:
                # Convert to DataFrame
                targets = pd.DataFrame.from_dict(target_query)

                # Pilih kolom yang relevan dan tambahkan kolom search_term
                search_term_formatted = search_term.replace(" ", "-")
                selected_columns = ['target_chembl_id', 'pref_name']
                targets['search_term'] = search_term_formatted  
                targets = targets[selected_columns]

                # Pastikan direktori tujuan ada
                if not os.path.exists(job_dir):
                    os.makedirs(job_dir)

                # Save DataFrame ke CSV
                targets_output_file_path = os.path.join(job_dir, f'targets_{search_term_formatted}.csv')
                targets.to_csv(targets_output_file_path, index=False)
                print(f"Results for '{search_term}' saved to {targets_output_file_path}")
            else:
                print(f"No results found for '{search_term}'")

        except Exception as e:
            print(f"Error occurred while searching for '{search_term}': {e}")

def main():
    # Definisikan query_list langsung di dalam kode
    query_list = ['alpha_glucosidase']  # Gantilah ini dengan kata kunci yang diinginkan

    job_dir = os.getcwd()  # Menggunakan direktori kerja saat ini

    # Menjalankan pencarian target
    search_targets(query_list, job_dir)

if __name__ == "__main__":
    main()
