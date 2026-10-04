# PRIVATE answer key — product data consolidation task (do NOT upload to the task repo or give to the agent)

## Phase 1

### Shopify variants (SKU = Sage code)

| SKU | barcode | price | qty | available | MAP | note |
|---|---|---|---|---|---|---|
| NHG-1001-BLU | 5060123400014 | 22.99 | 19 | 21 | 22.99 |  |
| NHG-1001-GRN | 5060123400021 | 22.99 | 9 | 11 | 22.99 |  |
| NHG-1001-RED | 5060123400038 | 22.99 | 0 | 4 | 22.99 | inactive |
| NHG-1002-S | 5060123400045 | 13.99 | 24 | 26 | 13.99 |  |
| NHG-1002-L | 5060123400052 | 15.00 | 14 | 16 | 14.99 |  |
| NHG-1003 | 5060123400069 | 11.94 | 12 | 14 | — |  |
| NHG-1004 | 5060123400076 | 14.99 | 7 | 9 | 14.99 |  |
| NHG-1005 | 5060123400083 | 39.99 | 4 | 6 | 39.99 |  |
| NHG-2001 | 5060123400090 | 2.49 | 128 | 130 | 2.49 |  |
| NHG-2002 | 5060123400106 | 2.49 | 88 | 90 | 2.49 |  |
| NHG-2003 | 5060123400113 | 2.49 | 118 | 120 | 2.49 |  |
| NHG-2004 | 5060123400120 | 6.50 | 36 | 38 | — |  |
| NHG-2005 | 5060123400137 | 9.99 | 20 | 22 | 9.99 |  |
| NHG-3001 | 5060123400144 | 16.20 | 12 | 14 | — |  |
| NHG-3002-GRY | 5060123400151 | 5.99 | 0 | 0 | 5.99 |  |
| NHG-3002-SGE | 5060123400168 | 5.99 | 16 | 18 | 5.99 |  |
| NHG-3003-S | 5060123400175 | 8.64 | 24 | 26 | — |  |
| NHG-3003-L | 5060123400182 | 12.96 | 10 | 12 | — |  |
| NHG-3004 | 5060123400199 | 34.99 | 4 | 6 | 34.99 |  |
| NHG-3005-S | 5060123400205 | 9.90 | 10 | 12 | — |  |
| NHG-3005-M | 5060123400212 | 9.90 | 26 | 28 | — |  |
| NHG-3005-L | 5060123400229 | 9.90 | 18 | 20 | — |  |
| NHG-3005-XL | 5060123400236 | 9.90 | 0 | 2 | — |  |
| NHG-3006 | 5060123400243 | 7.99 | 40 | 42 | 7.99 |  |
| NHG-3007 | 5060123400250 | 3.48 | 58 | 60 | — |  |
| NHG-3008 | 5060123400267 | 8.16 | 0 | 0 | — |  |
| NHG-3009-1M | 5060123400274 | 44.99 | 6 | 8 | 44.99 |  |
| NHG-3009-2M | 5060123400281 | 69.99 | 1 | 3 | 69.99 |  |
| NHG-3010 | 5060123400298 | 14.88 | 14 | 16 | — |  |
| NHG-3011 | 5060123400304 | 4.50 | 23 | 25 | — |  |
| NHG-3012 | 5060123400311 | 6.49 | 30 | 32 | 6.49 |  |
| NHG-KIT-01 | 5060123400328 | 21.60 | 12 | 14 | — |  |

### Amazon feed rows

| sku | price | min | max | qty | handling | channel | note |
|---|---|---|---|---|---|---|---|
| NHG-1001-BLU | 24.99 | 22.99 | 49.98 | 19 | 2 | DEFAULT |  |
| NHG-1001-BLU-FBA | 28.99 | 22.99 | 57.98 |  |  | AMAZON_EU | FBA qty 18 |
| NHG-1001-GRN | 24.99 | 22.99 | 49.98 | 9 | 2 | DEFAULT |  |
| NHG-1001-RED | 24.99 | 22.99 | 49.98 | 0 | 2 | DEFAULT | inactive |
| NHG-1002-S | 15.99 | 13.99 | 31.98 | 24 | 2 | DEFAULT |  |
| NHG-1002-S-FBA | 17.99 | 13.99 | 35.98 |  |  | AMAZON_EU | FBA qty 0 |
| NHG-1002-L | 16.99 | 14.99 | 33.98 | 14 | 2 | DEFAULT |  |
| 7K-QX2M-R4LD | 12.99 | 11.94 | 25.98 | 12 | 2 | DEFAULT |  |
| NHG-1005-FBA | 49.99 | 39.99 | 99.98 |  |  | AMAZON_EU | FBA qty 5 |
| NHG-2001 | 2.99 | 2.49 | 5.98 | 128 | 2 | DEFAULT |  |
| NHG-2001-X3 | 7.99 |  | 15.98 | 42 | 2 | DEFAULT | multipack x3 |
| NHG-2002-X3 | 7.99 |  | 15.98 | 29 | 2 | DEFAULT | multipack x3 |
| NHG-2005 | 10.99 | 9.99 | 21.98 | 20 | 2 | DEFAULT |  |
| NHG-3002-GRY-FBA | 8.99 | 5.99 | 17.98 |  |  | AMAZON_EU | FBA qty 22 |
| NHG-3002-SGE | 6.99 | 5.99 | 13.98 | 16 | 2 | DEFAULT |  |
| NHG-3003-L-FBA | 17.99 | 12.96 | 35.98 |  |  | AMAZON_EU | FBA qty 9 |
| NHG-3003-S | 9.99 | 8.64 | 19.98 | 24 | 2 | DEFAULT |  |
| 9B-HT4N-77PC | 37.99 | 34.99 | 75.98 | 4 | 2 | DEFAULT |  |
| NHG-3005-M-FBA | 13.99 | 9.90 | 27.98 |  |  | AMAZON_EU | FBA qty 31 |
| NHG-3005-L | 10.99 | 9.90 | 21.98 | 18 | 2 | DEFAULT |  |
| NHG-3006 | 8.99 | 7.99 | 17.98 | 40 | 2 | DEFAULT |  |
| NHG-3006-X3 | 23.99 |  | 47.98 | 13 | 2 | DEFAULT | multipack x3 |
| 2M-ZK8W-05TJ | 3.99 | 3.48 | 7.98 | 58 | 2 | DEFAULT |  |
| NHG-3007-X2 | 6.99 |  | 13.98 | 29 | 2 | DEFAULT | multipack x2 |
| NHG-3009-1M | 48.99 | 44.99 | 97.98 | 6 | 2 | DEFAULT |  |
| NHG-3010 | 16.99 | 14.88 | 33.98 | 14 | 2 | DEFAULT |  |
| 5R-LP3C-K9VE | 4.99 | 4.50 | 9.98 | 23 | 2 | DEFAULT |  |
| NHG-3012 | 7.99 | 6.49 | 15.98 | 30 | 2 | DEFAULT |  |
| NHG-KIT-01 | 23.99 | 21.60 | 47.98 | 12 | 2 | DEFAULT |  |
| NHG-0999 | 4.99 |  |  | 0 | 2 | DEFAULT | orphan |

## Final (after client_update)

### Shopify variants (SKU = Sage code)

| SKU | barcode | price | qty | available | MAP | note |
|---|---|---|---|---|---|---|
| NHG-1001-BLU | 5060123400014 | 24.99 | 19 | 21 | 24.99 |  |
| NHG-1001-GRN | 5060123400021 | 24.99 | 7 | 9 | 24.99 |  |
| NHG-1001-RED | 5060123400038 | 24.99 | 0 | 4 | 24.99 | inactive |
| NHG-1002-S | 5060123400045 | 15.49 | 24 | 26 | 15.49 |  |
| NHG-1002-L | 5060123400052 | 15.00 | 14 | 16 | 14.99 |  |
| NHG-1003 | 5060123400069 | 11.94 | 12 | 14 | — |  |
| NHG-1004 | 5060123400076 | 16.99 | 7 | 9 | 16.99 |  |
| NHG-1005 | 5060123400083 | 39.99 | 4 | 6 | 39.99 |  |
| NHG-2001 | 5060123400090 | 2.49 | 128 | 130 | 2.49 |  |
| NHG-2002 | 5060123400106 | 2.49 | 88 | 90 | 2.49 |  |
| NHG-2003 | 5060123400113 | 2.49 | 116 | 118 | 2.49 |  |
| NHG-2004 | 5060123400120 | 6.50 | 36 | 38 | — |  |
| NHG-2005 | 5060123400137 | 9.99 | 20 | 22 | 9.99 |  |
| NHG-3001 | 5060123400144 | 16.20 | 0 | 0 | — |  |
| NHG-3002-GRY | 5060123400151 | 5.99 | 5 | 7 | 5.99 |  |
| NHG-3002-SGE | 5060123400168 | 5.99 | 16 | 18 | 5.99 |  |
| NHG-3003-S | 5060123400175 | 8.64 | 0 | 26 | — | inactive |
| NHG-3003-L | 5060123400182 | 12.96 | 10 | 12 | — |  |
| NHG-3004 | 5060123400199 | 34.99 | 4 | 6 | 34.99 |  |
| NHG-3005-S | 5060123400205 | 9.90 | 10 | 12 | — |  |
| NHG-3005-M | 5060123400212 | 9.90 | 26 | 28 | — |  |
| NHG-3005-L | 5060123400229 | 9.90 | 18 | 20 | — |  |
| NHG-3005-XL | 5060123400236 | 9.90 | 0 | 2 | — |  |
| NHG-3006 | 5060123400243 | 7.99 | 40 | 42 | 7.99 |  |
| NHG-3007 | 5060123400250 | 3.48 | 58 | 60 | — |  |
| NHG-3008 | 5060123400267 | 8.16 | 1 | 3 | — |  |
| NHG-3009-1M | 5060123400274 | 44.99 | 6 | 8 | 44.99 |  |
| NHG-3009-2M | 5060123400281 | 69.99 | 0 | 2 | 69.99 |  |
| NHG-3010 | 5060123400298 | 14.88 | 14 | 16 | — |  |
| NHG-3011 | 5060123400304 | 4.50 | 23 | 25 | — |  |
| NHG-3012 | 5060123400311 | 6.49 | 30 | 32 | 6.49 |  |
| NHG-KIT-01 | 5060123400328 | 21.60 | 0 | 0 | — |  |

### Amazon feed rows

| sku | price | min | max | qty | handling | channel | note |
|---|---|---|---|---|---|---|---|
| NHG-1001-BLU | 26.99 | 24.99 | 53.98 | 19 | 2 | DEFAULT |  |
| NHG-1001-BLU-FBA | 30.99 | 24.99 | 61.98 |  |  | AMAZON_EU | FBA qty 15 |
| NHG-1001-GRN | 26.99 | 24.99 | 53.98 | 7 | 2 | DEFAULT |  |
| NHG-1001-RED | 26.99 | 24.99 | 53.98 | 0 | 2 | DEFAULT | inactive |
| NHG-1002-S | 16.99 | 15.49 | 33.98 | 24 | 2 | DEFAULT |  |
| NHG-1002-S-FBA | 19.99 | 15.49 | 39.98 |  |  | AMAZON_EU | FBA qty 12 |
| NHG-1002-L | 16.99 | 14.99 | 33.98 | 14 | 2 | DEFAULT |  |
| 7K-QX2M-R4LD | 12.99 | 11.94 | 25.98 | 12 | 2 | DEFAULT |  |
| NHG-1005-FBA | 49.99 | 39.99 | 99.98 |  |  | AMAZON_EU | FBA qty 5 |
| NHG-2001 | 2.99 | 2.49 | 5.98 | 128 | 2 | DEFAULT |  |
| NHG-2001-X3 | 7.99 |  | 15.98 | 42 | 2 | DEFAULT | multipack x3 |
| NHG-2002-X3 | 7.99 |  | 15.98 | 29 | 2 | DEFAULT | multipack x3 |
| NHG-2005 | 10.99 | 9.99 | 21.98 | 20 | 2 | DEFAULT |  |
| NHG-3002-GRY-FBA | 8.99 | 5.99 | 17.98 |  |  | AMAZON_EU | FBA qty 20 |
| NHG-3002-SGE | 6.99 | 5.99 | 13.98 | 16 | 2 | DEFAULT |  |
| NHG-3003-L-FBA | 17.99 | 12.96 | 35.98 |  |  | AMAZON_EU | FBA qty 0 |
| NHG-3003-S | 9.99 | 8.64 | 19.98 | 0 | 2 | DEFAULT | inactive |
| 9B-HT4N-77PC | 37.99 | 34.99 | 75.98 | 4 | 2 | DEFAULT |  |
| NHG-3005-M-FBA | 13.99 | 9.90 | 27.98 |  |  | AMAZON_EU | FBA qty 28 |
| NHG-3005-L | 10.99 | 9.90 | 21.98 | 18 | 2 | DEFAULT |  |
| NHG-3006 | 8.99 | 7.99 | 17.98 | 40 | 2 | DEFAULT |  |
| NHG-3006-X3 | 23.99 |  | 47.98 | 13 | 2 | DEFAULT | multipack x3 |
| 2M-ZK8W-05TJ | 3.99 | 3.48 | 7.98 | 58 | 2 | DEFAULT |  |
| NHG-3007-X2 | 6.99 |  | 13.98 | 29 | 2 | DEFAULT | multipack x2 |
| NHG-3009-1M | 48.99 | 44.99 | 97.98 | 6 | 2 | DEFAULT |  |
| NHG-3010 | 16.99 | 14.88 | 33.98 | 14 | 2 | DEFAULT |  |
| 5R-LP3C-K9VE | 4.99 | 4.50 | 9.98 | 23 | 2 | DEFAULT |  |
| NHG-3012 | 7.99 | 6.49 | 15.98 | 30 | 2 | DEFAULT |  |
| NHG-KIT-01 | 23.99 | 21.60 | 47.98 | 0 | 2 | DEFAULT |  |
| NHG-0999 | 4.99 |  |  | 0 | 2 | DEFAULT | orphan |

## What changes in the final phase

| item | field | phase 1 | final |
|---|---|---|---|
| Shopify NHG-1001-BLU | price | 22.99 | 24.99 |
| Shopify NHG-1001-GRN | price | 22.99 | 24.99 |
| Shopify NHG-1001-GRN | qty | 9 | 7 |
| Shopify NHG-1001-RED | price | 22.99 | 24.99 |
| Shopify NHG-1002-S | price | 13.99 | 15.49 |
| Shopify NHG-1004 | price | 14.99 | 16.99 |
| Shopify NHG-2003 | qty | 118 | 116 |
| Shopify NHG-3001 | qty | 12 | 0 |
| Shopify NHG-3002-GRY | qty | 0 | 5 |
| Shopify NHG-3003-S | qty | 24 | 0 |
| Shopify NHG-3008 | qty | 0 | 1 |
| Shopify NHG-3009-2M | qty | 1 | 0 |
| Shopify NHG-KIT-01 | qty | 12 | 0 |
| Amazon NHG-1001-BLU | price | 24.99 | 26.99 |
| Amazon NHG-1001-BLU | min | 22.99 | 24.99 |
| Amazon NHG-1001-BLU | max | 49.98 | 53.98 |
| Amazon NHG-1001-BLU-FBA | price | 28.99 | 30.99 |
| Amazon NHG-1001-BLU-FBA | min | 22.99 | 24.99 |
| Amazon NHG-1001-BLU-FBA | max | 57.98 | 61.98 |
| Amazon NHG-1001-GRN | price | 24.99 | 26.99 |
| Amazon NHG-1001-GRN | min | 22.99 | 24.99 |
| Amazon NHG-1001-GRN | max | 49.98 | 53.98 |
| Amazon NHG-1001-GRN | qty | 9 | 7 |
| Amazon NHG-1001-RED | price | 24.99 | 26.99 |
| Amazon NHG-1001-RED | min | 22.99 | 24.99 |
| Amazon NHG-1001-RED | max | 49.98 | 53.98 |
| Amazon NHG-1002-S | price | 15.99 | 16.99 |
| Amazon NHG-1002-S | min | 13.99 | 15.49 |
| Amazon NHG-1002-S | max | 31.98 | 33.98 |
| Amazon NHG-1002-S-FBA | price | 17.99 | 19.99 |
| Amazon NHG-1002-S-FBA | min | 13.99 | 15.49 |
| Amazon NHG-1002-S-FBA | max | 35.98 | 39.98 |
| Amazon NHG-3003-S | qty | 24 | 0 |
| Amazon NHG-KIT-01 | qty | 12 | 0 |

## Fixed decisions / traps
- **Sage barcodes to correct (sage_updates.csv):** NHG-1005, NHG-3002-SGE, NHG-3004, NHG-3011 (scientific notation → from Shopify); NHG-1002-L (bad check digit → Shopify 5060123400052); NHG-3007 (carries NHG-3006's EAN; Shopify blank → Amazon product-id for 2M-ZK8W-05TJ = 5060123400250).
- **Shopify barcode fixes:** NHG-3005-L (bad check digit → Sage 5060123400229); NHG-3007 (blank → 5060123400250).
- **Shopify SKU fixes:** nhg1002-s→NHG-1002-S, NHG3005XL→NHG-3005-XL, nhg-2003→NHG-2003, NHG-3009-2m→NHG-3009-2M, "NHG 1004"→NHG-1004, blank (Bird Feeder Large, matched by barcode)→NHG-3003-L.
- **Duplicate Shopify product:** "Slate Plant Labels - 10 Pack" (draft, sku NHG-3006) → archived.
- **Auto Amazon SKUs:** 7K-QX2M-R4LD=NHG-1003, 9B-HT4N-77PC=NHG-3004, 2M-ZK8W-05TJ=NHG-3007, 5R-LP3C-K9VE=NHG-3011 (match by EAN; 3004/3007 need the corrected barcode, not Sage's). Orphan: NHG-0999 (Wooden Dibber) → qty 0, price 4.99.
- **Inactive:** NHG-1001-RED (phase 1) → Shopify qty 0, Amazon qty 0; product stays active. Final: also NHG-3003-S.
- **Stock exceptions:** NHG-3008 negative QTY_IN_STOCK (-2) → 0 (final: counted 15 − 12 alloc = 3 → qty 1); NHG-3002-GRY allocated 7 > in-stock 5 → 0 (final 14−7 = 7 → qty 5).
- **Kit:** phase 1 min(130, 90, 120, 14) = 14 → qty 12; final trough counted 1 − 2 alloc → 0 → kit qty 0.
- **MAP binds** wherever gross < MAP (e.g. watering cans 18.00 → 22.99; final 24.99). Seeds are T0 (no VAT).
- **Mock API behaviour:** Shopify 4 calls/s → 429; price must be a 2-decimal string; invalid EAN → 422. Amazon: FBA rows with a quantity or handling-time error out; price < min errors; feed polling IN_QUEUE → IN_PROGRESS → DONE.
