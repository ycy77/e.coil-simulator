---
entity_id: "protein.P0A881"
entity_type: "protein"
name: "trpR"
source_database: "UniProt"
source_id: "P0A881"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "trpR rtrY b4393 JW4356"
---

# trpR

`protein.P0A881`

## Static

- Type: `protein`
- Source: `UniProt:P0A881`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm.

## Enriched Summary

FUNCTION: This protein is an aporepressor. When complexed with L-tryptophan it binds the operator region of the trp operon (5'-ACTAGT-'3') and prevents the initiation of transcription. The complex also regulates trp repressor biosynthesis by binding to its regulatory region.

## Biological Role

Component of DNA-binding transcriptional repressor TrpR (complex.ecocyc.PC00007).

## Annotation

FUNCTION: This protein is an aporepressor. When complexed with L-tryptophan it binds the operator region of the trp operon (5'-ACTAGT-'3') and prevents the initiation of transcription. The complex also regulates trp repressor biosynthesis by binding to its regulatory region.

## Outgoing Edges (13)

- `is_component_of` --> [[complex.ecocyc.PC00007|complex.ecocyc.PC00007]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2
- `represses` --> [[gene.b0388|gene.b0388]] `RegulonDB` `C` - regulator=TrpR; target=aroL; function=-
- `represses` --> [[gene.b0389|gene.b0389]] `RegulonDB` `C` - regulator=TrpR; target=yaiA; function=-
- `represses` --> [[gene.b0390|gene.b0390]] `RegulonDB` `C` - regulator=TrpR; target=aroM; function=-
- `represses` --> [[gene.b1260|gene.b1260]] `RegulonDB` `C` - regulator=TrpR; target=trpA; function=-
- `represses` --> [[gene.b1261|gene.b1261]] `RegulonDB` `C` - regulator=TrpR; target=trpB; function=-
- `represses` --> [[gene.b1262|gene.b1262]] `RegulonDB` `C` - regulator=TrpR; target=trpC; function=-
- `represses` --> [[gene.b1263|gene.b1263]] `RegulonDB` `C` - regulator=TrpR; target=trpD; function=-
- `represses` --> [[gene.b1264|gene.b1264]] `RegulonDB` `C` - regulator=TrpR; target=trpE; function=-
- `represses` --> [[gene.b1265|gene.b1265]] `RegulonDB` `C` - regulator=TrpR; target=trpL; function=-
- `represses` --> [[gene.b1704|gene.b1704]] `RegulonDB` `S` - regulator=TrpR; target=aroH; function=-
- `represses` --> [[gene.b3161|gene.b3161]] `RegulonDB` `C` - regulator=TrpR; target=mtr; function=-
- `represses` --> [[gene.b4393|gene.b4393]] `RegulonDB` `S` - regulator=TrpR; target=trpR; function=-

## Incoming Edges (1)

- `encodes` <-- [[gene.b4393|gene.b4393]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0A881`
- `KEGG:ecj:JW4356;eco:b4393;ecoc:C3026_23740;`
- `GeneID:93777452;948917;`
- `GO:GO:0003677; GO:0003700; GO:0005737; GO:0006355; GO:0043565; GO:0045892`

## Notes

Trp operon repressor
