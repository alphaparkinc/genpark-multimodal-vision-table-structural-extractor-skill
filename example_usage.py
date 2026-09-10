from client import MultimodalVisionTableStructuralExtractorClient

def main():
    client = MultimodalVisionTableStructuralExtractorClient()
    res = client.extract_structural_table()
    print('Vision Table Extractor: ' + res['extraction_id'] + ' (Rows: ' + str(res['reconstructed_rows_count']) + ', Cols: ' + str(res['reconstructed_columns_count']) + ')')
    print('Merged Cells Resolved: ' + str(res['merged_cells_resolved_count']) + ' | Coverage: ' + str(res['bounding_box_coverage']))
    print('Dossier: ' + res['structured_dossier_url'])

if __name__ == '__main__':
    main()
