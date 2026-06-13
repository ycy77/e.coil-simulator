---
entity_id: "gene.b3367"
entity_type: "gene"
name: "nirC"
source_database: "NCBI RefSeq"
source_id: "gene-b3367"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3367"
  - "nirC"
---

# nirC

`gene.b3367`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3367`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

nirC (gene.b3367) is a gene entity. It encodes nirC (protein.P0AC26). Encoded protein function: FUNCTION: Catalyzes nitrite uptake and nitrite export across the cytoplasmic membrane. Is up to 10-fold more active than NarK or NarU in nitrite uptake for subsequent reduction in the cytoplasm by the NirB/NirD nitrite reductase. {ECO:0000269|PubMed:11967075, ECO:0000269|PubMed:15667293, ECO:0000269|PubMed:18691156}. EcoCyc product frame: NIRC-MONOMER. Genomic coordinates: 3497003-3497809. EcoCyc protein note: NirC, encoded within the 4-gene nir operon , is an inner membrane nitrite channel that contributes to both nitrite uptake and nitrite efflux under anaerobic growth conditions (and see further ). Purified NirC, incorporated into liposomes, is permeable to nitrite, nitrate, and formate; it has low permeability to acetate and is impermeable to ammonium and magnesium cations. A pentameric structure has been modeled . In the Transporter Classification Database, NirC is a member of the Formate-Nitrate Transporter (FNT) family (see also ). Related review:

## Biological Role

Repressed by fis (protein.P0A6R3), hns (protein.P0ACF8), cra (protein.P0ACP1). Activated by rpoD (protein.P00579), fnr (protein.P0A9E5), narL (protein.P0AF28), narP (protein.P31802).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AC26|protein.P0AC26]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (7)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=nirC; function=+
- `activates` <-- [[protein.P0A9E5|protein.P0A9E5]] `RegulonDB` `C` - regulator=FNR; target=nirC; function=+
- `activates` <-- [[protein.P0AF28|protein.P0AF28]] `RegulonDB` `C` - regulator=NarL; target=nirC; function=+
- `activates` <-- [[protein.P31802|protein.P31802]] `RegulonDB` `C` - regulator=NarP; target=nirC; function=+
- `represses` <-- [[protein.P0A6R3|protein.P0A6R3]] `RegulonDB` `S` - regulator=Fis; target=nirC; function=-
- `represses` <-- [[protein.P0ACF8|protein.P0ACF8]] `RegulonDB` `S` - regulator=H-NS; target=nirC; function=-
- `represses` <-- [[protein.P0ACP1|protein.P0ACP1]] `RegulonDB` `S` - regulator=Cra; target=nirC; function=-

## External IDs

- `Dbxref:ASAP:ABE-0011008,ECOCYC:EG10654,GeneID:2847757`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3497003-3497809:+; feature_type=gene
