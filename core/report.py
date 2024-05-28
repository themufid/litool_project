
def generate_report(results):
    """
    Fungsi untuk menghasilkan laporan dari hasil pemindaian atau injeksi.

    Args:
        results (list): Daftar hasil pemindaian atau injeksi.

    Returns:
        str: String berisi laporan hasil pemindaian atau injeksi.
    """
    report = "Laporan Hasil Pemindaian atau Injeksi:\n"
    for idx, result in enumerate(results, 1):
        report += f"\nHasil #{idx}:\n"
        report += f"URL: {result['url']}\n"
        report += f"Status: {'Success' if result['success'] else 'Failed'}\n"
        if 'message' in result:
            report += f"Pesan: {result['message']}\n"
    return report
