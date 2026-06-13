---
entity_id: "gene.b0795"
entity_type: "gene"
name: "ybhG"
source_database: "NCBI RefSeq"
source_id: "gene-b0795"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0795"
  - "ybhG"
---

# ybhG

`gene.b0795`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0795`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ybhG (gene.b0795) is a gene entity. It encodes ybhG (protein.P75777). Encoded protein function: FUNCTION: Could be involved in the sensitivity control to chloramphenicol. {ECO:0000305|PubMed:27112147}. EcoCyc product frame: G6412-MONOMER. Genomic coordinates: 828974-829972. EcoCyc protein note: ΔybhG mutants show reduced growth in the presence of chloramphenicol and the third generation cephalosporin - cefoperazone . YbhG belongs to the HlyD_D23 family of proteins - defined in the Pfam database as 'the combined domains 2 and 3 of the membrane-fusion proteins CusB and HlyD, which forms a barrel-sandwich'. Transcription of the ybhG-containing operon (cecR-ybhGFSR) is negatively regulated by EG12406-MONOMER "CecR" . The mechanism by which YbhG contributes to drug resistance is not clear. Membrane fusion proteins typically function with RND family proteins plus an outer membrane factor to mediate export. The ybhF, ybhS and ybhR genes located in this operon encode the components of a putative ABC exporter implicated in the efflux of cefoperazone and tetracycline antibiotics . In the Transporter Classification Database YbhGFSR is annotated as a 4-component system within the ATP-binding Cassette (ABC) superfamily .

## Biological Role

Repressed by cecR (protein.P0ACU0).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P75777|protein.P75777]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.P0ACU0|protein.P0ACU0]] `RegulonDB` `C` - regulator=CecR; target=ybhG; function=-

## External IDs

- `Dbxref:ASAP:ABE-0002709,ECOCYC:G6412,GeneID:945414`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:828974-829972:-; feature_type=gene
