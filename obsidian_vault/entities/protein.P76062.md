---
entity_id: "protein.P76062"
entity_type: "protein"
name: "racR"
source_database: "UniProt"
source_id: "P76062"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "racR ydaR b1356 JW1351"
---

# racR

`protein.P76062`

## Static

- Type: `protein`
- Source: `UniProt:P76062`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Transcriptional regulator that represses the expression of ydaS and ydaT under normal physiological conditions (PubMed:29205228, PubMed:29205229). It binds to its own upstream sequence and represses the adjacent and divergently coded ydaS-ydaT operon (PubMed:29205228). RacR-mediated down-regulation of ydaS and ydaT may be critical for cell survival (PubMed:29205229). RacR ensures that the prophage DNA is maintained in the genome (PubMed:38153127). When the expression of the racR gene is reduced, the prophage Rac is excised from the genome, possibly to counteract the lethal toxicity of YdaT (PubMed:38153127). {ECO:0000269|PubMed:29205228, ECO:0000269|PubMed:29205229, ECO:0000269|PubMed:38153127}.

## Biological Role

Component of Rac prophage; DNA-binding transcriptional repressor RacR (complex.ecocyc.CPLX0-11758).

## Annotation

FUNCTION: Transcriptional regulator that represses the expression of ydaS and ydaT under normal physiological conditions (PubMed:29205228, PubMed:29205229). It binds to its own upstream sequence and represses the adjacent and divergently coded ydaS-ydaT operon (PubMed:29205228). RacR-mediated down-regulation of ydaS and ydaT may be critical for cell survival (PubMed:29205229). RacR ensures that the prophage DNA is maintained in the genome (PubMed:38153127). When the expression of the racR gene is reduced, the prophage Rac is excised from the genome, possibly to counteract the lethal toxicity of YdaT (PubMed:38153127). {ECO:0000269|PubMed:29205228, ECO:0000269|PubMed:29205229, ECO:0000269|PubMed:38153127}.

## Outgoing Edges (6)

- `is_component_of` --> [[complex.ecocyc.CPLX0-11758|complex.ecocyc.CPLX0-11758]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2
- `represses` --> [[gene.b1357|gene.b1357]] `RegulonDB` `S` - regulator=RacR; target=ydaS; function=-
- `represses` --> [[gene.b1358|gene.b1358]] `RegulonDB` `S` - regulator=RacR; target=ydaT; function=-
- `represses` --> [[gene.b1359|gene.b1359]] `RegulonDB` `S` - regulator=RacR; target=ydaU; function=-
- `represses` --> [[gene.b1360|gene.b1360]] `RegulonDB` `S` - regulator=RacR; target=ydaV; function=-
- `represses` --> [[gene.b1361|gene.b1361]] `RegulonDB` `S` - regulator=RacR; target=ydaW; function=-

## Incoming Edges (1)

- `encodes` <-- [[gene.b1356|gene.b1356]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P76062`
- `KEGG:ecj:JW1351;eco:b1356;ecoc:C3026_07935;`
- `GeneID:86946548;945899;`
- `GO:GO:0001217; GO:0003677; GO:2000143`

## Notes

DNA-binding transcriptional repressor RacR (Prophage repressor RacR) (Rac prophage repressor)
