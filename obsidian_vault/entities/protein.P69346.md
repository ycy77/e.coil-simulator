---
entity_id: "protein.P69346"
entity_type: "protein"
name: "yefM"
source_database: "UniProt"
source_id: "P69346"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "yefM b2017 JW5835"
---

# yefM

`protein.P69346`

## Static

- Type: `protein`
- Source: `UniProt:P69346`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Antitoxin component of a type II toxin-antitoxin (TA) system. Antitoxin that counteracts the effect of the YoeB toxin. YefM binds to the promoter region of the yefM-yeoB operon to repress transcription, YeoB acts as a corepressor. {ECO:0000269|PubMed:14672926, ECO:0000269|PubMed:15009896, ECO:0000269|PubMed:17170003, ECO:0000269|PubMed:19028895}.

## Biological Role

Component of YefM-YoeB antitoxin/toxin complex / DNA-binding transcriptional repressor (complex.ecocyc.CPLX0-3781), antitoxin/DNA-binding transcriptional repressor YefM (complex.ecocyc.CPLX0-7929).

## Annotation

FUNCTION: Antitoxin component of a type II toxin-antitoxin (TA) system. Antitoxin that counteracts the effect of the YoeB toxin. YefM binds to the promoter region of the yefM-yeoB operon to repress transcription, YeoB acts as a corepressor. {ECO:0000269|PubMed:14672926, ECO:0000269|PubMed:15009896, ECO:0000269|PubMed:17170003, ECO:0000269|PubMed:19028895}.

## Outgoing Edges (4)

- `is_component_of` --> [[complex.ecocyc.CPLX0-3781|complex.ecocyc.CPLX0-3781]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2
- `is_component_of` --> [[complex.ecocyc.CPLX0-7929|complex.ecocyc.CPLX0-7929]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2
- `represses` --> [[gene.b2017|gene.b2017]] `RegulonDB` `S` - regulator=YefM; target=yefM; function=-
- `represses` --> [[gene.b4539|gene.b4539]] `RegulonDB` `C` - regulator=YefM; target=yoeB; function=-

## Incoming Edges (1)

- `encodes` <-- [[gene.b2017|gene.b2017]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P69346`
- `KEGG:ecj:JW5835;eco:b2017;ecoc:C3026_11380;`
- `GeneID:86946971;93775156;946542;`
- `GO:GO:0003700; GO:0006355; GO:0015643; GO:0040008; GO:0042803; GO:0043565; GO:0044010; GO:0045892; GO:0110001`

## Notes

Antitoxin YefM
