class MultimodalVisionTableStructuralExtractorClient:
    def extract_structural_table(self, image_uri='spec_sheet_sample.png', expected_columns=['Feature', 'Standard', 'Pro Max']):
        return {
            'extraction_id': 'tbl_ext_9241',
            'image_uri': image_uri,
            'detected_table_count': 1,
            'reconstructed_rows_count': 8,
            'reconstructed_columns_count': len(expected_columns),
            'merged_cells_resolved_count': 3,
            'bounding_box_coverage': 0.962,
            'clean_markdown_table': '| Feature | Standard | Pro Max |\n|---|---|---|\n| Battery | 4000mAh | 5400mAh |\n| Fast Charge | 30W | 100W |',
            'structured_dossier_url': 'https://vision.table.genpark.ai/dossiers/9241.json'
        }
