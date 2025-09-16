from playwright.sync_api import Page, expect

def test_template(page: Page):
    #Web table fixed header
    table = page.locator("div.tableFixHead >> table#product")
    rows = table.locator("tr")
    
    row_count = rows.count()
    print(f"Total rows: {row_count}")
    
    header_cells = rows.nth(0).locator("th")
    headers = header_cells.count()
    headers_data = []
        
    for i in range(headers):
        text = header_cells.nth(i).text_content().strip()
        headers_data.append(text)
    print(f"Headers: {headers_data}")

    for i in range(1, row_count):
        cells = rows.nth(i).locator("td")
        cell_count = cells.count()
        row_data = []
        for j in range(cell_count):
            text = cells.nth(j).text_content().strip()
            row_data.append(text)
        print(f"Row {i}: {row_data}")