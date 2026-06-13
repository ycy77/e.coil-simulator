---
entity_id: "gene.b2416"
entity_type: "gene"
name: "ptsI"
source_database: "NCBI RefSeq"
source_id: "gene-b2416"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2416"
  - "ptsI"
---

# ptsI

`gene.b2416`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2416`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ptsI (gene.b2416) is a gene entity. It encodes ptsI (protein.P08839). Encoded protein function: FUNCTION: General (non sugar-specific) component of the phosphoenolpyruvate-dependent sugar phosphotransferase system (sugar PTS). This major carbohydrate active-transport system catalyzes the phosphorylation of incoming sugar substrates concomitantly with their translocation across the cell membrane. Enzyme I transfers the phosphoryl group from phosphoenolpyruvate (PEP) to the phosphoryl carrier protein (HPr) (PubMed:12705838, PubMed:17053069, PubMed:7876255). Can also use (Z)-3-fluoro-PEP (ZFPEP), (Z)-3-methyl-PEP (ZMePEP), (Z)-3-chloro-PEP (ZClPEP) and (E)-3-chloro-PEP (EClPEP) as alternative phosphoryl donors (PubMed:12705838). {ECO:0000269|PubMed:12705838, ECO:0000269|PubMed:17053069, ECO:0000269|PubMed:7876255}. EcoCyc product frame: PTSI-MONOMER. EcoCyc synonyms: ctr. Genomic coordinates: 2534066-2535793.

## Biological Role

Repressed by crp (protein.P0ACJ8), cra (protein.P0ACP1), mlc (protein.P50456). Activated by rpoD (protein.P00579), crp (protein.P0ACJ8), cra (protein.P0ACP1), rpoH (protein.P0AGB3).

## Enriched Pathways

- `eco02060` Phosphotransferase system (PTS) (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P08839|protein.P08839]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (7)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=ptsI; function=+
- `activates` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `S` - regulator=CRP; target=ptsI; function=-+
- `activates` <-- [[protein.P0ACP1|protein.P0ACP1]] `RegulonDB` `C` - regulator=Cra; target=ptsI; function=-+
- `activates` <-- [[protein.P0AGB3|protein.P0AGB3]] `RegulonDB` `S` - sigma=sigma32; target=ptsI; function=+
- `represses` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `S` - regulator=CRP; target=ptsI; function=-+
- `represses` <-- [[protein.P0ACP1|protein.P0ACP1]] `RegulonDB` `C` - regulator=Cra; target=ptsI; function=-+
- `represses` <-- [[protein.P50456|protein.P50456]] `RegulonDB` `S` - regulator=Mlc; target=ptsI; function=-

## External IDs

- `Dbxref:ASAP:ABE-0007967,ECOCYC:EG10789,GeneID:946879`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2534066-2535793:+; feature_type=gene
