---
entity_id: "gene.b3390"
entity_type: "gene"
name: "aroK"
source_database: "NCBI RefSeq"
source_id: "gene-b3390"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3390"
  - "aroK"
---

# aroK

`gene.b3390`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3390`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

aroK (gene.b3390) is a gene entity. It encodes aroK (protein.P0A6D7). Encoded protein function: FUNCTION: Catalyzes the specific phosphorylation of the 3-hydroxyl group of shikimic acid using ATP as a cosubstrate. {ECO:0000269|PubMed:1309529}. EcoCyc product frame: AROK-MONOMER. Genomic coordinates: 3518543-3519064. EcoCyc protein note: Shikimate kinase catalyzes the fifth step in the ARO-PWY pathway. Chorismate is the common precursor for the biosynthesis of the aromatic amino acids tyrosine, phenylalanine and tryptophan. The existence of two shikimate kinase isozymes was initially suggested because sucrose density gradient centrifugation and column chromatography of cell extracts showed two peaks of shikimate kinase activity. Although shikimate kinase 1 (AroK, described here) has not been assayed in pure form, mention that AroK has an approximately 100-fold lower affinity for shikimate than AROL-MONOMER (AroL). A fortuituously obtained L133P mutant of AroK appears to have lost shikimate kinase activity . The reportedly high KM value of AroK for shikimate suggested that the enzyme may have a different primary function in the cell . However, using purified AroK, the KM for shikimiate is 400 µM, similar to AroL's KM of 200 µM ; the specific activity of purified AroK is less than a third of that of AroL...

## Biological Role

Repressed by ArgR-L-arginine DNA-binding transcriptional dual regulator (complex.ecocyc.CPLX0-228), argR (protein.P0A6D0). Activated by rpoD (protein.P00579).

## Enriched Pathways

- `eco00400` Phenylalanine, tyrosine and tryptophan biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01230` Biosynthesis of amino acids (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A6D7|protein.P0A6D7]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=aroK; function=+
- `represses` <-- [[complex.ecocyc.CPLX0-228|complex.ecocyc.CPLX0-228]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[protein.P0A6D0|protein.P0A6D0]] `RegulonDB` `S` - regulator=ArgR; target=aroK; function=-

## External IDs

- `Dbxref:ASAP:ABE-0011069,ECOCYC:EG10081,GeneID:2847759`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3518543-3519064:-; feature_type=gene
