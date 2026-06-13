---
entity_id: "gene.b1702"
entity_type: "gene"
name: "ppsA"
source_database: "NCBI RefSeq"
source_id: "gene-b1702"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1702"
  - "ppsA"
---

# ppsA

`gene.b1702`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1702`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ppsA (gene.b1702) is a gene entity. It encodes ppsA (protein.P23538). Encoded protein function: FUNCTION: Catalyzes the phosphorylation of pyruvate to phosphoenolpyruvate. {ECO:0000269|PubMed:4319237}. EcoCyc product frame: PEPSYNTH-MONOMER. EcoCyc synonyms: pps. Genomic coordinates: 1784734-1787112.

## Biological Role

Repressed by lrp (protein.P0ACJ0). Activated by rpoD (protein.P00579), pdhR (protein.P0ACL9), cra (protein.P0ACP1).

## Enriched Pathways

- `eco00010` Glycolysis / Gluconeogenesis (KEGG)
- `eco00620` Pyruvate metabolism (KEGG)
- `eco00680` Methane metabolism (KEGG)
- `eco00720` Other carbon fixation pathways (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01200` Carbon metabolism (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P23538|protein.P23538]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (4)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=ppsA; function=+
- `activates` <-- [[protein.P0ACL9|protein.P0ACL9]] `RegulonDB|EcoCyc` `C` - regulator=PdhR; target=ppsA; function=+ | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` <-- [[protein.P0ACP1|protein.P0ACP1]] `RegulonDB` `C` - regulator=Cra; target=ppsA; function=+
- `represses` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0005678,ECOCYC:EG10759,GeneID:946209`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1784734-1787112:-; feature_type=gene
