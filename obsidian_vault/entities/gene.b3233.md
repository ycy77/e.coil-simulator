---
entity_id: "gene.b3233"
entity_type: "gene"
name: "yhcB"
source_database: "NCBI RefSeq"
source_id: "gene-b3233"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3233"
  - "yhcB"
---

# yhcB

`gene.b3233`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3233`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yhcB (gene.b3233) is a gene entity. It encodes zapG (protein.P0ADW3). Encoded protein function: FUNCTION: Involved in cell division, cell envelope biogenesis and cell shape maintenance (PubMed:27335665, PubMed:32323199, PubMed:33895137, PubMed:34941903). Is a key regulator of cell envelope growth, playing a crucial role in coordinating cell width, elongation and division to maintain cell envelope integrity (PubMed:34941903). Plays an important role in the lipopolysaccharide (LPS) assembly/transport (PubMed:36077106). It may regulate LpxC levels and assist MsbA-mediated LPS transport (PubMed:36077106). {ECO:0000269|PubMed:27335665, ECO:0000269|PubMed:32323199, ECO:0000269|PubMed:33895137, ECO:0000269|PubMed:34941903, ECO:0000269|PubMed:36077106}. EcoCyc product frame: G7681-MONOMER. EcoCyc synonyms: lapD, zapG. Genomic coordinates: 3380191-3380589. EcoCyc protein note: In a study of membrane protein complexes, YhcB (later named ZapG/LapD ) was found together with CydA and CydB in the inner membrane and was suggested to be a new subunit of the CYT-D-UBIOX-CPLX . However, it was later shown that YhcB is not associated with the CydAB heterodimer and is not required for the assembly or function of cytochrome bd . Proteomic analysis of membrane preparations suggests that YhcB may form a homo-oligomeric complex . The C-terminus of YhcB is located in the cytoplasm...

## Biological Role

Repressed by sdsR (gene.b4433).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0ADW3|protein.P0ADW3]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[gene.b4433|gene.b4433]] `RegulonDB` `S` - regulator=SdsR; target=yhcB; function=-

## External IDs

- `Dbxref:ASAP:ABE-0010606,ECOCYC:G7681,GeneID:947815`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3380191-3380589:+; feature_type=gene
