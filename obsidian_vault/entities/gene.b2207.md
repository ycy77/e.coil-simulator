---
entity_id: "gene.b2207"
entity_type: "gene"
name: "napD"
source_database: "NCBI RefSeq"
source_id: "gene-b2207"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2207"
  - "napD"
---

# napD

`gene.b2207`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2207`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

napD (gene.b2207) is a gene entity. It encodes napD (protein.P0A9I5). Encoded protein function: FUNCTION: Chaperone for NapA, the catalytic subunit of the periplasmic nitrate reductase. It binds directly and specifically to the twin-arginine signal peptide of NapA, preventing premature interaction with the Tat translocase and premature export (PubMed:17901208, PubMed:22329966). May have a role in the insertion of the NapA molybdenum cofactor (PubMed:24314029). {ECO:0000269|PubMed:17901208, ECO:0000269|PubMed:22329966, ECO:0000269|PubMed:24314029}. EcoCyc product frame: NAPD-MONOMER. EcoCyc synonyms: yojF. Genomic coordinates: 2302750-2303013. EcoCyc protein note: NapD is a dedicated chaperone for EG12067 NapA, the molybdoprotein subunit of the periplasmic nitrate reductase. It binds specifically to the twin-arginine signal peptide of NapA, preventing premature export. In the absence of NapD, NapA is unstable and degraded . NapD defines a second family of twin-arginine signal peptide binding proteins (see also the EG12195-MONOMER "TorD" chaperone). The solution structure of NapD has been solved, showing a ferredoxin-like fold . A NapD binding epitope is located towards the N-terminus of the NapA signal peptide and partially overlaps with the twin arginine motif . An NMR structure of the NapD-NapA signal peptide complex has been reported...

## Biological Role

Repressed by narL (protein.P0AF28), iscR (protein.P0AGK8), narP (protein.P31802). Activated by rpoD (protein.P00579), fnr (protein.P0A9E5), modE (protein.P0A9G8), narP (protein.P31802).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A9I5|protein.P0A9I5]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (7)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=napD; function=+
- `activates` <-- [[protein.P0A9E5|protein.P0A9E5]] `RegulonDB` `C` - regulator=FNR; target=napD; function=+
- `activates` <-- [[protein.P0A9G8|protein.P0A9G8]] `RegulonDB` `C` - regulator=ModE; target=napD; function=+
- `activates` <-- [[protein.P31802|protein.P31802]] `RegulonDB` `S` - regulator=NarP; target=napD; function=-+
- `represses` <-- [[protein.P0AF28|protein.P0AF28]] `RegulonDB` `S` - regulator=NarL; target=napD; function=-
- `represses` <-- [[protein.P0AGK8|protein.P0AGK8]] `RegulonDB` `S` - regulator=IscR; target=napD; function=-
- `represses` <-- [[protein.P31802|protein.P31802]] `RegulonDB` `S` - regulator=NarP; target=napD; function=-+

## External IDs

- `Dbxref:ASAP:ABE-0007291,ECOCYC:EG12143,GeneID:945187`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2302750-2303013:-; feature_type=gene
