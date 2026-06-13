---
entity_id: "gene.b1805"
entity_type: "gene"
name: "fadD"
source_database: "NCBI RefSeq"
source_id: "gene-b1805"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1805"
  - "fadD"
---

# fadD

`gene.b1805`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1805`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

fadD (gene.b1805) is a gene entity. It encodes fadD (protein.P69451). Encoded protein function: FUNCTION: Catalyzes the esterification, concomitant with transport, of exogenous long-chain fatty acids into metabolically active CoA thioesters for subsequent degradation or incorporation into phospholipids. Activity is the highest with fatty acid substrates of > 10 carbon atoms (PubMed:15213221). Is involved in the aerobic beta-oxidative degradation of fatty acids, which allows aerobic growth of E.coli on fatty acids as a sole carbon and energy source (PubMed:12535077). {ECO:0000269|PubMed:12535077, ECO:0000269|PubMed:15213221}. EcoCyc product frame: ACYLCOASYN-MONOMER. EcoCyc synonyms: oldD. Genomic coordinates: 1888061-1889746.

## Biological Role

Repressed by fadR (protein.P0A8V6), arcA (protein.P0A9Q1), rob (protein.P0ACI0). Activated by rpoD (protein.P00579), crp (protein.P0ACJ8).

## Enriched Pathways

- `eco00061` Fatty acid biosynthesis (KEGG)
- `eco00071` Fatty acid degradation (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01212` Fatty acid metabolism (KEGG)
- `eco02024` Quorum sensing (KEGG)
- `eco04146` Peroxisome (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P69451|protein.P69451]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (5)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=fadD; function=+
- `activates` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `S` - regulator=CRP; target=fadD; function=+
- `represses` <-- [[protein.P0A8V6|protein.P0A8V6]] `RegulonDB` `S` - regulator=FadR; target=fadD; function=-
- `represses` <-- [[protein.P0A9Q1|protein.P0A9Q1]] `RegulonDB` `C` - regulator=ArcA; target=fadD; function=-
- `represses` <-- [[protein.P0ACI0|protein.P0ACI0]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0006005,ECOCYC:EG11530,GeneID:946327`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1888061-1889746:-; feature_type=gene
