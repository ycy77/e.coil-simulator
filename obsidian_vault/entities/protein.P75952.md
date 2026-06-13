---
entity_id: "protein.P75952"
entity_type: "protein"
name: "comR"
source_database: "UniProt"
source_id: "P75952"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "comR ycfQ b1111 JW5159"
---

# comR

`protein.P75952`

## Static

- Type: `protein`
- Source: `UniProt:P75952`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Represses expression of BhsA/ComC by binding to its promoter region in the absence of copper. {ECO:0000269|PubMed:22089859}. ComR is a member of the TetR family of transcriptional repressors and has been implicated in the the response of E. coli K-12 to copper. ComR contains a helix-turn-helix motif to bind DNA in its N-terminal domain . In in vitro experiments, ComR binds to a 60 bp promotor region upstream of the comC gene but is released in the presence of copper, silver or gold. Expression of comC is dramatically increased (approx 270 fold) in a comR negative strain upon exposure to 3mM copper. comR knockout mutants have lower cytoplasmic copper levels compared to the wild type when exposed to copper . Expression of comR is not affected by copper , but its expression is affected by cadmium . Genome-wide ComR binding sites were determined in vivo in M9 glucose minimal medium by chromatin immunoprecipitation assays (ChIP-exo) . Various target genes of ComR were found upregulated after 10 min of exposure to 2.5 mM H2O2, despite the comR gene being slightly upregulated . Review: .

## Biological Role

Component of ComR-Cu+ (complex.ecocyc.CPLX0-8074).

## Annotation

FUNCTION: Represses expression of BhsA/ComC by binding to its promoter region in the absence of copper. {ECO:0000269|PubMed:22089859}.

## Outgoing Edges (2)

- `is_component_of` --> [[complex.ecocyc.CPLX0-8074|complex.ecocyc.CPLX0-8074]] `EcoCyc` `database` - EcoCyc component coefficient=
- `represses` --> [[gene.b1112|gene.b1112]] `RegulonDB` `S` - regulator=ComR; target=bhsA; function=-

## Incoming Edges (1)

- `encodes` <-- [[gene.b1111|gene.b1111]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P75952`
- `KEGG:ecj:JW5159;eco:b1111;ecoc:C3026_06700;`
- `GeneID:947425;`
- `GO:GO:0000976; GO:0003677; GO:0003700; GO:0006355; GO:0045892; GO:0046688`

## Notes

HTH-type transcriptional repressor ComR (Copper outer membrane regulator)
